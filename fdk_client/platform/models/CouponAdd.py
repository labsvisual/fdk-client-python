"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .RuleDefinition import RuleDefinition

from .CouponAuthor import CouponAuthor

from .Restrictions import Restrictions

from .DisplayMeta import DisplayMeta

from .Validity import Validity

from .CouponSchedule import CouponSchedule

from .Rule import Rule



from .Ownership import Ownership

from .Validation import Validation

from .CouponAction import CouponAction

from .State import State

from .CouponDateMeta import CouponDateMeta

from .Identifier import Identifier




class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    state = fields.Nested(State, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    type_slug = fields.Str(required=False)
    

