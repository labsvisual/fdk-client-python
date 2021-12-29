"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





































from .ArchiveConfig import ArchiveConfig










class EmailConfig(BaseSchema):
    # Inventory swagger.json

    
    recepient = fields.Str(required=False)
    
    host = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    unzip = fields.Boolean(required=False)
    
    read_from_content = fields.Boolean(required=False)
    
    filter_based_on_recepients = fields.Boolean(required=False)
    
    pcol = fields.Str(required=False)
    
    subject_line_regex = fields.Str(required=False)
    
    sender_address = fields.Str(required=False)
    
    local_dir = fields.Str(required=False)
    
    folder_name_hierarchies = fields.List(fields.Str(required=False), required=False)
    
    attachment_regex = fields.Str(required=False)
    
    body_content_regex = fields.Str(required=False)
    
    password_protected = fields.Boolean(required=False)
    
    zip_format = fields.Str(required=False)
    
    attachment_mandate = fields.Boolean(required=False)
    
    filter_files_after_extraction = fields.Boolean(required=False)
    
    archive_config = fields.Nested(ArchiveConfig, required=False)
    
    read_all_unread_mails = fields.Boolean(required=False)
    
    content_type = fields.Str(required=False)
    
    downloadable_link = fields.Boolean(required=False)
    
    properties = fields.Dict(required=False)
    

