"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UmdJs import UmdJs

from .CommonJs import CommonJs

from .Css import Css


class AssetsSchema(BaseSchema):
    # Theme swagger.json

    
    umd_js = fields.Nested(UmdJs, required=False)
    
    common_js = fields.Nested(CommonJs, required=False)
    
    css = fields.Nested(Css, required=False)
    

