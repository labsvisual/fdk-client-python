"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TaxLinesPriceSetShopMoney import TaxLinesPriceSetShopMoney

from .TaxLinesPriceSetPresentmentMoney import TaxLinesPriceSetPresentmentMoney


class TaxLinesPriceSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(TaxLinesPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TaxLinesPriceSetPresentmentMoney, required=False)
    

