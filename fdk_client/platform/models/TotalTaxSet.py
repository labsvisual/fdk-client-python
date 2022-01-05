"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TotalTaxSetShopMoney import TotalTaxSetShopMoney

from .TotalTaxSetPresentmentMoney import TotalTaxSetPresentmentMoney


class TotalTaxSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(TotalTaxSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalTaxSetPresentmentMoney, required=False)
    

