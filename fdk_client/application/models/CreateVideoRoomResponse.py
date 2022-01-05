"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class CreateVideoRoomResponse(BaseSchema):
    # Lead swagger.json

    
    unique_name = fields.Str(required=False)
    

