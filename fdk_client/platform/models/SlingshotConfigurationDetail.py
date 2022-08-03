"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SlingshotIntegration import SlingshotIntegration

from .GCompany import GCompany


class SlingshotConfigurationDetail(BaseSchema):
    # Inventory swagger.json

    
    integration = fields.Nested(SlingshotIntegration, required=False)
    
    companies = fields.List(fields.Nested(GCompany, required=False), required=False)
    

