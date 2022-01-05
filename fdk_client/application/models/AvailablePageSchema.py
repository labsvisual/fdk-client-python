"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .AvailablePageSchemaSections import AvailablePageSchemaSections

from .AvailablePageSectionMetaAttributes import AvailablePageSectionMetaAttributes



from .AvailablePageSeo import AvailablePageSeo






class AvailablePageSchema(BaseSchema):
    # Theme swagger.json

    
    value = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    path = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    sections = fields.List(fields.Nested(AvailablePageSchemaSections, required=False), required=False)
    
    sections_meta = fields.List(fields.Nested(AvailablePageSectionMetaAttributes, required=False), required=False)
    
    theme = fields.Str(required=False)
    
    seo = fields.Nested(AvailablePageSeo, required=False)
    
    props = fields.List(fields.Dict(required=False), required=False)
    
    _id = fields.Str(required=False)
    

