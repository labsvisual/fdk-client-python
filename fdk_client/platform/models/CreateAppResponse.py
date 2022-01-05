"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Application import Application

from .ApplicationInventory import ApplicationInventory


class CreateAppResponse(BaseSchema):
    # Configuration swagger.json

    
    app = fields.Nested(Application, required=False)
    
    configuration = fields.Nested(ApplicationInventory, required=False)
    

