"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .JsonSchema import JsonSchema




class StoreValidator(BaseSchema):
    # Configuration swagger.json

    
    json_schema = fields.List(fields.Nested(JsonSchema, required=False), required=False)
    
    browser_script = fields.Str(required=False)
    

