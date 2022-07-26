"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BasePrice import BasePrice

from .BasePrice import BasePrice


class ArticlePriceInfo(BaseSchema):
    # Cart swagger.json

    
    base = fields.Nested(BasePrice, required=False)
    
    converted = fields.Nested(BasePrice, required=False)
    

