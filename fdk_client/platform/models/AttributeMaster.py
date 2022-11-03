"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .AttributeSchemaRange import AttributeSchemaRange


class AttributeMaster(BaseSchema):
    # Catalog swagger.json

    
    allowed_values = fields.List(fields.Str(required=False), required=False)
    
    mandatory = fields.Boolean(required=False)
    
    multi = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    format = fields.Str(required=False)
    
    range = fields.Nested(AttributeSchemaRange, required=False)
    

