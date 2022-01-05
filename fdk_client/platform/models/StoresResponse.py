"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AppInventoryStores import AppInventoryStores

from .Page import Page


class StoresResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.Nested(AppInventoryStores, required=False)
    
    page = fields.Nested(Page, required=False)
    

