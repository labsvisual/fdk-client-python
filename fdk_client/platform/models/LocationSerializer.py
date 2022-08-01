"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LocationManagerSerializer import LocationManagerSerializer





from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .GetAddressSerializer import GetAddressSerializer



from .LocationDayWiseSerializer import LocationDayWiseSerializer











from .SellerPhoneNumber import SellerPhoneNumber

from .InvoiceDetailsSerializer import InvoiceDetailsSerializer

from .Document import Document




class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    name = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    company = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    

