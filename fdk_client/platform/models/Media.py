"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Media(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
