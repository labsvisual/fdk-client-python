"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Notification import Notification

from .SystemNotificationUser import SystemNotificationUser

from .SystemNotificationUser import SystemNotificationUser








class SystemNotification(BaseSchema):
    # Communication swagger.json

    
    notification = fields.Nested(Notification, required=False)
    
    user = fields.Nested(SystemNotificationUser, required=False)
    
    settings = fields.Nested(SystemNotificationUser, required=False)
    
    _id = fields.Str(required=False)
    
    group = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    

