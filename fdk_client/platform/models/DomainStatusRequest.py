"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DomainStatusRequest(BaseSchema):
    # Configuration swagger.json

    
    domain_url = fields.Str(required=False)
    

