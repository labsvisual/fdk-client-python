"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OAuthRequestAppleSchemaOauth import OAuthRequestAppleSchemaOauth

from .OAuthRequestAppleSchemaProfile import OAuthRequestAppleSchemaProfile


class OAuthRequestAppleSchema(BaseSchema):
    # User swagger.json

    
    user_identifier = fields.Str(required=False)
    
    oauth = fields.Nested(OAuthRequestAppleSchemaOauth, required=False)
    
    profile = fields.Nested(OAuthRequestAppleSchemaProfile, required=False)
    

