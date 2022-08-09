"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CouponAuthor import CouponAuthor

from .Restrictions import Restrictions

from .RuleDefinition import RuleDefinition



from .Ownership import Ownership

from .CouponAction import CouponAction

from .Rule import Rule



from .Validation import Validation

from .Identifier import Identifier

from .CouponSchedule import CouponSchedule

from .CouponDateMeta import CouponDateMeta

from .Validity import Validity

from .DisplayMeta import DisplayMeta

from .State import State


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    code = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    state = fields.Nested(State, required=False)
    

