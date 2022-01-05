"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class BagsForReorderArticleAssignment(BaseSchema):
    # Order swagger.json

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    

