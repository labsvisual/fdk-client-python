"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class AttributeSchemaRange(BaseSchema):
    # Catalog swagger.json

    
    max = fields.Int(required=False)
    
    min = fields.Int(required=False)
    

