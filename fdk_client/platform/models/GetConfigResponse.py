"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PageResponseType import PageResponseType




class GetConfigResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(PageResponseType, required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    

