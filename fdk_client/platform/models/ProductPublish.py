"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ProductPublish(BaseSchema):
    # Catalog swagger.json

    
    is_set = fields.Boolean(required=False)
    
    product_online_date = fields.Str(required=False)
    

