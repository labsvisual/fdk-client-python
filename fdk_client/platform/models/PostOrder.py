"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PostOrder(BaseSchema):
    # Cart swagger.json

    
    cancellation_allowed = fields.Boolean(required=False)
    
    return_allowed = fields.Boolean(required=False)
    
