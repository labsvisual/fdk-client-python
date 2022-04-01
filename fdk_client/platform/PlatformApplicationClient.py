"""Platform Client."""

from ..common.aiohttp_helper import AiohttpHelper
from ..common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .models.CommonValidator import CommonValidator
from .models.LeadValidator import LeadValidator
from .models.FeedbackValidator import FeedbackValidator
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
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    

class Lead:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getTickets(self, items=None, filters=None, q=None, status=None, priority=None, category=None):
        """Gets the list of Application level Tickets and/or ticket filters
        :param items : Decides that the reponse will contain the list of tickets : type boolean
        :param filters : Decides that the reponse will contain the ticket filters : type boolean
        :param q : Search through ticket titles and description : type string
        :param status : Filter tickets on status : type string
        :param priority : Filter tickets on priority : type 
        :param category : Filter tickets on category : type string
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
        

        # Parameter validation
        schema = LeadValidator.getTickets()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}}],"optional":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}}],"query":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}}]}""", items=items, filters=filters, q=q, status=status, priority=priority, category=category)
        query_string = await create_query_string(items=items, filters=filters, q=q, status=status, priority=priority, category=category)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket", items=items, filters=filters, q=q, status=status, priority=priority, category=category), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getTicket(self, id=None):
        """Retreives ticket details of a application level ticket with ticket ID
        :param id : Tiket ID of the ticket to be fetched : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.getTicket()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Tiket ID of the ticket to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Tiket ID of the ticket to be fetched","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def editTicket(self, id=None, body=""):
        """Edits ticket details of a application level ticket such as status, priority, category, tags, attachments, assigne & ticket content changes
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID of ticket to be edited","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID of ticket to be edited","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def createHistory(self, id=None, body=""):
        """Create history for specific application level ticket, this history is seen on ticket detail page, this can be comment, log or rating.
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}/history", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getTicketHistory(self, id=None):
        """Gets history list for specific application level ticket, this history is seen on ticket detail page, this can be comment, log or rating.
        :param id : Ticket ID for which history is to be fetched : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.getTicketHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID of application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is to be fetched","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ticket/{id}/history", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getCustomForm(self, slug=None):
        """Get specific custom form using it's slug, this is used to view the form.
        :param slug : Slug of form whose response is getting submitted : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = LeadValidator.getCustomForm()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", slug=slug), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def editCustomForm(self, slug=None, body=""):
        """Edit the given custom form field such as adding or deleting input, assignee, title, decription, notification and polling information.
        :param slug : Slug of form whose response is getting submitted : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = LeadValidator.editCustomForm()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EditCustomFormPayload import EditCustomFormPayload
        schema = EditCustomFormPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form/{slug}", slug=slug), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getCustomForms(self, ):
        """Get list of custom form for given application
        """
        payload = {}
        

        # Parameter validation
        schema = LeadValidator.getCustomForms()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createCustomForm(self, body=""):
        """Creates a new custom form for given application
        """
        payload = {}
        

        # Parameter validation
        schema = LeadValidator.createCustomForm()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateCustomFormPayload import CreateCustomFormPayload
        schema = CreateCustomFormPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/form", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room/{unique_name}/token", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of video room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of video room","required":true,"schema":{"type":"string"}}]}""", unique_name=unique_name)
        query_string = await create_query_string(unique_name=unique_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room/{unique_name}/token", unique_name=unique_name), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room/{unique_name}/participants", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}]}""", unique_name=unique_name)
        query_string = await create_query_string(unique_name=unique_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room/{unique_name}/participants", unique_name=unique_name), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def openVideoRoom(self, body=""):
        """Open a video room.
        """
        payload = {}
        

        # Parameter validation
        schema = LeadValidator.openVideoRoom()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateVideoRoomPayload import CreateVideoRoomPayload
        schema = CreateVideoRoomPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def closeVideoRoom(self, unique_name=None):
        """Close the video room and force all participants to leave.
        :param unique_name : Unique name of Video Room : type string
        """
        payload = {}
        
        if unique_name:
            payload["unique_name"] = unique_name
        

        # Parameter validation
        schema = LeadValidator.closeVideoRoom()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room/{unique_name}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}]}""", unique_name=unique_name)
        query_string = await create_query_string(unique_name=unique_name)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/lead/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/video/room/{unique_name}", unique_name=unique_name), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    

class Feedback:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getAttributes(self, page_no=None, page_size=None):
        """Provides a list of all attribute data.
        :param page_no : pagination page no : type integer
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = FeedbackValidator.getAttributes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/attributes/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"pagination page no","in":"query","name":"page_no","schema":{"type":"integer"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"pagination page no","in":"query","name":"page_no","schema":{"type":"integer"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/attributes/", page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getCustomerReviews(self, id=None, entity_id=None, entity_type=None, user_id=None, media=None, rating=None, attribute_rating=None, facets=None, sort=None, next=None, start=None, limit=None, count=None, page_id=None, page_size=None):
        """The endpoint provides a list of customer reviews based on entity and provided filters
        :param id : review id : type string
        :param entity_id : entity id : type string
        :param entity_type : entity type : type string
        :param user_id : user id : type string
        :param media : media type e.g. image | video | video_file | video_link : type string
        :param rating : rating filter, 1-5 : type array
        :param attribute_rating : attribute rating filter with ma,e of attribute : type array
        :param facets : facets (true|false) : type boolean
        :param sort : sort by : default | top | recent : type string
        :param next : pagination next : type string
        :param start : pagination start : type string
        :param limit : pagination limit : type string
        :param count : pagination count : type string
        :param page_id : pagination page id : type string
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if entity_id:
            payload["entity_id"] = entity_id
        
        if entity_type:
            payload["entity_type"] = entity_type
        
        if user_id:
            payload["user_id"] = user_id
        
        if media:
            payload["media"] = media
        
        if rating:
            payload["rating"] = rating
        
        if attribute_rating:
            payload["attribute_rating"] = attribute_rating
        
        if facets:
            payload["facets"] = facets
        
        if sort:
            payload["sort"] = sort
        
        if next:
            payload["next"] = next
        
        if start:
            payload["start"] = start
        
        if limit:
            payload["limit"] = limit
        
        if count:
            payload["count"] = count
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = FeedbackValidator.getCustomerReviews()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/reviews/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"review id","in":"query","name":"id","schema":{"type":"string"}},{"description":"entity id","in":"query","name":"entity_id","schema":{"type":"string"}},{"description":"entity type","in":"query","name":"entity_type","schema":{"type":"string"}},{"description":"user id","in":"query","name":"user_id","schema":{"type":"string"}},{"description":"media type e.g. image | video | video_file | video_link","in":"query","name":"media","schema":{"type":"string"}},{"description":"rating filter, 1-5","explode":false,"in":"query","name":"rating","schema":{"items":{"type":"number"},"type":"array"},"style":"form"},{"description":"attribute rating filter with ma,e of attribute","explode":false,"in":"query","name":"attribute_rating","schema":{"items":{"type":"string"},"type":"array"},"style":"form"},{"description":"facets (true|false)","in":"query","name":"facets","schema":{"type":"boolean"}},{"description":"sort by : default | top | recent","in":"query","name":"sort","schema":{"type":"string"}},{"description":"pagination next","in":"query","name":"next","schema":{"type":"string"}},{"description":"pagination start","in":"query","name":"start","schema":{"type":"string"}},{"description":"pagination limit","in":"query","name":"limit","schema":{"type":"string"}},{"description":"pagination count","in":"query","name":"count","schema":{"type":"string"}},{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"review id","in":"query","name":"id","schema":{"type":"string"}},{"description":"entity id","in":"query","name":"entity_id","schema":{"type":"string"}},{"description":"entity type","in":"query","name":"entity_type","schema":{"type":"string"}},{"description":"user id","in":"query","name":"user_id","schema":{"type":"string"}},{"description":"media type e.g. image | video | video_file | video_link","in":"query","name":"media","schema":{"type":"string"}},{"description":"rating filter, 1-5","explode":false,"in":"query","name":"rating","schema":{"items":{"type":"number"},"type":"array"},"style":"form"},{"description":"attribute rating filter with ma,e of attribute","explode":false,"in":"query","name":"attribute_rating","schema":{"items":{"type":"string"},"type":"array"},"style":"form"},{"description":"facets (true|false)","in":"query","name":"facets","schema":{"type":"boolean"}},{"description":"sort by : default | top | recent","in":"query","name":"sort","schema":{"type":"string"}},{"description":"pagination next","in":"query","name":"next","schema":{"type":"string"}},{"description":"pagination start","in":"query","name":"start","schema":{"type":"string"}},{"description":"pagination limit","in":"query","name":"limit","schema":{"type":"string"}},{"description":"pagination count","in":"query","name":"count","schema":{"type":"string"}},{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", id=id, entity_id=entity_id, entity_type=entity_type, user_id=user_id, media=media, rating=rating, attribute_rating=attribute_rating, facets=facets, sort=sort, next=next, start=start, limit=limit, count=count, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(id=id, entity_id=entity_id, entity_type=entity_type, user_id=user_id, media=media, rating=rating, attribute_rating=attribute_rating, facets=facets, sort=sort, next=next, start=start, limit=limit, count=count, page_id=page_id, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/reviews/", id=id, entity_id=entity_id, entity_type=entity_type, user_id=user_id, media=media, rating=rating, attribute_rating=attribute_rating, facets=facets, sort=sort, next=next, start=start, limit=limit, count=count, page_id=page_id, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateApprove(self, review_id=None, body=""):
        """The is used to update approve details like status and description text
        :param review_id : review id : type string
        """
        payload = {}
        
        if review_id:
            payload["review_id"] = review_id
        

        # Parameter validation
        schema = FeedbackValidator.updateApprove()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ApproveRequest import ApproveRequest
        schema = ApproveRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/reviews/{review_id}/approve/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"review id","in":"path","name":"review_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"review id","in":"path","name":"review_id","required":true,"schema":{"type":"string"}}]}""", review_id=review_id)
        query_string = await create_query_string(review_id=review_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/reviews/{review_id}/approve/", review_id=review_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getHistory(self, review_id=None):
        """The is used to get the history details like status and description text
        :param review_id : review id : type string
        """
        payload = {}
        
        if review_id:
            payload["review_id"] = review_id
        

        # Parameter validation
        schema = FeedbackValidator.getHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/reviews/{review_id}/history/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"review id","in":"path","name":"review_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"review id","in":"path","name":"review_id","required":true,"schema":{"type":"string"}}]}""", review_id=review_id)
        query_string = await create_query_string(review_id=review_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/reviews/{review_id}/history/", review_id=review_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getApplicationTemplates(self, page_id=None, page_size=None):
        """Get all templates of application
        :param page_id : pagination page id : type string
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = FeedbackValidator.getApplicationTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", page_id=page_id, page_size=page_size)
        query_string = await create_query_string(page_id=page_id, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/", page_id=page_id, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createTemplate(self, body=""):
        """Create a new template for review with following data:
- Enable media, rating and review
- Rating - active/inactive/selected rate choices, attributes, text on rate, comment for each rate, type
- Review - header, title, description, image and video meta, enable votes
        """
        payload = {}
        

        # Parameter validation
        schema = FeedbackValidator.createTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.TemplateRequestList import TemplateRequestList
        schema = TemplateRequestList()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getTemplateById(self, id=None):
        """Get the template for product or l3 type by ID
        :param id : template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = FeedbackValidator.getTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateTemplate(self, id=None, body=""):
        """Update existing template status, active/archive
        :param id : template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = FeedbackValidator.updateTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateTemplateRequest import UpdateTemplateRequest
        schema = UpdateTemplateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def updateTemplateStatus(self, id=None, body=""):
        """Update existing template status, active/archive
        :param id : template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = FeedbackValidator.updateTemplateStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateTemplateStatusRequest import UpdateTemplateStatusRequest
        schema = UpdateTemplateStatusRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/{id}/status/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/feedback/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/templates/{id}/status/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    

class Theme:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getAllPages(self, theme_id=None):
        """Use this API to retrieve all the available pages of a theme by its ID.
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getAllPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createPage(self, theme_id=None, body=""):
        """Use this API to create a page for a theme by its ID.
        :param theme_id : ID of the theme : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.createPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AvailablePageSchema import AvailablePageSchema
        schema = AvailablePageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def updateMultiplePages(self, theme_id=None, body=""):
        """Use this API to update multiple pages of a theme by its ID.
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.updateMultiplePages()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AllAvailablePageSchema import AllAvailablePageSchema
        schema = AllAvailablePageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/page", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getPage(self, theme_id=None, page_value=None):
        """Use this API to retrieve a page of a theme.
        :param theme_id : ID of the theme to be retrieved : type string
        :param page_value : Value of the page to be retrieved : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        if page_value:
            payload["page_value"] = page_value
        

        # Parameter validation
        schema = ThemeValidator.getPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id, page_value=page_value)
        query_string = await create_query_string(theme_id=theme_id, page_value=page_value)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", theme_id=theme_id, page_value=page_value), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updatePage(self, theme_id=None, page_value=None, body=""):
        """Use this API to update a page for a theme by its ID.
        :param theme_id : ID of the theme : type string
        :param page_value : Value of the page to be updated : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        if page_value:
            payload["page_value"] = page_value
        

        # Parameter validation
        schema = ThemeValidator.updatePage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AvailablePageSchema import AvailablePageSchema
        schema = AvailablePageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id, page_value=page_value)
        query_string = await create_query_string(theme_id=theme_id, page_value=page_value)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", theme_id=theme_id, page_value=page_value), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deletePage(self, theme_id=None, page_value=None):
        """Use this API to delete a page for a theme by its ID and page_value.
        :param theme_id : ID of the theme : type string
        :param page_value : Value of the page to be updated : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        if page_value:
            payload["page_value"] = page_value
        

        # Parameter validation
        schema = ThemeValidator.deletePage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id, page_value=page_value)
        query_string = await create_query_string(theme_id=theme_id, page_value=page_value)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/{page_value}", theme_id=theme_id, page_value=page_value), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getThemeLibrary(self, page_size=None, page_no=None):
        """Theme library is a personalized collection of themes that are chosen and added from the available themes. Use this API to fetch a list of themes from the library along with their configuration details. 
        :param page_size : The number of items to retrieve in each page. Default value is 10.  : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        """
        payload = {}
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = ThemeValidator.getThemeLibrary()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/library", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_size=page_size, page_no=page_no)
        query_string = await create_query_string(page_size=page_size, page_no=page_no)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/library", page_size=page_size, page_no=page_no), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def addToThemeLibrary(self, body=""):
        """Theme library is a personalized collection of themes that are chosen and added from the available themes. Use this API to choose a theme and add it to the theme library.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.addToThemeLibrary()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AddThemeRequestSchema import AddThemeRequestSchema
        schema = AddThemeRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/library", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/library", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def applyTheme(self, body=""):
        """Use this API to apply a theme to the website.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.applyTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AddThemeRequestSchema import AddThemeRequestSchema
        schema = AddThemeRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/apply", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/apply", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def isUpgradable(self, theme_id=None):
        """There's always a possibility that new features get added to a theme. Use this API to check if the applied theme has an upgrade available.
        :param theme_id : Theme ID : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.isUpgradable()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgradable", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"Theme ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"Theme ID","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgradable", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def upgradeTheme(self, theme_id=None):
        """Use this API to upgrade the current theme to its latest version.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.upgradeTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgrade", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/upgrade", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getPublicThemes(self, page_size=None, page_no=None):
        """Use this API to get a list of free themes that you can apply to your website.
        :param page_size : The number of items to retrieve in each page. Default value is 10.  : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        """
        payload = {}
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = ThemeValidator.getPublicThemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/list/public", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_size=page_size, page_no=page_no)
        query_string = await create_query_string(page_size=page_size, page_no=page_no)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/list/public", page_size=page_size, page_no=page_no), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createTheme(self, body=""):
        """Themes improve the look and appearance of a website. Use this API to create a theme.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.createTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ThemesSchema import ThemesSchema
        schema = ThemesSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getAppliedTheme(self, ):
        """Use this API to retrieve the theme that is currently applied to the website along with its details.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getAppliedTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getFonts(self, ):
        """Font is a collection of characters with a similar design. Use this API to retrieve a list of website fonts.
        """
        payload = {}
        

        # Parameter validation
        schema = ThemeValidator.getFonts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/fonts", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/fonts", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getThemeById(self, theme_id=None):
        """Use this API to retrieve the details of a specific theme by using its ID.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getThemeById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateTheme(self, theme_id=None, body=""):
        """Use this API to edit an existing theme. You can customize the website font, sections, images, styles, and many more.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.updateTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ThemesSchema import ThemesSchema
        schema = ThemesSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteTheme(self, theme_id=None):
        """Use this API to delete a theme from the theme library.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.deleteTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getThemeForPreview(self, theme_id=None):
        """A theme can be previewed before applying it. Use this API to retrieve the theme preview by using its ID.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getThemeForPreview()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/preview", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/preview", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def publishTheme(self, theme_id=None):
        """Use this API to publish a theme that is either newly created or edited.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.publishTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/publish", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/publish", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def unpublishTheme(self, theme_id=None):
        """Use this API to remove an existing theme from the list of available themes.
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.unpublishTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/unpublish", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/unpublish", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def archiveTheme(self, theme_id=None):
        """Use this API to store an existing theme but not delete it so that it can be used in future if required. 
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.archiveTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/archive", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/archive", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def unarchiveTheme(self, theme_id=None):
        """Use this API to restore an archived theme and bring it back for editing or publishing. 
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.unarchiveTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/unarchive", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/theme/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/{theme_id}/unarchive", theme_id=theme_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    

class User:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getCustomers(self, q=None, page_size=None, page_no=None):
        """Use this API to retrieve a list of customers who have registered in the application.
        :param q : The search query. Mobile number or email ID of a customer. : type string
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        """
        payload = {}
        
        if q:
            payload["q"] = q
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = UserValidator.getCustomers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/list", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", q=q, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(q=q, page_size=page_size, page_no=page_no)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/list", q=q, page_size=page_size, page_no=page_no), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def searchUsers(self, q=None):
        """Use this API to retrieve an existing user from a list.
        :param q : The search query. Mobile number or email ID of a customer. : type object
        """
        payload = {}
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = UserValidator.searchUsers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/search", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"object"}}],"query":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"object"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", q=q)
        query_string = await create_query_string(q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/search", q=q), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createUser(self, body=""):
        """Create user
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.createUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateUserRequestSchema import CreateUserRequestSchema
        schema = CreateUserRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def updateUser(self, user_id=None, body=""):
        """Update user
        :param user_id : User ID : type string
        """
        payload = {}
        
        if user_id:
            payload["user_id"] = user_id
        

        # Parameter validation
        schema = UserValidator.updateUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateUserRequestSchema import UpdateUserRequestSchema
        schema = UpdateUserRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/{user_id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"user_id","in":"path","description":"User ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"user_id","in":"path","description":"User ID","required":true,"schema":{"type":"string"}}]}""", user_id=user_id)
        query_string = await create_query_string(user_id=user_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/{user_id}", user_id=user_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def createUserSession(self, body=""):
        """Create user session
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.createUserSession()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateUserSessionRequestSchema import CreateUserSessionRequestSchema
        schema = CreateUserSessionRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/session", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/customers/session", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getPlatformConfig(self, ):
        """Use this API to get all the platform configurations such as mobile image, desktop image, social logins, and all other text.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.getPlatformConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform/config", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform/config", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updatePlatformConfig(self, body=""):
        """Use this API to edit the existing platform configurations such as mobile image, desktop image, social logins, and all other text.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.updatePlatformConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PlatformSchema import PlatformSchema
        schema = PlatformSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform/config", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/user/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform/config", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    

class Content:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getAnnouncementsList(self, page_no=None, page_size=None):
        """Announcements are useful to highlight a message or information on top of a webpage. Use this API to retrieve a list of announcements.	
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getAnnouncementsList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createAnnouncement(self, body=""):
        """Announcements are useful to highlight a message or information on top of a webpage. Use this API to create an announcement.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createAnnouncement()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AdminAnnouncementSchema import AdminAnnouncementSchema
        schema = AdminAnnouncementSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getAnnouncementById(self, announcement_id=None):
        """Use this API to retrieve an announcement and its details such as the target platform and pages on which it's applicable
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id:
            payload["announcement_id"] = announcement_id
        

        # Parameter validation
        schema = ContentValidator.getAnnouncementById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", announcement_id=announcement_id)
        query_string = await create_query_string(announcement_id=announcement_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateAnnouncement(self, announcement_id=None, body=""):
        """Use this API to edit an existing announcement and its details such as the target platform and pages on which it's applicable
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id:
            payload["announcement_id"] = announcement_id
        

        # Parameter validation
        schema = ContentValidator.updateAnnouncement()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AdminAnnouncementSchema import AdminAnnouncementSchema
        schema = AdminAnnouncementSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", announcement_id=announcement_id)
        query_string = await create_query_string(announcement_id=announcement_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def updateAnnouncementSchedule(self, announcement_id=None, body=""):
        """Use this API to edit the duration, i.e. start date-time and end date-time of an announcement. Moreover, you can enable/disable an announcement using this API.
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id:
            payload["announcement_id"] = announcement_id
        

        # Parameter validation
        schema = ContentValidator.updateAnnouncementSchedule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ScheduleSchema import ScheduleSchema
        schema = ScheduleSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", announcement_id=announcement_id)
        query_string = await create_query_string(announcement_id=announcement_id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteAnnouncement(self, announcement_id=None):
        """Use this API to delete an existing announcement.
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if announcement_id:
            payload["announcement_id"] = announcement_id
        

        # Parameter validation
        schema = ContentValidator.deleteAnnouncement()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}]}""", announcement_id=announcement_id)
        query_string = await create_query_string(announcement_id=announcement_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/announcements/{announcement_id}", announcement_id=announcement_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createBlog(self, body=""):
        """Use this API to create a blog.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createBlog()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.BlogRequest import BlogRequest
        schema = BlogRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getBlogs(self, page_no=None, page_size=None):
        """Use this API to get a list of blogs along with their details, such as the title, reading time, publish status, feature image, tags, author, etc.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getBlogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/", page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateBlog(self, id=None, body=""):
        """Use this API to update the details of an existing blog which includes title, feature image, content, SEO details, expiry, etc.
        :param id : ID allotted to the blog. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.updateBlog()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.BlogRequest import BlogRequest
        schema = BlogRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteBlog(self, id=None):
        """Use this API to delete a blog.
        :param id : ID allotted to the blog. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteBlog()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getComponentById(self, slug=None):
        """Use this API to retrieve the components of a blog, such as title, slug, feature image, content, schedule, publish status, author, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = ContentValidator.getComponentById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/blogs/{slug}", slug=slug), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def addDataLoader(self, body=""):
        """Use this API to add data loader. This includes the data loader name, operationId, service name and its type (url/function) with corresponding value.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.addDataLoader()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DataLoaderSchema import DataLoaderSchema
        schema = DataLoaderSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getDataLoaders(self, ):
        """Use this to get all data loaders of an application
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getDataLoaders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def deleteDataLoader(self, data_loader_id=None):
        """Use this API to delete data loader.
        :param data_loader_id : ID allotted to the data loader. : type string
        """
        payload = {}
        
        if data_loader_id:
            payload["data_loader_id"] = data_loader_id
        

        # Parameter validation
        schema = ContentValidator.deleteDataLoader()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}]}""", data_loader_id=data_loader_id)
        query_string = await create_query_string(data_loader_id=data_loader_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", data_loader_id=data_loader_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def editDataLoader(self, data_loader_id=None, body=""):
        """Use this API to edit the details of an existing data loader by its ID.
        :param data_loader_id : ID allotted to the data loader. : type string
        """
        payload = {}
        
        if data_loader_id:
            payload["data_loader_id"] = data_loader_id
        

        # Parameter validation
        schema = ContentValidator.editDataLoader()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DataLoaderSchema import DataLoaderSchema
        schema = DataLoaderSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}]}""", data_loader_id=data_loader_id)
        query_string = await create_query_string(data_loader_id=data_loader_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}", data_loader_id=data_loader_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getDataLoadersByService(self, service_name=None):
        """Use this to get all data loaders of an application by service name
        :param service_name : Service name of the data loader. : type string
        """
        payload = {}
        
        if service_name:
            payload["service_name"] = service_name
        

        # Parameter validation
        schema = ContentValidator.getDataLoadersByService()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/service/:service_name", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"service_name","in":"path","description":"Service name of the data loader.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"service_name","in":"path","description":"Service name of the data loader.","required":true,"schema":{"type":"string"}}]}""", service_name=service_name)
        query_string = await create_query_string(service_name=service_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/service/:service_name", service_name=service_name), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def selectDataLoader(self, data_loader_id=None):
        """Use this API to select a data loader to be used in applications.
        :param data_loader_id : ID allotted to the data loader. : type string
        """
        payload = {}
        
        if data_loader_id:
            payload["data_loader_id"] = data_loader_id
        

        # Parameter validation
        schema = ContentValidator.selectDataLoader()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}/select", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"data_loader_id","in":"path","description":"ID allotted to the data loader.","required":true,"schema":{"type":"string"}}]}""", data_loader_id=data_loader_id)
        query_string = await create_query_string(data_loader_id=data_loader_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{data_loader_id}/select", data_loader_id=data_loader_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def resetDataLoader(self, service=None, operation_id=None):
        """Use this API to reselect a data loader.
        :param service : Name of service. : type string
        :param operation_id : Name of operation id of the service. : type string
        """
        payload = {}
        
        if service:
            payload["service"] = service
        
        if operation_id:
            payload["operation_id"] = operation_id
        

        # Parameter validation
        schema = ContentValidator.resetDataLoader()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{service}/{operation_id}/reset", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"service","in":"path","description":"Name of service.","required":true,"schema":{"type":"string"}},{"name":"operation_id","in":"path","description":"Name of operation id of the service.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"service","in":"path","description":"Name of service.","required":true,"schema":{"type":"string"}},{"name":"operation_id","in":"path","description":"Name of operation id of the service.","required":true,"schema":{"type":"string"}}]}""", service=service, operation_id=operation_id)
        query_string = await create_query_string(service=service, operation_id=operation_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/data-loader/{service}/{operation_id}/reset", service=service, operation_id=operation_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getFaqCategories(self, ):
        """FAQs can be divided into categories. Use this API to get a list of FAQ categories.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getFaqCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/categories", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/categories", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getFaqCategoryBySlugOrId(self, id_or_slug=None):
        """FAQs can be divided into categories. Use this API to get an FAQ categories using its slug or ID.
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if id_or_slug:
            payload["id_or_slug"] = id_or_slug
        

        # Parameter validation
        schema = ContentValidator.getFaqCategoryBySlugOrId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}]}""", id_or_slug=id_or_slug)
        query_string = await create_query_string(id_or_slug=id_or_slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}", id_or_slug=id_or_slug), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createFaqCategory(self, body=""):
        """FAQs help users to solve an issue or know more about a process. FAQs can be categorized separately, for e.g. some questions can be related to payment, some could be related to purchase, shipping, navigating, etc. Use this API to create an FAQ category.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createFaqCategory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateFaqCategoryRequestSchema import CreateFaqCategoryRequestSchema
        schema = CreateFaqCategoryRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def updateFaqCategory(self, id=None, body=""):
        """Use this API to edit an existing FAQ category.
        :param id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.updateFaqCategory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateFaqCategoryRequestSchema import UpdateFaqCategoryRequestSchema
        schema = UpdateFaqCategoryRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteFaqCategory(self, id=None):
        """Use this API to delete an FAQ category.
        :param id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteFaqCategory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getFaqsByCategoryIdOrSlug(self, id_or_slug=None):
        """Use this API to retrieve all the commonly asked question and answers belonging to an FAQ category.
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if id_or_slug:
            payload["id_or_slug"] = id_or_slug
        

        # Parameter validation
        schema = ContentValidator.getFaqsByCategoryIdOrSlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}/faqs", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}]}""", id_or_slug=id_or_slug)
        query_string = await create_query_string(id_or_slug=id_or_slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{id_or_slug}/faqs", id_or_slug=id_or_slug), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def addFaq(self, category_id=None, body=""):
        """FAQs help users to solve an issue or know more about a process. Use this API to create an FAQ for a given FAQ category.
        :param category_id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if category_id:
            payload["category_id"] = category_id
        

        # Parameter validation
        schema = ContentValidator.addFaq()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateFaqSchema import CreateFaqSchema
        schema = CreateFaqSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faqs", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}]}""", category_id=category_id)
        query_string = await create_query_string(category_id=category_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faqs", category_id=category_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def updateFaq(self, category_id=None, faq_id=None, body=""):
        """Use this API to edit an existing FAQ.
        :param category_id : ID allotted to an FAQ category. : type string
        :param faq_id : ID allotted to an FAQ. : type string
        """
        payload = {}
        
        if category_id:
            payload["category_id"] = category_id
        
        if faq_id:
            payload["faq_id"] = faq_id
        

        # Parameter validation
        schema = ContentValidator.updateFaq()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateFaqSchema import CreateFaqSchema
        schema = CreateFaqSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}]}""", category_id=category_id, faq_id=faq_id)
        query_string = await create_query_string(category_id=category_id, faq_id=faq_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", category_id=category_id, faq_id=faq_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteFaq(self, category_id=None, faq_id=None):
        """Use this API to delete an existing FAQ.
        :param category_id : ID allotted to an FAQ category. : type string
        :param faq_id : ID allotted to an FAQ. : type string
        """
        payload = {}
        
        if category_id:
            payload["category_id"] = category_id
        
        if faq_id:
            payload["faq_id"] = faq_id
        

        # Parameter validation
        schema = ContentValidator.deleteFaq()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}]}""", category_id=category_id, faq_id=faq_id)
        query_string = await create_query_string(category_id=category_id, faq_id=faq_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/category/{category_id}/faq/{faq_id}", category_id=category_id, faq_id=faq_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getFaqByIdOrSlug(self, id_or_slug=None):
        """Use this API to retrieve a specific FAQ. You will get the question and answer of that FAQ.
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if id_or_slug:
            payload["id_or_slug"] = id_or_slug
        

        # Parameter validation
        schema = ContentValidator.getFaqByIdOrSlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/{id_or_slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}]}""", id_or_slug=id_or_slug)
        query_string = await create_query_string(id_or_slug=id_or_slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/faq/{id_or_slug}", id_or_slug=id_or_slug), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getLandingPages(self, page_no=None, page_size=None):
        """Landing page is the first page that a prospect lands upon while visiting a website. Use this API to fetch a list of landing pages.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getLandingPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createLandingPage(self, body=""):
        """Landing page is the first page that a prospect lands upon while visiting a website. Use this API to create a landing page.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createLandingPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.LandingPageSchema import LandingPageSchema
        schema = LandingPageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def updateLandingPage(self, id=None, body=""):
        """Use this API to edit the details of an existing landing page.
        :param id : ID allotted to a landing page. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.updateLandingPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.LandingPageSchema import LandingPageSchema
        schema = LandingPageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteLandingPage(self, id=None):
        """Use this API to delete an existing landing page.
        :param id : ID allotted to a landing page. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteLandingPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/landing-page/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getLegalInformation(self, ):
        """Use this API to get the legal information of an application, which includes Policy, Terms and Conditions, Shipping Policy and FAQ regarding the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getLegalInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateLegalInformation(self, body=""):
        """Use this API to edit, update and save the legal information of an application, which includes Policy, Terms and Conditions, Shipping Policy and FAQ regarding the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updateLegalInformation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ApplicationLegal import ApplicationLegal
        schema = ApplicationLegal()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/legal", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getNavigations(self, device_platform=None, page_no=None, page_size=None):
        """Use this API to fetch the navigations details which includes the items of the navigation pane. It also shows the orientation, links, sub-navigations, etc.
        :param device_platform : Filter navigations by platform. Acceptable values are: web, android, ios, all : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if device_platform:
            payload["device_platform"] = device_platform
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getNavigations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", device_platform=device_platform, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(device_platform=device_platform, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", device_platform=device_platform, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createNavigation(self, body=""):
        """Navigation is the arrangement of navigational items to ease the accessibility of resources for users on a website. Use this API to create a navigation.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createNavigation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.NavigationRequest import NavigationRequest
        schema = NavigationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getDefaultNavigations(self, ):
        """On any website (application), there are navigations that are present by default. Use this API to retrieve those default navigations.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getDefaultNavigations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/default", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/default", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getNavigationBySlug(self, slug=None, device_platform=None):
        """Use this API to retrieve a navigation by its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API. : type string
        :param device_platform : Filter navigations by platform. Acceptable values are: web, android, ios, all : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if device_platform:
            payload["device_platform"] = device_platform
        

        # Parameter validation
        schema = ContentValidator.getNavigationBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug, device_platform=device_platform)
        query_string = await create_query_string(slug=slug, device_platform=device_platform)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{slug}", slug=slug, device_platform=device_platform), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateNavigation(self, id=None, body=""):
        """Use this API to edit the details of an existing navigation.
        :param id : ID allotted to the navigation. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.updateNavigation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.NavigationRequest import NavigationRequest
        schema = NavigationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteNavigation(self, id=None):
        """Use this API to delete an existing navigation.
        :param id : ID allotted to the navigation. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteNavigation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/navigations/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getPageMeta(self, ):
        """Use this API to get the meta of custom pages (blog, page) and default system pages (e.g. home/brand/category/collection).
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getPageMeta()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/meta", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/meta", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getPageSpec(self, ):
        """Use this API to get the specifications of a page, such as page type, display name, params and query.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getPageSpec()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/spec", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/spec", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createPagePreview(self, body=""):
        """Use this API to create a page preview to check the appearance of a custom page.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createPagePreview()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PageRequest import PageRequest
        schema = PageRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/preview/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/preview/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def updatePagePreview(self, slug=None, body=""):
        """Use this API to change the publish status of an existing page. Allows you to publish and unpublish the page.
        :param slug : A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = ContentValidator.updatePagePreview()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PagePublishRequest import PagePublishRequest
        schema = PagePublishRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/publish/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/publish/{slug}", slug=slug), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deletePage(self, id=None):
        """Use this API to delete an existing page.
        :param id : ID allotted to the page. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deletePage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updatePathRedirectionRules(self, body=""):
        """Use this API to add, update or delete path-based redirection rules
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updatePathRedirectionRules()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PathMappingSchema import PathMappingSchema
        schema = PathMappingSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getPathRedirectionRules(self, ):
        """Use this API to get path based redirection rules.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getPathRedirectionRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/path-mappings", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getSEOConfiguration(self, ):
        """Use this API to know how the SEO is configured in the application. This includes the sitemap, robot.txt, custom meta tags, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getSEOConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateSEOConfiguration(self, body=""):
        """Use this API to edit the SEO details of an application. This includes the sitemap, robot.txt, custom meta tags, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updateSEOConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SeoComponent import SeoComponent
        schema = SeoComponent()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/seo", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getSlideshows(self, device_platform=None, page_no=None, page_size=None):
        """A slideshow is a group of images, videos or a combination of both that are shown on the website in the form of slides. Use this API to fetch a list of slideshows.
        :param device_platform : Filter slideshows by platform. Acceptable values are: web, android, ios and all : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if device_platform:
            payload["device_platform"] = device_platform
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getSlideshows()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", device_platform=device_platform, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(device_platform=device_platform, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/", device_platform=device_platform, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createSlideshow(self, body=""):
        """A slideshow is a group of images, videos or a combination of both that are shown on the website in the form of slides. Use this API to create a slideshow.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createSlideshow()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SlideshowRequest import SlideshowRequest
        schema = SlideshowRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getSlideshowBySlug(self, slug=None, device_platform=None):
        """Use this API to retrieve the details of a slideshow by its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API. : type string
        :param device_platform : Filter slideshows by platform. Acceptable values are: web, android, ios and all : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if device_platform:
            payload["device_platform"] = device_platform
        

        # Parameter validation
        schema = ContentValidator.getSlideshowBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug, device_platform=device_platform)
        query_string = await create_query_string(slug=slug, device_platform=device_platform)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{slug}", slug=slug, device_platform=device_platform), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateSlideshow(self, id=None, body=""):
        """Use this API to edit the details of an existing slideshow.
        :param id : ID allotted to the slideshow. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.updateSlideshow()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SlideshowRequest import SlideshowRequest
        schema = SlideshowRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteSlideshow(self, id=None):
        """Use this API to delete an existing slideshow.
        :param id : ID allotted to the slideshow. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteSlideshow()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/slideshows/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getSupportInformation(self, ):
        """Use this API to get the contact details for customer support, including emails and phone numbers.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getSupportInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateSupportInformation(self, body=""):
        """Use this API to edit the existing contact details for customer support, including emails and phone numbers.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updateSupportInformation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.Support import Support
        schema = Support()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/support", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def updateInjectableTag(self, body=""):
        """Use this API to edit the details of an existing tag. This includes the tag name, tag type (css/js), url and position of the tag.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.updateInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateTagRequestSchema import CreateTagRequestSchema
        schema = CreateTagRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteAllInjectableTags(self, ):
        """Use this API to delete all the existing tags at once.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.deleteAllInjectableTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getInjectableTags(self, ):
        """Use this API to get all the CSS and JS injected in the application in the form of tags.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.getInjectableTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def addInjectableTag(self, body=""):
        """CSS and JS can be injected in the application (website) with the help of tags. Use this API to create such tags by entering the tag name, tag type (css/js), url and position of the tag.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.addInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateTagRequestSchema import CreateTagRequestSchema
        schema = CreateTagRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/add", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/add", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def removeInjectableTag(self, body=""):
        """Use this API to delete an existing tag.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.removeInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.RemoveHandpickedSchema import RemoveHandpickedSchema
        schema = RemoveHandpickedSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/remove/handpicked", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/remove/handpicked", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def editInjectableTag(self, tag_id=None, body=""):
        """Use this API to edit the details of an existing tag by its ID.
        :param tag_id : ID allotted to the tag. : type string
        """
        payload = {}
        
        if tag_id:
            payload["tag_id"] = tag_id
        

        # Parameter validation
        schema = ContentValidator.editInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateHandpickedSchema import UpdateHandpickedSchema
        schema = UpdateHandpickedSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/edit/handpicked/{tag_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"tag_id","in":"path","description":"ID allotted to the tag.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"tag_id","in":"path","description":"ID allotted to the tag.","required":true,"schema":{"type":"string"}}]}""", tag_id=tag_id)
        query_string = await create_query_string(tag_id=tag_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/tags/edit/handpicked/{tag_id}", tag_id=tag_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def createPage(self, body=""):
        """Use this API to create a custom page using a title, seo, publish status, feature image, tags, meta, etc.
        """
        payload = {}
        

        # Parameter validation
        schema = ContentValidator.createPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PageRequest import PageRequest
        schema = PageRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getPages(self, page_no=None, page_size=None):
        """Use this API to retrieve a list of pages.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/", page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updatePage(self, id=None, body=""):
        """Use this API to edit the details of an existing page, such as its title, seo, publish status, feature image, tags, schedule, etc.
        :param id : ID allotted to the page. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.updatePage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PageSchema import PageSchema
        schema = PageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getPageBySlug(self, slug=None):
        """Use this API to retrieve the components of a page, such as its title, seo, publish status, feature image, tags, schedule, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = ContentValidator.getPageBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/content/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/pages/{slug}", slug=slug), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    

class Billing:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    

class Communication:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getCampaigns(self, page_no=None, page_size=None, sort=None):
        """Get campaigns
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getCampaigns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createCampaign(self, body=""):
        """Create campaign
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createCampaign()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CampaignReq import CampaignReq
        schema = CampaignReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getCampaignById(self, id=None):
        """Get campaign by id
        :param id : Campaign id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getCampaignById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateCampaignById(self, id=None, body=""):
        """Update campaign by id
        :param id : Campaign id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateCampaignById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CampaignReq import CampaignReq
        schema = CampaignReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getStatsOfCampaignById(self, id=None):
        """Get stats of campaign by id
        :param id : Campaign id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getStatsOfCampaignById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/get-stats/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/get-stats/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getAudiences(self, page_no=None, page_size=None, sort=None):
        """Get audiences
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getAudiences()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createAudience(self, body=""):
        """Create audience
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createAudience()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AudienceReq import AudienceReq
        schema = AudienceReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getBigqueryHeaders(self, body=""):
        """Get bigquery headers
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getBigqueryHeaders()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.BigqueryHeadersReq import BigqueryHeadersReq
        schema = BigqueryHeadersReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-headers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-headers", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getAudienceById(self, id=None):
        """Get audience by id
        :param id : Audience id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getAudienceById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateAudienceById(self, id=None, body=""):
        """Update audience by id
        :param id : Audience id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateAudienceById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AudienceReq import AudienceReq
        schema = AudienceReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getNSampleRecordsFromCsv(self, body=""):
        """Get n sample records from csv
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getNSampleRecordsFromCsv()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.GetNRecordsCsvReq import GetNRecordsCsvReq
        schema = GetNRecordsCsvReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/get-n-records", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/get-n-records", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getEmailProviders(self, page_no=None, page_size=None, sort=None):
        """Get email providers
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getEmailProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createEmailProvider(self, body=""):
        """Create email provider
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createEmailProvider()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EmailProviderReq import EmailProviderReq
        schema = EmailProviderReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getEmailProviderById(self, id=None):
        """Get email provider by id
        :param id : Email provider id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getEmailProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateEmailProviderById(self, id=None, body=""):
        """Update email provider by id
        :param id : Email provider id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateEmailProviderById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EmailProviderReq import EmailProviderReq
        schema = EmailProviderReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getEmailTemplates(self, page_no=None, page_size=None, sort=None):
        """Get email templates
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getEmailTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createEmailTemplate(self, body=""):
        """Create email template
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createEmailTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EmailTemplateReq import EmailTemplateReq
        schema = EmailTemplateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getSystemEmailTemplates(self, page_no=None, page_size=None, sort=None):
        """Get system email templates
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getSystemEmailTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/system-templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/system-templates", page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getEmailTemplateById(self, id=None):
        """Get email template by id
        :param id : Email template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getEmailTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateEmailTemplateById(self, id=None, body=""):
        """Update email template by id
        :param id : Email template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateEmailTemplateById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EmailTemplateReq import EmailTemplateReq
        schema = EmailTemplateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteEmailTemplateById(self, id=None):
        """Delete email template by id
        :param id : Email template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.deleteEmailTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def sendCommunicationSynchronously(self, body=""):
        """Send email or sms synchronously
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.sendCommunicationSynchronously()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EngineRequest import EngineRequest
        schema = EngineRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-instant", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-instant", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def sendCommunicationAsynchronously(self, body=""):
        """Send email or sms asynchronously
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.sendCommunicationAsynchronously()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EngineRequest import EngineRequest
        schema = EngineRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-async", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-async", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getEventSubscriptions(self, page_no=None, page_size=None, populate=None):
        """Get event subscriptions
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param populate : populate fields : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if populate:
            payload["populate"] = populate
        

        # Parameter validation
        schema = CommunicationValidator.getEventSubscriptions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"populate","in":"query","schema":{"type":"string"},"description":"populate fields"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"populate","in":"query","schema":{"type":"string"},"description":"populate fields"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, populate=populate)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, populate=populate)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions", page_no=page_no, page_size=page_size, populate=populate), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getJobs(self, page_no=None, page_size=None, sort=None):
        """Get jobs
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getJobs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/jobs", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/jobs", page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def triggerCampaignJob(self, body=""):
        """Trigger campaign job
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.triggerCampaignJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.TriggerJobRequest import TriggerJobRequest
        schema = TriggerJobRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/trigger-job", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/trigger-job", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getJobLogs(self, page_no=None, page_size=None, sort=None):
        """Get job logs
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getJobLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/logs", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/logs", page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getCommunicationLogs(self, page_id=None, page_size=None, sort=None, query=None):
        """Get communication logs
        :param page_id : Current page no : type string
        :param page_size : Current request items count : type integer
        :param sort : To sort based on _id : type object
        :param query :  : type object
        """
        payload = {}
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        
        if query:
            payload["query"] = query
        

        # Parameter validation
        schema = CommunicationValidator.getCommunicationLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/log", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_id","in":"query","schema":{"type":"string"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"_id":{"type":"integer"}}},"description":"To sort based on _id"},{"name":"query","in":"query","schema":{"type":"object"}}],"query":[{"name":"page_id","in":"query","schema":{"type":"string"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"_id":{"type":"integer"}}},"description":"To sort based on _id"},{"name":"query","in":"query","schema":{"type":"object"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_id=page_id, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_id=page_id, page_size=page_size, sort=sort, query=query)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/log", page_id=page_id, page_size=page_size, sort=sort, query=query), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getSmsProviders(self, page_no=None, page_size=None, sort=None):
        """Get sms providers
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getSmsProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createSmsProvider(self, body=""):
        """Create sms provider
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createSmsProvider()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SmsProviderReq import SmsProviderReq
        schema = SmsProviderReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getSmsProviderById(self, id=None):
        """Get sms provider by id
        :param id : Sms provider id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getSmsProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateSmsProviderById(self, id=None, body=""):
        """Update sms provider by id
        :param id : Sms provider id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateSmsProviderById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SmsProviderReq import SmsProviderReq
        schema = SmsProviderReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getSmsTemplates(self, page_no=None, page_size=None, sort=None):
        """Get sms templates
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getSmsTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createSmsTemplate(self, body=""):
        """Create sms template
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createSmsTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SmsTemplateReq import SmsTemplateReq
        schema = SmsTemplateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getSmsTemplateById(self, id=None):
        """Get sms template by id
        :param id : Sms template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getSmsTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateSmsTemplateById(self, id=None, body=""):
        """Update sms template by id
        :param id : Sms template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateSmsTemplateById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SmsTemplateReq import SmsTemplateReq
        schema = SmsTemplateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteSmsTemplateById(self, id=None):
        """Delete sms template by id
        :param id : Sms template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.deleteSmsTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getSystemSystemTemplates(self, page_no=None, page_size=None, sort=None):
        """Get system sms templates
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getSystemSystemTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/system-templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/system-templates", page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    

class Payment:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getBrandPaymentGatewayConfig(self, ):
        """Get All Brand Payment Gateway Config Secret
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.getBrandPaymentGatewayConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def saveBrandPaymentGatewayConfig(self, body=""):
        """Save Config Secret For Brand Payment Gateway
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.saveBrandPaymentGatewayConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PaymentGatewayConfigRequest import PaymentGatewayConfigRequest
        schema = PaymentGatewayConfigRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def updateBrandPaymentGatewayConfig(self, body=""):
        """Save Config Secret For Brand Payment Gateway
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.updateBrandPaymentGatewayConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PaymentGatewayConfigRequest import PaymentGatewayConfigRequest
        schema = PaymentGatewayConfigRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/aggregator/request", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getPaymentModeRoutes(self, refresh=None, request_type=None):
        """Use this API to get Get All Valid Payment Options for making payment
        :param refresh :  : type boolean
        :param request_type :  : type string
        """
        payload = {}
        
        if refresh:
            payload["refresh"] = refresh
        
        if request_type:
            payload["request_type"] = request_type
        

        # Parameter validation
        schema = PaymentValidator.getPaymentModeRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"refresh","in":"query","required":true,"schema":{"type":"boolean"}},{"name":"request_type","in":"query","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"refresh","in":"query","required":true,"schema":{"type":"boolean"}},{"name":"request_type","in":"query","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", refresh=refresh, request_type=request_type)
        query_string = await create_query_string(refresh=refresh, request_type=request_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/options", refresh=refresh, request_type=request_type), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def addBeneficiaryDetails(self, body=""):
        """Use this API to save bank details for returned/cancelled order to refund amount in his account.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.addBeneficiaryDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AddBeneficiaryDetailsRequest import AddBeneficiaryDetailsRequest
        schema = AddBeneficiaryDetailsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/account", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getUserOrderBeneficiaries(self, order_id=None):
        """Get all active  beneficiary details added by the user for refund
        :param order_id :  : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = PaymentValidator.getUserOrderBeneficiaries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/order", """{"required":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", order_id=order_id, )
        query_string = await create_query_string(order_id=order_id, )
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/order", order_id=order_id, ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getUserBeneficiaries(self, order_id=None):
        """Get all active  beneficiary details added by the user for refund
        :param order_id :  : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = PaymentValidator.getUserBeneficiaries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/user", """{"required":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", order_id=order_id, )
        query_string = await create_query_string(order_id=order_id, )
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/refund/accounts/user", order_id=order_id, ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def confirmPayment(self, body=""):
        """Use this API to confirm payment after payment gateway accepted payment.
        """
        payload = {}
        

        # Parameter validation
        schema = PaymentValidator.confirmPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PaymentConfirmationRequest import PaymentConfirmationRequest
        schema = PaymentConfirmationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/confirm", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/payment/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/confirm", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    

class Order:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/details", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"next","in":"query","description":"Next","required":false,"schema":{"type":"string"}},{"name":"previous","in":"query","description":"Previous","required":false,"schema":{"type":"string"}}],"query":[{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"next","in":"query","description":"Next","required":false,"schema":{"type":"string"}},{"name":"previous","in":"query","description":"Previous","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, next=next, previous=previous)
        query_string = await create_query_string(order_id=order_id, next=next, previous=previous)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/details", order_id=order_id, next=next, previous=previous), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def trackShipmentPlatform(self, shipment_id=None):
        """Shipment Track
        :param shipment_id : Shipment Id : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.trackShipmentPlatform()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/track", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"Shipment Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"Shipment Id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/track", shipment_id=shipment_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def trackOrder(self, order_id=None):
        """Order Track
        :param order_id : Order Id : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = OrderValidator.trackOrder()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/{order_id}/track", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"Order Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"Order Id","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/{order_id}/track", order_id=order_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def failedOrders(self, ):
        """Failed Orders
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.failedOrders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/failed", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/failed", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def reprocessOrder(self, order_id=None):
        """Order Reprocess
        :param order_id : Order Id : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = OrderValidator.reprocessOrder()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/{order_id}/reprocess", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"Order Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"Order Id","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/{order_id}/reprocess", order_id=order_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateShipment(self, shipment_id=None, body=""):
        """Update the shipment
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.updateShipment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ShipmentUpdateRequest import ShipmentUpdateRequest
        schema = ShipmentUpdateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/update", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/update", shipment_id=shipment_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getPlatformShipmentReasons(self, action=None):
        """Get reasons behind full or partial cancellation of a shipment
        :param action : Action : type string
        """
        payload = {}
        
        if action:
            payload["action"] = action
        

        # Parameter validation
        schema = OrderValidator.getPlatformShipmentReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/reasons/{action}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"action","in":"path","description":"Action","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"action","in":"path","description":"Action","required":true,"schema":{"type":"string"}}]}""", action=action)
        query_string = await create_query_string(action=action)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/reasons/{action}", action=action), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getShipmentTrackDetails(self, order_id=None, shipment_id=None):
        """Track shipment
        :param order_id : ID of the order. : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.getShipmentTrackDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/{order_id}/shipments/{shipment_id}/track", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"ID of the order.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"ID of the order.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, shipment_id=shipment_id)
        query_string = await create_query_string(order_id=order_id, shipment_id=shipment_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/{order_id}/shipments/{shipment_id}/track", order_id=order_id, shipment_id=shipment_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getOrdersByApplicationId(self, page_no=None, page_size=None, from_date=None, to_date=None, q=None, stage=None, sales_channels=None, order_id=None, stores=None, status=None, dp=None, shorten_urls=None, filter_type=None):
        """Get Orders at Application Level
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
        :param dp : Delivery Partners : type string
        :param shorten_urls : Shorten URL option : type boolean
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
        
        if dp:
            payload["dp"] = dp
        
        if shorten_urls:
            payload["shorten_urls"] = shorten_urls
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = OrderValidator.getOrdersByApplicationId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"dp","in":"query","description":"Delivery Partners","required":false,"schema":{"type":"string"}},{"name":"shorten_urls","in":"query","description":"Shorten URL option","required":false,"schema":{"type":"boolean"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"dp","in":"query","description":"Delivery Partners","required":false,"schema":{"type":"string"}},{"name":"shorten_urls","in":"query","description":"Shorten URL option","required":false,"schema":{"type":"boolean"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, dp=dp, shorten_urls=shorten_urls, filter_type=filter_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, dp=dp, shorten_urls=shorten_urls, filter_type=filter_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, dp=dp, shorten_urls=shorten_urls, filter_type=filter_type), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    

class Catalog:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def updateSearchKeywords(self, id=None, body=""):
        """Update Search Keyword by its id. On successful request, returns the updated collection
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateSearchKeywords()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateSearchKeyword import CreateSearchKeyword
        schema = CreateSearchKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteSearchKeywords(self, id=None):
        """Delete a keywords by it's id. Returns an object that tells whether the keywords was deleted successfully
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getSearchKeywords(self, id=None):
        """Get the details of a words by its `id`. If successful, returns a Collection resource in the response body specified in `GetSearchWordsDetailResponseSchema`
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createCustomKeyword(self, body=""):
        """Create a Custom Search Keywords. See `CreateSearchKeywordSchema` for the list of attributes needed to create a mapping and /collections/query-options for the available options to create a rule. On successful request, returns a paginated list of collections specified in `CreateSearchKeywordSchema`
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCustomKeyword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateSearchKeyword import CreateSearchKeyword
        schema = CreateSearchKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getAllSearchKeyword(self, ):
        """Custom Search Keyword allows you to map conditions with keywords to give you the ultimate results
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAllSearchKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/keyword/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateAutocompleteKeyword(self, id=None, body=""):
        """Update a mapping by it's id. On successful request, returns the updated Keyword mapping
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateAutocompleteKeyword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateAutocompleteKeyword import CreateAutocompleteKeyword
        schema = CreateAutocompleteKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteAutocompleteKeyword(self, id=None):
        """Delete a keywords by it's id. Returns an object that tells whether the keywords was deleted successfully
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteAutocompleteKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getAutocompleteKeywordDetail(self, id=None):
        """Get the details of a words by its `id`. If successful, returns a keywords resource in the response body specified in `GetAutocompleteWordsResponseSchema`
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getAutocompleteKeywordDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createCustomAutocompleteRule(self, body=""):
        """Create a Custom Autocomplete Keywords. See `CreateAutocompleteKeywordSchema` for the list of attributes needed to create a mapping and /collections/query-options for the available options to create a rule. On successful request, returns a paginated list of collections specified in `CreateAutocompleteKeywordSchema`
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCustomAutocompleteRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateAutocompleteKeyword import CreateAutocompleteKeyword
        schema = CreateAutocompleteKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getAutocompleteConfig(self, ):
        """Custom Autocomplete Keyword allows you to map conditions with keywords to give you the ultimate results
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getAutocompleteConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/search/autocomplete/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateAppProduct(self, item_id=None, body=""):
        """This API helps to update data associated to a item custom meta.
        :param item_id : product id for which the custom_meta is associated. : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        

        # Parameter validation
        schema = CatalogValidator.updateAppProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ApplicationItemMeta import ApplicationItemMeta
        schema = ApplicationItemMeta()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to custom meta.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"application id for which the custom_meta is associated.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"product id for which the custom_meta is associated.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to custom meta.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"application id for which the custom_meta is associated.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"product id for which the custom_meta is associated.","schema":{"type":"string"},"required":true}]}""", item_id=item_id)
        query_string = await create_query_string(item_id=item_id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product/{item_id}/", item_id=item_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getCatalogConfiguration(self, ):
        """configuration meta  details for catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getCatalogConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/metadata/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/metadata/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createConfigurationProductListing(self, body=""):
        """Add configuration for products & listing.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createConfigurationProductListing()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AppConfiguration import AppConfiguration
        schema = AppConfiguration()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getConfigurations(self, ):
        """configured details for catalog.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createConfigurationByType(self, type=None, body=""):
        """Add configuration for categories & brands.
        :param type : type can be brands, categories etc. : type string
        """
        payload = {}
        
        if type:
            payload["type"] = type
        

        # Parameter validation
        schema = CatalogValidator.createConfigurationByType()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AppConfiguration import AppConfiguration
        schema = AppConfiguration()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"type","description":"type can be brands, categories etc.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"type","description":"type can be brands, categories etc.","schema":{"type":"string"},"required":true}]}""", type=type)
        query_string = await create_query_string(type=type)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", type=type), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getConfigurationByType(self, type=None):
        """configured details for catalog.
        :param type : type can be brands, categories etc. : type string
        """
        payload = {}
        
        if type:
            payload["type"] = type
        

        # Parameter validation
        schema = CatalogValidator.getConfigurationByType()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"type","description":"type can be brands, categories etc.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"type","description":"type can be brands, categories etc.","schema":{"type":"string"},"required":true}]}""", type=type)
        query_string = await create_query_string(type=type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/product-configuration/{type}/", type=type), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getQueryFilters(self, ):
        """Get query filters to configure a collection
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getQueryFilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/query-options/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/query-options/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createCollection(self, body=""):
        """Create a collection. See `CreateCollectionRequestSchema` for the list of attributes needed to create a collection and collections/query-options for the available options to create a collection. On successful request, returns a paginated list of collections specified in `CollectionCreateResponse`
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.createCollection()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateCollection import CreateCollection
        schema = CreateCollection()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getAllCollections(self, q=None, tags=None, is_active=None, page_no=None, page_size=None):
        """A Collection allows you to organize your products into hierarchical groups. For example, a dress might be in the category _Clothing_, the individual product might also be in the collection _Summer_. On successful request, returns all the collections as specified in `CollectionListingSchema`
        :param q : Get collection list filtered by q string, : type string
        :param tags : Each response will contain next_id param, which should be sent back to make pagination work. : type array
        :param is_active : get collections filtered by active status. : type boolean
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if q:
            payload["q"] = q
        
        if tags:
            payload["tags"] = tags
        
        if is_active:
            payload["is_active"] = is_active
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getAllCollections()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"q","description":"Get collection list filtered by q string,","schema":{"type":"string"},"required":false},{"in":"query","name":"tags","description":"Each response will contain next_id param, which should be sent back to make pagination work.","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"is_active","description":"get collections filtered by active status.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"q","description":"Get collection list filtered by q string,","schema":{"type":"string"},"required":false},{"in":"query","name":"tags","description":"Each response will contain next_id param, which should be sent back to make pagination work.","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"is_active","description":"get collections filtered by active status.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", q=q, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(q=q, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/", q=q, tags=tags, is_active=is_active, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getCollectionDetail(self, slug=None):
        """Get the details of a collection by its `slug`. If successful, returns a Collection resource in the response body specified in `CollectionDetailResponse`
        :param slug : A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.getCollectionDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{slug}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","schema":{"type":"string"},"required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{slug}/", slug=slug), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateCollection(self, id=None, body=""):
        """Update a collection by it's id. On successful request, returns the updated collection
        :param id : A `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateCollection()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateCollection import UpdateCollection
        schema = UpdateCollection()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def deleteCollection(self, id=None):
        """Delete a collection by it's id. Returns an object that tells whether the collection was deleted successfully
        :param id : A `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteCollection()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def addCollectionItems(self, id=None, body=""):
        """Adds items to a collection specified by its `id`. See `CollectionItemRequest` for the list of attributes needed to add items to an collection.
        :param id : A `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.addCollectionItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CollectionItemRequest import CollectionItemRequest
        schema = CollectionItemRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getCollectionItems(self, id=None, sort_on=None, page_id=None, page_size=None):
        """Get items from a collection specified by its `id`.
        :param id : A `id` is a unique identifier of a collection. : type string
        :param sort_on : Each response will contain sort_on param, which should be sent back to make pagination work. : type string
        :param page_id : Each response will contain next_id param, which should be sent back to make pagination work. : type string
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if sort_on:
            payload["sort_on"] = sort_on
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getCollectionItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"sort_on","description":"Each response will contain sort_on param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_id","description":"Each response will contain next_id param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"sort_on","description":"Each response will contain sort_on param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_id","description":"Each response will contain next_id param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}]}""", id=id, sort_on=sort_on, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(id=id, sort_on=sort_on, page_id=page_id, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/collections/{id}/items/", id=id, sort_on=sort_on, page_id=page_id, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getCatalogInsights(self, brand=None):
        """Catalog Insights api returns the count of catalog related data like products, brands, departments and categories that have been made live as per configuration of the app.
        :param brand : Brand slug : type string
        """
        payload = {}
        
        if brand:
            payload["brand"] = brand
        

        # Parameter validation
        schema = CatalogValidator.getCatalogInsights()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/analytics/insights/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"brand","description":"Brand slug","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"brand","description":"Brand slug","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", brand=brand)
        query_string = await create_query_string(brand=brand)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/analytics/insights/", brand=brand), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getDiscountedInventoryBySizeIdentifier(self, item_id=None, size_identifier=None, page_no=None, page_size=None, q=None, location_ids=None):
        """This API allows get Inventory data for particular company grouped by size and store.
        :param item_id : Item code of the product of which size is to be get. : type integer
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
        schema = CatalogValidator.getDiscountedInventoryBySizeIdentifier()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{item_id}/inventory/{size_identifier}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Uniquer Application ID.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"integer"},"required":true},{"in":"path","name":"size_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"location_ids","description":"Search by store ids.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"location_ids","description":"Search by store ids.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Uniquer Application ID.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"integer"},"required":true},{"in":"path","name":"size_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}]}""", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)
        query_string = await create_query_string(item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{item_id}/inventory/{size_identifier}", item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getApplicationBrands(self, department=None, page_no=None, page_size=None, q=None, brand_id=None):
        """A brand is the name under which a product is being sold. Use this API to list all the brands. You can pass optionally filter the brands by the department. If successful, returns a paginated list of brands specified in `BrandListingResponse`
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search query with brand name.Use this parameter to search brands by  brand name. : type string
        :param brand_id : Helps to sort the brands list on the basis of uid list. : type array
        """
        payload = {}
        
        if department:
            payload["department"] = department
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if brand_id:
            payload["brand_id"] = brand_id
        

        # Parameter validation
        schema = CatalogValidator.getApplicationBrands()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brands", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"]},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search query with brand name.Use this parameter to search brands by  brand name.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_id","description":"Helps to sort the brands list on the basis of uid list.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"query":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"]},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search query with brand name.Use this parameter to search brands by  brand name.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_id","description":"Helps to sort the brands list on the basis of uid list.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id)
        query_string = await create_query_string(department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/brands", department=department, page_no=page_no, page_size=page_size, q=q, brand_id=brand_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getDepartments(self, ):
        """Departments are a way to categorise similar products. A product can lie in multiple departments. For example, a skirt can below to the 'Women's Fashion' Department while a handbag can lie in 'Women's Accessories' Department. Use this API to list all the departments. If successful, returns the list of departments specified in `DepartmentResponse`
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getDepartments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/departments", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/departments", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getCategories(self, department=None):
        """List all the categories. You can optionally pass filter the brands by the department. If successful, returns a paginated list of brands specified in `CategoryListingResponse`
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API : type string
        """
        payload = {}
        
        if department:
            payload["department"] = department
        

        # Parameter validation
        schema = CatalogValidator.getCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/categories", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"]},"required":false}],"query":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"]},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", department=department)
        query_string = await create_query_string(department=department)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/categories", department=department), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getAppicationProducts(self, q=None, f=None, filters=None, sort_on=None, page_id=None, page_size=None, page_no=None, page_type=None, item_ids=None):
        """List all the products associated with a brand, collection or category in a requested sort order. The API additionally supports arbitrary search queries that may refer the name of any product, brand, category or collection. If successful, returns a paginated list of products specified in `ApplicationProductListingResponse`
        :param q : The search query. This can be a partial or complete name of a either a product, brand or category : type string
        :param f : The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts** : type string
        :param filters : Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters : type boolean
        :param sort_on : The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below. : type string
        :param page_id : Each response will contain **page_id** param, which should be sent back to make pagination work. : type string
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param page_no : If page_type is number then pass it to fetch page items. Default is 1. : type integer
        :param page_type : For pagination type should be cursor or number. Default is cursor. : type string
        :param item_ids : Item Ids of product : type array
        """
        payload = {}
        
        if q:
            payload["q"] = q
        
        if f:
            payload["f"] = f
        
        if filters:
            payload["filters"] = filters
        
        if sort_on:
            payload["sort_on"] = sort_on
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_type:
            payload["page_type"] = page_type
        
        if item_ids:
            payload["item_ids"] = item_ids
        

        # Parameter validation
        schema = CatalogValidator.getAppicationProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"q","description":"The search query. This can be a partial or complete name of a either a product, brand or category","schema":{"type":"string"},"required":false},{"in":"query","name":"f","description":"The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts**","schema":{"type":"string"},"required":false},{"in":"query","name":"filters","description":"Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Each response will contain **page_id** param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_no","description":"If page_type is number then pass it to fetch page items. Default is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_type","description":"For pagination type should be cursor or number. Default is cursor.","schema":{"type":"string","default":"cursor"},"required":false},{"in":"query","name":"item_ids","description":"Item Ids of product","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"query":[{"in":"query","name":"q","description":"The search query. This can be a partial or complete name of a either a product, brand or category","schema":{"type":"string"},"required":false},{"in":"query","name":"f","description":"The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts**","schema":{"type":"string"},"required":false},{"in":"query","name":"filters","description":"Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Each response will contain **page_id** param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_no","description":"If page_type is number then pass it to fetch page items. Default is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_type","description":"For pagination type should be cursor or number. Default is cursor.","schema":{"type":"string","default":"cursor"},"required":false},{"in":"query","name":"item_ids","description":"Item Ids of product","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", q=q, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids)
        query_string = await create_query_string(q=q, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products", q=q, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getProductDetailBySlug(self, slug=None):
        """Products are the core resource of an application. Products can be associated by categories, collections, brands and more. This API retrieves the product specified by the given **slug**. If successful, returns a Product resource in the response body specified in `ProductDetail`
        :param slug : The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/** : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.getProductDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{slug}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/**","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/**","schema":{"type":"string"},"required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/products/{slug}", slug=slug), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getAppProducts(self, brand_ids=None, category_ids=None, department_ids=None, tags=None, page_no=None, page_size=None, q=None):
        """Products are the core resource of an application. Products can be associated by categories, collections, brands and more. If successful, returns a Product resource in the response body specified in `ApplicationProductListingResponseDatabasePowered`
        :param brand_ids : Get multiple products filtered by Brand Ids : type array
        :param category_ids : Get multiple products filtered by Category Ids : type array
        :param department_ids : Get multiple products filtered by Department Ids : type array
        :param tags : Get multiple products filtered by tags : type array
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param q : Search with Item Code, Name, Slug or Identifier. : type string
        """
        payload = {}
        
        if brand_ids:
            payload["brand_ids"] = brand_ids
        
        if category_ids:
            payload["category_ids"] = category_ids
        
        if department_ids:
            payload["department_ids"] = department_ids
        
        if tags:
            payload["tags"] = tags
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.getAppProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/raw-products/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false},{"in":"query","name":"q","description":"Search with Item Code, Name, Slug or Identifier.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false},{"in":"query","name":"q","description":"Search with Item Code, Name, Slug or Identifier.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, page_no=page_no, page_size=page_size, q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/raw-products/", brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, page_no=page_no, page_size=page_size, q=q), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getAppLocations(self, store_type=None, uid=None, q=None, stage=None, page_no=None, page_size=None):
        """This API allows to view all the locations asscoiated to a application.
        :param store_type : Helps to sort the location list on the basis of location type. : type string
        :param uid : Helps to sort the location list on the basis of uid list. : type array
        :param q : Query that is to be searched. : type string
        :param stage : to filter companies on basis of verified or unverified companies. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 20. : type integer
        """
        payload = {}
        
        if store_type:
            payload["store_type"] = store_type
        
        if uid:
            payload["uid"] = uid
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getAppLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/locations", """{"required":[{"in":"path","name":"company_id","description":"Id of the company whose locations are to fetched","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"Id of the application whose locations are to fetched","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"store_type","description":"Helps to sort the location list on the basis of location type.","schema":{"type":"string"},"required":false},{"in":"query","name":"uid","description":"Helps to sort the location list on the basis of uid list.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"stage","description":"to filter companies on basis of verified or unverified companies.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 20.","schema":{"type":"integer","default":20},"required":false}],"query":[{"in":"query","name":"store_type","description":"Helps to sort the location list on the basis of location type.","schema":{"type":"string"},"required":false},{"in":"query","name":"uid","description":"Helps to sort the location list on the basis of uid list.","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"stage","description":"to filter companies on basis of verified or unverified companies.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 20.","schema":{"type":"integer","default":20},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company whose locations are to fetched","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"Id of the application whose locations are to fetched","schema":{"type":"string"},"required":true}]}""", store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/catalog/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/locations", store_type=store_type, uid=uid, q=q, stage=stage, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    

class CompanyProfile:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    

class FileStorage:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def appStartUpload(self, namespace=None, body=""):
        """Uploads an arbitrarily sized buffer or blob.

It has three Major Steps:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `appStartUpload`.
It returns the storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `appStartUpload` api with file (Buffer or Blob) as a request body.

### Complete
After successfully upload, call `appCompleteUpload` api to complete the upload process.
This operation will return the url for the uploaded file.

        :param namespace : bucket name : type string
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        

        # Parameter validation
        schema = FileStorageValidator.appStartUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.StartRequest import StartRequest
        schema = StartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", namespace=namespace, )
        query_string = await create_query_string(namespace=namespace, )
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/start/", namespace=namespace, ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def appCompleteUpload(self, namespace=None, body=""):
        """Uploads an arbitrarily sized buffer or blob.

It has three Major Steps:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `appStartUpload`.
It returns the storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `appStartUpload` api with file (Buffer or Blob) as a request body.

### Complete
After successfully upload, call `appCompleteUpload` api to complete the upload process.
This operation will return the url for the uploaded file.

        :param namespace : bucket name : type string
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        

        # Parameter validation
        schema = FileStorageValidator.appCompleteUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.StartResponse import StartResponse
        schema = StartResponse()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}]}""", namespace=namespace, )
        query_string = await create_query_string(namespace=namespace, )
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/upload/complete/", namespace=namespace, ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def appCopyFiles(self, sync=None, body=""):
        """Copy Files
        :param sync : sync : type boolean
        """
        payload = {}
        
        if sync:
            payload["sync"] = sync
        

        # Parameter validation
        schema = FileStorageValidator.appCopyFiles()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.BulkRequest import BulkRequest
        schema = BulkRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/uploads/copy/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"query":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application_id","required":true,"schema":{"type":"integer"}}]}""", sync=sync, )
        query_string = await create_query_string(sync=sync, )
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/uploads/copy/", sync=sync, ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"page_no","in":"query","description":"page no","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page_no","in":"query","description":"page no","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application_id","required":true,"schema":{"type":"integer"}}]}""", namespace=namespace, page_no=page_no)
        query_string = await create_query_string(namespace=namespace, page_no=page_no)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/assets/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/namespaces/{namespace}/browse/", namespace=namespace, page_no=page_no), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    

class Share:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def createShortLink(self, body=""):
        """Create short link
        """
        payload = {}
        

        # Parameter validation
        schema = ShareValidator.createShortLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ShortLinkReq import ShortLinkReq
        schema = ShortLinkReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getShortLinks(self, page_no=None, page_size=None, created_by=None, active=None, q=None):
        """Get short links
        :param page_no : Current page number : type integer
        :param page_size : Current page size : type integer
        :param created_by : Short link creator : type string
        :param active : Short link active status : type string
        :param q : Search text for original and short url : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if created_by:
            payload["created_by"] = created_by
        
        if active:
            payload["active"] = active
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = ShareValidator.getShortLinks()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"default":1,"type":"integer"}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"default":10,"type":"integer"}},{"name":"created_by","in":"query","description":"Short link creator","required":false,"schema":{"type":"string","enum":["team"]}},{"name":"active","in":"query","description":"Short link active status","required":false,"schema":{"type":"string","enum":[true,false]}},{"name":"q","in":"query","description":"Search text for original and short url","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"default":1,"type":"integer"}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"default":10,"type":"integer"}},{"name":"created_by","in":"query","description":"Short link creator","required":false,"schema":{"type":"string","enum":["team"]}},{"name":"active","in":"query","description":"Short link active status","required":false,"schema":{"type":"string","enum":[true,false]}},{"name":"q","in":"query","description":"Search text for original and short url","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, created_by=created_by, active=active, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, created_by=created_by, active=active, q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/", page_no=page_no, page_size=page_size, created_by=created_by, active=active, q=q), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getShortLinkByHash(self, hash=None):
        """Get short link by hash
        :param hash : Hash of short url : type string
        """
        payload = {}
        
        if hash:
            payload["hash"] = hash
        

        # Parameter validation
        schema = ShareValidator.getShortLinkByHash()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/{hash}/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"hash","in":"path","description":"Hash of short url","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"hash","in":"path","description":"Hash of short url","required":true,"schema":{"type":"string"}}]}""", hash=hash)
        query_string = await create_query_string(hash=hash)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/{hash}/", hash=hash), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateShortLinkById(self, id=None, body=""):
        """Update short link by id
        :param id : Short link document identifier : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ShareValidator.updateShortLinkById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ShortLinkReq import ShortLinkReq
        schema = ShortLinkReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/{id}/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Short link document identifier","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Short link document identifier","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/share/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/links/short-link/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    

class Inventory:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    

class Configuration:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getBuildConfig(self, platform_type=None):
        """Get latest build config
        :param platform_type : Current platform name : type string
        """
        payload = {}
        
        if platform_type:
            payload["platform_type"] = platform_type
        

        # Parameter validation
        schema = ConfigurationValidator.getBuildConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"Current platform name","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"Current platform name","in":"path","required":true,"name":"platform_type"}]}""", platform_type=platform_type)
        query_string = await create_query_string(platform_type=platform_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", platform_type=platform_type), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateBuildConfig(self, platform_type=None, body=""):
        """Update build config for next build
        :param platform_type : Current platform name : type string
        """
        payload = {}
        
        if platform_type:
            payload["platform_type"] = platform_type
        

        # Parameter validation
        schema = ConfigurationValidator.updateBuildConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.MobileAppConfigRequest import MobileAppConfigRequest
        schema = MobileAppConfigRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"Current platform name","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"Current platform name","in":"path","required":true,"name":"platform_type"}]}""", platform_type=platform_type)
        query_string = await create_query_string(platform_type=platform_type)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/configuration", platform_type=platform_type), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getPreviousVersions(self, platform_type=None):
        """Get previous build versions
        :param platform_type : Current platform name : type string
        """
        payload = {}
        
        if platform_type:
            payload["platform_type"] = platform_type
        

        # Parameter validation
        schema = ConfigurationValidator.getPreviousVersions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/versions", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"Current platform name","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"Current platform name","in":"path","required":true,"name":"platform_type"}]}""", platform_type=platform_type)
        query_string = await create_query_string(platform_type=platform_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/build/{platform_type}/versions", platform_type=platform_type), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getAppFeatures(self, ):
        """Get features of application
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppFeatures()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateAppFeatures(self, body=""):
        """Update features of application
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppFeatures()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AppFeatureRequest import AppFeatureRequest
        schema = AppFeatureRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/feature", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getAppBasicDetails(self, ):
        """Get basic application details like name
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppBasicDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateAppBasicDetails(self, body=""):
        """Add or update application's basic details
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppBasicDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ApplicationDetail import ApplicationDetail
        schema = ApplicationDetail()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getAppContactInfo(self, ):
        """Get Application Current Information. This includes information about social links, address and contact information of company/seller/brand of the application.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppContactInfo()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateAppContactInfo(self, body=""):
        """Save Application Current Information. This includes information about social links, address and contact information of an application.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppContactInfo()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ApplicationInformation import ApplicationInformation
        schema = ApplicationInformation()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/information", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getAppApiTokens(self, ):
        """Get social tokens.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppApiTokens()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateAppApiTokens(self, body=""):
        """Add social tokens.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppApiTokens()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.TokenResponse import TokenResponse
        schema = TokenResponse()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/token", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getAppCompanies(self, uid=None, page_no=None, page_size=None):
        """Application inventory enabled companies.
        :param uid : uid of companies to be fetched : type integer
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if uid:
            payload["uid"] = uid
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getAppCompanies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/companies", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"uid","in":"query","schema":{"type":"integer"},"description":"uid of companies to be fetched"},{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"uid","in":"query","schema":{"type":"integer"},"description":"uid of companies to be fetched"},{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", uid=uid, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(uid=uid, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/companies", uid=uid, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getAppStores(self, page_no=None, page_size=None):
        """Application inventory enabled stores.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getAppStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stores", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stores", page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getInventoryConfig(self, ):
        """Get application configuration for various features and data
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getInventoryConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateInventoryConfig(self, body=""):
        """Update application configuration for various features and data
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateInventoryConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ApplicationInventory import ApplicationInventory
        schema = ApplicationInventory()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def partiallyUpdateInventoryConfig(self, body=""):
        """Partially update application configuration for various features and data
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.partiallyUpdateInventoryConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AppInventoryPartialUpdate import AppInventoryPartialUpdate
        schema = AppInventoryPartialUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/configuration", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getAppCurrencyConfig(self, ):
        """Get application enabled currency list
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppCurrencyConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateAppCurrencyConfig(self, body=""):
        """Add initial application supported currency for various features and data. Default INR will be enabled.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppCurrencyConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AppSupportedCurrency import AppSupportedCurrency
        schema = AppSupportedCurrency()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getAppSupportedCurrency(self, ):
        """Use this API to get a list of currencies allowed in the current application. Moreover, get the name, code, symbol, and the decimal digits of the currencies.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppSupportedCurrency()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency/supported", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/currency/supported", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getOrderingStoresByFilter(self, page_no=None, page_size=None, body=""):
        """Get ordering store by filter
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getOrderingStoresByFilter()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.FilterOrderingStoreRequest import FilterOrderingStoreRequest
        schema = FilterOrderingStoreRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/stores/filter", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/stores/filter", page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def updateOrderingStoreConfig(self, body=""):
        """Add/Update ordering store config.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.updateOrderingStoreConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OrderingStoreConfig import OrderingStoreConfig
        schema = OrderingStoreConfig()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getStaffOrderingStores(self, page_no=None, page_size=None, q=None):
        """Use this API to retrieve the details of all stores access given to the staff member (the selling locations where the application will be utilized for placing orders).
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param q : Store code or name of the ordering store. : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = ConfigurationValidator.getStaffOrderingStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/staff-stores", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store."}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/ordering-store/staff-stores", page_no=page_no, page_size=page_size, q=q), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getDomains(self, ):
        """Get attached domain list.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getDomains()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def addDomain(self, body=""):
        """Add new domain to application.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.addDomain()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DomainAddRequest import DomainAddRequest
        schema = DomainAddRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def removeDomainById(self, id=None):
        """Remove attached domain.
        :param id : Domain _id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.removeDomainById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"description":"Domain _id","schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"description":"Domain _id","schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def changeDomainType(self, body=""):
        """Change a domain to Primary or Shortlink domain
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.changeDomainType()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateDomainTypeRequest import UpdateDomainTypeRequest
        schema = UpdateDomainTypeRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/set-domain", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/set-domain", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getDomainStatus(self, body=""):
        """Get domain connected status. Check if domain is live and mapped to appropriate IP to fynd servers.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getDomainStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DomainStatusRequest import DomainStatusRequest
        schema = DomainStatusRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/domain-status", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/domain/domain-status", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getApplicationById(self, ):
        """Get application data from id
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getApplicationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application/{self.applicationId}", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    

class Cart:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getCoupons(self, page_no=None, page_size=None, is_archived=None, title=None, is_public=None, is_display=None, type_slug=None, code=None):
        """Get coupon list with pagination
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param is_archived :  : type boolean
        :param title :  : type string
        :param is_public :  : type boolean
        :param is_display :  : type boolean
        :param type_slug :  : type string
        :param code :  : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if is_archived:
            payload["is_archived"] = is_archived
        
        if title:
            payload["title"] = title
        
        if is_public:
            payload["is_public"] = is_public
        
        if is_display:
            payload["is_display"] = is_display
        
        if type_slug:
            payload["type_slug"] = type_slug
        
        if code:
            payload["code"] = code
        

        # Parameter validation
        schema = CartValidator.getCoupons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Coupon max records fetched in single request"}},{"name":"is_archived","in":"query","schema":{"type":"boolean","description":"Filter by active or inactive coupon","default":false}},{"name":"title","in":"query","schema":{"type":"string","description":"Filter by `title`"}},{"name":"is_public","in":"query","schema":{"type":"boolean","description":"Filter by `is_public`"}},{"name":"is_display","in":"query","schema":{"type":"boolean","description":"Filter by `is_display`"}},{"name":"type_slug","in":"query","schema":{"type":"string","description":"Filter by coupon type"}},{"name":"code","in":"query","schema":{"type":"string","description":"Filter by `code`"}}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Coupon max records fetched in single request"}},{"name":"is_archived","in":"query","schema":{"type":"boolean","description":"Filter by active or inactive coupon","default":false}},{"name":"title","in":"query","schema":{"type":"string","description":"Filter by `title`"}},{"name":"is_public","in":"query","schema":{"type":"boolean","description":"Filter by `is_public`"}},{"name":"is_display","in":"query","schema":{"type":"boolean","description":"Filter by `is_display`"}},{"name":"type_slug","in":"query","schema":{"type":"string","description":"Filter by coupon type"}},{"name":"code","in":"query","schema":{"type":"string","description":"Filter by `code`"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createCoupon(self, body=""):
        """Create new coupon
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.createCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CouponAdd import CouponAdd
        schema = CouponAdd()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getCouponById(self, id=None):
        """Get single coupon details with `id` in path param
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CartValidator.getCouponById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateCoupon(self, id=None, body=""):
        """Update coupon with id sent in `id`
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CartValidator.updateCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CouponUpdate import CouponUpdate
        schema = CouponUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def updateCouponPartially(self, id=None, body=""):
        """Update archive/unarchive and change schedule for coupon
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CartValidator.updateCouponPartially()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CouponPartialUpdate import CouponPartialUpdate
        schema = CouponPartialUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def fetchAndvalidateCartItems(self, body=""):
        """Get all the details of cart for a list of provided `cart_items`
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.fetchAndvalidateCartItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OpenapiCartDetailsRequest import OpenapiCartDetailsRequest
        schema = OpenapiCartDetailsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/validate", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/validate", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def checkCartServiceability(self, body=""):
        """Check Pincode serviceability for cart items provided in `cart_items` and address pincode in `shipping_address`
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.checkCartServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OpenApiCartServiceabilityRequest import OpenApiCartServiceabilityRequest
        schema = OpenApiCartServiceabilityRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/serviceability", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/serviceability", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def checkoutCart(self, body=""):
        """Generate Fynd order for cart details send with provided `cart_items`
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.checkoutCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OpenApiPlatformCheckoutReq import OpenApiPlatformCheckoutReq
        schema = OpenApiPlatformCheckoutReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/checkout", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/checkout", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    

class Rewards:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getGiveaways(self, page_id=None, page_size=None):
        """List of giveaways of the current application.
        :param page_id : pagination page id : type string
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = RewardsValidator.getGiveaways()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", page_id=page_id, page_size=page_size)
        query_string = await create_query_string(page_id=page_id, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/", page_id=page_id, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def createGiveaway(self, body=""):
        """Adds a new giveaway.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.createGiveaway()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.Giveaway import Giveaway
        schema = Giveaway()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getGiveawayByID(self, id=None):
        """Get giveaway by ID.
        :param id : Giveaway ID : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = RewardsValidator.getGiveawayByID()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Giveaway ID","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Giveaway ID","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateGiveaway(self, id=None, body=""):
        """Updates the giveaway by it's ID.
        :param id : Giveaway ID : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = RewardsValidator.updateGiveaway()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.Giveaway import Giveaway
        schema = Giveaway()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Giveaway ID","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Giveaway ID","in":"path","name":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/giveaways/{id}/", id=id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getOffers(self, ):
        """List of offer of the current application.
        """
        payload = {}
        

        # Parameter validation
        schema = RewardsValidator.getOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getOfferByName(self, cookie=None, name=None):
        """Get offer by name.
        :param cookie : User's session cookie. This cookie is set in browser cookie when logged-in to fynd's authentication system i.e. `Grimlock` or by using grimlock-backend SDK for backend implementation. : type string
        :param name : Offer name : type string
        """
        payload = {}
        
        if cookie:
            payload["cookie"] = cookie
        
        if name:
            payload["name"] = name
        

        # Parameter validation
        schema = RewardsValidator.getOfferByName()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"User's session cookie. This cookie is set in browser cookie when logged-in to fynd's authentication system i.e. `Grimlock` or by using grimlock-backend SDK for backend implementation.","in":"header","name":"cookie","required":true,"schema":{"type":"string"}},{"description":"Offer name","in":"path","name":"name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[{"description":"User's session cookie. This cookie is set in browser cookie when logged-in to fynd's authentication system i.e. `Grimlock` or by using grimlock-backend SDK for backend implementation.","in":"header","name":"cookie","required":true,"schema":{"type":"string"}}],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Offer name","in":"path","name":"name","required":true,"schema":{"type":"string"}}]}""", cookie=cookie, name=name)
        query_string = await create_query_string(cookie=cookie, name=name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", cookie=cookie, name=name), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateOfferByName(self, name=None, body=""):
        """Updates the offer by name.
        :param name : Offer name : type string
        """
        payload = {}
        
        if name:
            payload["name"] = name
        

        # Parameter validation
        schema = RewardsValidator.updateOfferByName()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.Offer import Offer
        schema = Offer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Offer name","in":"path","name":"name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Offer name","in":"path","name":"name","required":true,"schema":{"type":"string"}}]}""", name=name)
        query_string = await create_query_string(name=name)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/offers/{name}/", name=name), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getUserAvailablePoints(self, user_id=None):
        """User's reward details.
        :param user_id : user id : type string
        """
        payload = {}
        
        if user_id:
            payload["user_id"] = user_id
        

        # Parameter validation
        schema = RewardsValidator.getUserAvailablePoints()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}]}""", user_id=user_id)
        query_string = await create_query_string(user_id=user_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", user_id=user_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def updateUserStatus(self, user_id=None, body=""):
        """Update user status, active/archive
        :param user_id : user id : type string
        """
        payload = {}
        
        if user_id:
            payload["user_id"] = user_id
        

        # Parameter validation
        schema = RewardsValidator.updateUserStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AppUser import AppUser
        schema = AppUser()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}]}""", user_id=user_id)
        query_string = await create_query_string(user_id=user_id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/", user_id=user_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def getUserPointsHistory(self, user_id=None, page_id=None, page_limit=None, page_size=None):
        """Get list of points transactions.
The list of points history is paginated.
        :param user_id : user id : type string
        :param page_id : PageID is the ID of the requested page. For first request it should be kept empty. : type string
        :param page_limit : PageLimit is the number of requested items in response. : type integer
        :param page_size : PageSize is the number of requested items in response. : type integer
        """
        payload = {}
        
        if user_id:
            payload["user_id"] = user_id
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_limit:
            payload["page_limit"] = page_limit
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = RewardsValidator.getUserPointsHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/points/history/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"PageID is the ID of the requested page. For first request it should be kept empty.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"PageLimit is the number of requested items in response.","in":"query","name":"page_limit","schema":{"type":"integer"}},{"description":"PageSize is the number of requested items in response.","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"PageID is the ID of the requested page. For first request it should be kept empty.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"PageLimit is the number of requested items in response.","in":"query","name":"page_limit","schema":{"type":"integer"}},{"description":"PageSize is the number of requested items in response.","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}]}""", user_id=user_id, page_id=page_id, page_limit=page_limit, page_size=page_size)
        query_string = await create_query_string(user_id=user_id, page_id=page_id, page_limit=page_limit, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/rewards/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/users/{user_id}/points/history/", user_id=user_id, page_id=page_id, page_limit=page_limit, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    

class Analytics:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getStatiscticsGroups(self, ):
        """Get statistics groups
        """
        payload = {}
        

        # Parameter validation
        schema = AnalyticsValidator.getStatiscticsGroups()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/group", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/group", ), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getStatiscticsGroupComponents(self, group_name=None):
        """Get statistics group components
        :param group_name : Group name : type string
        """
        payload = {}
        
        if group_name:
            payload["group_name"] = group_name
        

        # Parameter validation
        schema = AnalyticsValidator.getStatiscticsGroupComponents()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/group/{group_name}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"group_name","in":"path","description":"Group name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"group_name","in":"path","description":"Group name","required":true,"schema":{"type":"string"}}]}""", group_name=group_name)
        query_string = await create_query_string(group_name=group_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/group/{group_name}", group_name=group_name), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getComponentStatsCSV(self, component_name=None):
        """Get component statistics csv
        :param component_name : Component name : type string
        """
        payload = {}
        
        if component_name:
            payload["component_name"] = component_name
        

        # Parameter validation
        schema = AnalyticsValidator.getComponentStatsCSV()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/component/{component_name}.csv", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}]}""", component_name=component_name)
        query_string = await create_query_string(component_name=component_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/component/{component_name}.csv", component_name=component_name), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getComponentStatsPDF(self, component_name=None):
        """Get component statistics pdf
        :param component_name : Component name : type string
        """
        payload = {}
        
        if component_name:
            payload["component_name"] = component_name
        

        # Parameter validation
        schema = AnalyticsValidator.getComponentStatsPDF()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/component/{component_name}.pdf", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}]}""", component_name=component_name)
        query_string = await create_query_string(component_name=component_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/component/{component_name}.pdf", component_name=component_name), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getComponentStats(self, component_name=None):
        """Get component statistics
        :param component_name : Component name : type string
        """
        payload = {}
        
        if component_name:
            payload["component_name"] = component_name
        

        # Parameter validation
        schema = AnalyticsValidator.getComponentStats()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/component/{component_name}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}]}""", component_name=component_name)
        query_string = await create_query_string(component_name=component_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/component/{component_name}", component_name=component_name), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getAbandonCartList(self, from_date=None, to_date=None, page_no=None, page_size=None):
        """Get abandon carts list
        :param from_date : From date : type string
        :param to_date : To date : type string
        :param page_no : Current page number : type integer
        :param page_size : Current page size : type integer
        """
        payload = {}
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = AnalyticsValidator.getAbandonCartList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/from/{from_date}/to/{to_date}/abandon-cart/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"from_date","in":"path","description":"From date","required":true,"schema":{"type":"string"}},{"name":"to_date","in":"path","description":"To date","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"from_date","in":"path","description":"From date","required":true,"schema":{"type":"string"}},{"name":"to_date","in":"path","description":"To date","required":true,"schema":{"type":"string"}}]}""", from_date=from_date, to_date=to_date, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(from_date=from_date, to_date=to_date, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/from/{from_date}/to/{to_date}/abandon-cart/", from_date=from_date, to_date=to_date, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getAbandonCartsCSV(self, from_date=None, to_date=None):
        """Get abandon carts csv
        :param from_date : From date : type string
        :param to_date : To date : type string
        """
        payload = {}
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        

        # Parameter validation
        schema = AnalyticsValidator.getAbandonCartsCSV()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/{from_date}/to/{to_date}/abandon-cart.csv", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"from_date","in":"path","description":"From date","required":true,"schema":{"type":"string"}},{"name":"to_date","in":"path","description":"To date","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"from_date","in":"path","description":"From date","required":true,"schema":{"type":"string"}},{"name":"to_date","in":"path","description":"To date","required":true,"schema":{"type":"string"}}]}""", from_date=from_date, to_date=to_date)
        query_string = await create_query_string(from_date=from_date, to_date=to_date)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/{from_date}/to/{to_date}/abandon-cart.csv", from_date=from_date, to_date=to_date), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    
    async def getAbandonCartDetail(self, cart_id=None):
        """Get abandon cart details
        :param cart_id : Cart Id : type string
        """
        payload = {}
        
        if cart_id:
            payload["cart_id"] = cart_id
        

        # Parameter validation
        schema = AnalyticsValidator.getAbandonCartDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/abandon-cart/{cart_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"cart_id","in":"path","description":"Cart Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"cart_id","in":"path","description":"Cart Id","required":true,"schema":{"type":"string"}}]}""", cart_id=cart_id)
        query_string = await create_query_string(cart_id=cart_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/abandon-cart/{cart_id}", cart_id=cart_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    

class Discount:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    

class Partner:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def addProxyPath(self, extension_id=None, body=""):
        """Add proxy path for external url
        :param extension_id : Extension id : type string
        """
        payload = {}
        
        if extension_id:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = PartnerValidator.addProxyPath()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AddProxyReq import AddProxyReq
        schema = AddProxyReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/proxy/{extension_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"extension_id","in":"path","description":"Extension id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"extension_id","in":"path","description":"Extension id","required":true,"schema":{"type":"string"}}]}""", extension_id=extension_id)
        query_string = await create_query_string(extension_id=extension_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/proxy/{extension_id}", extension_id=extension_id), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, body, exclude_headers=["Authorization"]), data=body)
    
    async def removeProxyPath(self, extension_id=None, attached_path=None):
        """Remove proxy path for external url
        :param extension_id : Extension id : type string
        :param attached_path : Attachaed path slug : type string
        """
        payload = {}
        
        if extension_id:
            payload["extension_id"] = extension_id
        
        if attached_path:
            payload["attached_path"] = attached_path
        

        # Parameter validation
        schema = PartnerValidator.removeProxyPath()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/partners/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/proxy/{extension_id}/{attached_path}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"extension_id","in":"path","description":"Extension id","required":true,"schema":{"type":"string"}},{"name":"attached_path","in":"path","description":"Attachaed path slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"extension_id","in":"path","description":"Extension id","required":true,"schema":{"type":"string"}},{"name":"attached_path","in":"path","description":"Attachaed path slug","required":true,"schema":{"type":"string"}}]}""", extension_id=extension_id, attached_path=attached_path)
        query_string = await create_query_string(extension_id=extension_id, attached_path=attached_path)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/partners/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/proxy/{extension_id}/{attached_path}", extension_id=extension_id, attached_path=attached_path), query_string, {"Authorization": "Bearer " + await self._conf.getAccessToken()}, "", exclude_headers=["Authorization"]), data="")
    

class Webhook:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    

class AuditTrail:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    



class PlatformApplicationClient:
    def __init__(self, applicationId, config):
        self.common = Common(config, applicationId)
        self.lead = Lead(config, applicationId)
        self.feedback = Feedback(config, applicationId)
        self.theme = Theme(config, applicationId)
        self.user = User(config, applicationId)
        self.content = Content(config, applicationId)
        self.billing = Billing(config, applicationId)
        self.communication = Communication(config, applicationId)
        self.payment = Payment(config, applicationId)
        self.order = Order(config, applicationId)
        self.catalog = Catalog(config, applicationId)
        self.companyProfile = CompanyProfile(config, applicationId)
        self.fileStorage = FileStorage(config, applicationId)
        self.share = Share(config, applicationId)
        self.inventory = Inventory(config, applicationId)
        self.configuration = Configuration(config, applicationId)
        self.cart = Cart(config, applicationId)
        self.rewards = Rewards(config, applicationId)
        self.analytics = Analytics(config, applicationId)
        self.discount = Discount(config, applicationId)
        self.partner = Partner(config, applicationId)
        self.webhook = Webhook(config, applicationId)
        self.auditTrail = AuditTrail(config, applicationId)
        
