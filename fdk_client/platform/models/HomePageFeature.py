"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class HomePageFeature(BaseSchema):
    # Configuration swagger.json

    
    order_processing = fields.Boolean(required=False)
    

