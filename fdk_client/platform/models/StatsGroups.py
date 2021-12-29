"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StatGroup import StatGroup


class StatsGroups(BaseSchema):
    # Analytics swagger.json

    
    groups = fields.List(fields.Nested(StatGroup, required=False), required=False)
    

