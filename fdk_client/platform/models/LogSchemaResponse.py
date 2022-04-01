"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LogDocs import LogDocs


class LogSchemaResponse(BaseSchema):
    # AuditTrail swagger.json

    
    docs = fields.List(fields.Nested(LogDocs, required=False), required=False)
    

