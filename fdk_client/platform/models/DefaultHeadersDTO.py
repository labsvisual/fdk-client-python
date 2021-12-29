"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PropBeanDTO import PropBeanDTO

from .PropBeanDTO import PropBeanDTO

from .PropBeanDTO import PropBeanDTO

from .PropBeanDTO import PropBeanDTO


class DefaultHeadersDTO(BaseSchema):
    # Inventory swagger.json

    
    store = fields.Nested(PropBeanDTO, required=False)
    
    intf_article_id = fields.Nested(PropBeanDTO, required=False)
    
    price_effective = fields.Nested(PropBeanDTO, required=False)
    
    quantity = fields.Nested(PropBeanDTO, required=False)
    

