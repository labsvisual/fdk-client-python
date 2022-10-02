"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ItemQueryForUserCollection(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    

