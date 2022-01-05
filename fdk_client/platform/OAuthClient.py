"""OAuth Client."""

from threading import Timer
from typing import Dict
from urllib import parse
import base64
import asyncio

from ..common.exceptions import FDKOAuthCodeError
from ..common.aiohttp_helper import AiohttpHelper
from ..common.utils import get_headers_with_signature


class OAuthClient:
    def __init__(self, config):
        self._conf = config
        self.token = None
        self.refreshToken = None
        self.retryOAuthTokenTimer = None
        self.raw_token = None
        self.token_expires_in = None

    async def getAccessToken(self):
        return self.token

    async def setToken(self, token):
        self.raw_token = token
        self.token_expires_in = token.get("expires_in")
        self.token = token.get("access_token")
        self.refreshToken = token.get("refresh_token") if token.get("refresh_token") else None
        if self.refreshToken:
            await self.retryOAuthToken(token.get("expires_in"))

    async def retryOAuthToken(self, expires_in):
        if self.retryOAuthTokenTimer:
            self.retryOAuthTokenTimer.cancel()
        if expires_in > 60:
            self.retryOAuthTokenTimer = Timer(float(expires_in - 60), lambda: asyncio.run(self.renewAccessToken()))
            self.retryOAuthTokenTimer.start()

    async def startAuthorization(self, options: Dict):
        query = {
            "access_mode": options.get("access_mode", ""),
            "client_id": self._conf.apiKey,
            "redirect_uri": options.get("redirectUri", ""),
            "response_type": "code",
            "scope": ",".join(options.get("scope", [])),
            "state": options.get("state", "")
        }
        queryString = parse.urlencode(query)
        reqPath = f"/service/panel/authentication/v1.0/company/{self._conf.companyId}/oauth/authorize"
        signingOptions = {
          "method": "GET",
          "host": self._conf.domain,
          "path": reqPath,
          "body": None,
          "headers": {},
          "signQuery": True
        }
        queryString = await get_headers_with_signature(self._conf.domain, "get",
                                                            f"/service/panel/authentication/v1.0/company/"
                                                            f"{self._conf.companyId}/oauth/authorize",
                                                            queryString, {}, sign_query=True)
        return f"{self._conf.domain}{signingOptions['path']}?{queryString}"

    async def verifyCallback(self, query):
        if query.get("error"):
            raise FDKOAuthCodeError(query["error_description"])
        # try:
        res = await self.getAccesstokenObj(grant_type="authorization_code", code=query.get("code", ""))
        await self.setToken(res)
        # except Exception as e:
        #   if error.isAxiosError:
        #     throw new FDKTokenIssueError(error.message)

    async def renewAccessToken(self):
        res = await self.getAccesstokenObj(grant_type="refresh_token", refresh_token=self.refreshToken)
        await self.setToken(res)
        return res

    async def getAccesstokenObj(self, grant_type="", refresh_token="", code=""):
        reqData = {
            "grant_type": grant_type,
        }
        if grant_type == "refresh_token":
            reqData = {**reqData, "refresh_token": refresh_token}
        elif grant_type == "authorization_code":
            reqData = {**reqData, "code": code}

        token = base64.b64encode(f"{self._conf.apiKey}:{self._conf.apiSecret}".encode()).decode()
        url = f"{self._conf.domain}/service/panel/authentication/v1.0/company/{self._conf.companyId}/oauth/token"
        headers = {
            "Authorization": f"Basic {token}"
        }
        headers = await get_headers_with_signature(self._conf.domain, "post",
                                             f"/service/panel/authentication/v1.0/company/{self._conf.companyId}/oauth/token",
                                             "", headers, reqData, ["Authorization"])
        response = await AiohttpHelper().aiohttp_request("POST", url, reqData, headers)
        return response["json"]

