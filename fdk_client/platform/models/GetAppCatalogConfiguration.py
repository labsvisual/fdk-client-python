"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .AppCatalogConfiguration import AppCatalogConfiguration


class GetAppCatalogConfiguration(BaseSchema):
    # Catalog swagger.json

    
    is_default = fields.Boolean(required=False)
    
    data = fields.Nested(AppCatalogConfiguration, required=False)
    

