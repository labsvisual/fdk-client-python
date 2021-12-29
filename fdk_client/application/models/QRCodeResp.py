"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class QRCodeResp(BaseSchema):
    # Share swagger.json

    
    link = fields.Str(required=False)
    
    svg = fields.Str(required=False)
    

