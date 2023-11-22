# 🎥 MovieGPT: A RAG, Gen AI application for Movie Recommendations

![version](https://img.shields.io/badge/version-0.0.1-red?style=for-the-badge) ![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white) ![python](https://img.shields.io/badge/python-3.10-blue?style=for-the-badge) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![ruff](https://img.shields.io/badge/lint-ruff-gold?style=for-the-badge) ![poetry](https://img.shields.io/badge/packaging-poetry-cyan?style=for-the-badge) ![LlamaIndex](https://img.shields.io/badge/LlamaIndex-%F0%9F%A6%99-black?labelColor=purple&style=for-the-badge)

## AI Powered Movie Recommendations

**MovieGPT** leverages the power of **Generative AI** in order to provide relevant movie recommendations based on user input. In order to achieve that, it relies on the following components:

📚 **Open Source Data**: we rely on movie data provided by [Wikipedia](https://www.wikipedia.org/), such as: movie summaries, genres, actor names and so on. This data is converted to embeddings for further indexing in a **Vector Database**.

🐕 **Retrieval Augmented Generation (RAG)**: we use a **Vector Database** and **semantic search** in order to guarantee relevant results. This way, we limit the **context** that is provided to **large language models** when generating movie recommendations, hence reducing the risk of **hallucinations** in the process.

🤖 **ChatGPT**: we use [ChatGPT](https://chat.openai.com/) for formatting the responses with movie recommendations in a human-like fashion. 

## Architecture

The diagram below describes the architecture of **MovieGPT** in high level:

**TODO**

## Getting started
### Docker

🤖 Set up your OpenAI API Token:
```bash
export OPENAI_API_TOKEN=#YOUR_TOKEN
```

🐋 Build the Docker image:
```bash
make docker
```

🏃‍♂️ Run the container:
```bash
make run
```

```bash

         __   __  _______  __   __  ___   _______  _______  _______  _______ 
        |  |_|  ||       ||  | |  ||   | |       ||       ||       ||       |
        |       ||   _   ||  |_|  ||   | |    ___||    ___||    _  ||_     _|
        |       ||  | |  ||       ||   | |   |___ |   | __ |   |_| |  |   |  
        |       ||  |_|  ||       ||   | |    ___||   ||  ||    ___|  |   |  
        | ||_|| ||       | |     | |   | |   |___ |   |_| ||   |      |   |  
        |_|   |_||_______|  |___|  |___| |_______||_______||___|      |___|  
    
INFO:root:Starting web server...
INFO:     Started server process [29]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

🕸️ Open the API docs and try it out: http://localhost/docs

### Running locally

⚠️ Before proceeding, make sure you are using **Python 3.10.12**

🏠 Install `poetry`:
```bash
pip install poetry
```

🏗️ Install the dependencies and activate a Poetry environment:
```bash
cd src && poetry shell && poetry install
```

🎥 Run **MovieGPT**:
```bash
> poetry run moviegpt

Usage: moviegpt [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  data   Downloads WikiData for movies.
  index  Creates a VectorDB Index based on Movie Metadata in JSON.
  query  Queries the VectorDB using Semantic Similarity and outputs movie...
  web    Runs our MovieGPT RAG App and exposes it through Fast API.
```

🪜 Run the following steps:
```bash
poetry run moviegpt data && \
poetry run index && \
poetry run web
```

### Sample API response

<img src="https://github.com/rafaelpierre/moviegpt/blob/main/img/fastapi.png?raw=true" />

## Documentation

**TODO**