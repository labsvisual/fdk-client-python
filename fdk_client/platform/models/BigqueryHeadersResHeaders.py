"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class BigqueryHeadersResHeaders(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

