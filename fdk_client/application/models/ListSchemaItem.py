"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ConfigPage import ConfigPage




class ListSchemaItem(BaseSchema):
    # Theme swagger.json

    
    global_config = fields.Dict(required=False)
    
    page = fields.List(fields.Nested(ConfigPage, required=False), required=False)
    
    name = fields.Str(required=False)
    

