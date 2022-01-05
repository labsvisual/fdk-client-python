"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class CommunicationOptinDialogFeature(BaseSchema):
    # Configuration swagger.json

    
    visibility = fields.Boolean(required=False)
    

