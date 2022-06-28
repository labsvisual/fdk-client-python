"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class OrderValidator:
    
    class getOrders(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        status = fields.Int(required=False)
         
    
    class getOrderById(BaseSchema):
        
        order_id = fields.Str(required=False)
         
    
    class getShipmentById(BaseSchema):
        
        shipment_id = fields.Str(required=False)
         
    
    class getShipmentReasons(BaseSchema):
        
        shipment_id = fields.Str(required=False)
         
    
    class updateShipmentStatus(BaseSchema):
        
        shipment_id = fields.Str(required=False)
         
    
    class trackShipment(BaseSchema):
        
        shipment_id = fields.Str(required=False)
         
    
    class getPosOrderById(BaseSchema):
        
        order_id = fields.Str(required=False)
         
    
    class getCustomerDetailsByShipmentId(BaseSchema):
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class sendOtpToShipmentCustomer(BaseSchema):
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class verifyOtpShipmentCustomer(BaseSchema):
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class getInvoiceByShipmentId(BaseSchema):
        
        shipment_id = fields.Str(required=False)
         
    