"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class Google(BaseSchema):
    # User swagger.json

    
    app_id = fields.Str(required=False)
    

