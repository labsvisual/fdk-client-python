"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TatacliqLuxury import TatacliqLuxury


class MarketplaceIdentifiers(BaseSchema):
    # Order swagger.json

    
    tatacliq_luxury = fields.Nested(TatacliqLuxury, required=False)
    

