"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FacebookLink import FacebookLink

from .InstagramLink import InstagramLink

from .TwitterLink import TwitterLink

from .PinterestLink import PinterestLink

from .GooglePlusLink import GooglePlusLink

from .YoutubeLink import YoutubeLink

from .LinkedInLink import LinkedInLink

from .VimeoLink import VimeoLink

from .BlogLink import BlogLink


class SocialLinks(BaseSchema):
    # Configuration swagger.json

    
    facebook = fields.Nested(FacebookLink, required=False)
    
    instagram = fields.Nested(InstagramLink, required=False)
    
    twitter = fields.Nested(TwitterLink, required=False)
    
    pinterest = fields.Nested(PinterestLink, required=False)
    
    google_plus = fields.Nested(GooglePlusLink, required=False)
    
    youtube = fields.Nested(YoutubeLink, required=False)
    
    linked_in = fields.Nested(LinkedInLink, required=False)
    
    vimeo = fields.Nested(VimeoLink, required=False)
    
    blog_link = fields.Nested(BlogLink, required=False)
    

