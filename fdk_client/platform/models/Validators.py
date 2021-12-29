"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CompanyValidator import CompanyValidator

from .StoreValidator import StoreValidator

from .InventoryValidator import InventoryValidator

from .OrderValidator import OrderValidator


class Validators(BaseSchema):
    # Configuration swagger.json

    
    company = fields.Nested(CompanyValidator, required=False)
    
    store = fields.Nested(StoreValidator, required=False)
    
    inventory = fields.Nested(InventoryValidator, required=False)
    
    order = fields.Nested(OrderValidator, required=False)
    

