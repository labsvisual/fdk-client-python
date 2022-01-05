"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class CDN(BaseSchema):
    # FileStorage swagger.json

    
    url = fields.Str(required=False)
    

