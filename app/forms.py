# app/forms.py
import re
from email_validator import validate_email, EmailNotValidError

class ContactForm:
    def __init__(self, data):
        self.data = data
        self.errors = {}
        
    def validate(self):
        name = self.data.get('name', '').strip()
        email = self.data.get('email', '').strip()
        company = self.data.get('company', '').strip()
        message = self.data.get('message', '').strip()
        
        if not name:
            self.errors['name'] = 'Name is required.'
        elif len(name) < 2:
            self.errors['name'] = 'Name must be at least 2 characters.'
            
        if not email:
            self.errors['email'] = 'Email is required.'
        else:
            try:
                validate_email(email)
            except EmailNotValidError:
                self.errors['email'] = 'Enter a valid corporate email address.'
                
        if not company:
            self.errors['company'] = 'Company name is required.'
            
        if not message:
            self.errors['message'] = 'Message details are required.'
        elif len(message) < 10:
            self.errors['message'] = 'Please write a brief summary (at least 10 characters).'
            
        return len(self.errors) == 0

class ConsultationForm:
    def __init__(self, data):
        self.data = data
        self.errors = {}
        
    def validate(self):
        name = self.data.get('name', '').strip()
        email = self.data.get('email', '').strip()
        company = self.data.get('company', '').strip()
        company_size = self.data.get('company_size', '').strip()
        ai_interest = self.data.get('ai_interest', '').strip()
        date = self.data.get('date', '').strip()
        time = self.data.get('time', '').strip()
        
        if not name:
            self.errors['name'] = 'Name is required.'
        if not email:
            self.errors['email'] = 'Corporate email is required.'
        else:
            try:
                validate_email(email)
            except EmailNotValidError:
                self.errors['email'] = 'Enter a valid email address.'
                
        if not company:
            self.errors['company'] = 'Company name is required.'
        if not company_size:
            self.errors['company_size'] = 'Company size is required.'
        if not ai_interest:
            self.errors['ai_interest'] = 'Please select a solution area of interest.'
        if not date:
            self.errors['date'] = 'Please select a preferred date.'
        if not time:
            self.errors['time'] = 'Please select a preferred time slot.'
            
        return len(self.errors) == 0
