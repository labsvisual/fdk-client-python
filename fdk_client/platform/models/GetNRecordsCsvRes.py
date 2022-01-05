"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetNRecordsCsvResItems import GetNRecordsCsvResItems


class GetNRecordsCsvRes(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(GetNRecordsCsvResItems, required=False), required=False)
    

