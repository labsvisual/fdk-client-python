"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

























from .ArchiveConfig import ArchiveConfig


class AWSS3config(BaseSchema):
    # Inventory swagger.json

    
    bucket = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    dir = fields.Str(required=False)
    
    access_key = fields.Str(required=False)
    
    secret_key = fields.Str(required=False)
    
    local_file_path = fields.Str(required=False)
    
    archive_path = fields.Str(required=False)
    
    archive = fields.Boolean(required=False)
    
    delete = fields.Boolean(required=False)
    
    unzip = fields.Boolean(required=False)
    
    zip_format = fields.Str(required=False)
    
    file_regex = fields.Str(required=False)
    
    archive_config = fields.Nested(ArchiveConfig, required=False)
    

