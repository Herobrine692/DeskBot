"""
DeskBot Browser Module

Handles browser-related actions.
"""

import webbrowser
from urllib.parse import urlparse


class Browser:

    def __init__(self, config):
        self.config = config


    def is_valid_url(self, url):
        """
        Check if a URL is valid.
        """

        parsed = urlparse(url)

        return (
            parsed.scheme in ["http", "https"]
            and parsed.netloc != ""
        )


    def open_url(self, url):
        """
        Open a URL in the default browser.
        """

        if not self.is_valid_url(url):
            return {
                "success": False,
                "error": "Invalid URL"
            }

        webbrowser.open(url)

        return {
            "success": True,
            "url": url
        }