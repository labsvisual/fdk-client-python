"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TotalLineItemsPriceSetShopMoney import TotalLineItemsPriceSetShopMoney

from .TotalLineItemsPriceSetPresentmentMoney import TotalLineItemsPriceSetPresentmentMoney


class TotalLineItemsPriceSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(TotalLineItemsPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalLineItemsPriceSetPresentmentMoney, required=False)
    

