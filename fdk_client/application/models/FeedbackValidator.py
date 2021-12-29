"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class FeedbackValidator:
    
    class createAbuseReport(BaseSchema):
        
        pass 
    
    class updateAbuseReport(BaseSchema):
        
        pass 
    
    class getAbuseReports(BaseSchema):
        
        entity_id = fields.Str(required=False)
        
        entity_type = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getAttributes(BaseSchema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class createAttribute(BaseSchema):
        
        pass 
    
    class getAttribute(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class updateAttribute(BaseSchema):
        
        slug = fields.Str(required=False)
         
    
    class createComment(BaseSchema):
        
        pass 
    
    class updateComment(BaseSchema):
        
        pass 
    
    class getComments(BaseSchema):
        
        entity_type = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class checkEligibility(BaseSchema):
        
        entity_type = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
         
    
    class deleteMedia(BaseSchema):
        
        ids = fields.List(fields.Str(required=False), required=False)
         
    
    class createMedia(BaseSchema):
        
        pass 
    
    class updateMedia(BaseSchema):
        
        pass 
    
    class getMedias(BaseSchema):
        
        entity_type = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        type = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getReviewSummaries(BaseSchema):
        
        entity_type = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class createReview(BaseSchema):
        
        pass 
    
    class updateReview(BaseSchema):
        
        pass 
    
    class getReviews(BaseSchema):
        
        entity_type = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        media = fields.Str(required=False)
        
        rating = fields.List(fields.Float(required=False), required=False)
        
        attribute_rating = fields.List(fields.Str(required=False), required=False)
        
        facets = fields.Boolean(required=False)
        
        sort = fields.Str(required=False)
        
        active = fields.Boolean(required=False)
        
        approve = fields.Boolean(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getTemplates(BaseSchema):
        
        template_id = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        entity_type = fields.Str(required=False)
         
    
    class createQuestion(BaseSchema):
        
        pass 
    
    class updateQuestion(BaseSchema):
        
        pass 
    
    class getQuestionAndAnswers(BaseSchema):
        
        entity_type = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        show_answer = fields.Boolean(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getVotes(BaseSchema):
        
        id = fields.Str(required=False)
        
        ref_type = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class createVote(BaseSchema):
        
        pass 
    
    class updateVote(BaseSchema):
        
        pass 
    