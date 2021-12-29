"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EditMobileRequestSchema(BaseSchema):
    # User swagger.json

    
    country_code = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    

