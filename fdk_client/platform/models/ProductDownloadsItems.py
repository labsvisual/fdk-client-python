"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductDownloadItemsData import ProductDownloadItemsData









from .VerifiedBy import VerifiedBy








class ProductDownloadsItems(BaseSchema):
    # Catalog swagger.json

    
    status = fields.Str(required=False)
    
    data = fields.Nested(ProductDownloadItemsData, required=False)
    
    url = fields.Str(required=False)
    
    template_tags = fields.Dict(required=False)
    
    seller_id = fields.Float(required=False)
    
    id = fields.Str(required=False)
    
    created_by = fields.Nested(VerifiedBy, required=False)
    
    trigger_on = fields.Str(required=False)
    
    completed_on = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    

