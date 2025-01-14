"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CollectionQuery(BaseSchema):
    # Catalog swagger.json

    
    attribute = fields.Str(required=False)
    
    op = fields.Str(required=False)
    
    value = fields.List(fields.Raw(required=False), required=False)
    

