# FDK Python

![GitHub requirements.txt version](https://img.shields.io/github/package-json/v/gofynd/fdk-client-python?style=plastic)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/gofynd/fdk-client-python?style=plastic)
![GitHub](https://img.shields.io/github/license/gofynd/fdk-client-python?style=plastic)
[![Coverage Status](https://coveralls.io/repos/github/gofynd/fdk-client-python/badge.svg)](https://coveralls.io/github/gofynd/fdk-client-python)

FDK client for python

## Getting Started

Get started with the python Development SDK for Fynd Platform

### Usage

```
pip install fdk-client-python
```

Using this method, you can `import` fdk-client-python like so:

```python
from fdk_client.application.ApplicationClient import ApplicationClient
from fdk_client.application.ApplicationConfig import ApplicationConfig
```

### Sample Usage - ApplicationClient

```python
config = ApplicationConfig({
    "applicationID": "YOUR_APPLICATION_ID",
    "applicationToken": "YOUR_APPLICATION_TOKEN",
    "domain": "YOUR_DOMAIN",
    "locationDetails": "LOCATION_DETAILS_OBJECT"
})

applicationClient = ApplicationClient(config)
applicationClient.setLocationDetails(
    { 
        "pincode":"385001",
        "country": "India",
        "city":  "Ahmedabad",
        "location": {
            "longitude": "72.585022", 
            "latitude": "23.033863"
        }
    }
)

async def getProductDetails():
    try:
        product = await applicationClient.catalog.getProductDetailBySlug(slug="product-slug")
        print(product)
    except Exception as e:
        print(e)

getProductDetails()
```
#### Persisting cookies across requests
Some APIs require a login to proceed ahead. For this, we have several login options mentioned in these [User methods](/documentation/application/USER.md).
Using any of these methods, you can get a cookie. All you need to do is store the cookie in application config. Consider an example with mobile OTP:
```python
send_otp_response = applicationClient.user.loginWithOTP(
    platform=YOUR_APPLICATION_ID,
    body={
        "countryCode": "<your country code without the + sign>",
        "captchaCode": "<your captcha code>",
        "mobile": "<your mobile number>"
    }
)

login_response = applicationClient.user.verifyMobileOTP(
    platform=YOUR_APPLICATION_ID,
    body={
        "requestId": send_otp_response["json"]["request_id"],
        "otp": <your OTP>
    }
)

applicationClient.config.cookies = login_response["cookies"]
```
This will make sure the cookies are passed in all subsequent API calls.


### Sample Usage - PlatformClient


```python
from fdk_client.common.aiohttp_helper import AiohttpHelper
from fdk_client.platform.PlatformConfig import PlatformConfig
from fdk_client.platform.PlatformClient import PlatformClient
from fdk_client.common.utils import create_url_without_domain, get_headers_with_signature


async def setAccessToken(platformConfig, cookies):
    reqData = {
        "grant_type": "client_credentials",
        "client_id": platformConfig.apiKey,
        "client_secret": platformConfig.apiSecret
    }
    url = f"{platformConfig.domain}/service/panel/authentication/v1.0/company/{platformConfig.companyId}/oauth/token"
    url_without_domain = await create_url_without_domain(f"/service/panel/authentication/v1.0/company/{platformConfig.companyId}/oauth/token")
    headers = await get_headers_with_signature(platformConfig.domain, "post", url_without_domain, "", {}, reqData)
    res = await AiohttpHelper().aiohttp_request("POST", url, reqData, headers, cookies=cookies)
    return res["json"]

async def loginUser(platformConfig):
    skywarpURL = f"{platformConfig.domain}/service/panel/authentication/v1.0/auth/login/password"
    userData = {
        "username": "YOUR_USERNAME",
        "password": "YOUR_PASSWORD",
        "g-recaptcha-response": "_skip_"
    }
    url_without_domain = "/service/panel/authentication/v1.0/auth/login/password"
    headers = await get_headers_with_signature(platformConfig.domain, "post", url_without_domain, "", {}, userData)
    res = await AiohttpHelper().aiohttp_request("POST", skywarpURL, userData, headers)
    return res

try:
    platformConfig = PlatformConfig({
        "companyId": "YOUR_COMPANY_ID",
        "domain": "YOUR_DOMAIN",
        "apiKey": "YOUR_APIKEY",
        "apiSecret": "YOUR_APISECRET"
    })
    loginResponse = await loginUser(platformConfig)
    # print(loginResponse)
    tokenResponse = await setAccessToken(platformConfig, loginResponse["cookies"])
    # print(tokenResponse)
    await platformConfig.oauthClient.setToken(tokenResponse)
    platformClient = PlatformClient(platformConfig)
    res = await platformClient.lead.getTicket(id="YOUR_TICKET_ID")
    # use res
except Exception as e:
    print(e)
```
