"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .Priority import Priority







from .SubmitButton import SubmitButton



from .CreatedOn import CreatedOn



from .PollForAssignment import PollForAssignment




class CustomForm(BaseSchema):
    # Lead swagger.json

    
    application_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    header_image = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    priority = fields.Nested(Priority, required=False)
    
    login_required = fields.Boolean(required=False)
    
    should_notify = fields.Boolean(required=False)
    
    success_message = fields.Str(required=False)
    
    submit_button = fields.Nested(SubmitButton, required=False)
    
    inputs = fields.List(fields.Dict(required=False), required=False)
    
    created_on = fields.Nested(CreatedOn, required=False)
    
    created_by = fields.Dict(required=False)
    
    poll_for_assignment = fields.Nested(PollForAssignment, required=False)
    
    _id = fields.Str(required=False)
    

