"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Stage import Stage

from .Stages import Stages


class Filters(BaseSchema):
    # Order swagger.json

    
    stage = fields.Nested(Stage, required=False)
    
    stages = fields.Nested(Stages, required=False)
    

