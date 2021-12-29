"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .EntityMeta import EntityMeta




class ProductEntity(BaseSchema):
    # Feedback swagger.json

    
    id = fields.Str(required=False)
    
    meta = fields.Nested(EntityMeta, required=False)
    
    type = fields.Str(required=False)
    

