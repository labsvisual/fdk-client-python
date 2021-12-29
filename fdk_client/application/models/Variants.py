"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Medium import Medium

from .SemiBold import SemiBold

from .Bold import Bold

from .Light import Light

from .Regular import Regular


class Variants(BaseSchema):
    # Theme swagger.json

    
    medium = fields.Nested(Medium, required=False)
    
    semi_bold = fields.Nested(SemiBold, required=False)
    
    bold = fields.Nested(Bold, required=False)
    
    light = fields.Nested(Light, required=False)
    
    regular = fields.Nested(Regular, required=False)
    

