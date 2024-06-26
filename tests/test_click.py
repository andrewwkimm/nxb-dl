"""Tests the click() method."""

from pytest_mock import MockerFixture
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.webelement import WebElement

from nxbdl.browsers import ChromeDriver


def test_click_element(mocker: MockerFixture) -> None:
    """Tests if click_element calls the click method on the WebElement."""
    mock_element = mocker.Mock(spec=WebElement)

    options = ChromeOptions()
    driver = ChromeDriver(options=options)
    driver.click(mock_element)

    mock_element.click.assert_called_once()
