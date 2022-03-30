"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class IntentAppErrorList(BaseSchema):
    # Payment swagger.json

    
    package_name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
