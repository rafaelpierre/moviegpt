from llama_index import (
    ServiceContext,
    OpenAIEmbedding,
    PromptHelper,
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage
)
from llama_index.llms import OpenAI
from llama_index.node_parser import SimpleNodeParser
import tiktoken
from moviegpt.prompts.recommendation import RecommendationPrompt
from typing import List
import logging

class RAGProvider:

    def __init__(
        self,
        api_key,
        model: str = 'gpt-3.5-turbo',
        persist_dir: str = "/tmp"
    ):

        self.model = model
        self.persist_dir = persist_dir

        self.llm = OpenAI(
            model = model,
            temperature = 0,
            max_tokens = 256,
            api_key = api_key
        )

        self.embed_model = OpenAIEmbedding(api_key = api_key)

    def create_index(
        self,
        separator: str = " ",
        chunk_size: int = 1024,
        chunk_overlap: int = 20,
        prompt_context_window: int = 4096,
        num_output: int = 256,
        chunk_overlap_ratio: float = 0.1,
        chunk_size_limit = None,
        input_files: List[str] = ["/tmp/movies.json"]
    ):

        node_parser = SimpleNodeParser.from_defaults(
            separator = separator,
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap,
            tokenizer = tiktoken.encoding_for_model(self.model).encode
        )

        prompt_helper = PromptHelper(
            context_window = prompt_context_window, 
            num_output = num_output, 
            chunk_overlap_ratio = chunk_overlap_ratio, 
            chunk_size_limit = chunk_size_limit
        )

        service_context = ServiceContext.from_defaults(
            llm = self.llm,
            embed_model = self.embed_model,
            node_parser = node_parser,
            prompt_helper = prompt_helper
        )

        documents = SimpleDirectoryReader(input_files=input_files).load_data()

        index = VectorStoreIndex.from_documents(
            documents, 
            service_context = service_context
        )

        index.storage_context.persist(persist_dir = self.persist_dir)

    def query(
        self,
        prompt: RecommendationPrompt,
        index_dir: str = "/tmp/"
    ) -> str:
        
        storage_context = StorageContext.from_defaults(persist_dir = index_dir)
        index = load_index_from_storage(storage_context = storage_context)
        query_engine = index.as_query_engine()

        formatted_prompt = str(prompt)
        logging.info(f"Formatted prompt: {formatted_prompt}")
        response = query_engine.query(formatted_prompt)
        return response
        