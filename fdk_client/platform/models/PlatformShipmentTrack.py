"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Results import Results


class PlatformShipmentTrack(BaseSchema):
    # Order swagger.json

    
    results = fields.Nested(Results, required=False)
    

