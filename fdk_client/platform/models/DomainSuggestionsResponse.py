"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DomainSuggestion import DomainSuggestion


class DomainSuggestionsResponse(BaseSchema):
    # Configuration swagger.json

    
    domains = fields.List(fields.Nested(DomainSuggestion, required=False), required=False)
    

