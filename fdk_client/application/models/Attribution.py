"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class Attribution(BaseSchema):
    # Share swagger.json

    
    campaign_cookie_expiry = fields.Str(required=False)
    

