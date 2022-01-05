"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class InformationPhone(BaseSchema):
    # Configuration swagger.json

    
    code = fields.Str(required=False)
    
    number = fields.Str(required=False)
    

