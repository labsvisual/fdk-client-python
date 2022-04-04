"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetCatalogConfigurationDetailsProduct import GetCatalogConfigurationDetailsProduct

from .MetaDataListingResponse import MetaDataListingResponse


class GetCatalogConfigurationMetaData(BaseSchema):
    # Catalog swagger.json

    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    
    listing = fields.Nested(MetaDataListingResponse, required=False)
    

