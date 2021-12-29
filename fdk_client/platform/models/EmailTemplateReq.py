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






class EmailTemplateReq(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    keys = fields.Nested(EmailTemplateKeys, required=False)
    
    from_ = fields.Str(required=False)
    
    static_to = fields.List(fields.Str(required=False), required=False)
    
    static_cc = fields.List(fields.Str(required=False), required=False)
    
    static_bcc = fields.List(fields.Str(required=False), required=False)
    
    reply_to = fields.Str(required=False)
    
    headers = fields.List(fields.Nested(EmailTemplateHeaders, required=False), required=False)
    
    subject = fields.Nested(TemplateAndType, required=False)
    
    html = fields.Nested(TemplateAndType, required=False)
    
    text = fields.Nested(TemplateAndType, required=False)
    
    attachments = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    

