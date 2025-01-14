"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .AttributeDetailsGroup import AttributeDetailsGroup






class AppConfigurationDetail(BaseSchema):
    # Catalog swagger.json

    
    template_slugs = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    attributes = fields.List(fields.Nested(AttributeDetailsGroup, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    

