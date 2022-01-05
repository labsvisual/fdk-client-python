"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BagStateMapper import BagStateMapper






class BagCurrentStatus(BaseSchema):
    # Order swagger.json

    
    updated_at = fields.Str(required=False)
    
    bag_state_mapper = fields.Nested(BagStateMapper, required=False)
    
    status = fields.Str(required=False)
    
    state_type = fields.Str(required=False)
    

