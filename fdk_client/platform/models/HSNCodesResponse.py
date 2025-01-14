"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .HSNData import HSNData


class HSNCodesResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Nested(HSNData, required=False)
    

