"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Blocks import Blocks





from .BlocksProps import BlocksProps


class availableSectionSchema(BaseSchema):
    # Theme swagger.json

    
    blocks = fields.List(fields.Nested(Blocks, required=False), required=False)
    
    name = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    props = fields.List(fields.Nested(BlocksProps, required=False), required=False)
    

