"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ConfigurationListingSort import ConfigurationListingSort

from .ConfigurationListingFilter import ConfigurationListingFilter


class ConfigurationListing(BaseSchema):
    # Catalog swagger.json

    
    sort = fields.Nested(ConfigurationListingSort, required=False)
    
    filter = fields.Nested(ConfigurationListingFilter, required=False)
    

