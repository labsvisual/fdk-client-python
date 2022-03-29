"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema























from .EmailTemplateKeys import EmailTemplateKeys



from .EmailTemplateHeaders import EmailTemplateHeaders

from .TemplateAndType import TemplateAndType

from .TemplateAndType import TemplateAndType

from .TemplateAndType import TemplateAndType












class EmailTemplateRes(BaseSchema):
    # Communication swagger.json

    
    is_system = fields.Boolean(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    static_to = fields.List(fields.Str(required=False), required=False)
    
    static_cc = fields.List(fields.Str(required=False), required=False)
    
    static_bcc = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    keys = fields.Nested(EmailTemplateKeys, required=False)
    
    reply_to = fields.Str(required=False)
    
    headers = fields.List(fields.Nested(EmailTemplateHeaders, required=False), required=False)
    
    subject = fields.Nested(TemplateAndType, required=False)
    
    html = fields.Nested(TemplateAndType, required=False)
    
    text = fields.Nested(TemplateAndType, required=False)
    
    attachments = fields.List(fields.Raw(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    

