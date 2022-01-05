"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





























from .TemplateAndType import TemplateAndType

from .TemplateAndType import TemplateAndType

from .TemplateAndType import TemplateAndType












class SystemEmailTemplate(BaseSchema):
    # Communication swagger.json

    
    is_system = fields.Boolean(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    static_to = fields.List(fields.Raw(required=False), required=False)
    
    static_cc = fields.List(fields.Raw(required=False), required=False)
    
    static_bcc = fields.List(fields.Raw(required=False), required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    from_ = fields.Str(required=False)
    
    from_name = fields.Str(required=False)
    
    subject = fields.Nested(TemplateAndType, required=False)
    
    html = fields.Nested(TemplateAndType, required=False)
    
    text = fields.Nested(TemplateAndType, required=False)
    
    headers = fields.List(fields.Raw(required=False), required=False)
    
    attachments = fields.List(fields.Raw(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    

