"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class LogisticRequestCategory(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Int(required=False)
    
    level = fields.Str(required=False)
    

