"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class CollectionItemRequest(BaseSchema):
    # Catalog swagger.json

    
    sort = fields.Str(required=False)
    
    q = fields.Str(required=False)
    
    variant = fields.Str(required=False)
    
    page_size = fields.Int(required=False)
    
    page_no = fields.Int(required=False)
    
    department = fields.Str(required=False)
    

