"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponAction import CouponAction

from .Restrictions import Restrictions

from .Validation import Validation



from .CouponDateMeta import CouponDateMeta

from .Validity import Validity

from .CouponSchedule import CouponSchedule

from .State import State



from .CouponAuthor import CouponAuthor

from .DisplayMeta import DisplayMeta

from .RuleDefinition import RuleDefinition

from .Rule import Rule



from .Ownership import Ownership

from .Identifier import Identifier


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    action = fields.Nested(CouponAction, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    type_slug = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    

