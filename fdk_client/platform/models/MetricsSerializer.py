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

    
    store_documents = fields.Nested(DocumentsObj, required=False)
    
    stage = fields.Str(required=False)
    
    store = fields.Nested(DocumentsObj, required=False)
    
    brand = fields.Nested(DocumentsObj, required=False)
    
    company_documents = fields.Nested(DocumentsObj, required=False)
    
    uid = fields.Int(required=False)
    
    product = fields.Nested(DocumentsObj, required=False)
    

