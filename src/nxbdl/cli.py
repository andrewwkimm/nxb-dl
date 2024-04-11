"""The nxb-dl CLI."""

from pathlib import Path
from typing import Optional, Tuple

import click

from nxbdl.api import nxbdlAPI
from nxbdl.exceptions import NoViableLinkError


@click.command()
@click.argument("urls", nargs=-1, required=True)
@click.option("--download_path", "-p", default=None, help="Path for the download.")
@click.option("--resolution", "-r", default=None, help="Resolution of the video")
def main(
    urls: Tuple[str], download_path: Optional[Path], resolution: Optional[str]
) -> None:
    """Download video(s) using nxb-dl."""
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    nxbdl = nxbdlAPI()

    try:
        click.echo(GREEN + "Downloading video(s)..." + RESET)

        nxbdl.download(urls, download_path, resolution)

        click.echo(GREEN + "Download(s) successful!" + RESET)
    except NoViableLinkError as excinfo:
        click.echo(f"{RED}NoViableLinkError: {excinfo}{RESET}")


if __name__ == "__main__":
    main()
