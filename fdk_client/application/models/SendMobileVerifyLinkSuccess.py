"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class SendMobileVerifyLinkSuccess(BaseSchema):
    # User swagger.json

    
    verify_mobile_link = fields.Boolean(required=False)
    

