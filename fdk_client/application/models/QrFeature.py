"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class QrFeature(BaseSchema):
    # Configuration swagger.json

    
    application = fields.Boolean(required=False)
    
    products = fields.Boolean(required=False)
    
    collections = fields.Boolean(required=False)
    

