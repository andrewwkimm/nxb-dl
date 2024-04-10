"""Tests the click() method."""

from selenium.webdriver.remote.webelement import WebElement

from nxbdl.browsers import ChromeDriver


def test_click_element(mocker):
    """Tests if click_element calls the click method on the WebElement."""
    mock_element = mocker.Mock(spec=WebElement)

    driver = ChromeDriver()
    driver.click(mock_element)

    mock_element.click.assert_called_once()