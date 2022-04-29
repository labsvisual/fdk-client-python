"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .MetaDataListingSortResponse import MetaDataListingSortResponse

from .MetaDataListingFilterResponse import MetaDataListingFilterResponse


class MetaDataListingResponse(BaseSchema):
    # Catalog swagger.json

    
    sort = fields.Nested(MetaDataListingSortResponse, required=False)
    
    filter = fields.Nested(MetaDataListingFilterResponse, required=False)
    

