"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class FilerList(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Str(required=False)
    
    display = fields.Str(required=False)
    

