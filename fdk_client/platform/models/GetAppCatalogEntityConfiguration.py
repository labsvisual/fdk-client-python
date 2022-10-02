"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntityConfiguration import EntityConfiguration




class GetAppCatalogEntityConfiguration(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(EntityConfiguration, required=False)
    
    is_default = fields.Boolean(required=False)
    

