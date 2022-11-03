"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Page import Page




class ProdcutTemplateCategoriesResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    

