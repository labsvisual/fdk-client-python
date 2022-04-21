"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .Document import Document

from .SellerPhoneNumber import SellerPhoneNumber



from .LocationManagerSerializer import LocationManagerSerializer



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .LocationDayWiseSerializer import LocationDayWiseSerializer



from .GetAddressSerializer1 import GetAddressSerializer1


class LocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    code = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    company = fields.Int(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    address = fields.Nested(GetAddressSerializer1, required=False)
    

