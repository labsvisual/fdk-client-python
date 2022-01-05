"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FyndRewardsCredentials import FyndRewardsCredentials


class FyndRewards(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(FyndRewardsCredentials, required=False)
    

