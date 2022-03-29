"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class CommunicationValidator:
    
    class getCampaigns(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        sort = fields.Dict(required=False)
         
    
    class createCampaign(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getCampaignById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateCampaignById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getStatsOfCampaignById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getAudiences(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        sort = fields.Dict(required=False)
         
    
    class createAudience(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getBigqueryHeaders(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAudienceById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateAudienceById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getNSampleRecordsFromCsv(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getEmailProviders(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        sort = fields.Dict(required=False)
         
    
    class createEmailProvider(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getEmailProviderById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateEmailProviderById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getEmailTemplates(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        sort = fields.Dict(required=False)
         
    
    class createEmailTemplate(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getSystemEmailTemplates(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        sort = fields.Dict(required=False)
         
    
    class getEmailTemplateById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateEmailTemplateById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class deleteEmailTemplateById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class sendCommunicationSynchronously(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class sendCommunicationAsynchronously(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getEventSubscriptions(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        populate = fields.Str(required=False)
         
    
    class getJobs(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        sort = fields.Dict(required=False)
         
    
    class triggerCampaignJob(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getJobLogs(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        sort = fields.Dict(required=False)
         
    
    class getCommunicationLogs(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        sort = fields.Dict(required=False)
        
        query = fields.Dict(required=False)
         
    
    class getSystemNotifications(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getSmsProviders(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        sort = fields.Dict(required=False)
         
    
    class createSmsProvider(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getSmsProviderById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateSmsProviderById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getSmsTemplates(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        sort = fields.Dict(required=False)
         
    
    class createSmsTemplate(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getSmsTemplateById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateSmsTemplateById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class deleteSmsTemplateById(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getSystemSystemTemplates(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        sort = fields.Dict(required=False)
         
    