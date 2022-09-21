"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class CompareObject(BaseSchema):
    # Cart swagger.json

    
    less_than = fields.Float(required=False)
    
    equals = fields.Float(required=False)
    
    greater_than = fields.Float(required=False)
    
    greater_than_equals = fields.Float(required=False)
    
    less_than_equals = fields.Float(required=False)
    

