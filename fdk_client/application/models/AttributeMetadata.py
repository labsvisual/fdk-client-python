"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AttributeDetail import AttributeDetail




class AttributeMetadata(BaseSchema):
    # Catalog swagger.json

    
    details = fields.List(fields.Nested(AttributeDetail, required=False), required=False)
    
    title = fields.Str(required=False)
    

