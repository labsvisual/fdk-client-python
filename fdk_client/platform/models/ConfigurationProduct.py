"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ConfigurationProductSimilar import ConfigurationProductSimilar

from .ConfigurationProductVariant import ConfigurationProductVariant


class ConfigurationProduct(BaseSchema):
    # Catalog swagger.json

    
    similar = fields.Nested(ConfigurationProductSimilar, required=False)
    
    variant = fields.Nested(ConfigurationProductVariant, required=False)
    

