"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .StatsGroupComponent import StatsGroupComponent


class StatsGroupComponents(BaseSchema):
    # Analytics swagger.json

    
    title = fields.Str(required=False)
    
    components = fields.List(fields.Nested(StatsGroupComponent, required=False), required=False)
    

