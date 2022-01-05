"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ChildrenSchema(BaseSchema):
    # Content swagger.json

    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    

