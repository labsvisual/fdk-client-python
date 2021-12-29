"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .MetaDataListingFilterMetaResponse import MetaDataListingFilterMetaResponse


class MetaDataListingFilterResponse(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(MetaDataListingFilterMetaResponse, required=False), required=False)
    

