import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from config import Config
from modules.browser import Browser


config = Config()

browser = Browser(config)


print(
    browser.is_valid_url(
        "https://www.google.com"
    )
)

print(
    browser.is_valid_url(
        "hello"
    )
)