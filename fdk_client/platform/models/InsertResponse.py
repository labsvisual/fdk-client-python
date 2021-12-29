"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class InsertResponse(BaseSchema):
    # Feedback swagger.json

    
    count = fields.Int(required=False)
    

