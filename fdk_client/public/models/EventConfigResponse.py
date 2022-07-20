"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EventConfig import EventConfig


class EventConfigResponse(BaseSchema):
    # Webhook swagger.json

    
    event_configs = fields.List(fields.Nested(EventConfig, required=False), required=False)
    

