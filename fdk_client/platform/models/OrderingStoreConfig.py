"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DeploymentMeta import DeploymentMeta


class OrderingStoreConfig(BaseSchema):
    # Configuration swagger.json

    
    deployment_meta = fields.Nested(DeploymentMeta, required=False)
    

