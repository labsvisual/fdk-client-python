"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DpDetails(BaseSchema):
    # Order swagger.json

    
    gst_tag = fields.Str(required=False)
    

