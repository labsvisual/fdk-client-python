"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ArchiveConfig(BaseSchema):
    # Inventory swagger.json

    
    delete = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    
    archive_dir = fields.Str(required=False)
    

