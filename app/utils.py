# app/utils.py
import json
from flask import url_for

def get_seo_metadata(title=None, description=None, url=None, image=None):
    """Generates standard SEO dictionaries for pages."""
    base_title = "Altimet AI - Enterprise AI Copilots, Data Intelligence & Agentic Automation"
    base_desc = "Altimet AI builds production-grade AI copilots, enterprise knowledge networks, and agentic workflows that empower organizations to transform data into intelligence."
    
    meta_title = f"{title} | Altimet AI" if title else base_title
    meta_desc = description or base_desc
    meta_url = url or "https://altimetai.com"
    meta_image = image or "https://altimetai.com/static/images/og-image.jpg"
    
    return {
        "title": meta_title,
        "description": meta_desc,
        "url": meta_url,
        "image": meta_image,
        "site_name": "Altimet AI",
        "twitter_card": "summary_large_image"
    }

def get_schema_markup(schema_type, data=None):
    """Generates JSON-LD structures for search engine crawlers."""
    if schema_type == "organization":
        schema = {
            "@context": "https://schema.org",
            "@type": "Corporation",
            "name": "Altimet AI",
            "url": "https://altimetai.com",
            "logo": "https://altimetai.com/static/images/logo.png",
            "description": "Enterprise AI Consulting, AI Copilots & Agentic Automation",
            "sameAs": [
                "https://twitter.com/altimetai",
                "https://linkedin.com/company/altimetai"
            ],
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": "+1-800-ALTIMET",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            }
        }
    elif schema_type == "services":
        services_list = []
        for s in (data or []):
            services_list.append({
                "@type": "Service",
                "name": s["name"],
                "description": s["short_description"],
                "provider": {
                    "@type": "LocalBusiness",
                    "name": "Altimet AI"
                }
            })
        schema = {
            "@context": "https://schema.org",
            "@graph": services_list
        }
    elif schema_type == "faq":
        faq_list = []
        for item in (data or []):
            faq_list.append({
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": item["a"]
                }
            })
        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_list
        }
    else:
        schema = {}
        
    return json.dumps(schema)

def send_notification_email(subject, html_content, to_email=None):
    """
    Sends an email notification via SMTP.
    If SMTP variables are not configured in .env, it logs the email output
    to a file under instance/emails/ for verification during development.
    """
    import os
    import datetime
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    
    # Securely retrieve Flask or standard library logger
    try:
        from flask import current_app
        logger = current_app.logger
    except RuntimeError:
        import logging
        logger = logging.getLogger('altimet_ai')

    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = os.environ.get('SMTP_PORT')
    smtp_username = os.environ.get('SMTP_USERNAME')
    smtp_password = os.environ.get('SMTP_PASSWORD')
    smtp_from = os.environ.get('SMTP_FROM', 'no-reply@altimetai.com')
    
    target_email = to_email or os.environ.get('NOTIFICATION_RECEIVER', 'leads@altimetai.com')
    
    # Check if SMTP is configured
    if smtp_server and smtp_port and smtp_username and smtp_password:
        logger.info(f"Attempting to send email. Server: {smtp_server}:{smtp_port}, From: {smtp_from}, To: {target_email}")
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = smtp_from
            msg['To'] = target_email
            
            part = MIMEText(html_content, 'html')
            msg.attach(part)
            
            server = smtplib.SMTP(smtp_server, int(smtp_port))
            if os.environ.get('SMTP_USE_TLS', 'True').lower() in ('true', '1', 't'):
                server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_from, target_email, msg.as_string())
            server.quit()
            logger.info(f"[Email Sent Successfully] Subject: {subject} to {target_email}")
            return True
        except Exception as e:
            logger.error(f"[SMTP Error] Failed to send email: {e}", exc_info=True)
            # Fallback to local logging below
    else:
        logger.warning("SMTP server variables are not fully configured in .env. Falling back to local logging.")
            
    # Local Logging Fallback (Useful for local testing/dev)
    os.makedirs('instance/emails', exist_ok=True)
    filename = f"instance/emails/email_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.html"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"<!--\nSubject: {subject}\nTo: {target_email}\nFrom: {smtp_from}\nDate: {datetime.datetime.now()}\n-->\n")
            f.write(html_content)
        logger.info(f"[Mock Email Logged] Local path: {filename}")
        return True
    except Exception as log_err:
        logger.error(f"[Mock Email Log Fail] Error writing to file: {log_err}", exc_info=True)
    return False

