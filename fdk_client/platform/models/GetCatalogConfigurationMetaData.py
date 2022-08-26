"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .MetaDataListingResponse import MetaDataListingResponse

from .GetCatalogConfigurationDetailsProduct import GetCatalogConfigurationDetailsProduct


class GetCatalogConfigurationMetaData(BaseSchema):
    # Catalog swagger.json

    
    listing = fields.Nested(MetaDataListingResponse, required=False)
    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    

