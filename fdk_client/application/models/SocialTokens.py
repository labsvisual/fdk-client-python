"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Facebook import Facebook

from .Accountkit import Accountkit

from .Google import Google


class SocialTokens(BaseSchema):
    # User swagger.json

    
    facebook = fields.Nested(Facebook, required=False)
    
    account_kit = fields.Nested(Accountkit, required=False)
    
    google = fields.Nested(Google, required=False)
    

