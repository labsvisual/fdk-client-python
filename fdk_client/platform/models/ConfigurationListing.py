"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ConfigurationListingFilter import ConfigurationListingFilter

from .ConfigurationListingSort import ConfigurationListingSort


class ConfigurationListing(BaseSchema):
    # Catalog swagger.json

    
    filter = fields.Nested(ConfigurationListingFilter, required=False)
    
    sort = fields.Nested(ConfigurationListingSort, required=False)
    

