"""Python code/sdk/common/aiohttp_helper.py."""

import ssl
import time

import aiohttp
import ujson

from .constants import HTTP_TIMEOUT
from .date_helper import get_ist_now


class AiohttpHelper:
    """Aiohttp Helper."""

    @staticmethod
    async def parse_data(data):
        """parse_data."""
        try:
            text = ujson.loads(data)

        except ValueError:
            text = {}

        return text

    async def aiohttp_request(
            self,
            request_type,
            url,
            data=None,
            headers={},
            auth=None,
            cookies=None,
            cert=None,
            verify_ssl=True,
            protocol="HTTP",
            timeout_allowed=HTTP_TIMEOUT,
            http_file_config=None):
        """Asynchronous HTTP Request Method.

        :param protocol: HTTP or HTTPS
        :param verify_ssl: This param is used for a request ignoring ssl verification (Too Risky) (Used in Jiopos)
        :param cert: certificate path as tuple (used in amazon)
        :param cookies:
        :param auth:
        :param request_type: String GET/POST/PUT
        :param url: String
        :param data: Dict  Nullable
        :param headers: Dict Nullable
        :param timeout_allowed: int Max timeout allowed for API call
        :param http_file_config: Optional[Dict] file config to send a file via http
        :return: Tuple with status_code and json response


        Example:
        resp1 = await aiohttp_request('GET', 'http://localhost:8000/ping/', data={'a': 1})
        print(resp1)

        resp2 = await aiohttp_request('POST', 'http://localhost:8000/pong/', data={'a': 1})
        print(resp2)

        """
        start_time = time.time()
        timeout = aiohttp.ClientTimeout(total=timeout_allowed)
        # auth_data is passed to send_soap_request() as it cannot use BasicAuth
        auth_data = {"username": auth[0], "password": auth[1]} if auth else {}
        auth = aiohttp.BasicAuth(auth[0], auth[1]) if auth else None
        ssl_context = None
        open_file_object = None
        if cert:
            ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            ssl_context.load_cert_chain(cert[0], cert[1])
        async with aiohttp.ClientSession(
                cookies=cookies, headers=headers,
                timeout=timeout, auth=auth, json_serialize=ujson.dumps
        ) as session:
            response = {
                "url": url,
                "method": request_type,
                "payload": data,
                "external_call_request_time": str(get_ist_now()),
                "status_code": None,
                "text": "",
                "headers": "",
                "cookies": None,
                "error_message": "",
            }
            try:
                # verify_ssl, ssl_context, fingerprint and ssl parameters are mutually exclusive
                # Jiopos doesnt use ssl; it uses an IP in production whereas Amazon uses SSL Certificate and those combined
                # usage in aiohttp session_obj contradict each other thereby raising a ValueError Exception
                if protocol == "HTTP" and request_type.upper() in ["GET", "POST", "PUT", "DELETE"]:
                    filters = {}
                    if data and headers.get("Content-Type") == "application/x-www-form-urlencoded":
                        form_data = aiohttp.FormData()
                        for form_key, form_value in data.items():
                            value = ujson.dumps(form_value) if isinstance(form_value, dict) else form_value
                            form_data.add_field(form_key, value)
                        filters = {"data": form_data}
                    else:
                        if request_type == "GET":
                            if http_file_config:
                                pass  # TODO add support for file GET call
                            else:
                                if isinstance(data, dict):
                                    data.update(
                                        {
                                            key: str(data[key]) for key in data if type(data[key]) in [bool]})
                                    filters = {"params": data}
                        else:
                            if http_file_config:
                                # Deal with file data over HTTP
                                # TODO Add FTP support
                                pass
                            else:
                                if isinstance(data, dict):
                                    filters = {"json": data}
                                else:
                                    if not isinstance(data, str):
                                        data = ujson.dumps(data)
                                    filters = {"data": data}

                    if ssl_context:
                        filters.update({"ssl_context": ssl_context})
                    else:
                        filters.update({"ssl": verify_ssl})

                    request_obj = getattr(session, request_type.lower())
                    session_obj = request_obj(url, **filters)

                    async with session_obj as resp:
                        response["status_code"] = resp.status
                        response["headers"] = dict(resp.headers)
                        response["cookies"] = dict(resp.cookies)

                        try:
                            response["content"] = await resp.content.read()  # resp.content is a StreamReader
                            response["text"] = response["content"].decode()  # converting to str
                        except UnicodeDecodeError as err:
                            response["error_message"] = f"Error occurred while converting bytes to string - {err}"

                elif protocol == "SOAP":
                    pass
                else:
                    raise Exception("Invalid request_type: {}".format(request_type))
                response["latency"] = time.time() - start_time
                response["json"] = await self.parse_data(response["text"])
            except Exception as request_error:
                response["status_code"] = 999
                response["latency"] = (time.time() - start_time)
                response["text"] = request_error
            finally:
                if open_file_object:
                    open_file_object.close()
                if http_file_config:
                    pass
            return response
