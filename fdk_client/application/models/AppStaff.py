"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class AppStaff(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    order_incent = fields.Boolean(required=False)
    
    stores = fields.List(fields.Int(required=False), required=False)
    
    application = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    employee_code = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    profile_pic_url = fields.Str(required=False)
    

