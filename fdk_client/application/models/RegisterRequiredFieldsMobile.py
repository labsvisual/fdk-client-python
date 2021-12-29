"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class RegisterRequiredFieldsMobile(BaseSchema):
    # User swagger.json

    
    is_required = fields.Boolean(required=False)
    
    level = fields.Str(required=False)
    

