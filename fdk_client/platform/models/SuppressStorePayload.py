"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SuppressStoreModel import SuppressStoreModel

from .KafkaMetaModel import KafkaMetaModel


class SuppressStorePayload(BaseSchema):
    # Inventory swagger.json

    
    payload = fields.List(fields.Nested(SuppressStoreModel, required=False), required=False)
    
    meta = fields.Nested(KafkaMetaModel, required=False)
    

