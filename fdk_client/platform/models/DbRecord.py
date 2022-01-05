"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .Upload import Upload

from .CDN import CDN






class DbRecord(BaseSchema):
    # FileStorage swagger.json

    
    success = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    upload = fields.Nested(Upload, required=False)
    
    cdn = fields.Nested(CDN, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    

