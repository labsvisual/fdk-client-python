"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .MOQ import MOQ



from .SEO import SEO


class ApplicationItemResponse(BaseSchema):
    # Catalog swagger.json

    
    moq = fields.Nested(MOQ, required=False)
    
    alt_text = fields.Dict(required=False)
    
    seo = fields.Nested(SEO, required=False)
    

