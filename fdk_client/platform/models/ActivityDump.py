"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Activity import Activity

from .CreatedBy import CreatedBy

from .DateMeta import DateMeta






class ActivityDump(BaseSchema):
    # Feedback swagger.json

    
    activity = fields.Nested(Activity, required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

