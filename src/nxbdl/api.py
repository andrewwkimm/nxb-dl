"""The nxb-dl API."""

from pathlib import Path
from typing import List, Optional, Tuple
from typing_extensions import Self

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from nxbdl.exceptions import NoViableLinkError


class nxbdlAPI:
    """An interface to Selenium for nxb-dl."""

    _file_path: Optional[Path] = Path("~/Downloads")
    _resolutions: Optional[List[str]] = ["1440", "1080", "720", "520"]
    _default_video_name_xpath: str = "/html/body/main/section/section[3]/div[2]"
    _default_download_links_xpath: str = "/html/body/main/section/section[3]/section[2]"

    def __init__(self) -> None:
        """Initializes the browser."""
        self.driver = None

    def download(self, urls: Tuple[str], resolution: Optional[str] = None) -> None:
        """Downloads the desired video file."""
        for url in urls:
            self.launch_browser()
            self.navigate_to_page(url)

            download_links = self.get_download_links()
            download_link = self.get_link_for_resolution(download_links, resolution)

            click_link(download_link)

            video_file_name = self.get_video_file_name(self._default_video_name_xpath)
            validate_file_is_downloaded(video_file_name, self._file_path)

            self.driver.quit()
        # TODO: Add a feature to retry n number of times before raising an error.

    def get_download_links(self) -> List[WebElement]:
        """Gets all links available to download."""
        wait = WebDriverWait(self.driver, 30)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, self._default_download_links_xpath)
            )
        )

        download_links = self.driver.find_elements(By.TAG_NAME, "a")
        return download_links

    def get_link_for_resolution(
        self, links: WebElement, resolution: Optional[str]
    ) -> WebElement:
        """Retrieves the link for the specified resolution."""
        # TODO: Potentially rethink how to handle default resolutions.
        if resolution is not None:
            for link in links:
                if resolution in link.get_attribute("href"):
                    return link
        else:
            for resolution in self._resolutions:
                for link in links:
                    if resolution in link.get_attribute("href"):
                        return link
        raise NoViableLinkError(
            "No download link is available for the given resolution."
        )

    def get_video_file_name(self, xpath: str) -> str:
        """Gets the file name of the video to be downloaded."""
        element = self.driver.find_element(By.XPATH, xpath)
        video_file_name = element.text
        return video_file_name

    def launch_browser(self) -> Self:
        """Launches the Chromium browser."""
        self.driver = webdriver.Chrome()

    def navigate_to_page(self, url: str) -> Self:
        """Navigates to the given URL."""
        self.driver.get(url)


def click_link(link: WebElement) -> None:
    """Clicks a given link."""
    link.click()


def validate_file_is_downloaded(file_name: str, file_path: Path) -> None:
    """Validates the video is fully downloaded."""
    # TODO: Add validation that checks that the video is fully downloaded.
    #       It should have a way to verify that ${file_name}.${ext} is in
    #       the listed file path instead of a .crdownload temp file.
    pass
