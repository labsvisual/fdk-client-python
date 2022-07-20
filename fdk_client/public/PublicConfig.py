"""Python code/fdk_client/public/PublicConfig.py."""

from typing import Dict


class PublicConfig:
    def __init__(self, _conf: Dict):
        """Public Config constructor."""
        self.domain = _conf.get("domain", "https://api.fynd.com")
        self.userAgent = _conf.get("userAgent", "")
        self.language = _conf.get("language")
        self.currency = _conf.get("currency")
        self.extraHeaders = []
