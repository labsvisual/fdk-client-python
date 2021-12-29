"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AdditionalContactDetails import AdditionalContactDetails

from .Documents import Documents





from .ProductReturnConfig import ProductReturnConfig





from .Timing import Timing


class FulfillingStoreMeta(BaseSchema):
    # Order swagger.json

    
    additional_contact_details = fields.Nested(AdditionalContactDetails, required=False)
    
    documents = fields.Nested(Documents, required=False)
    
    gst_number = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfig, required=False)
    
    allow_dp_assignment_from_fynd = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    timing = fields.Nested(Timing, required=False)
    

