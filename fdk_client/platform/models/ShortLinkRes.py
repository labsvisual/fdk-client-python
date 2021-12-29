"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .UrlInfo import UrlInfo



























from .CampaignShortLink import CampaignShortLink

from .Redirects import Redirects

from .Attribution import Attribution

from .SocialMediaTags import SocialMediaTags




class ShortLinkRes(BaseSchema):
    # Share swagger.json

    
    title = fields.Str(required=False)
    
    url = fields.Nested(UrlInfo, required=False)
    
    created_by = fields.Str(required=False)
    
    app_redirect = fields.Boolean(required=False)
    
    fallback = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    expire_at = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    updated_at = fields.Str(required=False)
    
    personalized = fields.Boolean(required=False)
    
    campaign = fields.Nested(CampaignShortLink, required=False)
    
    redirects = fields.Nested(Redirects, required=False)
    
    attribution = fields.Nested(Attribution, required=False)
    
    social_media_tags = fields.Nested(SocialMediaTags, required=False)
    
    count = fields.Int(required=False)
    

