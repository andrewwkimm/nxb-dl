"""Browser interfaces."""

# mypy: disable-error-code=operator

from abc import ABC, abstractmethod
from typing import List, Optional, Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from nxbdl.exceptions import NoViableLinkError
from nxbdl.defaults import Default


class Browser(ABC):
    """An abstract base class for browser interaction using Selenium."""

    def __init__(
        self, options: Optional[Union[ChromeOptions, FirefoxOptions]] = None
    ) -> None:
        """Initializes a new Browser instance."""
        self.driver: Union[webdriver.Chrome, webdriver.Firefox]
        self.driver = self._create_driver(options)

    @abstractmethod
    def _create_driver(
        self, options: Optional[Union[ChromeOptions, FirefoxOptions]] = None
    ) -> Union[webdriver.Chrome, webdriver.Firefox]:
        """An abstract method to create a specific browser driver."""
        # TODO: Add a way to accept additional parameters from the CLI
        #       that can be passed down as an option for the drivers.

    def click(self, element: WebElement) -> None:
        """Clicks on a specific element."""
        element.click()

    def get_download_links(
        self, downloads_xpath: str, element: str
    ) -> List[WebElement]:
        """Gets all links available to download."""
        wait = WebDriverWait(self.driver, Default.timeout)
        wait.until(EC.presence_of_element_located((By.XPATH, downloads_xpath)))

        download_links = self.driver.find_elements(By.TAG_NAME, element)
        return download_links

    def get_link_for_resolution(
        self, links: List[WebElement], resolution: Optional[str] = None
    ) -> WebElement:
        """Retrieves the link for the specified resolution."""
        if resolution is str:
            for link in links:
                if resolution in link.get_attribute("href"):
                    return link
        else:
            for resolution in Default.resolutions:
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

    def navigate_to_page(self, url: str) -> None:
        """Navigates the browser to the specified URL."""
        self.driver.get(url)

    def quit(self) -> None:
        """Quits the browser driver and closes the browser window."""
        self.driver.quit()


class ChromeDriver(Browser):
    """Interface for Chrome to the Selenium WebDriver."""

    def _create_driver(
        self, options: Optional[Union[ChromeOptions, FirefoxOptions]] = None
    ) -> webdriver.Chrome:
        """Creates a Chrome WebDriver instance."""
        if not options or isinstance(options, FirefoxOptions):
            options = ChromeOptions()
        options.add_argument("--headless")
        return webdriver.Chrome(options)


class FirefoxDriver(Browser):
    """Interface for Firefox to the Selenium WebDriver."""

    def _create_driver(
        self, options: Optional[Union[ChromeOptions, FirefoxOptions]] = None
    ) -> webdriver.Firefox:
        """Creates a Firefox WebDriver instance."""
        if not options or isinstance(options, ChromeOptions):
            options = FirefoxOptions()
        return webdriver.Firefox()
