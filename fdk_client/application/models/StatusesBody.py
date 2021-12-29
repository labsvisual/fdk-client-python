"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class StatusesBody(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    shipments = fields.Dict(required=False)
    

