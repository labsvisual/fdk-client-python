"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .HSNDataInsertV2 import HSNDataInsertV2

from .PageResponse import PageResponse


class HsnCodesListingResponseSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(HSNDataInsertV2, required=False), required=False)
    
    page = fields.Nested(PageResponse, required=False)
    

