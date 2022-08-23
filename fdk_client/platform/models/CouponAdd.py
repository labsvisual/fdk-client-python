"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .State import State

from .Validity import Validity





from .CouponDateMeta import CouponDateMeta

from .CouponSchedule import CouponSchedule

from .Rule import Rule

from .Identifier import Identifier

from .Validation import Validation

from .Restrictions import Restrictions

from .CouponAction import CouponAction

from .CouponAuthor import CouponAuthor

from .Ownership import Ownership

from .RuleDefinition import RuleDefinition

from .DisplayMeta import DisplayMeta




class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    state = fields.Nested(State, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    type_slug = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    

