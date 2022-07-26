"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ThirdLevelChild import ThirdLevelChild

from .Action import Action

from .ImageUrls import ImageUrls




class SecondLevelChild(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    slug = fields.Str(required=False)
    

