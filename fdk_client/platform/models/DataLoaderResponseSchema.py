"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



















from .DataLoaderSourceSchema import DataLoaderSourceSchema


class DataLoaderResponseSchema(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    service = fields.Str(required=False)
    
    operation_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
    __source = fields.Nested(DataLoaderSourceSchema, required=False)
    

