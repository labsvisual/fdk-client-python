"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SystemNotification import SystemNotification



from .Page import Page


class SystemNotifications(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(SystemNotification, required=False), required=False)
    
    last_read_anchor = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    

