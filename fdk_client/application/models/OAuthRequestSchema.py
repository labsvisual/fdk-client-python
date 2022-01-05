"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OAuthRequestSchemaOauth2 import OAuthRequestSchemaOauth2

from .OAuthRequestSchemaProfile import OAuthRequestSchemaProfile


class OAuthRequestSchema(BaseSchema):
    # User swagger.json

    
    is_signed_in = fields.Boolean(required=False)
    
    oauth2 = fields.Nested(OAuthRequestSchemaOauth2, required=False)
    
    profile = fields.Nested(OAuthRequestSchemaProfile, required=False)
    

