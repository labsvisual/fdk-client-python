"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CallbackUrl(BaseSchema):
    # Configuration swagger.json

    
    app = fields.Str(required=False)
    
    web = fields.Str(required=False)
    

