"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Guide import Guide
























class ValidateSizeGuide(BaseSchema):
    # Catalog swagger.json

    
    tag = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
    guide = fields.Nested(Guide, required=False)
    
    modified_on = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    subtitle = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    
    active = fields.Boolean(required=False)
    
    company_id = fields.Int(required=False)
    
    description = fields.Str(required=False)
    

