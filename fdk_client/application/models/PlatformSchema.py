"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .LookAndFeel import LookAndFeel







from .Login import Login





from .MetaSchema import MetaSchema



from .Social import Social

from .RequiredFields import RequiredFields

from .RegisterRequiredFields import RegisterRequiredFields



from .FlashCard import FlashCard



from .SocialTokens import SocialTokens











from .DeleteAccountReasons import DeleteAccountReasons




class PlatformSchema(BaseSchema):
    # User swagger.json

    
    display = fields.Str(required=False)
    
    look_and_feel = fields.Nested(LookAndFeel, required=False)
    
    updated_at = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    forgot_password = fields.Boolean(required=False)
    
    login = fields.Nested(Login, required=False)
    
    skip_captcha = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Nested(MetaSchema, required=False)
    
    _id = fields.Str(required=False)
    
    social = fields.Nested(Social, required=False)
    
    required_fields = fields.Nested(RequiredFields, required=False)
    
    register_required_fields = fields.Nested(RegisterRequiredFields, required=False)
    
    skip_login = fields.Boolean(required=False)
    
    flash_card = fields.Nested(FlashCard, required=False)
    
    subtext = fields.Str(required=False)
    
    social_tokens = fields.Nested(SocialTokens, required=False)
    
    created_at = fields.Str(required=False)
    
    register = fields.Boolean(required=False)
    
    mobile_image = fields.Str(required=False)
    
    desktop_image = fields.Str(required=False)
    
    delete_account_day = fields.Int(required=False)
    
    delete_account_reasons = fields.List(fields.Nested(DeleteAccountReasons, required=False), required=False)
    
    delete_account_consent = fields.Dict(required=False)
    

