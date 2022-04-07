"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





















from .Information import Information



from .Src import Src

from .AssetsSchema import AssetsSchema

from .availableSectionSchema import availableSectionSchema



from .Config import Config

from .Font import Font





from .Colors import Colors


class ThemesSchema(BaseSchema):
    # Theme swagger.json

    
    application = fields.Str(required=False)
    
    applied = fields.Boolean(required=False)
    
    customized = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    archived = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    parent_theme_version = fields.Str(required=False)
    
    parent_theme = fields.Str(required=False)
    
    information = fields.Nested(Information, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    src = fields.Nested(Src, required=False)
    
    assets = fields.Nested(AssetsSchema, required=False)
    
    available_sections = fields.List(fields.Nested(availableSectionSchema, required=False), required=False)
    
    styles = fields.Dict(required=False)
    
    config = fields.Nested(Config, required=False)
    
    font = fields.Nested(Font, required=False)
    
    _id = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
    colors = fields.Nested(Colors, required=False)
    

