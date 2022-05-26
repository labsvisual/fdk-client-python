"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class HSNData(BaseSchema):
    # Catalog swagger.json

    
    country_of_origin = fields.List(fields.Str(required=False), required=False)
    
    hsn_code = fields.List(fields.Str(required=False), required=False)
    

