"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .CreatedBySchema import CreatedBySchema

from .DateMeta import DateMeta

from .Orientation import Orientation



from .NavigationReference import NavigationReference


class NavigationSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    archived = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    platform = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    orientation = fields.Nested(Orientation, required=False)
    
    version = fields.Float(required=False)
    
    navigation = fields.List(fields.Nested(NavigationReference, required=False), required=False)
    

