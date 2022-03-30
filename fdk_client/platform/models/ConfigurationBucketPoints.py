"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ConfigurationBucketPoints(BaseSchema):
    # Catalog swagger.json

    
    start = fields.Float(required=False)
    
    end = fields.Float(required=False)
    

