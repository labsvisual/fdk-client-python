"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PresentmentMoney import PresentmentMoney

from .ShopMoney import ShopMoney


class TotalDiscountsSet(BaseSchema):
    # Order swagger.json

    
    presentment_money = fields.Nested(PresentmentMoney, required=False)
    
    shop_money = fields.Nested(ShopMoney, required=False)
    

