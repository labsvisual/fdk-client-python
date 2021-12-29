"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .IntegrationOptIn import IntegrationOptIn

from .Page import Page


class GetIntegrationsOptInsResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(IntegrationOptIn, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

