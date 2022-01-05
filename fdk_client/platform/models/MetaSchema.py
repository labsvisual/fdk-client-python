"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class MetaSchema(BaseSchema):
    # User swagger.json

    
    fynd_default = fields.Boolean(required=False)
    

