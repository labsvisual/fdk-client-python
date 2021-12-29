"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Detail(BaseSchema):
    # Content swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    

