"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ActivityHistory import ActivityHistory


class GetActivityStatus(BaseSchema):
    # Order swagger.json

    
    activity_history = fields.Nested(ActivityHistory, required=False)
    

