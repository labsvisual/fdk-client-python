"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .App import App

from .AppInventory import AppInventory

from .AppDomain import AppDomain


class CreateApplicationRequest(BaseSchema):
    # Configuration swagger.json

    
    app = fields.Nested(App, required=False)
    
    configuration = fields.Nested(AppInventory, required=False)
    
    domain = fields.Nested(AppDomain, required=False)
    

