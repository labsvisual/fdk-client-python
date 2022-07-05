"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PromoMeta import PromoMeta

from .CartProduct import CartProduct



from .AppliedPromotion import AppliedPromotion







from .ProductArticle import ProductArticle

from .ProductAvailability import ProductAvailability



from .ProductPriceInfo import ProductPriceInfo



from .CartProductIdentifer import CartProductIdentifer



from .ProductPriceInfo import ProductPriceInfo


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    coupon_message = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    message = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    key = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    

