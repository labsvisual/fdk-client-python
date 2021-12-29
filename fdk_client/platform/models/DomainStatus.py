"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class DomainStatus(BaseSchema):
    # Configuration swagger.json

    
    display = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    

