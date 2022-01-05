"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Opening import Opening





from .Closing import Closing


class Timing(BaseSchema):
    # Order swagger.json

    
    opening = fields.Nested(Opening, required=False)
    
    weekday = fields.Str(required=False)
    
    open = fields.Boolean(required=False)
    
    closing = fields.Nested(Closing, required=False)
    

