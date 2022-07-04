"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PromotionSchedule import PromotionSchedule

from .PromotionAction import PromotionAction







from .Restrictions1 import Restrictions1

from .DiscountRule import DiscountRule

from .PromotionDateMeta import PromotionDateMeta

from .Visibility import Visibility



from .PromotionAuthor import PromotionAuthor









from .Ownership1 import Ownership1







from .DisplayMeta1 import DisplayMeta1




class PromotionUpdate(BaseSchema):
    # Cart swagger.json

    
    _schedule = fields.Nested(PromotionSchedule, required=False)
    
    post_order_action = fields.Nested(PromotionAction, required=False)
    
    currency = fields.Str(required=False)
    
    apply_exclusive = fields.Str(required=False)
    
    promo_group = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions1, required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRule, required=False), required=False)
    
    date_meta = fields.Nested(PromotionDateMeta, required=False)
    
    visiblility = fields.Nested(Visibility, required=False)
    
    promotion_type = fields.Str(required=False)
    
    author = fields.Nested(PromotionAuthor, required=False)
    
    code = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    apply_all_discount = fields.Boolean(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    ownership = fields.Nested(Ownership1, required=False)
    
    stackable = fields.Boolean(required=False)
    
    apply_priority = fields.Int(required=False)
    
    mode = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta1, required=False)
    
    application_id = fields.Str(required=False)
    

