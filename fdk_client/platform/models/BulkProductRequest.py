"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class BulkProductRequest(BaseSchema):
    # Catalog swagger.json

    
    template_tag = fields.Str(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    batch_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    

