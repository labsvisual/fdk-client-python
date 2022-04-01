"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class Location(BaseSchema):
    # AuditTrail swagger.json

    
    extra_meta = fields.Dict(required=False)
    

