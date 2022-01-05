"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UpdateDomain import UpdateDomain




class UpdateDomainTypeRequest(BaseSchema):
    # Configuration swagger.json

    
    domain = fields.Nested(UpdateDomain, required=False)
    
    action = fields.Str(required=False)
    

