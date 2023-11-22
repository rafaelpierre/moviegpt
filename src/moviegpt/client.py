"""CLI Entrypoints for Workflows functionality."""

import pathlib
import logging
import click
from moviegpt.data.utils import get_movies

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


app.add_command(name="data", cmd=get_data)


def main():
    app(standalone_mode=True)

if __name__ == "__main__":
    main()