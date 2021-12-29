"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Firebase import Firebase

from .Moengage import Moengage

from .Segment import Segment

from .Gtm import Gtm

from .Freshchat import Freshchat

from .Safetynet import Safetynet

from .FyndRewards import FyndRewards

from .GoogleMap import GoogleMap


class Tokens(BaseSchema):
    # Configuration swagger.json

    
    firebase = fields.Nested(Firebase, required=False)
    
    moengage = fields.Nested(Moengage, required=False)
    
    segment = fields.Nested(Segment, required=False)
    
    gtm = fields.Nested(Gtm, required=False)
    
    freshchat = fields.Nested(Freshchat, required=False)
    
    safetynet = fields.Nested(Safetynet, required=False)
    
    fynd_rewards = fields.Nested(FyndRewards, required=False)
    
    google_map = fields.Nested(GoogleMap, required=False)
    

