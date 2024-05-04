"""Tests for nxbdl."""

from importlib.metadata import version

from nxbdl import __version__


def test_version() -> None:
    """Tests that version is set to expected value."""
    assert __version__ == version("nxbdl")
