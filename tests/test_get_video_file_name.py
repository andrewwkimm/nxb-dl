"""Tests the get_video_file_name() method."""

from nxbdl.browsers import ChromeDriver


def test_get_video_file_name(mocker):
    """Tests if get_video_file_name returns the text from the WebElement."""
    mock_element = mocker.Mock(text="sample_file_name")

    driver = ChromeDriver()

    mocker.patch.object(driver.driver, "find_element", return_value=mock_element)

    file_name = driver.get_video_file_name("some_xpath")
    assert file_name == "sample_file_name"
