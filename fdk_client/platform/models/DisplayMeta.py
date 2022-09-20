"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DisplayMetaDict import DisplayMetaDict

from .DisplayMetaDict import DisplayMetaDict

from .DisplayMetaDict import DisplayMetaDict








class DisplayMeta(BaseSchema):
    # Cart swagger.json

    
    auto = fields.Nested(DisplayMetaDict, required=False)
    
    remove = fields.Nested(DisplayMetaDict, required=False)
    
    apply = fields.Nested(DisplayMetaDict, required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    

