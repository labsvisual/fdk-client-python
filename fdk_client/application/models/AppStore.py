"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .StoreManagerSerializer import StoreManagerSerializer

from .StoreDepartments import StoreDepartments

from .CompanyStore import CompanyStore

from .SellerPhoneNumber import SellerPhoneNumber

from .StoreAddressSerializer import StoreAddressSerializer


class AppStore(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    

