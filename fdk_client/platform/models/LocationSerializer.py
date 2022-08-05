"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .Document import Document

from .LocationDayWiseSerializer import LocationDayWiseSerializer

from .InvoiceDetailsSerializer import InvoiceDetailsSerializer





from .LocationManagerSerializer import LocationManagerSerializer

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .GetAddressSerializer import GetAddressSerializer

from .SellerPhoneNumber import SellerPhoneNumber








class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    store_type = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    company = fields.Int(required=False)
    

