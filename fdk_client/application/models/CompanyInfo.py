"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .CompanyAboutAddress import CompanyAboutAddress




class CompanyInfo(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(CompanyAboutAddress, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    

