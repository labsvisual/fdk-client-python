"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ConfigurationProductVariant import ConfigurationProductVariant

from .ConfigurationProductSimilar import ConfigurationProductSimilar


class ConfigurationProduct(BaseSchema):
    # Catalog swagger.json

    
    variant = fields.Nested(ConfigurationProductVariant, required=False)
    
    similar = fields.Nested(ConfigurationProductSimilar, required=False)
    

