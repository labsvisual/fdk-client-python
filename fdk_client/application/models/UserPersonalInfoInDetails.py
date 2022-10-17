"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

























from .KYCAddress import KYCAddress








class UserPersonalInfoInDetails(BaseSchema):
    # Payment swagger.json

    
    driving_license = fields.Str(required=False)
    
    voter_id = fields.Str(required=False)
    
    middle_name = fields.Str(required=False)
    
    passport = fields.Str(required=False)
    
    mobile_verified = fields.Boolean(required=False)
    
    pan = fields.Str(required=False)
    
    fathers_name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    dob = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    address_as_per_id = fields.Nested(KYCAddress, required=False)
    
    phone = fields.Str(required=False)
    
    mothers_name = fields.Str(required=False)
    
    email_verified = fields.Boolean(required=False)
    

