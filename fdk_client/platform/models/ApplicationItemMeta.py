"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .MetaFields import MetaFields




class ApplicationItemMeta(BaseSchema):
    # Catalog swagger.json

    
    _custom_meta = fields.List(fields.Nested(MetaFields, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    

