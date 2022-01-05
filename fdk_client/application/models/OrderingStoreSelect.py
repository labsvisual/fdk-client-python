"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class OrderingStoreSelect(BaseSchema):
    # Configuration swagger.json

    
    uid = fields.Int(required=False)
    

