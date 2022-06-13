"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DocumentsObj import DocumentsObj



from .DocumentsObj import DocumentsObj

from .DocumentsObj import DocumentsObj



from .DocumentsObj import DocumentsObj

from .DocumentsObj import DocumentsObj


class MetricsSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    product = fields.Nested(DocumentsObj, required=False)
    
    stage = fields.Str(required=False)
    
    company_documents = fields.Nested(DocumentsObj, required=False)
    
    store = fields.Nested(DocumentsObj, required=False)
    
    uid = fields.Int(required=False)
    
    brand = fields.Nested(DocumentsObj, required=False)
    
    store_documents = fields.Nested(DocumentsObj, required=False)
    

