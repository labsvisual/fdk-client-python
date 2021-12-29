"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SetSize import SetSize


class SizeDistribution(BaseSchema):
    # Catalog swagger.json

    
    sizes = fields.List(fields.Nested(SetSize, required=False), required=False)
    

