"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .GenericDTO import GenericDTO


class TaskDTO(BaseSchema):
    # Inventory swagger.json

    
    type = fields.Int(required=False)
    
    group_list = fields.List(fields.Nested(GenericDTO, required=False), required=False)
    

