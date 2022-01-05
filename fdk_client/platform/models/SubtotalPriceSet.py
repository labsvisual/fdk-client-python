"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SubtotalPriceSetShopMoney import SubtotalPriceSetShopMoney

from .SubtotalPriceSetPresentmentMoney import SubtotalPriceSetPresentmentMoney


class SubtotalPriceSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(SubtotalPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(SubtotalPriceSetPresentmentMoney, required=False)
    

