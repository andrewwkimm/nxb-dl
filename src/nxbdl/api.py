"""The nxb-dl API."""

# mypy: disable-error-code=operator

from pathlib import Path
import time
from typing import Optional, Tuple, Union

from nxbdl.browsers import ChromeDriver, FirefoxDriver
from nxbdl.defaults import Default, ninexbuddy


class nxbdlAPI:
    """An interface to Selenium for nxb-dl."""

    def __init__(self) -> None:
        """Initializes the browser."""
        self.driver = Union[ChromeDriver, FirefoxDriver]

    def download(
        self,
        urls: Union[str, Tuple[str]],
        download_path: Optional[Path],
        resolution: Optional[str],
    ) -> None:
        """Downloads the desired video file."""
        for website in Default.websites:
            self._download_from_website(urls, download_path, resolution, website)

    def _download_from_website(
        self,
        urls: Union[str, Tuple[str]],
        download_path: Optional[Path],
        resolution: Optional[str],
        website: str,
    ) -> None:
        if website == "ninexbuddy":
            for url in urls:
                if download_path is None:
                    download_path = Default.download_path

                self.driver = ChromeDriver()

                self.driver.navigate_to_page(ninexbuddy.url + url)

                download_links = self.driver.get_download_links(
                    ninexbuddy.downloads_xpath, ninexbuddy.tag_element
                )
                download_link = self.driver.get_link_for_resolution(
                    download_links, resolution
                )

                self.driver.click(download_link)

                video_file_name = self.driver.get_video_file_name(
                    ninexbuddy.video_name_xpath
                )
                validate_file_is_downloaded(download_path, video_file_name)

                self.driver.quit()


def validate_file_is_downloaded(download_path: Path, video_file_name: str) -> None:
    """Validates the video is fully downloaded."""
    # TODO: Add validation that checks that the video is fully downloaded.
    #       It should have a way to verify that ${file_name}.${ext} is in
    #       the listed file path instead of a .crdownload temp file.

    time.sleep(Default.timeout)
