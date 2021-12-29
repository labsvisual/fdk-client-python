"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DomainAdd import DomainAdd


class DomainAddRequest(BaseSchema):
    # Configuration swagger.json

    
    domain = fields.Nested(DomainAdd, required=False)
    

