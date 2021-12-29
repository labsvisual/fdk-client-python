"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TotalShippingPriceSetShopMoney import TotalShippingPriceSetShopMoney

from .TotalShippingPriceSetPresentmentMoney import TotalShippingPriceSetPresentmentMoney


class TotalShippingPriceSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(TotalShippingPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalShippingPriceSetPresentmentMoney, required=False)
    

