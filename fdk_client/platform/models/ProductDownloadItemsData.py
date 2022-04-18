"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ProductDownloadItemsData(BaseSchema):
    # Catalog swagger.json

    
    templates = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    

