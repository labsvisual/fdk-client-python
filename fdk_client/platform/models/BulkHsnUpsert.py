"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .HsnUpsert import HsnUpsert


class BulkHsnUpsert(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(HsnUpsert, required=False), required=False)
    

