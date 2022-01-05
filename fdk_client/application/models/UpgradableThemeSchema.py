"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class UpgradableThemeSchema(BaseSchema):
    # Theme swagger.json

    
    parent_theme = fields.Str(required=False)
    
    applied_theme = fields.Str(required=False)
    
    upgrade = fields.Boolean(required=False)
    

