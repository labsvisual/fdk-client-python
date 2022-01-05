"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .MetaDataListingSortMetaResponse import MetaDataListingSortMetaResponse


class MetaDataListingSortResponse(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(MetaDataListingSortMetaResponse, required=False), required=False)
    

