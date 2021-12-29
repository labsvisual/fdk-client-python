"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class CodeRequestBodySchema(BaseSchema):
    # User swagger.json

    
    code = fields.Str(required=False)
    

