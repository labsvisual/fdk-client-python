"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CampaignShortLink(BaseSchema):
    # Share swagger.json

    
    source = fields.Str(required=False)
    
    medium = fields.Str(required=False)
    

