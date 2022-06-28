"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class GetConfigMetadataResponse(BaseSchema):
    # Catalog swagger.json

    
    condition = fields.List(fields.Dict(required=False), required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    values = fields.List(fields.Dict(required=False), required=False)
    

