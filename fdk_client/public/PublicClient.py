"""Public Client."""

import base64
import ujson
from urllib.parse import urlparse

from ..common.aiohttp_helper import AiohttpHelper
from ..common.exceptions import FDKClientValidationError
from ..common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .models.ConfigurationValidator import ConfigurationValidator
from .models.WebhookValidator import WebhookValidator
from .models.InventoryValidator import InventoryValidator


class Configuration:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "searchApplication": "/service/common/configuration/v1.0/application/search-application",
            "getLocations": "/service/common/configuration/v1.0/location"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def searchApplication(self, authorization=None, query=None, body=""):
        """Provide application name or domain url
        :param authorization :  : type string
        :param query : Provide application name : type string
        """
        payload = {}
        
        if authorization:
            payload["authorization"] = authorization
        
        if query:
            payload["query"] = query
        
        # Parameter validation
        schema = ConfigurationValidator.searchApplication()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["searchApplication"], proccessed_params="""{"required":[],"optional":[{"in":"header","name":"authorization","schema":{"type":"string"}},{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"query":[{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"headers":[{"in":"header","name":"authorization","schema":{"type":"string"}}],"path":[]}""", authorization=authorization, query=query)
        query_string = await create_query_string(authorization=authorization, query=query)
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["searchApplication"]).netloc, "get", await create_url_without_domain("/service/common/configuration/v1.0/application/search-application", authorization=authorization, query=query), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getLocations(self, location_type=None, id=None, body=""):
        """
        :param location_type : Provide location type to query on. Possible values : country, state, city : type string
        :param id : Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state. : type string
        """
        payload = {}
        
        if location_type:
            payload["location_type"] = location_type
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = ConfigurationValidator.getLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocations"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"query":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"headers":[],"path":[]}""", location_type=location_type, id=id)
        query_string = await create_query_string(location_type=location_type, id=id)
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getLocations"]).netloc, "get", await create_url_without_domain("/service/common/configuration/v1.0/location", location_type=location_type, id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

class Webhook:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "fetchAllWebhookEvents": "/service/common/webhook/v1.0/events",
            "queryWebhookEventDetails": "/service/common/webhook/v1.0/events/query-event-details"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def fetchAllWebhookEvents(self, body=""):
        """Get All Webhook Events
        """
        payload = {}
        
        # Parameter validation
        schema = WebhookValidator.fetchAllWebhookEvents()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["fetchAllWebhookEvents"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["fetchAllWebhookEvents"]).netloc, "get", await create_url_without_domain("/service/common/webhook/v1.0/events", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def queryWebhookEventDetails(self, body=""):
        """Get Webhook Event Details for provided events
        """
        payload = {}
        
        # Parameter validation
        schema = WebhookValidator.queryWebhookEventDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["queryWebhookEventDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["queryWebhookEventDetails"]).netloc, "post", await create_url_without_domain("/service/common/webhook/v1.0/events/query-event-details", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

class Inventory:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getJobByCode": "/service/common/inventory/v1.0/company/jobs/code/{code}",
            "getJobConfigByIntegrationType": "/service/common/inventory/v1.0/company/job/config",
            "getJobCodesMetrics": "/service/common/inventory/v1.0/company/email/jobCode",
            "saveJobCodesMetrics": "/service/common/inventory/v1.0/company/email/jobCode"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getJobByCode(self, code=None, body=""):
        """REST Endpoint that returns job config by code
        :param code : Job Code : type string
        """
        payload = {}
        
        if code:
            payload["code"] = code
        
        # Parameter validation
        schema = InventoryValidator.getJobByCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getJobByCode"], proccessed_params="""{"required":[{"name":"code","in":"path","description":"Job Code","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"code","in":"path","description":"Job Code","required":true,"schema":{"type":"string"}}]}""", code=code)
        query_string = await create_query_string(code=code)
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getJobByCode"]).netloc, "get", await create_url_without_domain("/service/common/inventory/v1.0/company/jobs/code/{code}", code=code), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getJobConfigByIntegrationType(self, integration_type=None, disable=None, body=""):
        """REST Endpoint that returns all job Configs by Integration Type
        :param integration_type : Integration Type : type string
        :param disable : JobConfig current state : type boolean
        """
        payload = {}
        
        if integration_type:
            payload["integration_type"] = integration_type
        
        if disable:
            payload["disable"] = disable
        
        # Parameter validation
        schema = InventoryValidator.getJobConfigByIntegrationType()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getJobConfigByIntegrationType"], proccessed_params="""{"required":[{"name":"integration_type","in":"query","description":"Integration Type","required":true,"schema":{"type":"string"}}],"optional":[{"name":"disable","in":"query","description":"JobConfig current state","required":false,"schema":{"type":"boolean","default":false}}],"query":[{"name":"integration_type","in":"query","description":"Integration Type","required":true,"schema":{"type":"string"}},{"name":"disable","in":"query","description":"JobConfig current state","required":false,"schema":{"type":"boolean","default":false}}],"headers":[],"path":[]}""", integration_type=integration_type, disable=disable)
        query_string = await create_query_string(integration_type=integration_type, disable=disable)
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getJobConfigByIntegrationType"]).netloc, "get", await create_url_without_domain("/service/common/inventory/v1.0/company/job/config", integration_type=integration_type, disable=disable), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getJobCodesMetrics(self, daily_job=None, job_code=None, body=""):
        """Endpoint to return all JobCodes present in Metrics Collection
        :param daily_job : Daily Job Flag : type boolean
        :param job_code : Email Job Code : type string
        """
        payload = {}
        
        if daily_job:
            payload["daily_job"] = daily_job
        
        if job_code:
            payload["job_code"] = job_code
        
        # Parameter validation
        schema = InventoryValidator.getJobCodesMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getJobCodesMetrics"], proccessed_params="""{"required":[],"optional":[{"name":"daily_job","in":"query","description":"Daily Job Flag","required":false,"schema":{"type":"boolean"}},{"name":"job_code","in":"query","description":"Email Job Code","required":false,"schema":{"type":"string"}}],"query":[{"name":"daily_job","in":"query","description":"Daily Job Flag","required":false,"schema":{"type":"boolean"}},{"name":"job_code","in":"query","description":"Email Job Code","required":false,"schema":{"type":"string"}}],"headers":[],"path":[]}""", daily_job=daily_job, job_code=job_code)
        query_string = await create_query_string(daily_job=daily_job, job_code=job_code)
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getJobCodesMetrics"]).netloc, "get", await create_url_without_domain("/service/common/inventory/v1.0/company/email/jobCode", daily_job=daily_job, job_code=job_code), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def saveJobCodesMetrics(self, body=""):
        """Endpoint to save JobCode Metrics
        """
        payload = {}
        
        # Parameter validation
        schema = InventoryValidator.saveJobCodesMetrics()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EmailJobMetrics import EmailJobMetrics
        schema = EmailJobMetrics()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["saveJobCodesMetrics"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["saveJobCodesMetrics"]).netloc, "post", await create_url_without_domain("/service/common/inventory/v1.0/company/email/jobCode", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

class PublicClient:
    def __init__(self, config):
        self.config = config
        self.configuration = Configuration(config)
        self.webhook = Webhook(config)
        self.inventory = Inventory(config)
        
    async def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
