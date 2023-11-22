"""CLI Entrypoints for Workflows functionality."""

import pathlib
import logging
import click
from moviegpt.data.utils import get_movies
from moviegpt.providers.rag import RAGProvider
from moviegpt.prompts.recommendation import RecommendationPrompt
from moviegpt.api import server
import os

@click.group()
def app():
    intro = """
         __   __  _______  __   __  ___   _______  _______  _______  _______ 
        |  |_|  ||       ||  | |  ||   | |       ||       ||       ||       |
        |       ||   _   ||  |_|  ||   | |    ___||    ___||    _  ||_     _|
        |       ||  | |  ||       ||   | |   |___ |   | __ |   |_| |  |   |  
        |       ||  |_|  ||       ||   | |    ___||   ||  ||    ___|  |   |  
        | ||_|| ||       | |     | |   | |   |___ |   |_| ||   |      |   |  
        |_|   |_||_______|  |___|  |___| |_______||_______||___|      |___|  
    """
    click.echo(
        click.style(
            intro,
            fg = "bright_yellow"
        )
    )
    pass

@click.command(name="data")
@click.option("--start", type=int, default=1970)
@click.option("--end", type=int, default=2020)
@click.option("--path", type=str, default="./")
@click.option("--sample", type=float, default=1.0)
@click.option("--debug", type=bool, default=False, is_flag=True, help="Debug mode")
def get_data(start: int, end: int, path: str, sample: float, debug: bool):
    """
    Downloads WikiData for movies.

    Params:
        start: Starting decade.
        end: Ending decade.
        path: Path where JSON file will be saved.
    """

    if debug:
        logging.basicConfig(level="DEBUG")

    try:
        path = pathlib.Path(path)
        target_path = f"{str(path)}/movies.json"
        click.echo(
            click.style(
                "\n🍿 Downloading movie data...\n",
                bold = True,
                fg = "cyan"
            )
        )

        movies_df = get_movies(start = start, end = end)
        if sample < 1.0:
            movies_df = movies_df.sample(frac = sample)
        movies_df.to_json(target_path, orient = "records")

        click.echo(
            click.style(
                f"\n✨ Successfully downloaded metadata from {len(movies_df)} movies into {target_path} 😀\n",
                bold = True,
                fg = "white"
            )
        )


    except Exception as exception:
        logging.error(f"Error: {str(exception)}")
        raise exception


@click.command(name="index")
@click.option("--input_path", type=str, default="/tmp/movies.json")
@click.option("--api_key", type=str)
def create_index(input_path: str, api_key: str):
    """
    Creates a VectorDB Index based on Movie Metadata in JSON.

    Params:
        input_path: Path to JSON file containing movie metadata.
    """

    click.echo(
        click.style(
            f"\n\n🎥 Creating vector index based on data from {input_path}...",
            bold = True,
            fg = "white"
        )
    )
    provider = RAGProvider(api_key = api_key)
    provider.create_index()

    click.echo(
        click.style(
            "\n✨ Finished!",
            bold = True,
            fg = "white"
        )
    )

@click.command(name="query")
def query():
    """
    Queries the VectorDB using Semantic Similarity and outputs movie recommendations
    using OpenAI.
    """

    intro_msg = """
    \n🤔 Hey! Give me some details about your favorite types of movies
🎁 I'll then do my best to provide some awesome movie recommendations.
🍿 Feel free to mention genres, actors, storyline aspects or movie titles!
    """.replace("\t", "")

    click.echo(
        click.style(
            intro_msg,
            bold = True,
            fg = "white"
        )
    )

    query_text = input("\n🎥 Tips: ")

    provider = RAGProvider(api_key = os.environ["OPENAI_API_KEY"])
    prompt = RecommendationPrompt(details = query_text)

    click.echo(
        click.style(
            "\n⌛ Getting movie recommendations from OpenAI...",
            bold = True,
            fg = "white"
        )
    )

    recommendations = provider.query(prompt = prompt)

    click.echo(
        click.style(
            "\n✨ Here are your movie recommendations:\n\n",
            bold = True,
            fg = "white"
        )
    )

    recommendation_text = "🤓 " + str(recommendations)

    click.echo(
        click.style(
            recommendation_text,
            bold = False,
            fg = "white"
        )
    )

    sources = recommendations.get_formatted_sources()
    sources_txt = (
        "\n\n🕸️  Sources:\n\n {sources}\n"
            .format(sources = sources)
    )

    click.echo(
        click.style(
            sources_txt,
            bold = False,
            fg = "white"
        )
    )

    click.echo(
        click.style(
            "\n✨ Hope you enjoyed my recommendations! 😀\n",
            bold = True,
            fg = "green"
        )
    )

@click.command()
@click.option('--logs', default='info', help='Verbosity level, defaults to INFO')
@click.option('--host', default='0.0.0.0', help='Host Address, defaults to 0.0.0.0')
@click.option('--port', default='8000', help='HTTP Port for Backend, defaults to 8000')
def web(logs: str, host: str, port: str):
    """Runs our MovieGPT RAG App and exposes it through Fast API."""

    logging.basicConfig(level = logs.upper())
    logging.info("Starting web server...")
    server.run(["uvicorn", "moviegpt.api.web:app", "--host", host, "--port", port])

    


app.add_command(name="data", cmd=get_data)
app.add_command(name="index", cmd=create_index)
app.add_command(name="query", cmd=query)
app.add_command(name="web", cmd=web)

def main():
    app(standalone_mode=True)

if __name__ == "__main__":
    main()