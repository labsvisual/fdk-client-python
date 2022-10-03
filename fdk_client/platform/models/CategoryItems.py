"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Action import Action

from .Child import Child

from .ImageUrls import ImageUrls






class CategoryItems(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

