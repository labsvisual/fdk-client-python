"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PageSpecParam(BaseSchema):
    # Content swagger.json

    
    key = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    

