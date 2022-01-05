"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .BlocksProps import BlocksProps


class Blocks(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    props = fields.List(fields.Nested(BlocksProps, required=False), required=False)
    

