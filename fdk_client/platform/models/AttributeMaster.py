"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .AttributeSchemaRange import AttributeSchemaRange




class AttributeMaster(BaseSchema):
    # Catalog swagger.json

    
    format = fields.Str(required=False)
    
    mandatory = fields.Boolean(required=False)
    
    allowed_values = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    range = fields.Nested(AttributeSchemaRange, required=False)
    
    multi = fields.Boolean(required=False)
    

