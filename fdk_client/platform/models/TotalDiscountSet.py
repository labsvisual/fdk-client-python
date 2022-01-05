"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TotalDiscountSetPresentmentMoney import TotalDiscountSetPresentmentMoney

from .TotalDiscountSetShopMoney import TotalDiscountSetShopMoney


class TotalDiscountSet(BaseSchema):
    # Order swagger.json

    
    presentment_money = fields.Nested(TotalDiscountSetPresentmentMoney, required=False)
    
    shop_money = fields.Nested(TotalDiscountSetShopMoney, required=False)
    

