"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .SetSizeDistribution import SetSizeDistribution


class Set(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(SetSizeDistribution, required=False)
    

