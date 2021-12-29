"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class Custom(BaseSchema):
    # Theme swagger.json

    
    props = fields.Dict(required=False)
    

