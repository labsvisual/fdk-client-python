"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class OrderFeature(BaseSchema):
    # Configuration swagger.json

    
    buy_again = fields.Boolean(required=False)
    

