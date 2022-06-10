"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CollectionImage import CollectionImage

from .CollectionImage import CollectionImage


class CollectionBanner(BaseSchema):
    # Catalog swagger.json

    
    portrait = fields.Nested(CollectionImage, required=False)
    
    landscape = fields.Nested(CollectionImage, required=False)
    

