"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ConfigurationListingSortConfig import ConfigurationListingSortConfig




class ConfigurationListingSort(BaseSchema):
    # Catalog swagger.json

    
    config = fields.List(fields.Nested(ConfigurationListingSortConfig, required=False), required=False)
    
    default_key = fields.Str(required=False)
    

