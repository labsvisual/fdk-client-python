"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .LogisticRequestCategory import LogisticRequestCategory


class TatReqProductArticles(BaseSchema):
    # Logistic swagger.json

    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    category = fields.Nested(LogisticRequestCategory, required=False)
    

