"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .ArchiveConfig import ArchiveConfig




class LocalFileConfig(BaseSchema):
    # Inventory swagger.json

    
    retries = fields.Int(required=False)
    
    interval = fields.Int(required=False)
    
    local_dir = fields.Str(required=False)
    
    working_dir = fields.Str(required=False)
    
    unzip = fields.Boolean(required=False)
    
    zip_file_regex = fields.Str(required=False)
    
    file_regex = fields.Str(required=False)
    
    zip_format = fields.Str(required=False)
    
    archive_config = fields.Nested(ArchiveConfig, required=False)
    
    read_all_files = fields.Boolean(required=False)
    

