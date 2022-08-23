"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class BulkProductRequest(BaseSchema):
    # Catalog swagger.json

    
    batch_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    template_tag = fields.Str(required=False)
    

