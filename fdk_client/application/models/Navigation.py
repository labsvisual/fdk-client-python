"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .CreatedBySchema import CreatedBySchema

from .DateMeta import DateMeta









from .NavigationReference import NavigationReference


class Navigation(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    orientation = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    _id = fields.Str(required=False)
    
    position = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    navigation = fields.Nested(NavigationReference, required=False)
    

