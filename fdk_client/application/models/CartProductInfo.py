"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CartProductIdentifer import CartProductIdentifer





from .ProductPriceInfo import ProductPriceInfo



from .ProductPriceInfo import ProductPriceInfo





from .AppliedPromotion import AppliedPromotion

from .PromoMeta import PromoMeta

from .ProductArticle import ProductArticle

from .CartProduct import CartProduct

from .ProductAvailability import ProductAvailability




class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    key = fields.Str(required=False)
    
    coupon_message = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    is_set = fields.Boolean(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    discount = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    message = fields.Str(required=False)
    

