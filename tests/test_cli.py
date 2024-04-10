"""Tests CLI."""

import click.testing
import pytest
from pytest_mock import MockerFixture

from nxbdl.cli import main
from nxbdl.default_values import DefaultValues


@pytest.mark.parametrize("resolution", DefaultValues.resolutions)
def test_cli_run(mocker: MockerFixture, resolution: str) -> None:
    """Tests main function with successful download."""
    mocker.patch("nxbdl.api.nxbdlAPI.download", return_value=None)

    recorder = click.testing.CliRunner()
    result = recorder.invoke(main, ["url1", "url2"], resolution)

    assert result.exit_code == 0

    expected_output = "Downloading video(s)...\n" "Download(s) successful!\n"
    assert result.output == expected_output
