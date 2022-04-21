"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class LocationIntegrationType(BaseSchema):
    # Catalog swagger.json

    
    order = fields.Str(required=False)
    
    inventory = fields.Str(required=False)
    

