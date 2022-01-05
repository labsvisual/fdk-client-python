"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class RegistrationPageFeature(BaseSchema):
    # Configuration swagger.json

    
    ask_store_address = fields.Boolean(required=False)
    

