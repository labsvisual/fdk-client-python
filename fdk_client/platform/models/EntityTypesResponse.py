"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntityTypeObj import EntityTypeObj


class EntityTypesResponse(BaseSchema):
    # AuditTrail swagger.json

    
    items = fields.List(fields.Nested(EntityTypeObj, required=False), required=False)
    

