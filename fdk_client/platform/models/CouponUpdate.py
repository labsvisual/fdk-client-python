"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .State import State

from .CouponSchedule import CouponSchedule



from .Restrictions import Restrictions

from .Validity import Validity

from .DisplayMeta import DisplayMeta

from .Ownership import Ownership

from .Validation import Validation

from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta

from .Rule import Rule



from .Identifier import Identifier

from .CouponAction import CouponAction

from .RuleDefinition import RuleDefinition




class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    state = fields.Nested(State, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    type_slug = fields.Str(required=False)
    

