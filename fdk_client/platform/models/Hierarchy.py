"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Hierarchy(BaseSchema):
    # Catalog swagger.json

    
    l2 = fields.Int(required=False)
    
    department = fields.Int(required=False)
    
    l1 = fields.Int(required=False)
    

