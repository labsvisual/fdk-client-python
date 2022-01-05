"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Charges(BaseSchema):
    # Configuration swagger.json

    
    threshold = fields.Float(required=False)
    
    charges = fields.Float(required=False)
    

