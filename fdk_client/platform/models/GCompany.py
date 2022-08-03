"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .GStore import GStore

from .GStore import GStore


class GCompany(BaseSchema):
    # Inventory swagger.json

    
    _id = fields.Str(required=False)
    
    integration = fields.Str(required=False)
    
    level = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    opted = fields.Boolean(required=False)
    
    permissions = fields.List(fields.Str(required=False), required=False)
    
    token = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    stores = fields.List(fields.Nested(GStore, required=False), required=False)
    
    gstores = fields.List(fields.Nested(GStore, required=False), required=False)
    

