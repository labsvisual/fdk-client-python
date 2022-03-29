"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PromoMeta import PromoMeta





from .CartProductIdentifer import CartProductIdentifer





from .ProductPriceInfo import ProductPriceInfo



from .CartProduct import CartProduct

from .ProductAvailability import ProductAvailability

from .ProductArticle import ProductArticle

from .ProductPriceInfo import ProductPriceInfo


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    is_set = fields.Boolean(required=False)
    
    discount = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    coupon_message = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    

