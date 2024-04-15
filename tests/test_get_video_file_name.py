"""Tests the get_video_file_name() method."""

from pytest_mock import MockerFixture

from selenium.webdriver.chrome.options import Options as ChromeOptions

from nxbdl.browsers import ChromeDriver


def test_get_video_file_name(mocker: MockerFixture) -> None:
    """Tests if get_video_file_name returns the text from the WebElement."""
    mock_element = mocker.Mock(text="sample_file_name")

    options = ChromeOptions()
    driver = ChromeDriver(options=options)

    mocker.patch.object(driver.driver, "find_element", return_value=mock_element)

    file_name = driver.get_video_file_name("some_xpath")
    assert file_name == "sample_file_name"
