"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ThirdLevelChild import ThirdLevelChild

from .ImageUrls import ImageUrls





from .Action import Action




class SecondLevelChild(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(Action, required=False)
    
    slug = fields.Str(required=False)
    

