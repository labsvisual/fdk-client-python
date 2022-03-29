"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DataLoaderResetResponseSchema(BaseSchema):
    # Content swagger.json

    
    reset = fields.Str(required=False)
    

