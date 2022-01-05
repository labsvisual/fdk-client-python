"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .IntegrationLevel import IntegrationLevel


class IntegrationConfigResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(IntegrationLevel, required=False), required=False)
    

