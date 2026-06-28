import os
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv(override=True)

class Config:
    """Base configuration settings for Altimet AI website."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'altimet_ai_enterprise_secret_key_192837465')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    TESTING = False
    
    # Cache settings (mocked or custom config can be placed here)
    SITE_NAME = "Altimet AI"
    SITE_DOMAIN = "altimetai.com"
    SITE_TITLE = "Altimet AI - Enterprise AI Copilots, Data Intelligence & Agentic Automation"
    SITE_DESCRIPTION = (
        "Altimet AI builds production-grade AI copilots, enterprise knowledge networks, "
        "and agentic workflows that empower organizations to transform data into intelligence."
    )
