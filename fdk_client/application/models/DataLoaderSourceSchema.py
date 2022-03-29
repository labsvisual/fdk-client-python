"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class DataLoaderSourceSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    

