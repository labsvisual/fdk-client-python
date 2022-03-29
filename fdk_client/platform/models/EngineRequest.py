"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PayloadStructure import PayloadStructure

from .MetaStructure import MetaStructure


class EngineRequest(BaseSchema):
    # Communication swagger.json

    
    payload = fields.Nested(PayloadStructure, required=False)
    
    meta = fields.Nested(MetaStructure, required=False)
    

