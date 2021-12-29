"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .InformationAddress import InformationAddress

from .InformationSupport import InformationSupport

from .SocialLinks import SocialLinks

from .Links import Links





from .BusinessHighlights import BusinessHighlights










class ApplicationInformation(BaseSchema):
    # Configuration swagger.json

    
    address = fields.Nested(InformationAddress, required=False)
    
    support = fields.Nested(InformationSupport, required=False)
    
    social_links = fields.Nested(SocialLinks, required=False)
    
    links = fields.Nested(Links, required=False)
    
    copyright_text = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    business_highlights = fields.Nested(BusinessHighlights, required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    

