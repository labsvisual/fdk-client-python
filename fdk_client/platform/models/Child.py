"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Action import Action



from .SecondLevelChild import SecondLevelChild





from .ImageUrls import ImageUrls


class Child(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    action = fields.Nested(Action, required=False)
    
    name = fields.Str(required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    

