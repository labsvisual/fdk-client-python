"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ItemQueryForUserCollection(BaseSchema):
    # Catalog swagger.json

    
    item_id = fields.Int(required=False)
    
    action = fields.Str(required=False)
    

