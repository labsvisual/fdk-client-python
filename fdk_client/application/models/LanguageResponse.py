"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SupportedLanguage import SupportedLanguage


class LanguageResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(SupportedLanguage, required=False), required=False)
    

