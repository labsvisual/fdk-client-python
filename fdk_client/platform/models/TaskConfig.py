"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .TaskParam import TaskParam


class TaskConfig(BaseSchema):
    # Inventory swagger.json

    
    name = fields.Str(required=False)
    
    task_config_id = fields.Int(required=False)
    
    task_params = fields.List(fields.Nested(TaskParam, required=False), required=False)
    

