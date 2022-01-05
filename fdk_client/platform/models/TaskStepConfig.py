"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TaskConfig import TaskConfig






class TaskStepConfig(BaseSchema):
    # Inventory swagger.json

    
    task_configs = fields.List(fields.Nested(TaskConfig, required=False), required=False)
    
    task_config_ids = fields.List(fields.Int(required=False), required=False)
    
    task_config_group_ids = fields.List(fields.Int(required=False), required=False)
    

