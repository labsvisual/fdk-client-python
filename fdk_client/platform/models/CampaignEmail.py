"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CampaignEmailTemplate import CampaignEmailTemplate

from .CampignEmailProvider import CampignEmailProvider


class CampaignEmail(BaseSchema):
    # Communication swagger.json

    
    template = fields.Nested(CampaignEmailTemplate, required=False)
    
    provider = fields.Nested(CampignEmailProvider, required=False)
    

