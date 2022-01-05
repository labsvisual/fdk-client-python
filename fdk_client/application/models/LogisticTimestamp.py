"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class LogisticTimestamp(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    

