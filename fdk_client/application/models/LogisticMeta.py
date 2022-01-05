"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class LogisticMeta(BaseSchema):
    # Logistic swagger.json

    
    zone = fields.Str(required=False)
    
    deliverables = fields.List(fields.Raw(required=False), required=False)
    

