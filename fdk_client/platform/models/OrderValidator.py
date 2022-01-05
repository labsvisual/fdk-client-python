"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class OrderValidator:
    
    class shipmentStatusUpdate(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class activityStatus(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        bag_id = fields.Str(required=False)
         
    
    class storeProcessShipmentUpdate(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class checkRefund(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class ShipmentBagsCanBreak(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class getOrdersByCompanyId(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        is_priority_sort = fields.Boolean(required=False)
        
        lock_status = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        deployment_stores = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        dp = fields.Str(required=False)
        
        shorten_urls = fields.Boolean(required=False)
        
        filter_type = fields.Str(required=False)
         
    
    class getOrderLanesCountByCompanyId(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        shorten_urls = fields.Boolean(required=False)
        
        filter_type = fields.Str(required=False)
         
    
    class getOrderDetails(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        next = fields.Str(required=False)
        
        previous = fields.Str(required=False)
         
    
    class getOrderDetails(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        next = fields.Str(required=False)
        
        previous = fields.Str(required=False)
         
    
    class getPicklistOrdersByCompanyId(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        shorten_urls = fields.Boolean(required=False)
        
        filter_type = fields.Str(required=False)
         
    
    class trackShipmentPlatform(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class trackOrder(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
         
    
    class failedOrders(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class reprocessOrder(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
         
    
    class updateShipment(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class getPlatformShipmentReasons(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        action = fields.Str(required=False)
         
    
    class getShipmentTrackDetails(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class getShipmentAddress(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
        
        address_category = fields.Str(required=False)
         
    
    class updateShipmentAddress(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
        
        address_category = fields.Str(required=False)
         
    
    class getOrdersByApplicationId(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        dp = fields.Str(required=False)
        
        shorten_urls = fields.Boolean(required=False)
        
        filter_type = fields.Str(required=False)
         
    
    class getPing(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class voiceCallback(BaseSchema):
        
        company_id = fields.Str(required=False)
         
    
    class voiceClickToCall(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        caller = fields.Str(required=False)
        
        receiver = fields.Str(required=False)
         
    