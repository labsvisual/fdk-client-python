"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .MetaDataListingFilterResponse import MetaDataListingFilterResponse

from .MetaDataListingSortResponse import MetaDataListingSortResponse


class MetaDataListingResponse(BaseSchema):
    # Catalog swagger.json

    
    filter = fields.Nested(MetaDataListingFilterResponse, required=False)
    
    sort = fields.Nested(MetaDataListingSortResponse, required=False)
    

