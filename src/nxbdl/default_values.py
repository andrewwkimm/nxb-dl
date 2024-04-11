"""Default values for nxb-dl."""

from dataclasses import dataclass

from pathlib import Path
from typing import List


class DefaultValues:
    """Default values."""

    resolutions: List[str] = ["1440", "1080", "720", "520"]
    download_path: Path = Path("~/Downloads")
    timeout: int = 30
    websites: List = ["ninexbuddy"]


@dataclass(frozen=True)
class ninexbuddy:
    """Default values for 9xbuddy.com."""

    downloads_xpath: str = "/html/body/main/section/section[3]/section[2]"
    tag_element = "a"
    url: str = "https://9xbuddy.in/process?url="
    video_name_xpath: str = "/html/body/main/section/section[3]/div[2]"
