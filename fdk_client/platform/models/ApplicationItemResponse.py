"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SEO import SEO

from .MOQ import MOQ




class ApplicationItemResponse(BaseSchema):
    # Catalog swagger.json

    
    seo = fields.Nested(SEO, required=False)
    
    moq = fields.Nested(MOQ, required=False)
    
    alt_text = fields.Dict(required=False)
    

