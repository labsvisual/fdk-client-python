"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LogMetaObj import LogMetaObj




class RequestBodyAuditLog(BaseSchema):
    # AuditTrail swagger.json

    
    log_meta = fields.Nested(LogMetaObj, required=False)
    
    log_payload = fields.Dict(required=False)
    

