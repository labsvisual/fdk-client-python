"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CampignEmailProvider(BaseSchema):
    # Communication swagger.json

    
    _id = fields.Str(required=False)
    
    from_name = fields.Str(required=False)
    
    from_email = fields.Str(required=False)
    

