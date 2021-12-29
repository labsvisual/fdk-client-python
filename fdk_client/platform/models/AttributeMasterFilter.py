"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class AttributeMasterFilter(BaseSchema):
    # Catalog swagger.json

    
    indexing = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    depends_on = fields.List(fields.Str(required=False), required=False)
    

