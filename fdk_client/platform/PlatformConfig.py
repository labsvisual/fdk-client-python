"""Platform Config."""

from typing import Dict

from ..common.constants import DEFAULT_DOMAIN
from ..platform.OAuthClient import OAuthClient


class PlatformConfig:
    def __init__(self, config: Dict):
        self.companyId = config.get("companyId", "")
        self.domain = config.get("domain", DEFAULT_DOMAIN)
        self.apiKey = config.get("apiKey", "")
        self.apiSecret = config.get("apiSecret", "")
        self.oauthClient = OAuthClient(self)

    async def getAccessToken(self):
        token = await self.oauthClient.getAccessToken()
        return token
