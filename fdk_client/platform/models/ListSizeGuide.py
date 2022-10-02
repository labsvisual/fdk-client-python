"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ListSizeGuide(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Dict(required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    

