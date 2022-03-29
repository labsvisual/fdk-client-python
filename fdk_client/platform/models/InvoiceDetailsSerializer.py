"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .InvoiceCredSerializer import InvoiceCredSerializer

from .InvoiceCredSerializer import InvoiceCredSerializer


class InvoiceDetailsSerializer(BaseSchema):
    # Catalog swagger.json

    
    e_invoice = fields.Nested(InvoiceCredSerializer, required=False)
    
    e_waybill = fields.Nested(InvoiceCredSerializer, required=False)
    

