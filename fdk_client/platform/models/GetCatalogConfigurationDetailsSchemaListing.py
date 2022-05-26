"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GetCatalogConfigurationDetailsSchemaListing(BaseSchema):
    # Catalog swagger.json

    
    sort = fields.Dict(required=False)
    
    filter = fields.Dict(required=False)
    

