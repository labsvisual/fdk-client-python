"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RecipientHeaders import RecipientHeaders

from .CampaignEmail import CampaignEmail


























class Campaign(BaseSchema):
    # Communication swagger.json

    
    recipient_headers = fields.Nested(RecipientHeaders, required=False)
    
    email = fields.Nested(CampaignEmail, required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    datasource = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    

