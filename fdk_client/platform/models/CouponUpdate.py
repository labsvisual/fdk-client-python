"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponSchedule import CouponSchedule

from .Identifier import Identifier

from .Validity import Validity



from .Validation import Validation

from .RuleDefinition import RuleDefinition

from .CouponDateMeta import CouponDateMeta

from .DisplayMeta import DisplayMeta

from .Restrictions import Restrictions

from .State import State

from .Ownership import Ownership

from .CouponAuthor import CouponAuthor

from .CouponAction import CouponAction



from .Rule import Rule




class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    state = fields.Nested(State, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    type_slug = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    

