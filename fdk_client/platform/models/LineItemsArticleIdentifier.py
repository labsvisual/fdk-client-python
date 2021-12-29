"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class LineItemsArticleIdentifier(BaseSchema):
    # Order swagger.json

    
    sku_code = fields.Str(required=False)
    

