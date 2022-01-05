"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .DomainStatus import DomainStatus


class DomainStatusResponse(BaseSchema):
    # Configuration swagger.json

    
    connected = fields.Boolean(required=False)
    
    status = fields.List(fields.Nested(DomainStatus, required=False), required=False)
    

