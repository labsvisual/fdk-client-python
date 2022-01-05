"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FreshchatCredentials import FreshchatCredentials




class Freshchat(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(FreshchatCredentials, required=False)
    
    enabled = fields.Boolean(required=False)
    

