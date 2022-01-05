"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Access import Access


class CheckEligibilityResponse(BaseSchema):
    # Feedback swagger.json

    
    access = fields.Nested(Access, required=False)
    

