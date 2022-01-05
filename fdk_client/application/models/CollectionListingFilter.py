"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CollectionListingFilterType import CollectionListingFilterType

from .CollectionListingFilterTag import CollectionListingFilterTag


class CollectionListingFilter(BaseSchema):
    # Catalog swagger.json

    
    type = fields.List(fields.Nested(CollectionListingFilterType, required=False), required=False)
    
    tags = fields.List(fields.Nested(CollectionListingFilterTag, required=False), required=False)
    

