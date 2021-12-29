"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Sizes import Sizes


class SetSizeDistribution(BaseSchema):
    # Order swagger.json

    
    sizes = fields.Nested(Sizes, required=False)
    

