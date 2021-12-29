"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class TemplateAndType(BaseSchema):
    # Communication swagger.json

    
    template_type = fields.Str(required=False)
    
    template = fields.Str(required=False)
    

