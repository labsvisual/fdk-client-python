"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .TaxLinesPriceSet import TaxLinesPriceSet


class TaxLines(BaseSchema):
    # Order swagger.json

    
    title = fields.Str(required=False)
    
    price = fields.Str(required=False)
    
    rate = fields.Int(required=False)
    
    price_set = fields.Nested(TaxLinesPriceSet, required=False)
    

