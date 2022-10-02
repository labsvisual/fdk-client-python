"""Platform Client."""

from .PlatformApplicationClient import PlatformApplicationClient
from ..common.aiohttp_helper import AiohttpHelper
from ..common.exceptions import FDKClientValidationError
from ..common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .models.CommonValidator import CommonValidator
from .models.LeadValidator import LeadValidator
from .models.ThemeValidator import ThemeValidator
from .models.UserValidator import UserValidator
from .models.ContentValidator import ContentValidator
from .models.BillingValidator import BillingValidator
from .models.CommunicationValidator import CommunicationValidator
from .models.PaymentValidator import PaymentValidator
from .models.OrderValidator import OrderValidator
from .models.CatalogValidator import CatalogValidator
from .models.CompanyProfileValidator import CompanyProfileValidator
from .models.FileStorageValidator import FileStorageValidator
from .models.ShareValidator import ShareValidator
from .models.InventoryValidator import InventoryValidator
from .models.ConfigurationValidator import ConfigurationValidator
from .models.CartValidator import CartValidator
from .models.RewardsValidator import RewardsValidator
from .models.AnalyticsValidator import AnalyticsValidator
from .models.DiscountValidator import DiscountValidator
from .models.PartnerValidator import PartnerValidator
from .models.WebhookValidator import WebhookValidator
from .models.AuditTrailValidator import AuditTrailValidator



class Common:
    def __init__(self, config):
        self._conf = config
    
    async def searchApplication(self, authorization=None, query=None):
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
        schema = CommonValidator.searchApplication()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/common/configuration/v1.0/application/search-application", """{"required":[],"optional":[{"in":"header","name":"authorization","schema":{"type":"string"}},{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"query":[{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"headers":[{"in":"header","name":"authorization","schema":{"type":"string"}}],"path":[]}""", authorization=authorization, query=query)
        query_string = await create_query_string(authorization=authorization, query=query)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/common/configuration/v1.0/application/search-application", authorization=authorization, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getLocations(self, location_type=None, id=None):
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
        schema = CommonValidator.getLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/common/configuration/v1.0/location", """{"required":[],"optional":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"query":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"headers":[],"path":[]}""", location_type=location_type, id=id)
        query_string = await create_query_string(location_type=location_type, id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/common/configuration/v1.0/location", location_type=location_type, id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

class Lead:
    def __init__(self, config):
        self._conf = config
    
    async def getTickets(self, items=None, filters=None, q=None, status=None, priority=None, category=None, page_no=None, page_size=None):
        """Gets the list of company level tickets and/or ticket filters
        :param items : Decides that the reponse will contain the list of tickets : type boolean
        :param filters : Decides that the reponse will contain the ticket filters : type boolean
        :param q : Search through ticket titles and description : type string
        :param status : Filter tickets on status : type string
        :param priority : Filter tickets on priority : type 
        :param category : Filter tickets on category : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if items:
            payload["items"] = items
        
        if filters:
            payload["filters"] = filters
        
        if q:
            payload["q"] = q
        
        if status:
            payload["status"] = status
        
        if priority:
            payload["priority"] = priority
        
        if category:
            payload["category"] = category
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = LeadValidator.getTickets()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket", """{"required":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}}],"optional":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"name":"page_size","in":"query","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"name":"page_size","in":"query","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}}]}""", items=items, filters=filters, q=q, status=status, priority=priority, category=category, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(items=items, filters=filters, q=q, status=status, priority=priority, category=category, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket", items=items, filters=filters, q=q, status=status, priority=priority, category=category, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createTicket(self, body=""):
        """Creates a company level ticket
        """
        payload = {}
        

        # Parameter validation
        schema = LeadValidator.createTicket()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AddTicketPayload import AddTicketPayload
        schema = AddTicketPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket", """{"required":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getTicket(self, id=None):
        """Retreives ticket details of a company level ticket
        :param id : Tiket ID of the ticket to be fetched : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.getTicket()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Tiket ID of the ticket to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Tiket ID of the ticket to be fetched","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def editTicket(self, id=None, body=""):
        """Edits ticket details of a company level ticket such as status, priority, category, tags, attachments, assigne & ticket content changes
        :param id : Ticket ID of ticket to be edited : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.editTicket()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EditTicketPayload import EditTicketPayload
        schema = EditTicketPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID of ticket to be edited","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID of ticket to be edited","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def createHistory(self, id=None, body=""):
        """Create history for specific company level ticket, this history is seen on ticket detail page, this can be comment, log or rating.
        :param id : Ticket ID for which history is created : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.createHistory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.TicketHistoryPayload import TicketHistoryPayload
        schema = TicketHistoryPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/history", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getTicketHistory(self, id=None):
        """Gets history list for specific company level ticket, this history is seen on ticket detail page, this can be comment, log or rating.
        :param id : Ticket ID for which history is to be fetched : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.getTicketHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is to be fetched","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/history", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getFeedbacks(self, id=None):
        """Gets a list of feedback submitted against that ticket
        :param id : Ticket ID for which feedbacks are to be fetched : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.getFeedbacks()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/feedback", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which feedbacks are to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which feedbacks are to be fetched","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/feedback", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def submitFeedback(self, id=None, body=""):
        """Submit a response for feeback form against that ticket
        :param id : Ticket ID for which feedback is to be submitted : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.submitFeedback()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.TicketFeedbackPayload import TicketFeedbackPayload
        schema = TicketFeedbackPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/feedback", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which feedback is to be submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which feedback is to be submitted","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/ticket/{id}/feedback", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getTokenForVideoRoom(self, unique_name=None):
        """Get Token to join a specific Video Room using it's unqiue name, this Token is your ticket to Room and also creates your identity there.
        :param unique_name : Unique name of video room : type string
        """
        payload = {}
        
        if unique_name:
            payload["unique_name"] = unique_name
        

        # Parameter validation
        schema = LeadValidator.getTokenForVideoRoom()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/video/room/{unique_name}/token", """{"required":[{"name":"company_id","in":"path","description":"Company Id for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of video room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of video room","required":true,"schema":{"type":"string"}}]}""", unique_name=unique_name)
        query_string = await create_query_string(unique_name=unique_name)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/video/room/{unique_name}/token", unique_name=unique_name), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getVideoParticipants(self, unique_name=None):
        """Get participants of a specific Video Room using it's unique name, this can be used to check if people are already there in the room and also to show their names.
        :param unique_name : Unique name of Video Room : type string
        """
        payload = {}
        
        if unique_name:
            payload["unique_name"] = unique_name
        

        # Parameter validation
        schema = LeadValidator.getVideoParticipants()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/video/room/{unique_name}/participants", """{"required":[{"name":"company_id","in":"path","description":"Company Id for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}]}""", unique_name=unique_name)
        query_string = await create_query_string(unique_name=unique_name)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/video/room/{unique_name}/participants", unique_name=unique_name), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getGeneralConfig(self, ):
        """Get general support configuration.
        """
        payload = {}
        

        # Parameter validation
        schema = LeadValidator.getGeneralConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/general-config", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/general-config", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

class Theme:
    def __init__(self, config):
        self._conf = config
    

class User:
    def __init__(self, config):
        self._conf = config
    

class Content:
    def __init__(self, config):
        self._conf = config
    

class Billing:
    def __init__(self, config):
        self._conf = config
    
    async def checkCouponValidity(self, plan=None, coupon_code=None):
        """Check coupon validity.
        :param plan : ID of the plan. : type string
        :param coupon_code : Coupon code. : type string
        """
        payload = {}
        
        if plan:
            payload["plan"] = plan
        
        if coupon_code:
            payload["coupon_code"] = coupon_code
        

        # Parameter validation
        schema = BillingValidator.checkCouponValidity()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/coupon/check-validity", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"query","name":"plan","description":"ID of the plan.","required":true,"schema":{"type":"string","example":"61a5d6ea3e8c230f3aa2c507"}},{"in":"query","name":"coupon_code","description":"Coupon code.","required":true,"schema":{"type":"string","example":"FYND1"}}],"optional":[],"query":[{"in":"query","name":"plan","description":"ID of the plan.","required":true,"schema":{"type":"string","example":"61a5d6ea3e8c230f3aa2c507"}},{"in":"query","name":"coupon_code","description":"Coupon code.","required":true,"schema":{"type":"string","example":"FYND1"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", plan=plan, coupon_code=coupon_code)
        query_string = await create_query_string(plan=plan, coupon_code=coupon_code)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/coupon/check-validity", plan=plan, coupon_code=coupon_code), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createSubscriptionCharge(self, extension_id=None, body=""):
        """Register subscription charge for a seller of your extension.
        :param extension_id : Extension _id : type string
        """
        payload = {}
        
        if extension_id:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = BillingValidator.createSubscriptionCharge()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateSubscriptionCharge import CreateSubscriptionCharge
        schema = CreateSubscriptionCharge()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", extension_id=extension_id)
        query_string = await create_query_string(extension_id=extension_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSubscriptionCharge(self, extension_id=None, subscription_id=None):
        """Get created subscription charge details
        :param extension_id : Extension _id : type string
        :param subscription_id : Subscription charge _id : type string
        """
        payload = {}
        
        if extension_id:
            payload["extension_id"] = extension_id
        
        if subscription_id:
            payload["subscription_id"] = subscription_id
        

        # Parameter validation
        schema = BillingValidator.getSubscriptionCharge()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", extension_id=extension_id, subscription_id=subscription_id)
        query_string = await create_query_string(extension_id=extension_id, subscription_id=subscription_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}", extension_id=extension_id, subscription_id=subscription_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def cancelSubscriptionCharge(self, extension_id=None, subscription_id=None):
        """Cancel subscription and attached charges.
        :param extension_id : Extension _id : type string
        :param subscription_id : Subscription charge _id : type string
        """
        payload = {}
        
        if extension_id:
            payload["extension_id"] = extension_id
        
        if subscription_id:
            payload["subscription_id"] = subscription_id
        

        # Parameter validation
        schema = BillingValidator.cancelSubscriptionCharge()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}/cancel", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", extension_id=extension_id, subscription_id=subscription_id)
        query_string = await create_query_string(extension_id=extension_id, subscription_id=subscription_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscription/{subscription_id}/cancel", extension_id=extension_id, subscription_id=subscription_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getInvoices(self, ):
        """Get invoices.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getInvoices()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/list", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/list", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getInvoiceById(self, invoice_id=None):
        """Get invoice by id.
        :param invoice_id : Invoice id : type string
        """
        payload = {}
        
        if invoice_id:
            payload["invoice_id"] = invoice_id
        

        # Parameter validation
        schema = BillingValidator.getInvoiceById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/{invoice_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"invoice_id","description":"Invoice id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"invoice_id","description":"Invoice id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}]}""", invoice_id=invoice_id)
        query_string = await create_query_string(invoice_id=invoice_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/invoice/{invoice_id}", invoice_id=invoice_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCustomerDetail(self, ):
        """Get subscription customer detail.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getCustomerDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def upsertCustomerDetail(self, body=""):
        """Upsert subscription customer detail.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.upsertCustomerDetail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SubscriptionCustomerCreate import SubscriptionCustomerCreate
        schema = SubscriptionCustomerCreate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/customer-detail", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSubscription(self, ):
        """If subscription is active then it will return is_enabled true and return subscription object. If subscription is not active then is_enabled false and message.

        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getSubscription()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getFeatureLimitConfig(self, ):
        """Get subscription subscription limits.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.getFeatureLimitConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current-limit", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/current-limit", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def activateSubscriptionPlan(self, body=""):
        """It will activate subscription plan for customer
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.activateSubscriptionPlan()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SubscriptionActivateReq import SubscriptionActivateReq
        schema = SubscriptionActivateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/activate", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/activate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def cancelSubscriptionPlan(self, body=""):
        """It will cancel current active subscription.
        """
        payload = {}
        

        # Parameter validation
        schema = BillingValidator.cancelSubscriptionPlan()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CancelSubscriptionReq import CancelSubscriptionReq
        schema = CancelSubscriptionReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/cancel", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/billing/v1.0/company/{self._conf.companyId}/subscription/cancel", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

class Communication:
    def __init__(self, config):
        self._conf = config
    
    async def getSystemNotifications(self, page_no=None, page_size=None):
        """Get system notifications
        :param page_no :  : type integer
        :param page_size :  : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CommunicationValidator.getSystemNotifications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/notification/system-notifications/", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}}],"optional":[{"in":"query","name":"page_no","schema":{"type":"integer","format":"int32","example":1}},{"in":"query","name":"page_size","schema":{"type":"integer","format":"int32","example":10}}],"query":[{"in":"query","name":"page_no","schema":{"type":"integer","format":"int32","example":1}},{"in":"query","name":"page_size","schema":{"type":"integer","format":"int32","example":10}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/notification/system-notifications/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

class Payment:
    def __init__(self, config):
        self._conf = config
    
    async def getAllPayouts(self, unique_external_id=None):
        """Get All Payouts
        :param unique_external_id : Fetch payouts using unique external id : type string
        """
        payload = {}
        
        if unique_external_id:
            payload["unique_external_id"] = unique_external_id
        

        # Parameter validation
        schema = PaymentValidator.getAllPayouts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[{"name":"unique_external_id","in":"query","description":"Fetch payouts using unique external id","schema":{"type":"string"}}],"query":[{"name":"unique_external_id","in":"query","description":"Fetch payouts using unique external id","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", unique_external_id=unique_external_id)
        query_string = await create_query_string(unique_external_id=unique_external_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", unique_external_id=unique_external_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def savePayout(self, body=""):
        """Save Payout
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.savePayout()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PayoutRequest import PayoutRequest
        schema = PayoutRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updatePayout(self, unique_transfer_no=None, body=""):
        """Update Payout
        :param unique_transfer_no : Unique transfer id : type string
        """
        payload = {}
        
        if unique_transfer_no:
            payload["unique_transfer_no"] = unique_transfer_no
        

        # Parameter validation
        schema = PaymentValidator.updatePayout()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PayoutRequest import PayoutRequest
        schema = PayoutRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}]}""", unique_transfer_no=unique_transfer_no)
        query_string = await create_query_string(unique_transfer_no=unique_transfer_no)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def activateAndDectivatePayout(self, unique_transfer_no=None, body=""):
        """Partial Update Payout
        :param unique_transfer_no : Unique transfer id : type string
        """
        payload = {}
        
        if unique_transfer_no:
            payload["unique_transfer_no"] = unique_transfer_no
        

        # Parameter validation
        schema = PaymentValidator.activateAndDectivatePayout()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdatePayoutRequest import UpdatePayoutRequest
        schema = UpdatePayoutRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}]}""", unique_transfer_no=unique_transfer_no)
        query_string = await create_query_string(unique_transfer_no=unique_transfer_no)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def deletePayout(self, unique_transfer_no=None):
        """Delete Payout
        :param unique_transfer_no : Unique transfer id : type string
        """
        payload = {}
        
        if unique_transfer_no:
            payload["unique_transfer_no"] = unique_transfer_no
        

        # Parameter validation
        schema = PaymentValidator.deletePayout()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}]}""", unique_transfer_no=unique_transfer_no)
        query_string = await create_query_string(unique_transfer_no=unique_transfer_no)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/payouts/{unique_transfer_no}", unique_transfer_no=unique_transfer_no), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getSubscriptionPaymentMethod(self, unique_external_id=None):
        """Get all  Subscription  Payment Method
        :param unique_external_id : Unique external id : type string
        """
        payload = {}
        
        if unique_external_id:
            payload["unique_external_id"] = unique_external_id
        

        # Parameter validation
        schema = PaymentValidator.getSubscriptionPaymentMethod()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/subscription/methods", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[{"name":"unique_external_id","in":"query","description":"Unique external id","schema":{"type":"string"}}],"query":[{"name":"unique_external_id","in":"query","description":"Unique external id","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", unique_external_id=unique_external_id)
        query_string = await create_query_string(unique_external_id=unique_external_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/subscription/methods", unique_external_id=unique_external_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def deleteSubscriptionPaymentMethod(self, unique_external_id=None, payment_method_id=None):
        """Uses this api to Delete Subscription Payment Method
        :param unique_external_id :  : type string
        :param payment_method_id :  : type string
        """
        payload = {}
        
        if unique_external_id:
            payload["unique_external_id"] = unique_external_id
        
        if payment_method_id:
            payload["payment_method_id"] = payment_method_id
        

        # Parameter validation
        schema = PaymentValidator.deleteSubscriptionPaymentMethod()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/subscription/methods", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_external_id","in":"query","required":true,"schema":{"type":"string"}},{"name":"payment_method_id","in":"query","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"unique_external_id","in":"query","required":true,"schema":{"type":"string"}},{"name":"payment_method_id","in":"query","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", unique_external_id=unique_external_id, payment_method_id=payment_method_id)
        query_string = await create_query_string(unique_external_id=unique_external_id, payment_method_id=payment_method_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/subscription/methods", unique_external_id=unique_external_id, payment_method_id=payment_method_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getSubscriptionConfig(self, ):
        """Get all  Subscription Config details
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getSubscriptionConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/subscription/configs", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/subscription/configs", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def saveSubscriptionSetupIntent(self, body=""):
        """Uses this api to Save Subscription Setup Intent
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.saveSubscriptionSetupIntent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SaveSubscriptionSetupIntentRequest import SaveSubscriptionSetupIntentRequest
        schema = SaveSubscriptionSetupIntentRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/subscription/setup/intent", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/subscription/setup/intent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def verifyIfscCode(self, ifsc_code=None):
        """Get True/False for correct IFSC Code for adding bank details for refund
        :param ifsc_code :  : type string
        """
        payload = {}
        
        if ifsc_code:
            payload["ifsc_code"] = ifsc_code
        

        # Parameter validation
        schema = PaymentValidator.verifyIfscCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/ifsc-code/verify", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[{"name":"ifsc_code","in":"query","schema":{"type":"string","description":"Fetch bank details for correct ifsc code"}}],"query":[{"name":"ifsc_code","in":"query","schema":{"type":"string","description":"Fetch bank details for correct ifsc code"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}]}""", ifsc_code=ifsc_code)
        query_string = await create_query_string(ifsc_code=ifsc_code)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/ifsc-code/verify", ifsc_code=ifsc_code), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

class Order:
    def __init__(self, config):
        self._conf = config
    
    async def shipmentStatusUpdate(self, body=""):
        """Update Shipment Status
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.shipmentStatusUpdate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateShipmentStatusBody import UpdateShipmentStatusBody
        schema = UpdateShipmentStatusBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/status", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/status", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def activityStatus(self, bag_id=None):
        """Get Activity Status
        :param bag_id : Bag Id : type string
        """
        payload = {}
        
        if bag_id:
            payload["bag_id"] = bag_id
        

        # Parameter validation
        schema = OrderValidator.activityStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/activity/status", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"bag_id","in":"query","description":"Bag Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"bag_id","in":"query","description":"Bag Id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", bag_id=bag_id)
        query_string = await create_query_string(bag_id=bag_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/activity/status", bag_id=bag_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def storeProcessShipmentUpdate(self, body=""):
        """Update Store Process-Shipment
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.storeProcessShipmentUpdate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateProcessShipmenstRequestBody import UpdateProcessShipmenstRequestBody
        schema = UpdateProcessShipmenstRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/store/process-shipments", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/store/process-shipments", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def checkRefund(self, shipment_id=None):
        """Check Refund is available or not
        :param shipment_id : Shipment Id : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.checkRefund()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/check-refund/{shipment_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"Shipment Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"Shipment Id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/check-refund/{shipment_id}", shipment_id=shipment_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def shipmentBagsCanBreak(self, body=""):
        """Decides if Shipment bags can break
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.shipmentBagsCanBreak()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CanBreakRequestBody import CanBreakRequestBody
        schema = CanBreakRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/can-break", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/can-break", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getOrdersByCompanyId(self, page_no=None, page_size=None, from_date=None, to_date=None, is_priority_sort=None, lock_status=None, user_id=None, q=None, stage=None, sales_channels=None, order_id=None, stores=None, deployment_stores=None, status=None, dp=None, filter_type=None):
        """Get Orders
        :param page_no : Current page number : type string
        :param page_size : Page limit : type string
        :param from_date : From Date : type string
        :param to_date : To Date : type string
        :param is_priority_sort : Sorting Order : type boolean
        :param lock_status : Hide Lock Status : type boolean
        :param user_id : User Id : type string
        :param q : Keyword for Search : type string
        :param stage : Specefic Order Stage : type string
        :param sales_channels : Selected Sales Channel : type string
        :param order_id : Order Id : type string
        :param stores : Selected Stores : type string
        :param deployment_stores : Selected Deployment Stores : type string
        :param status : Status of order : type string
        :param dp : Delivery Partners : type string
        :param filter_type : Filters : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if is_priority_sort:
            payload["is_priority_sort"] = is_priority_sort
        
        if lock_status:
            payload["lock_status"] = lock_status
        
        if user_id:
            payload["user_id"] = user_id
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if sales_channels:
            payload["sales_channels"] = sales_channels
        
        if order_id:
            payload["order_id"] = order_id
        
        if stores:
            payload["stores"] = stores
        
        if deployment_stores:
            payload["deployment_stores"] = deployment_stores
        
        if status:
            payload["status"] = status
        
        if dp:
            payload["dp"] = dp
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = OrderValidator.getOrdersByCompanyId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"is_priority_sort","in":"query","description":"Sorting Order","required":false,"schema":{"type":"boolean"}},{"name":"lock_status","in":"query","description":"Hide Lock Status","required":false,"schema":{"type":"boolean"}},{"name":"user_id","in":"query","description":"User Id","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"deployment_stores","in":"query","description":"Selected Deployment Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"dp","in":"query","description":"Delivery Partners","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"is_priority_sort","in":"query","description":"Sorting Order","required":false,"schema":{"type":"boolean"}},{"name":"lock_status","in":"query","description":"Hide Lock Status","required":false,"schema":{"type":"boolean"}},{"name":"user_id","in":"query","description":"User Id","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"deployment_stores","in":"query","description":"Selected Deployment Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"dp","in":"query","description":"Delivery Partners","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, is_priority_sort=is_priority_sort, lock_status=lock_status, user_id=user_id, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, deployment_stores=deployment_stores, status=status, dp=dp, filter_type=filter_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, is_priority_sort=is_priority_sort, lock_status=lock_status, user_id=user_id, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, deployment_stores=deployment_stores, status=status, dp=dp, filter_type=filter_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, is_priority_sort=is_priority_sort, lock_status=lock_status, user_id=user_id, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, deployment_stores=deployment_stores, status=status, dp=dp, filter_type=filter_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOrderLanesCountByCompanyId(self, page_no=None, page_size=None, from_date=None, to_date=None, q=None, stage=None, sales_channels=None, order_id=None, stores=None, status=None, filter_type=None):
        """Get Orders Seperate Lane Count
        :param page_no : Current page number : type string
        :param page_size : Page limit : type string
        :param from_date : From Date : type string
        :param to_date : To Date : type string
        :param q : Keyword for Search : type string
        :param stage : Specefic Order Stage : type string
        :param sales_channels : Selected Sales Channel : type string
        :param order_id : Order Id : type string
        :param stores : Selected Stores : type string
        :param status : Status of order : type string
        :param filter_type : Filters : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if sales_channels:
            payload["sales_channels"] = sales_channels
        
        if order_id:
            payload["order_id"] = order_id
        
        if stores:
            payload["stores"] = stores
        
        if status:
            payload["status"] = status
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = OrderValidator.getOrderLanesCountByCompanyId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/lane-count", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, filter_type=filter_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, filter_type=filter_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/lane-count", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, filter_type=filter_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOrderDetails(self, order_id=None, next=None, previous=None):
        """Get Orders
        :param order_id : Order Id : type string
        :param next : Next : type string
        :param previous : Previous : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if next:
            payload["next"] = next
        
        if previous:
            payload["previous"] = previous
        

        # Parameter validation
        schema = OrderValidator.getOrderDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/details", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"next","in":"query","description":"Next","required":false,"schema":{"type":"string"}},{"name":"previous","in":"query","description":"Previous","required":false,"schema":{"type":"string"}}],"query":[{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"next","in":"query","description":"Next","required":false,"schema":{"type":"string"}},{"name":"previous","in":"query","description":"Previous","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, next=next, previous=previous)
        query_string = await create_query_string(order_id=order_id, next=next, previous=previous)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/details", order_id=order_id, next=next, previous=previous), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getPicklistOrdersByCompanyId(self, page_no=None, page_size=None, from_date=None, to_date=None, q=None, stage=None, sales_channels=None, order_id=None, stores=None, status=None, filter_type=None):
        """Get Orders
        :param page_no : Current page number : type string
        :param page_size : Page limit : type string
        :param from_date : From Date : type string
        :param to_date : To Date : type string
        :param q : Keyword for Search : type string
        :param stage : Specefic Order Stage : type string
        :param sales_channels : Selected Sales Channel : type string
        :param order_id : Order Id : type string
        :param stores : Selected Stores : type string
        :param status : Status of order : type string
        :param filter_type : Filters : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if sales_channels:
            payload["sales_channels"] = sales_channels
        
        if order_id:
            payload["order_id"] = order_id
        
        if stores:
            payload["stores"] = stores
        
        if status:
            payload["status"] = status
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = OrderValidator.getPicklistOrdersByCompanyId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/picklist", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, filter_type=filter_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, filter_type=filter_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/picklist", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, filter_type=filter_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getShipmentAddress(self, shipment_id=None, address_category=None):
        """Get Shipment Address
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param address_category : Category of the address it falls into(billing or delivery). : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if address_category:
            payload["address_category"] = address_category
        

        # Parameter validation
        schema = OrderValidator.getShipmentAddress()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/shipments/{shipment_id}/address/{address_category}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"name":"address_category","in":"path","description":"Category of the address it falls into(billing or delivery).","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"name":"address_category","in":"path","description":"Category of the address it falls into(billing or delivery).","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id, address_category=address_category)
        query_string = await create_query_string(shipment_id=shipment_id, address_category=address_category)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/shipments/{shipment_id}/address/{address_category}", shipment_id=shipment_id, address_category=address_category), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateShipmentAddress(self, shipment_id=None, address_category=None, body=""):
        """Update Shipment Address
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param address_category : Category of the address it falls into(billing or delivery). : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if address_category:
            payload["address_category"] = address_category
        

        # Parameter validation
        schema = OrderValidator.updateShipmentAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateShipmentAddressRequest import UpdateShipmentAddressRequest
        schema = UpdateShipmentAddressRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/shipments/{shipment_id}/address/{address_category}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"name":"address_category","in":"path","description":"Category of the address it falls into(billing or delivery).","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"name":"address_category","in":"path","description":"Category of the address it falls into(billing or delivery).","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id, address_category=address_category)
        query_string = await create_query_string(shipment_id=shipment_id, address_category=address_category)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/shipments/{shipment_id}/address/{address_category}", shipment_id=shipment_id, address_category=address_category), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

class Catalog:
    def __init__(self, config):
        self._conf = config
    
    async def createProductBundle(self, body=""):
        """Create Product Bundle. See `ProductBundleRequest` for the request body parameter need to create a product bundle. On successful request, returns in `ProductBundleRequest` with id
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createProductBundle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ProductBundleRequest import ProductBundleRequest
        schema = ProductBundleRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProductBundle(self, q=None, slug=None):
        """Get all product bundles for a particular company
        :param q : A search string that is searched with product bundle name. : type string
        :param slug : slugs of bundles to be retrieved. : type array
        """
        payload = {}
        
        if q:
            payload["q"] = q
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.getProductBundle()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"q","description":"A search string that is searched with product bundle name.","schema":{"type":"string"},"required":false},{"in":"query","name":"slug","description":"slugs of bundles to be retrieved.","schema":{"type":"array","items":{"type":"string"}},"required":false}],"query":[{"in":"query","name":"q","description":"A search string that is searched with product bundle name.","schema":{"type":"string"},"required":false},{"in":"query","name":"slug","description":"slugs of bundles to be retrieved.","schema":{"type":"array","items":{"type":"string"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", q=q, slug=slug)
        query_string = await create_query_string(q=q, slug=slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/", q=q, slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateProductBundle(self, id=None, body=""):
        """Update a Product Bundle by its id. On successful request, returns the updated product bundle
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateProductBundle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ProductBundleUpdateRequest import ProductBundleUpdateRequest
        schema = ProductBundleUpdateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProductBundleDetail(self, id=None):
        """Get a particular Bundle details by its `id`. If successful, returns a Product bundle resource in the response body specified in `GetProductBundleResponse`
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getProductBundleDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-bundle/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createSizeGuide(self, body=""):
        """This API allows to create a size guide associated to a brand.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createSizeGuide()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ValidateSizeGuide import ValidateSizeGuide
        schema = ValidateSizeGuide()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the size guide is to be created.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the size guide is to be created.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSizeGuides(self, active=None, q=None, tag=None, page_no=None, page_size=None):
        """This API allows to view all the size guides associated to the seller.
        :param active : filter size guide on basis of active, in-active : type boolean
        :param q : Query that is to be searched. : type string
        :param tag : to filter size guide on basis of tag. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if active:
            payload["active"] = active
        
        if q:
            payload["q"] = q
        
        if tag:
            payload["tag"] = tag
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getSizeGuides()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide", """{"required":[{"in":"path","name":"company_id","description":"Id of the company for which the size guides are to be fetched.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"active","description":"filter size guide on basis of active, in-active","schema":{"type":"boolean"},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"tag","description":"to filter size guide on basis of tag.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"query":[{"in":"query","name":"active","description":"filter size guide on basis of active, in-active","schema":{"type":"boolean"},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"tag","description":"to filter size guide on basis of tag.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company for which the size guides are to be fetched.","schema":{"type":"string"},"required":true}]}""", active=active, q=q, tag=tag, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(active=active, q=q, tag=tag, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide", active=active, q=q, tag=tag, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateSizeGuide(self, id=None, body=""):
        """This API allows to edit a size guide.
        :param id : Mongo id of the size guide to be edited : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateSizeGuide()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ValidateSizeGuide import ValidateSizeGuide
        schema = ValidateSizeGuide()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide/{id}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Mongo id of the size guide to be edited","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Mongo id of the size guide to be edited","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSizeGuide(self, id=None):
        """This API helps to get data associated to a size guide.
        :param id : Id of the size guide to be viewed. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getSizeGuide()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide/{id}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to size guide.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Id of the size guide to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to size guide.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Id of the size guide to be viewed.","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/sizeguide/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getSellerInsights(self, seller_app_id=None):
        """Analytics data of catalog and inventory that are being cross-selled.
        :param seller_app_id : Id of the seller application which is serving the invetory/catalog of the company : type string
        """
        payload = {}
        
        if seller_app_id:
            payload["seller_app_id"] = seller_app_id
        

        # Parameter validation
        schema = CatalogValidator.getSellerInsights()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/cross-selling/{seller_app_id}/analytics/insights/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"seller_app_id","description":"Id of the seller application which is serving the invetory/catalog of the company","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"seller_app_id","description":"Id of the seller application which is serving the invetory/catalog of the company","schema":{"type":"string"},"required":true}]}""", seller_app_id=seller_app_id)
        query_string = await create_query_string(seller_app_id=seller_app_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/cross-selling/{seller_app_id}/analytics/insights/", seller_app_id=seller_app_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createMarketplaceOptin(self, marketplace=None, body=""):
        """Use this API to create/update opt-in information for given platform. If successful, returns data in the response body as specified in `OptInPostResponseSchema`
        :param marketplace : The marketplace for which the detail needs to be retrieved. : type string
        """
        payload = {}
        
        if marketplace:
            payload["marketplace"] = marketplace
        

        # Parameter validation
        schema = CatalogValidator.createMarketplaceOptin()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OptInPostRequest import OptInPostRequest
        schema = OptInPostRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/{marketplace}/optin/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true},{"in":"path","name":"marketplace","description":"The marketplace for which the detail needs to be retrieved.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true},{"in":"path","name":"marketplace","description":"The marketplace for which the detail needs to be retrieved.","schema":{"type":"string"},"required":true}]}""", marketplace=marketplace)
        query_string = await create_query_string(marketplace=marketplace)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/{marketplace}/optin/", marketplace=marketplace), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getMarketplaceOptinDetail(self, ):
        """Use this API to fetch opt-in information for all the platforms. If successful, returns a logs in the response body as specified in `GetOptInPlatformSchema`
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getMarketplaceOptinDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/", """{"required":[{"in":"path","name":"company_id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCompanyDetail(self, ):
        """Get the details of the company associated with the given company_id passed.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getCompanyDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-details/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-details/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCompanyBrandDetail(self, is_active=None, q=None, page_no=None, page_size=None, marketplace=None):
        """Get the details of the Brands associated with the given company_id passed.
        :param is_active : The is_active status for the optin id. : type boolean
        :param q : The search value to filter the list. : type boolean
        :param page_no : The number of page for the company id. : type integer
        :param page_size : Number of records that can be seen on the page for the company id. : type integer
        :param marketplace : The marketplace platform associated with the company id. : type string
        """
        payload = {}
        
        if is_active:
            payload["is_active"] = is_active
        
        if q:
            payload["q"] = q
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if marketplace:
            payload["marketplace"] = marketplace
        

        # Parameter validation
        schema = CatalogValidator.getCompanyBrandDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-brand-details/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"is_active","description":"The is_active status for the optin id.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"q","description":"The search value to filter the list.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The number of page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of records that can be seen on the page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"marketplace","description":"The marketplace platform associated with the company id.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"is_active","description":"The is_active status for the optin id.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"q","description":"The search value to filter the list.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The number of page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of records that can be seen on the page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"marketplace","description":"The marketplace platform associated with the company id.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}]}""", is_active=is_active, q=q, page_no=page_no, page_size=page_size, marketplace=marketplace)
        query_string = await create_query_string(is_active=is_active, q=q, page_no=page_no, page_size=page_size, marketplace=marketplace)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-brand-details/", is_active=is_active, q=q, page_no=page_no, page_size=page_size, marketplace=marketplace), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCompanyMetrics(self, ):
        """Get the Company metrics associated with the company ID passed.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getCompanyMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-metrics/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/company-metrics/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getStoreDetail(self, q=None, page_no=None, page_size=None):
        """Get the details of the store associated with the company ID passed.
        :param q : The search related the store for the company id. : type string
        :param page_no : The number of page for the company id. : type integer
        :param page_size : Number of records that can be seen on the page for the company id. : type integer
        """
        payload = {}
        
        if q:
            payload["q"] = q
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getStoreDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/location-details/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"q","description":"The search related the store for the company id.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The number of page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of records that can be seen on the page for the company id.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"q","description":"The search related the store for the company id.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The number of page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of records that can be seen on the page for the company id.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}]}""", q=q, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(q=q, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/marketplaces/location-details/", q=q, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getGenderAttribute(self, attribute_slug=None):
        """This API allows to view the gender attribute details.
        :param attribute_slug : slug of the attribute for which you want to view the genders : type string
        """
        payload = {}
        
        if attribute_slug:
            payload["attribute_slug"] = attribute_slug
        

        # Parameter validation
        schema = CatalogValidator.getGenderAttribute()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-attributes/{attribute_slug}", """{"required":[{"in":"path","name":"company_id","description":"company for which you want to view the genders","schema":{"type":"integer"},"required":true},{"in":"path","name":"attribute_slug","description":"slug of the attribute for which you want to view the genders","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company for which you want to view the genders","schema":{"type":"integer"},"required":true},{"in":"path","name":"attribute_slug","description":"slug of the attribute for which you want to view the genders","schema":{"type":"string"},"required":true}]}""", attribute_slug=attribute_slug)
        query_string = await create_query_string(attribute_slug=attribute_slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-attributes/{attribute_slug}", attribute_slug=attribute_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def listProductTemplateCategories(self, departments=None, item_type=None):
        """Allows you to list all product categories values for the departments specified
        :param departments : A `department` is name of a departments whose category needs to be listed. Can specify multiple departments. : type string
        :param item_type : An `item_type` is the type of item, it can be `set`, `standard`, `digital`, etc. : type string
        """
        payload = {}
        
        if departments:
            payload["departments"] = departments
        
        if item_type:
            payload["item_type"] = item_type
        

        # Parameter validation
        schema = CatalogValidator.listProductTemplateCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/categories/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"departments","description":"A `department` is name of a departments whose category needs to be listed. Can specify multiple departments.","schema":{"type":"string"},"required":true},{"in":"query","name":"item_type","description":"An `item_type` is the type of item, it can be `set`, `standard`, `digital`, etc.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"departments","description":"A `department` is name of a departments whose category needs to be listed. Can specify multiple departments.","schema":{"type":"string"},"required":true},{"in":"query","name":"item_type","description":"An `item_type` is the type of item, it can be `set`, `standard`, `digital`, etc.","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", departments=departments, item_type=item_type)
        query_string = await create_query_string(departments=departments, item_type=item_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/categories/", departments=departments, item_type=item_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createDepartments(self, body=""):
        """Create departments using the API.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createDepartments()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DepartmentCreateUpdate import DepartmentCreateUpdate
        schema = DepartmentCreateUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def listDepartmentsData(self, page_no=None, page_size=None, name=None, search=None, is_active=None):
        """Allows you to list all departments, also can search using name and filter active and incative departments, and item type.
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param name : Can search departments by passing name. : type string
        :param search : Can search departments by passing name of the department in search parameter. : type string
        :param is_active : Can query for departments based on whether they are active or inactive. : type boolean
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if name:
            payload["name"] = name
        
        if search:
            payload["search"] = search
        
        if is_active:
            payload["is_active"] = is_active
        

        # Parameter validation
        schema = CatalogValidator.listDepartmentsData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer"},"required":false},{"in":"query","name":"name","description":"Can search departments by passing name.","schema":{"type":"string"},"required":false},{"in":"query","name":"search","description":"Can search departments by passing name of the department in search parameter.","schema":{"type":"string"},"required":false},{"in":"query","name":"is_active","description":"Can query for departments based on whether they are active or inactive.","schema":{"type":"boolean"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer"},"required":false},{"in":"query","name":"name","description":"Can search departments by passing name.","schema":{"type":"string"},"required":false},{"in":"query","name":"search","description":"Can search departments by passing name of the department in search parameter.","schema":{"type":"string"},"required":false},{"in":"query","name":"is_active","description":"Can query for departments based on whether they are active or inactive.","schema":{"type":"boolean"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", page_no=page_no, page_size=page_size, name=name, search=search, is_active=is_active)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, name=name, search=search, is_active=is_active)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/", page_no=page_no, page_size=page_size, name=name, search=search, is_active=is_active), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateDepartment(self, uid=None, body=""):
        """Update the department by their uid using this API.
        :param uid : A `uid` is a unique identifier of a department. : type string
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.updateDepartment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DepartmentCreateUpdate import DepartmentCreateUpdate
        schema = DepartmentCreateUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/{uid}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"A `uid` is a unique identifier of a department.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"A `uid` is a unique identifier of a department.","schema":{"type":"string"},"required":true}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/{uid}/", uid=uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getDepartmentData(self, uid=None):
        """Allows you to get department data, by uid.
        :param uid : A `uid` is a unique identifier of a department. : type string
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.getDepartmentData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/{uid}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"A `uid` is a unique identifier of a department.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"A `uid` is a unique identifier of a department.","schema":{"type":"string"},"required":true}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/departments/{uid}/", uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def listProductTemplate(self, department=None):
        """Allows you to list all product templates, also can filter by department
        :param department : A `department` is the name of a particular department. : type string
        """
        payload = {}
        
        if department:
            payload["department"] = department
        

        # Parameter validation
        schema = CatalogValidator.listProductTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"department","description":"A `department` is the name of a particular department.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"department","description":"A `department` is the name of a particular department.","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", department=department)
        query_string = await create_query_string(department=department)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/", department=department), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def validateProductTemplate(self, slug=None):
        """Allows you to list all product templates validation values for all the fields present in the database
        :param slug : A `slug` is a unique identifier for a particular template. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.validateProductTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/{slug}/validation/schema/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a unique identifier for a particular template.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a unique identifier for a particular template.","schema":{"type":"string"},"required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/{slug}/validation/schema/", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def downloadProductTemplateViews(self, slug=None):
        """Allows you to download product template data
        :param slug : A `slug` is a unique identifier for a particular template. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.downloadProductTemplateViews()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/{slug}/download/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a unique identifier for a particular template.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a unique identifier for a particular template.","schema":{"type":"string"},"required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/templates/{slug}/download/", slug=slug), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def downloadProductTemplateView(self, item_type=None):
        """Allows you to download product template data
        :param item_type : An `item_type` defines the type of item. : type string
        """
        payload = {}
        
        if item_type:
            payload["item_type"] = item_type
        

        # Parameter validation
        schema = CatalogValidator.downloadProductTemplateView()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/templates/download/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"item_type","description":"An `item_type` defines the type of item.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"item_type","description":"An `item_type` defines the type of item.","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", item_type=item_type)
        query_string = await create_query_string(item_type=item_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/templates/download/", item_type=item_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def validateProductTemplateSchema(self, item_type=None):
        """Allows you to list all product templates validation values for all the fields present in the database
        :param item_type : An `item_type` defines the type of item. The default value is standard. : type string
        """
        payload = {}
        
        if item_type:
            payload["item_type"] = item_type
        

        # Parameter validation
        schema = CatalogValidator.validateProductTemplateSchema()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/templates/validation/schema/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"item_type","description":"An `item_type` defines the type of item. The default value is standard.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"item_type","description":"An `item_type` defines the type of item. The default value is standard.","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", item_type=item_type)
        query_string = await create_query_string(item_type=item_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/templates/validation/schema/", item_type=item_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def listHSNCodes(self, ):
        """Allows you to list all hsn Codes
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.listHSNCodes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/hsn/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/hsn/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def listProductTemplateExportDetails(self, ):
        """Can view details including trigger data, task id , etc.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.listProductTemplateExportDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/downloads/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/downloads/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def listTemplateBrandTypeValues(self, filter=None):
        """The filter type query parameter defines what type of data to return. The type of query returns the valid values for the same
        :param filter : A `filter` is the unique identifier of the type of value required. : type string
        """
        payload = {}
        
        if filter:
            payload["filter"] = filter
        

        # Parameter validation
        schema = CatalogValidator.listTemplateBrandTypeValues()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/downloads/configuration/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"filter","description":"A `filter` is the unique identifier of the type of value required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"filter","description":"A `filter` is the unique identifier of the type of value required.","schema":{"type":"string"},"required":true}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", filter=filter)
        query_string = await create_query_string(filter=filter)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/downloads/configuration/", filter=filter), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createCategories(self, body=""):
        """This API lets user create product categories
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCategories()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CategoryRequestBody import CategoryRequestBody
        schema = CategoryRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def listCategories(self, level=None, departments=None, q=None, page_no=None, page_size=None):
        """This API gets meta associated to product categories.
        :param level : Get category for multiple levels : type string
        :param departments : Get category for multiple departments filtered : type string
        :param q : Get multiple categories filtered by search string : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if level:
            payload["level"] = level
        
        if departments:
            payload["departments"] = departments
        
        if q:
            payload["q"] = q
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.listCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"level","description":"Get category for multiple levels","schema":{"type":"string"},"required":false},{"in":"query","name":"departments","description":"Get category for multiple departments filtered","schema":{"type":"string"},"required":false},{"in":"query","name":"q","description":"Get multiple categories filtered by search string","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"level","description":"Get category for multiple levels","schema":{"type":"string"},"required":false},{"in":"query","name":"departments","description":"Get category for multiple departments filtered","schema":{"type":"string"},"required":false},{"in":"query","name":"q","description":"Get multiple categories filtered by search string","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", level=level, departments=departments, q=q, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(level=level, departments=departments, q=q, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/", level=level, departments=departments, q=q, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateCategory(self, uid=None, body=""):
        """Update a product category using this apu
        :param uid : Category unique id : type string
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.updateCategory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CategoryRequestBody import CategoryRequestBody
        schema = CategoryRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/{uid}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"Category unique id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"Category unique id","schema":{"type":"string"},"required":true}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/{uid}/", uid=uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getCategoryData(self, uid=None):
        """This API gets meta associated to product categories.
        :param uid : Category unique id : type string
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.getCategoryData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/{uid}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"Category unique id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"Category unique id","schema":{"type":"string"},"required":true}]}""", uid=uid)
        query_string = await create_query_string(uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/category/{uid}/", uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createProduct(self, body=""):
        """This API allows to create product.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ProductCreateUpdate import ProductCreateUpdate
        schema = ProductCreateUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProducts(self, brand_ids=None, category_ids=None, item_ids=None, department_ids=None, item_code=None, q=None, tags=None, page_no=None, page_size=None):
        """This API gets meta associated to products.
        :param brand_ids : Get multiple products filtered by Brand Ids : type array
        :param category_ids : Get multiple products filtered by Category Ids : type array
        :param item_ids : Get multiple products filtered by Item Ids : type array
        :param department_ids : Get multiple products filtered by Department Ids : type array
        :param item_code : Get multiple products filtered by Item Code : type array
        :param q : Get multiple products filtered by q string : type string
        :param tags : Get multiple products filtered by tags : type array
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if brand_ids:
            payload["brand_ids"] = brand_ids
        
        if category_ids:
            payload["category_ids"] = category_ids
        
        if item_ids:
            payload["item_ids"] = item_ids
        
        if department_ids:
            payload["department_ids"] = department_ids
        
        if item_code:
            payload["item_code"] = item_code
        
        if q:
            payload["q"] = q
        
        if tags:
            payload["tags"] = tags
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/", """{"required":[{"in":"path","name":"company_id","description":"Get list of products filtered by company Id","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"item_ids","description":"Get multiple products filtered by Item Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"item_code","description":"Get multiple products filtered by Item Code","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"q","description":"Get multiple products filtered by q string","schema":{"type":"string"},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"query":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"item_ids","description":"Get multiple products filtered by Item Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"item_code","description":"Get multiple products filtered by Item Code","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"q","description":"Get multiple products filtered by q string","schema":{"type":"string"},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Get list of products filtered by company Id","schema":{"type":"integer"},"required":true}]}""", brand_ids=brand_ids, category_ids=category_ids, item_ids=item_ids, department_ids=department_ids, item_code=item_code, q=q, tags=tags, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(brand_ids=brand_ids, category_ids=category_ids, item_ids=item_ids, department_ids=department_ids, item_code=item_code, q=q, tags=tags, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/", brand_ids=brand_ids, category_ids=category_ids, item_ids=item_ids, department_ids=department_ids, item_code=item_code, q=q, tags=tags, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getProductAttributes(self, category=None, filter=None):
        """This API allows to list all the attributes by their l3_categories.
        :param category : It is the name of the l3 cateogry : type string
        :param filter : If true, returns filtered values, else returns all the attributes : type boolean
        """
        payload = {}
        
        if category:
            payload["category"] = category
        
        if filter:
            payload["filter"] = filter
        

        # Parameter validation
        schema = CatalogValidator.getProductAttributes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-attributes/", """{"required":[{"in":"path","name":"company_id","description":"company for which you want to view the genders","schema":{"type":"integer"},"required":true},{"in":"query","name":"category","description":"It is the name of the l3 cateogry","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"filter","description":"If true, returns filtered values, else returns all the attributes","schema":{"type":"boolean"},"required":false}],"query":[{"in":"query","name":"category","description":"It is the name of the l3 cateogry","schema":{"type":"string"},"required":true},{"in":"query","name":"filter","description":"If true, returns filtered values, else returns all the attributes","schema":{"type":"boolean"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"company for which you want to view the genders","schema":{"type":"integer"},"required":true}]}""", category=category, filter=filter)
        query_string = await create_query_string(category=category, filter=filter)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/product-attributes/", category=category, filter=filter), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def deleteProduct(self, item_id=None):
        """This API allows to delete product.
        :param item_id : Id of the product to be updated. : type integer
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        

        # Parameter validation
        schema = CatalogValidator.deleteProduct()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company associated to product that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product to be updated.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the company associated to product that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product to be updated.","schema":{"type":"integer"},"required":true}]}""", item_id=item_id)
        query_string = await create_query_string(item_id=item_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/", item_id=item_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def editProduct(self, item_id=None, body=""):
        """This API allows to edit product.
        :param item_id : Id of the product to be updated. : type integer
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        

        # Parameter validation
        schema = CatalogValidator.editProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ProductCreateUpdate import ProductCreateUpdate
        schema = ProductCreateUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product to be updated.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product to be updated.","schema":{"type":"integer"},"required":true}]}""", item_id=item_id)
        query_string = await create_query_string(item_id=item_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/", item_id=item_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProduct(self, item_code=None, item_id=None, brand_uid=None):
        """This API helps to get data associated to a particular product.
        :param item_code : Item code of the product. : type string
        :param item_id : Item Id of the product. : type integer
        :param brand_uid : Brand Id of the product. : type integer
        """
        payload = {}
        
        if item_code:
            payload["item_code"] = item_code
        
        if item_id:
            payload["item_id"] = item_id
        
        if brand_uid:
            payload["brand_uid"] = brand_uid
        

        # Parameter validation
        schema = CatalogValidator.getProduct()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the product.","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"item_code","description":"Item code of the product.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_uid","description":"Brand Id of the product.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"item_code","description":"Item code of the product.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_uid","description":"Brand Id of the product.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the product.","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product.","schema":{"type":"integer"},"required":true}]}""", item_code=item_code, item_id=item_id, brand_uid=brand_uid)
        query_string = await create_query_string(item_code=item_code, item_id=item_id, brand_uid=brand_uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/", item_code=item_code, item_id=item_id, brand_uid=brand_uid), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getProductValidation(self, ):
        """This API validates product data.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getProductValidation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/validation/", """{"required":[{"in":"path","name":"company_id","description":"Validates data against given company","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Validates data against given company","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/validation/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getProductSize(self, item_code=None, item_id=None, brand_uid=None, uid=None):
        """This API helps to get data associated to a particular product size.
        :param item_code : Item code of the product size. : type string
        :param item_id : Item Id of the product size. : type integer
        :param brand_uid : Brand Id of the product size. : type integer
        :param uid : Id of the product size. : type integer
        """
        payload = {}
        
        if item_code:
            payload["item_code"] = item_code
        
        if item_id:
            payload["item_id"] = item_id
        
        if brand_uid:
            payload["brand_uid"] = brand_uid
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.getProductSize()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the product size.","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product size.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"item_code","description":"Item code of the product size.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_uid","description":"Brand Id of the product size.","schema":{"type":"integer"},"required":false},{"in":"query","name":"uid","description":"Id of the product size.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"item_code","description":"Item code of the product size.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_uid","description":"Brand Id of the product size.","schema":{"type":"integer"},"required":false},{"in":"query","name":"uid","description":"Id of the product size.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the product size.","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product size.","schema":{"type":"integer"},"required":true}]}""", item_code=item_code, item_id=item_id, brand_uid=brand_uid, uid=uid)
        query_string = await create_query_string(item_code=item_code, item_id=item_id, brand_uid=brand_uid, uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/", item_code=item_code, item_id=item_id, brand_uid=brand_uid, uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createBulkProductUploadJob(self, body=""):
        """This API helps to create a bulk products upload job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createBulkProductUploadJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.BulkJob import BulkJob
        schema = BulkJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProductBulkUploadHistory(self, page_no=None, page_size=None):
        """This API helps to get bulk product upload jobs data.
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getProductBulkUploadHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk", """{"required":[{"in":"path","name":"company_id","description":"Company Id of of which Product Bulk Upload History to be obtained.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of of which Product Bulk Upload History to be obtained.","schema":{"type":"integer"},"required":true}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def deleteProductBulkJob(self, batch_id=None):
        """This API allows to delete bulk product job associated with company.
        :param batch_id : Batch Id of the bulk product job to be deleted. : type integer
        """
        payload = {}
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = CatalogValidator.deleteProductBulkJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk/{batch_id}", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company associated to size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk product job to be deleted.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the company associated to size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk product job to be deleted.","schema":{"type":"integer"},"required":true}]}""", batch_id=batch_id)
        query_string = await create_query_string(batch_id=batch_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk/{batch_id}", batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createProductsInBulk(self, batch_id=None, body=""):
        """This API helps to create products in bulk push to kafka for approval/creation.
        :param batch_id : Batch Id in which assets to be uploaded. : type string
        """
        payload = {}
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = CatalogValidator.createProductsInBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.BulkProductRequest import BulkProductRequest
        schema = BulkProductRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk/{batch_id}", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id in which assets to be uploaded.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id in which assets to be uploaded.","schema":{"type":"string"},"required":true}]}""", batch_id=batch_id)
        query_string = await create_query_string(batch_id=batch_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/bulk/{batch_id}", batch_id=batch_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProductTags(self, ):
        """This API helps to get tags data associated to a particular company.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getProductTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/tags", """{"required":[{"in":"path","name":"company_id","description":"Company Id for which tags to be fetched.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id for which tags to be fetched.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/tags", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createProductAssetsInBulk(self, body=""):
        """This API helps to create a bulk asset upload job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createProductAssetsInBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ProductBulkAssets import ProductBulkAssets
        schema = ProductBulkAssets()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/assets/bulk/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/assets/bulk/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getProductAssetsInBulk(self, page_no=None, page_size=None):
        """This API helps to get bulk asset jobs data associated to a particular company.
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getProductAssetsInBulk()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/assets/bulk/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the product size.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the product size.","schema":{"type":"integer"},"required":true}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/assets/bulk/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def deleteSize(self, item_id=None, size=None):
        """This API allows to delete size associated with product.
        :param item_id : Item Id of the product associated with size to be deleted. : type integer
        :param size : size to be deleted. : type integer
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if size:
            payload["size"] = size
        

        # Parameter validation
        schema = CatalogValidator.deleteSize()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company associated to size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product associated with size to be deleted.","schema":{"type":"integer"},"required":true},{"in":"path","name":"size","description":"size to be deleted.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the company associated to size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product associated with size to be deleted.","schema":{"type":"integer"},"required":true},{"in":"path","name":"size","description":"size to be deleted.","schema":{"type":"integer"},"required":true}]}""", item_id=item_id, size=size)
        query_string = await create_query_string(item_id=item_id, size=size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", item_id=item_id, size=size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def addInventory(self, item_id=None, size=None, body=""):
        """This API allows add Inventory for particular size and store.
        :param item_id : Item code of the product of which size is to be get. : type number
        :param size : Size in which inventory is to be added. : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if size:
            payload["size"] = size
        

        # Parameter validation
        schema = CatalogValidator.addInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.InventoryRequest import InventoryRequest
        schema = InventoryRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"number"},"required":true},{"in":"path","name":"size","description":"Size in which inventory is to be added.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"number"},"required":true},{"in":"path","name":"size","description":"Size in which inventory is to be added.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, size=size)
        query_string = await create_query_string(item_id=item_id, size=size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", item_id=item_id, size=size), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getInventoryBySize(self, item_id=None, size=None, page_no=None, page_size=None, q=None, sellable=None):
        """This API allows get Inventory data for particular company grouped by size and store.
        :param item_id : Item code of the product of which size is to be get. : type string
        :param size : Size of which inventory is to get. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search with help of store code. : type string
        :param sellable : Filter on whether product is in stock or not. : type boolean
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if size:
            payload["size"] = size
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if sellable:
            payload["sellable"] = sellable
        

        # Parameter validation
        schema = CatalogValidator.getInventoryBySize()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"Size of which inventory is to get.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"sellable","description":"Filter on whether product is in stock or not.","schema":{"type":"boolean","default":false},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"sellable","description":"Filter on whether product is in stock or not.","schema":{"type":"boolean","default":false},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"Size of which inventory is to get.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable)
        query_string = await create_query_string(item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}", item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getInventoryBySizeIdentifier(self, item_id=None, size_identifier=None, page_no=None, page_size=None, q=None, location_ids=None):
        """This API allows get Inventory data for particular company grouped by size and store.
        :param item_id : Item code of the product of which size is to be get. : type string
        :param size_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search with help of store code. : type string
        :param location_ids : Search by store ids. : type array
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if size_identifier:
            payload["size_identifier"] = size_identifier
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if location_ids:
            payload["location_ids"] = location_ids
        

        # Parameter validation
        schema = CatalogValidator.getInventoryBySizeIdentifier()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/inventory/{size_identifier}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"string"},"required":true},{"in":"path","name":"size_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"location_ids","description":"Search by store ids.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"location_ids","description":"Search by store ids.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"string"},"required":true},{"in":"path","name":"size_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)
        query_string = await create_query_string(item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/inventory/{size_identifier}", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def deleteInventory(self, size=None, item_id=None, location_id=None):
        """This API allows to delete inventory of a particular product for particular company.
        :param size : size that is to be deleted. : type string
        :param item_id : Id of the product associated with Inventory to be deleted. : type integer
        :param location_id : Location ID of store of which inventory is to be deleted. : type number
        """
        payload = {}
        
        if size:
            payload["size"] = size
        
        if item_id:
            payload["item_id"] = item_id
        
        if location_id:
            payload["location_id"] = location_id
        

        # Parameter validation
        schema = CatalogValidator.deleteInventory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}/location/{location_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company associated with Inventory that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product associated with Inventory to be deleted.","schema":{"type":"integer"},"required":true},{"in":"path","name":"location_id","description":"Location ID of store of which inventory is to be deleted.","schema":{"type":"number"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the company associated with Inventory that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product associated with Inventory to be deleted.","schema":{"type":"integer"},"required":true},{"in":"path","name":"location_id","description":"Location ID of store of which inventory is to be deleted.","schema":{"type":"number"},"required":true}]}""", size=size, item_id=item_id, location_id=location_id)
        query_string = await create_query_string(size=size, item_id=item_id, location_id=location_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/products/{item_id}/sizes/{size}/location/{location_id}/", size=size, item_id=item_id, location_id=location_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createBulkInventoryJob(self, body=""):
        """This API helps to create a bulk Inventory upload job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createBulkInventoryJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.BulkJob import BulkJob
        schema = BulkJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which Inventory to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which Inventory to be uploaded.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getInventoryBulkUploadHistory(self, page_no=None, page_size=None):
        """This API helps to get bulk Inventory upload jobs data.
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getInventoryBulkUploadHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of of which Inventory Bulk Upload History to be obtained.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of of which Inventory Bulk Upload History to be obtained.","schema":{"type":"integer"},"required":true}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def deleteBulkInventoryJob(self, batch_id=None):
        """This API allows to delete bulk Inventory job associated with company.
        :param batch_id : Batch Id of the bulk delete job. : type string
        """
        payload = {}
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = CatalogValidator.deleteBulkInventoryJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/{batch_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company of which bulk Inventory job is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk delete job.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id of the company of which bulk Inventory job is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk delete job.","schema":{"type":"string"},"required":true}]}""", batch_id=batch_id)
        query_string = await create_query_string(batch_id=batch_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/{batch_id}/", batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createBulkInventory(self, batch_id=None, body=""):
        """This API helps to create products in bulk push to kafka for approval/creation.
        :param batch_id : Batch Id of the bulk create job. : type string
        """
        payload = {}
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = CatalogValidator.createBulkInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.InventoryBulkRequest import InventoryBulkRequest
        schema = InventoryBulkRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/{batch_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which Inventory is to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk create job.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which Inventory is to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk create job.","schema":{"type":"string"},"required":true}]}""", batch_id=batch_id)
        query_string = await create_query_string(batch_id=batch_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/bulk/{batch_id}/", batch_id=batch_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def createInventoryExportJob(self, body=""):
        """This API helps to create a Inventory export job.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createInventoryExportJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.InventoryExportRequest import InventoryExportRequest
        schema = InventoryExportRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getInventoryExport(self, ):
        """This API helps to get Inventory export history.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getInventoryExport()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def exportInventoryConfig(self, filter_type=None):
        """This API allows get List of different filters like brand, store, and type for inventory export.
        :param filter_type : filter type from any one of ['brand', 'store', 'type'] : type string
        """
        payload = {}
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = CatalogValidator.exportInventoryConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/configuration/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"filter_type","description":"filter type from any one of ['brand', 'store', 'type']","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"filter_type","description":"filter type from any one of ['brand', 'store', 'type']","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}]}""", filter_type=filter_type)
        query_string = await create_query_string(filter_type=filter_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/inventory/download/configuration/", filter_type=filter_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def deleteRealtimeInventory(self, item_id=None, seller_identifier=None, body=""):
        """This API allows add Inventory for particular size and store.
        :param item_id : Item code of the product of which size is to be get. : type number
        :param seller_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get. : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if seller_identifier:
            payload["seller_identifier"] = seller_identifier
        

        # Parameter validation
        schema = CatalogValidator.deleteRealtimeInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.InventoryRequestSchemaV2 import InventoryRequestSchemaV2
        schema = InventoryRequestSchemaV2()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/inventory/{seller_identifier}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"number"},"required":true},{"in":"path","name":"seller_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"number"},"required":true},{"in":"path","name":"seller_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, seller_identifier=seller_identifier)
        query_string = await create_query_string(item_id=item_id, seller_identifier=seller_identifier)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/inventory/{seller_identifier}/", item_id=item_id, seller_identifier=seller_identifier), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateRealtimeInventory(self, item_id=None, seller_identifier=None, body=""):
        """This API allows add Inventory for particular size and store.
        :param item_id : Item code of the product of which size is to be get. : type number
        :param seller_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get. : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if seller_identifier:
            payload["seller_identifier"] = seller_identifier
        

        # Parameter validation
        schema = CatalogValidator.updateRealtimeInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.InventoryRequestSchemaV2 import InventoryRequestSchemaV2
        schema = InventoryRequestSchemaV2()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/inventory/{seller_identifier}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"number"},"required":true},{"in":"path","name":"seller_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"number"},"required":true},{"in":"path","name":"seller_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, seller_identifier=seller_identifier)
        query_string = await create_query_string(item_id=item_id, seller_identifier=seller_identifier)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/products/{item_id}/inventory/{seller_identifier}/", item_id=item_id, seller_identifier=seller_identifier), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateInventories(self, body=""):
        """This API allows add Inventory for particular size and store.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.updateInventories()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.InventoryRequestSchemaV2 import InventoryRequestSchemaV2
        schema = InventoryRequestSchemaV2()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/inventory/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def createHsnCode(self, body=""):
        """Create Hsn Code.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createHsnCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.HsnUpsert import HsnUpsert
        schema = HsnUpsert()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAllHsnCodes(self, page_no=None, page_size=None, q=None):
        """Hsn Code List.
        :param page_no : page no : type integer
        :param page_size : page size : type integer
        :param q : search using hsn code. : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.getAllHsnCodes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"page no","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"search using hsn code.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"page no","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"search using hsn code.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true}]}""", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateHsnCode(self, id=None, body=""):
        """Update Hsn Code.
        :param id : Unique id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateHsnCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.HsnUpsert import HsnUpsert
        schema = HsnUpsert()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/{id}/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Unique id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Unique id","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getHsnCode(self, id=None):
        """Fetch Hsn Code.
        :param id : Unique id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getHsnCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/{id}/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Unique id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Unique id","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def bulkHsnCode(self, body=""):
        """Bulk Create or Update Hsn Code.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.bulkHsnCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.BulkHsnUpsert import BulkHsnUpsert
        schema = BulkHsnUpsert()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/bulk/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/hsn/bulk/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAllProductHsnCodes(self, page_no=None, page_size=None, q=None, type=None):
        """Hsn Code List.
        :param page_no : page no : type integer
        :param page_size : page size : type integer
        :param q : search using hsn code, description, reporting_hsn : type string
        :param type : search using type : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if type:
            payload["type"] = type
        

        # Parameter validation
        schema = CatalogValidator.getAllProductHsnCodes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/hsn/", """{"required":[{"in":"path","name":"company_id","description":"Company Id for which HSN codes needs to be fetched","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"page no","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"search using hsn code, description, reporting_hsn","schema":{"type":"string"},"required":false},{"in":"query","name":"type","description":"search using type","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"page no","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"search using hsn code, description, reporting_hsn","schema":{"type":"string"},"required":false},{"in":"query","name":"type","description":"search using type","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company Id for which HSN codes needs to be fetched","schema":{"type":"integer"},"required":true}]}""", page_no=page_no, page_size=page_size, q=q, type=type, )
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, type=type, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/hsn/", page_no=page_no, page_size=page_size, q=q, type=type, ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getSingleProductHSNCode(self, reporting_hsn=None):
        """Hsn Code List.
        :param reporting_hsn : reporting_hsn : type string
        """
        payload = {}
        
        if reporting_hsn:
            payload["reporting_hsn"] = reporting_hsn
        

        # Parameter validation
        schema = CatalogValidator.getSingleProductHSNCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/hsn/{reporting_hsn}", """{"required":[{"in":"path","name":"reporting_hsn","description":"reporting_hsn","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"Company Id for which HSN codes needs to be fetched","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"reporting_hsn","description":"reporting_hsn","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"Company Id for which HSN codes needs to be fetched","schema":{"type":"integer"},"required":true}]}""", reporting_hsn=reporting_hsn, )
        query_string = await create_query_string(reporting_hsn=reporting_hsn, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v2.0/company/{self._conf.companyId}/hsn/{reporting_hsn}", reporting_hsn=reporting_hsn, ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOptimalLocations(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getOptimalLocations()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AssignStore import AssignStore
        schema = AssignStore()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/location/reassign/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/location/reassign/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

class CompanyProfile:
    def __init__(self, config):
        self._conf = config
    
    async def cbsOnboardGet(self, ):
        """This API allows to view the company profile of the seller account.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.cbsOnboardGet()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateCompany(self, body=""):
        """This API allows to edit the company profile of the seller account.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.updateCompany()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateCompany import UpdateCompany
        schema = UpdateCompany()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getCompanyMetrics(self, ):
        """This API allows to view the company metrics, i.e. the status of its brand and stores. Also its allows to view the number of products, company documents & store documents which are verified and unverified.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.getCompanyMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/metrics", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/metrics", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getBrand(self, brand_id=None):
        """This API helps to get data associated to a particular brand.
        :param brand_id : Id of the brand to be viewed. : type string
        """
        payload = {}
        
        if brand_id:
            payload["brand_id"] = brand_id
        

        # Parameter validation
        schema = CompanyProfileValidator.getBrand()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/brand/{brand_id}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to brand that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"brand_id","description":"Id of the brand to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to brand that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"brand_id","description":"Id of the brand to be viewed.","schema":{"type":"string"},"required":true}]}""", brand_id=brand_id)
        query_string = await create_query_string(brand_id=brand_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/brand/{brand_id}", brand_id=brand_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def editBrand(self, brand_id=None, body=""):
        """This API allows to edit meta of a brand.
        :param brand_id : Id of the brand to be viewed. : type string
        """
        payload = {}
        
        if brand_id:
            payload["brand_id"] = brand_id
        

        # Parameter validation
        schema = CompanyProfileValidator.editBrand()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateUpdateBrandRequestSerializer import CreateUpdateBrandRequestSerializer
        schema = CreateUpdateBrandRequestSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/brand/{brand_id}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to brand that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"brand_id","description":"Id of the brand to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to brand that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"brand_id","description":"Id of the brand to be viewed.","schema":{"type":"string"},"required":true}]}""", brand_id=brand_id)
        query_string = await create_query_string(brand_id=brand_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/brand/{brand_id}", brand_id=brand_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def createBrand(self, body=""):
        """This API allows to create a brand associated to a company.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.createBrand()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateUpdateBrandRequestSerializer import CreateUpdateBrandRequestSerializer
        schema = CreateUpdateBrandRequestSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/brand/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/brand/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getBrands(self, page_no=None, page_size=None, q=None):
        """This API helps to get view brands associated to a particular company.
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param q : Search term for name. : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = CompanyProfileValidator.getBrands()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/company-brand", """{"required":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":20},"required":false},{"in":"query","name":"q","description":"Search term for name.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":20},"required":false},{"in":"query","name":"q","description":"Search term for name.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true}]}""", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/company-brand", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createCompanyBrandMapping(self, body=""):
        """This API allows to create a company brand mapping, for a already existing brand in the system.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.createCompanyBrandMapping()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CompanyBrandPostRequestSerializer import CompanyBrandPostRequestSerializer
        schema = CompanyBrandPostRequestSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/company-brand", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the brand is to be mapped.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the brand is to be mapped.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/company-brand", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getLocations(self, store_type=None, q=None, stage=None, page_no=None, page_size=None):
        """This API allows to view all the locations associated to a company.
        :param store_type : Helps to sort the location list on the basis of location type. : type string
        :param q : Query that is to be searched. : type string
        :param stage : to filter companies on basis of verified or unverified companies. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if store_type:
            payload["store_type"] = store_type
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CompanyProfileValidator.getLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location", """{"required":[{"in":"path","name":"company_id","description":"Id of the company whose locations are to fetched","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"store_type","description":"Helps to sort the location list on the basis of location type.","schema":{"type":"string"},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"stage","description":"to filter companies on basis of verified or unverified companies.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":20},"required":false}],"query":[{"in":"query","name":"store_type","description":"Helps to sort the location list on the basis of location type.","schema":{"type":"string"},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"stage","description":"to filter companies on basis of verified or unverified companies.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":20},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company whose locations are to fetched","schema":{"type":"string"},"required":true}]}""", store_type=store_type, q=q, stage=stage, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(store_type=store_type, q=q, stage=stage, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location", store_type=store_type, q=q, stage=stage, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createLocation(self, body=""):
        """This API allows to edit a location associated to a company.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.createLocation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.LocationSerializer import LocationSerializer
        schema = LocationSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getLocationDetail(self, location_id=None):
        """This API helps to get data associated to a specific location.
        :param location_id : Id of the location which you want to view. : type string
        """
        payload = {}
        
        if location_id:
            payload["location_id"] = location_id
        

        # Parameter validation
        schema = CompanyProfileValidator.getLocationDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location/{location_id}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location lies.","schema":{"type":"string"},"required":true},{"in":"path","name":"location_id","description":"Id of the location which you want to view.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the location lies.","schema":{"type":"string"},"required":true},{"in":"path","name":"location_id","description":"Id of the location which you want to view.","schema":{"type":"string"},"required":true}]}""", location_id=location_id)
        query_string = await create_query_string(location_id=location_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location/{location_id}", location_id=location_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateLocation(self, location_id=None, body=""):
        """This API allows to edit a location associated to a company.
        :param location_id : Id of the location which you want to edit. : type string
        """
        payload = {}
        
        if location_id:
            payload["location_id"] = location_id
        

        # Parameter validation
        schema = CompanyProfileValidator.updateLocation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.LocationSerializer import LocationSerializer
        schema = LocationSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location/{location_id}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true},{"in":"path","name":"location_id","description":"Id of the location which you want to edit.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true},{"in":"path","name":"location_id","description":"Id of the location which you want to edit.","schema":{"type":"string"},"required":true}]}""", location_id=location_id)
        query_string = await create_query_string(location_id=location_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location/{location_id}", location_id=location_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def createLocationBulk(self, body=""):
        """This API allows to create a location associated to a company.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.createLocationBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.BulkLocationSerializer import BulkLocationSerializer
        schema = BulkLocationSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location/bulk", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location/bulk", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

class FileStorage:
    def __init__(self, config):
        self._conf = config
    
    async def startUpload(self, namespace=None, body=""):
        """Uploads an arbitrarily sized buffer or blob.

It has three Major Steps:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `startUpload`.
It returns the storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `startUpload` api with file (Buffer or Blob) as a request body.

### Complete
After successfully upload, call `completeUpload` api to complete the upload process.
This operation will return the url for the uploaded file.

        :param namespace : bucket name : type string
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        

        # Parameter validation
        schema = FileStorageValidator.startUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.StartRequest import StartRequest
        schema = StartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/start/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", namespace=namespace, )
        query_string = await create_query_string(namespace=namespace, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/start/", namespace=namespace, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def completeUpload(self, namespace=None, body=""):
        """Uploads an arbitrarily sized buffer or blob.

It has three Major Steps:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `startUpload`.
It returns the storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `startUpload` api with file (Buffer or Blob) as a request body.

### Complete
After successfully upload, call `completeUpload` api to complete the upload process.
This operation will return the url for the uploaded file.

        :param namespace : bucket name : type string
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        

        # Parameter validation
        schema = FileStorageValidator.completeUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.StartResponse import StartResponse
        schema = StartResponse()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/complete/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", namespace=namespace, )
        query_string = await create_query_string(namespace=namespace, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/upload/complete/", namespace=namespace, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSignUrls(self, body=""):
        """Describe here
        """
        payload = {}
        

        # Parameter validation
        schema = FileStorageValidator.getSignUrls()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SignUrlRequest import SignUrlRequest
        schema = SignUrlRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/sign-urls/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/sign-urls/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def copyFiles(self, sync=None, body=""):
        """Copy Files
        :param sync : sync : type boolean
        """
        payload = {}
        
        if sync:
            payload["sync"] = sync
        

        # Parameter validation
        schema = FileStorageValidator.copyFiles()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.BulkRequest import BulkRequest
        schema = BulkRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/uploads/copy/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"query":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", sync=sync, )
        query_string = await create_query_string(sync=sync, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/uploads/copy/", sync=sync, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def browse(self, namespace=None, page_no=None):
        """Browse Files
        :param namespace : bucket name : type string
        :param page_no : page no : type integer
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = FileStorageValidator.browse()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/browse/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"page_no","in":"query","description":"page no","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page_no","in":"query","description":"page no","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", namespace=namespace, page_no=page_no)
        query_string = await create_query_string(namespace=namespace, page_no=page_no)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/namespaces/{namespace}/browse/", namespace=namespace, page_no=page_no), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def proxy(self, url=None):
        """Proxy
        :param url : url : type string
        """
        payload = {}
        
        if url:
            payload["url"] = url
        

        # Parameter validation
        schema = FileStorageValidator.proxy()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/proxy/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", url=url)
        query_string = await create_query_string(url=url)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/proxy/", url=url), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

class Share:
    def __init__(self, config):
        self._conf = config
    

class Inventory:
    def __init__(self, config):
        self._conf = config
    
    async def getConfigByCompany(self, ):
        """REST Endpoint that returns all configuration detail of a company
        """
        payload = {}
        

        # Parameter validation
        schema = InventoryValidator.getConfigByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/slingshot", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/slingshot", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def suppressStores(self, body=""):
        """REST Endpoint that returns all configuration detail of a company
        """
        payload = {}
        

        # Parameter validation
        schema = InventoryValidator.suppressStores()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SuppressStorePayload import SuppressStorePayload
        schema = SuppressStorePayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/kafka/suppressStore", """{"required":[{"name":"company_id","in":"path","description":"Company id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/kafka/suppressStore", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getJobsByCompany(self, page_no=None, page_size=None):
        """REST Endpoint that returns all job configs for a company
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = InventoryValidator.getJobsByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateJob(self, body=""):
        """REST Endpoint that updates a job config
        """
        payload = {}
        

        # Parameter validation
        schema = InventoryValidator.updateJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.JobConfigDTO import JobConfigDTO
        schema = JobConfigDTO()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def createJob(self, body=""):
        """REST Endpoint that creates a new job config
        """
        payload = {}
        

        # Parameter validation
        schema = InventoryValidator.createJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.JobConfigDTO import JobConfigDTO
        schema = JobConfigDTO()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getJobSteps(self, job_id=None):
        """REST Endpoint that returns Inventory Job Steps
        :param job_id : Job Id : type integer
        """
        payload = {}
        
        if job_id:
            payload["job_id"] = job_id
        

        # Parameter validation
        schema = InventoryValidator.getJobSteps()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/steps/{job_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"job_id","in":"path","description":"Job Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"job_id","in":"path","description":"Job Id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", job_id=job_id)
        query_string = await create_query_string(job_id=job_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/steps/{job_id}", job_id=job_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getJobByCompanyAndIntegration(self, integration_id=None, page_no=None, page_size=None):
        """REST Endpoint that returns all job configs by company And integration
        :param integration_id : Integration Id : type string
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        """
        payload = {}
        
        if integration_id:
            payload["integration_id"] = integration_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = InventoryValidator.getJobByCompanyAndIntegration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/integration/{integration_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"Integration Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"Integration Id","required":true,"schema":{"type":"string"}}]}""", integration_id=integration_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(integration_id=integration_id, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/integration/{integration_id}", integration_id=integration_id, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def disable(self, integration_id=None):
        """REST Endpoint that disables Inventory Job Config
        :param integration_id : IntegrationId : type string
        """
        payload = {}
        
        if integration_id:
            payload["integration_id"] = integration_id
        

        # Parameter validation
        schema = InventoryValidator.disable()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/disable/integration/{integration_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"IntegrationId","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"IntegrationId","required":true,"schema":{"type":"string"}}]}""", integration_id=integration_id)
        query_string = await create_query_string(integration_id=integration_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/disable/integration/{integration_id}", integration_id=integration_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getJobConfigDefaults(self, ):
        """REST Endpoint that returns default fields job configs by company And integration
        """
        payload = {}
        

        # Parameter validation
        schema = InventoryValidator.getJobConfigDefaults()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/defaults", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/defaults", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getJobByCode(self, code=None):
        """REST Endpoint that returns job config by code
        :param code : Job Code : type string
        """
        payload = {}
        
        if code:
            payload["code"] = code
        

        # Parameter validation
        schema = InventoryValidator.getJobByCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/code/{code}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"code","in":"path","description":"Job Code","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"code","in":"path","description":"Job Code","required":true,"schema":{"type":"string"}}]}""", code=code)
        query_string = await create_query_string(code=code)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/code/{code}", code=code), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getJobCodeMetrics(self, code=None, page_no=None, page_size=None, status=None, date=None):
        """REST Endpoint that returns Inventory Run History For A Job Code
        :param code : Code : type string
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        :param status : Status : type string
        :param date : From Date : type string
        """
        payload = {}
        
        if code:
            payload["code"] = code
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if status:
            payload["status"] = status
        
        if date:
            payload["date"] = date
        

        # Parameter validation
        schema = InventoryValidator.getJobCodeMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/code/{code}/metrics", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"code","in":"path","description":"Code","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}},{"name":"status","in":"query","description":"Status","required":false,"schema":{"type":"string"}},{"name":"date","in":"query","description":"From Date","required":false,"schema":{"type":"string","format":"date-time"}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}},{"name":"status","in":"query","description":"Status","required":false,"schema":{"type":"string"}},{"name":"date","in":"query","description":"From Date","required":false,"schema":{"type":"string","format":"date-time"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"code","in":"path","description":"Code","required":true,"schema":{"type":"string"}}]}""", code=code, page_no=page_no, page_size=page_size, status=status, date=date)
        query_string = await create_query_string(code=code, page_no=page_no, page_size=page_size, status=status, date=date)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/code/{code}/metrics", code=code, page_no=page_no, page_size=page_size, status=status, date=date), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getJobCodesByCompanyAndIntegration(self, integration_id=None, page_no=None, page_size=None):
        """REST Endpoint that returns all job codes by company And integration
        :param integration_id : Integration Id : type string
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        """
        payload = {}
        
        if integration_id:
            payload["integration_id"] = integration_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = InventoryValidator.getJobCodesByCompanyAndIntegration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/code/integration/{integration_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"Integration Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"Integration Id","required":true,"schema":{"type":"string"}}]}""", integration_id=integration_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(integration_id=integration_id, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/inventory/v1.0/company/{self._conf.companyId}/jobs/code/integration/{integration_id}", integration_id=integration_id, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

class Configuration:
    def __init__(self, config):
        self._conf = config
    
    async def createApplication(self, body=""):
        """Create new application
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.createApplication()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateApplicationRequest import CreateApplicationRequest
        schema = CreateApplicationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getApplications(self, page_no=None, page_size=None, q=None):
        """Get list of application under company
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param q : Url encoded object used as mongodb query : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = ConfigurationValidator.getApplications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"in":"query","name":"page_no","schema":{"type":"integer"}},{"name":"page_size","schema":{"type":"integer"},"in":"query"},{"name":"q","schema":{"type":"string"},"in":"query","description":"Url encoded object used as mongodb query"}],"query":[{"in":"query","name":"page_no","schema":{"type":"integer"}},{"name":"page_size","schema":{"type":"integer"},"in":"query"},{"name":"q","schema":{"type":"string"},"in":"query","description":"Url encoded object used as mongodb query"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCurrencies(self, ):
        """Get all currencies
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getCurrencies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/currencies", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/currencies", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getDomainAvailibility(self, body=""):
        """Check domain availibility before linking to application. Also sends domain suggestions with similar to queried domain. \ Custom domain search is currently powered by GoDaddy provider.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getDomainAvailibility()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DomainSuggestionsRequest import DomainSuggestionsRequest
        schema = DomainSuggestionsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/domain/suggestions", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/domain/suggestions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getIntegrationById(self, id=None):
        """Get integration data
        :param id : Integration id : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"integer"},"description":"Integration id","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"integer"},"description":"Integration id","required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getAvailableOptIns(self, page_no=None, page_size=None):
        """Get all available integration opt-ins
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getAvailableOptIns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/available", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/available", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getSelectedOptIns(self, level=None, uid=None, page_no=None, page_size=None):
        """Get company/store level integration opt-ins
        :param level : Integration level : type string
        :param uid : Integration level uid : type integer
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if level:
            payload["level"] = level
        
        if uid:
            payload["uid"] = uid
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getSelectedOptIns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/selected/{level}/{uid}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Integration level uid","required":true}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Integration level uid","required":true}]}""", level=level, uid=uid, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(level=level, uid=uid, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/selected/{level}/{uid}", level=level, uid=uid, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getIntegrationLevelConfig(self, id=None, level=None, opted=None, check_permission=None):
        """Get integration/integration-opt-in level config
        :param id : Integration id : type string
        :param level : Integration level : type string
        :param opted : Filter on opted stores : type boolean
        :param check_permission : Filter on if permissions are present : type boolean
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        
        if opted:
            payload["opted"] = opted
        
        if check_permission:
            payload["check_permission"] = check_permission
        

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationLevelConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true}],"optional":[{"name":"opted","in":"query","schema":{"type":"boolean"},"description":"Filter on opted stores","required":false},{"name":"check_permission","in":"query","schema":{"type":"boolean"},"description":"Filter on if permissions are present","required":false}],"query":[{"name":"opted","in":"query","schema":{"type":"boolean"},"description":"Filter on opted stores","required":false},{"name":"check_permission","in":"query","schema":{"type":"boolean"},"description":"Filter on if permissions are present","required":false}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true}]}""", id=id, level=level, opted=opted, check_permission=check_permission)
        query_string = await create_query_string(id=id, level=level, opted=opted, check_permission=check_permission)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}", id=id, level=level, opted=opted, check_permission=check_permission), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateLevelIntegration(self, id=None, level=None, body=""):
        """Update a store level opt-in for integration
        :param id : Integration id : type string
        :param level : Integration level : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        

        # Parameter validation
        schema = ConfigurationValidator.updateLevelIntegration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateIntegrationLevelRequest import UpdateIntegrationLevelRequest
        schema = UpdateIntegrationLevelRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true}]}""", id=id, level=level)
        query_string = await create_query_string(id=id, level=level)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}", id=id, level=level), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getIntegrationByLevelId(self, id=None, level=None, uid=None):
        """Get level data for integration
        :param id : Integration id : type string
        :param level : Integration level : type string
        :param uid : Integration level uid : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationByLevelId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}/{uid}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Integration level uid","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Integration level uid","required":true}]}""", id=id, level=level, uid=uid)
        query_string = await create_query_string(id=id, level=level, uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}/{uid}", id=id, level=level, uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateLevelUidIntegration(self, id=None, level=None, uid=None, body=""):
        """Update a store level opt-in for integration
        :param id : Integration id : type string
        :param level : Integration level : type string
        :param uid : Integration level uid : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = ConfigurationValidator.updateLevelUidIntegration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.IntegrationLevel import IntegrationLevel
        schema = IntegrationLevel()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}/{uid}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Integration level uid","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Integration level uid","required":true}]}""", id=id, level=level, uid=uid)
        query_string = await create_query_string(id=id, level=level, uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/configuration/{id}/{level}/{uid}", id=id, level=level, uid=uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getLevelActiveIntegrations(self, id=None, level=None, uid=None):
        """API checks if a store is already opted in any other integrations
        :param id : Integration id : type string
        :param level : Integration level : type string
        :param uid : Integration level uid : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = ConfigurationValidator.getLevelActiveIntegrations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/check/configuration/{id}/{level}/{uid}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Integration level uid","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Integration level uid","required":true}]}""", id=id, level=level, uid=uid)
        query_string = await create_query_string(id=id, level=level, uid=uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/integration-opt-in/check/configuration/{id}/{level}/{uid}", id=id, level=level, uid=uid), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getBrandsByCompany(self, q=None):
        """Get brands by company
        :param q : Search text for brand name : type string
        """
        payload = {}
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = ConfigurationValidator.getBrandsByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/brands-by-companies", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"q","in":"query","schema":{"type":"string"},"description":"Search text for brand name"}],"query":[{"name":"q","in":"query","schema":{"type":"string"},"description":"Search text for brand name"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", q=q)
        query_string = await create_query_string(q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/brands-by-companies", q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCompanyByBrands(self, page_no=None, page_size=None, body=""):
        """Get company by brand uids
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getCompanyByBrands()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CompanyByBrandsRequest import CompanyByBrandsRequest
        schema = CompanyByBrandsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/companies-by-brands", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/companies-by-brands", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getStoreByBrands(self, page_no=None, page_size=None, body=""):
        """Get stores by brand uids
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getStoreByBrands()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.StoreByBrandsRequest import StoreByBrandsRequest
        schema = StoreByBrandsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/stores-by-brands", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/stores-by-brands", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getOtherSellerApplications(self, page_no=None, page_size=None):
        """Get other seller applications who has opted current company as inventory
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getOtherSellerApplications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOtherSellerApplicationById(self, id=None):
        """Get other seller application
        :param id : Application Id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.getOtherSellerApplicationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Application Id","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Application Id","required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def optOutFromApplication(self, id=None, body=""):
        """Opt out company or store from other seller application
        :param id : Application Id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.optOutFromApplication()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OptOutInventory import OptOutInventory
        schema = OptOutInventory()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}/opt_out", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Application Id","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Application Id","required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}/opt_out", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

class Cart:
    def __init__(self, config):
        self._conf = config
    

class Rewards:
    def __init__(self, config):
        self._conf = config
    

class Analytics:
    def __init__(self, config):
        self._conf = config
    
    async def createExportJob(self, export_type=None, body=""):
        """Create data export job in required format
        :param export_type : Export type / format : type string
        """
        payload = {}
        
        if export_type:
            payload["export_type"] = export_type
        

        # Parameter validation
        schema = AnalyticsValidator.createExportJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ExportJobReq import ExportJobReq
        schema = ExportJobReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/export/{export_type}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"export_type","in":"path","description":"Export type / format","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"export_type","in":"path","description":"Export type / format","required":true,"schema":{"type":"string"}}]}""", export_type=export_type)
        query_string = await create_query_string(export_type=export_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/export/{export_type}", export_type=export_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getExportJobStatus(self, export_type=None, job_id=None):
        """Get data export job status
        :param export_type : Export type / format : type string
        :param job_id : Export job id : type string
        """
        payload = {}
        
        if export_type:
            payload["export_type"] = export_type
        
        if job_id:
            payload["job_id"] = job_id
        

        # Parameter validation
        schema = AnalyticsValidator.getExportJobStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/export/{export_type}/job/{job_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"export_type","in":"path","description":"Export type / format","required":true,"schema":{"type":"string"}},{"name":"job_id","in":"path","description":"Export job id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"export_type","in":"path","description":"Export type / format","required":true,"schema":{"type":"string"}},{"name":"job_id","in":"path","description":"Export job id","required":true,"schema":{"type":"string"}}]}""", export_type=export_type, job_id=job_id)
        query_string = await create_query_string(export_type=export_type, job_id=job_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/export/{export_type}/job/{job_id}", export_type=export_type, job_id=job_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getLogsList(self, log_type=None, page_no=None, page_size=None, body=""):
        """Get logs list
        :param log_type : Log type : type string
        :param page_no : Current page number : type integer
        :param page_size : Current page size : type integer
        """
        payload = {}
        
        if log_type:
            payload["log_type"] = log_type
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = AnalyticsValidator.getLogsList()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.GetLogsListReq import GetLogsListReq
        schema = GetLogsListReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/logs/{log_type}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"log_type","in":"path","description":"Log type","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"log_type","in":"path","description":"Log type","required":true,"schema":{"type":"string"}}]}""", log_type=log_type, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(log_type=log_type, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/logs/{log_type}", log_type=log_type, page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def searchLogs(self, page_no=None, page_size=None, log_type=None, body=""):
        """Search logs
        :param page_no : Current page number : type integer
        :param page_size : Current page size : type integer
        :param log_type : Log type : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if log_type:
            payload["log_type"] = log_type
        

        # Parameter validation
        schema = AnalyticsValidator.searchLogs()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SearchLogReq import SearchLogReq
        schema = SearchLogReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/logs/{log_type}/search", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"log_type","in":"path","description":"Log type","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"log_type","in":"path","description":"Log type","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, log_type=log_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, log_type=log_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/logs/{log_type}/search", page_no=page_no, page_size=page_size, log_type=log_type), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

class Discount:
    def __init__(self, config):
        self._conf = config
    
    async def getDiscounts(self, view=None, q=None, page_no=None, page_size=None, archived=None, month=None, year=None, type=None, app_ids=None):
        """Fetch discount list.
        :param view : listing or calender.  Default is listing. : type string
        :param q : The search query. This can be a partial or complete name of a discount. : type string
        :param page_no : page number. Default is 1. : type integer
        :param page_size : page size. Default is 12. : type integer
        :param archived : archived. Default is false. : type boolean
        :param month : month. Default is current month. : type integer
        :param year : year. Default is current year. : type integer
        :param type : basic or custom. : type string
        :param app_ids : application ids. : type array
        """
        payload = {}
        
        if view:
            payload["view"] = view
        
        if q:
            payload["q"] = q
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if archived:
            payload["archived"] = archived
        
        if month:
            payload["month"] = month
        
        if year:
            payload["year"] = year
        
        if type:
            payload["type"] = type
        
        if app_ids:
            payload["app_ids"] = app_ids
        

        # Parameter validation
        schema = DiscountValidator.getDiscounts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"view","in":"query","description":"listing or calender.  Default is listing.","required":false,"schema":{"type":"string","enum":["listing","calender"]}},{"name":"q","in":"query","description":"The search query. This can be a partial or complete name of a discount.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"page number. Default is 1.","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"page size. Default is 12.","required":false,"schema":{"type":"integer"}},{"name":"archived","in":"query","description":"archived. Default is false.","required":false,"schema":{"type":"boolean","enum":[true,false]}},{"name":"month","in":"query","description":"month. Default is current month.","required":false,"schema":{"type":"integer"}},{"name":"year","in":"query","description":"year. Default is current year.","required":false,"schema":{"type":"integer"}},{"name":"type","in":"query","description":"basic or custom.","required":false,"schema":{"type":"string"}},{"name":"app_ids","in":"query","description":"application ids.","required":false,"schema":{"type":"array","items":{"type":"string"}}}],"query":[{"name":"view","in":"query","description":"listing or calender.  Default is listing.","required":false,"schema":{"type":"string","enum":["listing","calender"]}},{"name":"q","in":"query","description":"The search query. This can be a partial or complete name of a discount.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"page number. Default is 1.","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"page size. Default is 12.","required":false,"schema":{"type":"integer"}},{"name":"archived","in":"query","description":"archived. Default is false.","required":false,"schema":{"type":"boolean","enum":[true,false]}},{"name":"month","in":"query","description":"month. Default is current month.","required":false,"schema":{"type":"integer"}},{"name":"year","in":"query","description":"year. Default is current year.","required":false,"schema":{"type":"integer"}},{"name":"type","in":"query","description":"basic or custom.","required":false,"schema":{"type":"string"}},{"name":"app_ids","in":"query","description":"application ids.","required":false,"schema":{"type":"array","items":{"type":"string"}}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids)
        query_string = await create_query_string(view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createDiscount(self, body=""):
        """Create Discount.
        """
        payload = {}
        

        # Parameter validation
        schema = DiscountValidator.createDiscount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateUpdateDiscount import CreateUpdateDiscount
        schema = CreateUpdateDiscount()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getDiscount(self, id=None):
        """Fetch discount.
        :param id : unique id. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.getDiscount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"unique id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"unique id.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateDiscount(self, id=None, body=""):
        """Create Discount.
        :param id : id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.updateDiscount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateUpdateDiscount import CreateUpdateDiscount
        schema = CreateUpdateDiscount()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def validateDiscountFile(self, discount=None, body=""):
        """Validate File.
        :param discount : discount : type string
        """
        payload = {}
        
        if discount:
            payload["discount"] = discount
        

        # Parameter validation
        schema = DiscountValidator.validateDiscountFile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DiscountJob import DiscountJob
        schema = DiscountJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"discount","in":"query","description":"discount","required":false,"schema":{"type":"string"}}],"query":[{"name":"discount","in":"query","description":"discount","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", discount=discount)
        query_string = await create_query_string(discount=discount)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/", discount=discount), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def downloadDiscountFile(self, type=None, body=""):
        """Validate File.
        :param type : type : type string
        """
        payload = {}
        
        if type:
            payload["type"] = type
        

        # Parameter validation
        schema = DiscountValidator.downloadDiscountFile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DownloadFileJob import DownloadFileJob
        schema = DownloadFileJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/{type}/download/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"type","in":"path","description":"type","required":true,"schema":{"type":"string","enum":["product","inventory"]}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"type","in":"path","description":"type","required":true,"schema":{"type":"string","enum":["product","inventory"]}}]}""", type=type)
        query_string = await create_query_string(type=type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/{type}/download/", type=type), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getValidationJob(self, id=None):
        """Validate File Job.
        :param id : id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.getValidationJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def cancelValidationJob(self, id=None):
        """Cancel Validation Job.
        :param id : id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.cancelValidationJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getDownloadJob(self, id=None):
        """Download File Job.
        :param id : id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.getDownloadJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def cancelDownloadJob(self, id=None):
        """Cancel Download Job.
        :param id : id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.cancelDownloadJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

class Partner:
    def __init__(self, config):
        self._conf = config
    

class Webhook:
    def __init__(self, config):
        self._conf = config
    
    async def getSubscribersByCompany(self, page_no=None, page_size=None, extension_id=None):
        """Get Subscribers By CompanyId
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        :param extension_id : Extension ID : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if extension_id:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = WebhookValidator.getSubscribersByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}},{"name":"extension_id","in":"query","description":"Extension ID","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}},{"name":"extension_id","in":"query","description":"Extension ID","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}]}""", page_no=page_no, page_size=page_size, extension_id=extension_id)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, extension_id=extension_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber", page_no=page_no, page_size=page_size, extension_id=extension_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def registerSubscriberToEvent(self, body=""):
        """Register Subscriber
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.registerSubscriberToEvent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SubscriberConfig import SubscriberConfig
        schema = SubscriberConfig()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber", """{"required":[{"name":"company_id","in":"path","description":"Company Id of the application","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id of the application","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateSubscriberConfig(self, body=""):
        """Update Subscriber
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.updateSubscriberConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SubscriberConfig import SubscriberConfig
        schema = SubscriberConfig()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getSubscribersByExtensionId(self, page_no=None, page_size=None, extension_id=None):
        """Get Subscribers By ExtensionID
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        :param extension_id : Extension ID : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if extension_id:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = WebhookValidator.getSubscribersByExtensionId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscriber", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"extension_id","in":"path","description":"Extension ID","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"extension_id","in":"path","description":"Extension ID","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, extension_id=extension_id)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, extension_id=extension_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscriber", page_no=page_no, page_size=page_size, extension_id=extension_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getSubscriberById(self, subscriber_id=None):
        """Get Subscriber By Subscriber ID
        :param subscriber_id : Subscriber ID : type integer
        """
        payload = {}
        
        if subscriber_id:
            payload["subscriber_id"] = subscriber_id
        

        # Parameter validation
        schema = WebhookValidator.getSubscriberById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/{subscriber_id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"subscriber_id","in":"path","description":"Subscriber ID","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"subscriber_id","in":"path","description":"Subscriber ID","required":true,"schema":{"type":"integer","format":"int32"}}]}""", subscriber_id=subscriber_id)
        query_string = await create_query_string(subscriber_id=subscriber_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/{subscriber_id}", subscriber_id=subscriber_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def fetchAllEventConfigurations(self, ):
        """Get All Webhook Events
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.fetchAllEventConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/events", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/events", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

class AuditTrail:
    def __init__(self, config):
        self._conf = config
    
    async def getAuditLogs(self, qs=None):
        """Get audit logs
        :param qs : Logs Query : type string
        """
        payload = {}
        
        if qs:
            payload["qs"] = qs
        

        # Parameter validation
        schema = AuditTrailValidator.getAuditLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/", """{"required":[{"in":"path","name":"company_id","description":"Compnay Id","required":true,"schema":{"type":"string","example":"1"}},{"in":"query","name":"qs","description":"Logs Query","required":true,"schema":{"type":"string","example":"%7B%7D&limit=10&company=61&sort=%7B%22_id%22%3A-1%7D"}}],"optional":[],"query":[{"in":"query","name":"qs","description":"Logs Query","required":true,"schema":{"type":"string","example":"%7B%7D&limit=10&company=61&sort=%7B%22_id%22%3A-1%7D"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Compnay Id","required":true,"schema":{"type":"string","example":"1"}}]}""", qs=qs)
        query_string = await create_query_string(qs=qs)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/", qs=qs), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createAuditLog(self, body=""):
        """Create a Audit log
        """
        payload = {}
        

        # Parameter validation
        schema = AuditTrailValidator.createAuditLog()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.RequestBodyAuditLog import RequestBodyAuditLog
        schema = RequestBodyAuditLog()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string","example":"1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAuditLog(self, id=None):
        """Get audit logs by logs uuid
        :param id : log uuid : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = AuditTrailValidator.getAuditLog()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/{id}", """{"required":[{"in":"path","name":"company_id","description":"Compnay Id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"id","description":"log uuid","required":true,"schema":{"type":"string","example":"602a1366a7486d63f1e915b2"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Compnay Id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"id","description":"log uuid","required":true,"schema":{"type":"string","example":"602a1366a7486d63f1e915b2"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/logs/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getEntityTypes(self, ):
        """Get entity types
        """
        payload = {}
        

        # Parameter validation
        schema = AuditTrailValidator.getEntityTypes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/entity-types", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string","example":"1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/audit-trail/v1.0/company/{self._conf.companyId}/entity-types", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    



class PlatformClient:
    def __init__(self, config):
        self._conf = config
        self.common = Common(config)
        self.lead = Lead(config)
        self.theme = Theme(config)
        self.user = User(config)
        self.content = Content(config)
        self.billing = Billing(config)
        self.communication = Communication(config)
        self.payment = Payment(config)
        self.order = Order(config)
        self.catalog = Catalog(config)
        self.companyProfile = CompanyProfile(config)
        self.fileStorage = FileStorage(config)
        self.share = Share(config)
        self.inventory = Inventory(config)
        self.configuration = Configuration(config)
        self.cart = Cart(config)
        self.rewards = Rewards(config)
        self.analytics = Analytics(config)
        self.discount = Discount(config)
        self.partner = Partner(config)
        self.webhook = Webhook(config)
        self.auditTrail = AuditTrail(config)
        

    def application(self, applicationId):
        return PlatformApplicationClient(applicationId, self._conf)

    async def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
