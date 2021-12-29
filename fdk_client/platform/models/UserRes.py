"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Points import Points

from .RewardUser import RewardUser


class UserRes(BaseSchema):
    # Rewards swagger.json

    
    points = fields.Nested(Points, required=False)
    
    user = fields.Nested(RewardUser, required=False)
    

