"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ArticleMeta(BaseSchema):
    # Order swagger.json

    
    service = fields.Str(required=False)
    

