"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Meta import Meta


class Guide(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Nested(Meta, required=False)
    

