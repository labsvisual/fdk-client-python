"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class TriggerJobResponse(BaseSchema):
    # Communication swagger.json

    
    status = fields.Int(required=False)
    

