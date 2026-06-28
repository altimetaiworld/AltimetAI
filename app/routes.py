# app/routes.py
import os
from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for, abort, make_response
from app.services import ContentService
from app.forms import ContactForm, ConsultationForm
from app.utils import get_seo_metadata, get_schema_markup, send_notification_email

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    services = ContentService.get_services()
    industries = ContentService.get_industries()
    case_studies = ContentService.get_case_studies()
    faqs = services[0]['faq'] + services[1]['faq'] # combine some FAQs for home page
    
    seo = get_seo_metadata(
        title="Enterprise AI Copilots & Agentic Automation",
        description="Altimet AI builds custom data copilots, knowledge indexes, and autonomous agents for enterprise scale."
    )
    schema_org = get_schema_markup("organization")
    
    return render_template('index.html', 
                           services=services, 
                           industries=industries,
                           case_studies=case_studies,
                           faqs=faqs[:5],
                           seo=seo,
                           schema_org=schema_org)

@main_bp.route('/services')
def services():
    services_list = ContentService.get_services()
    seo = get_seo_metadata(
        title="Enterprise AI Services",
        description="Explore Altimet AI's core capabilities: AI Data Copilots, Enterprise Knowledge Networks, AI Agent Systems, and Custom Model Tuning."
    )
    schema_org = get_schema_markup("services", services_list)
    return render_template('services.html', services=services_list, seo=seo, schema_org=schema_org)

@main_bp.route('/services/<slug>')
def service_detail(slug):
    services_list = ContentService.get_services()
    service = next((s for s in services_list if s['slug'] == slug), None)
    if not service:
        abort(404)
        
    seo = get_seo_metadata(
        title=f"{service['name']} - Services",
        description=service['short_description']
    )
    schema_org = get_schema_markup("faq", service['faq'])
    return render_template('services-detail.html', service=service, seo=seo, schema_org=schema_org)

@main_bp.route('/industries')
def industries():
    industries_list = ContentService.get_industries()
    seo = get_seo_metadata(
        title="AI Solutions by Industry Vertical",
        description="Delivering measurable financial impact across Retail, Ecommerce, Manufacturing, Financial Services, and Healthcare."
    )
    return render_template('industries.html', industries=industries_list, seo=seo)

@main_bp.route('/industries/<slug>')
def industry_detail(slug):
    industries_list = ContentService.get_industries()
    industry = next((i for i in industries_list if i['slug'] == slug), None)
    if not industry:
        abort(404)
        
    seo = get_seo_metadata(
        title=f"AI for {industry['name']} - Industry Solutions",
        description=industry['intro']
    )
    return render_template('industries-detail.html', industry=industry, seo=seo)

@main_bp.route('/case-studies')
def case_studies():
    cases = ContentService.get_case_studies()
    seo = get_seo_metadata(
        title="Enterprise AI Case Studies & ROI",
        description="Real-world case studies demonstrating 30%+ downtime reduction, 80% database reporting cuts, and automation scales."
    )
    return render_template('case-studies.html', case_studies=cases, seo=seo)

@main_bp.route('/case-studies/<slug>')
def case_study_detail(slug):
    cases = ContentService.get_case_studies()
    cs = next((c for c in cases if c['slug'] == slug), None)
    if not cs:
        abort(404)
        
    seo = get_seo_metadata(
        title=f"{cs['title']} - Case Study",
        description=cs['summary']
    )
    return render_template('case-studies-detail.html', cs=cs, seo=seo)

@main_bp.route('/about')
def about():
    seo = get_seo_metadata(
        title="About Altimet AI - Enterprise AI Consulting & Products",
        description="Learn about Altimet AI's mission, engineering principles, and core executive leadership team."
    )
    return render_template('about.html', seo=seo)

@main_bp.route('/blog')
def blog():
    posts = ContentService.get_blog_posts()
    query = request.args.get('q', '').strip()
    category = request.args.get('category', '').strip()
    
    if query:
        posts = [p for p in posts if query.lower() in p['title'].lower() or query.lower() in p['summary'].lower()]
    if category:
        posts = [p for p in posts if category.lower() == p['category'].lower()]
        
    seo = get_seo_metadata(
        title="Insights, Architecture & Guides",
        description="Technical analysis, vector database strategies, model fine-tuning budgets, and agentic workflows."
    )
    return render_template('blog.html', blog_posts=posts, query=query, category=category, seo=seo)

@main_bp.route('/blog/<slug>')
def blog_detail(slug):
    posts = ContentService.get_blog_posts()
    post = next((p for p in posts if p['slug'] == slug), None)
    if not post:
        abort(404)
        
    seo = get_seo_metadata(
        title=post['title'],
        description=post['summary']
    )
    return render_template('blog-detail.html', post=post, seo=seo)

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    errors = {}
    success = False
    name = ""
    
    if request.method == 'POST':
        form = ContactForm(request.form)
        if form.validate():
            success = True
            
            name = request.form.get('name')
            email = request.form.get('email')
            company = request.form.get('company')
            message = request.form.get('message')
            
            # 1. Dispatch scoping notification email to administrator
            admin_subject = f"New Enterprise Inquiry from {company}"
            admin_html = f"""
            <h2>New Contact Form Inquiry</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Company:</strong> {company}</p>
            <p><strong>Message:</strong><br>{message}</p>
            """
            send_notification_email(admin_subject, admin_html)
            
            # 2. Dispatch receipt confirmation to the visitor
            smtp_from = os.environ.get('SMTP_FROM', 'altimetaiworld@gmail.com')
            visitor_subject = "Inquiry Received | Altimet AI"
            visitor_html = f"""
            <h2>Thank you for reaching out to Altimet AI, {name}!</h2>
            <p>We have successfully received your inquiry regarding <strong>{company}</strong>.</p>
            <p>Our Principal AI Architects are reviewing your description parameters and will follow up with you within 12 hours.</p>
            <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
            <p style="font-size: 11px; color: #777;">This is an automated confirmation sent from Altimet AI ({smtp_from}).</p>
            """
            send_notification_email(visitor_subject, visitor_html, to_email=email)

            if request.headers.get('HX-Request'):
                # Handle HTMX request with a sleek partial return
                return render_template('components/contact-success.html', name=name)
            flash("Thank you for your message! Our engineering team will review and reply within 12 hours.", "success")
        else:
            errors = form.errors
            if request.headers.get('HX-Request'):
                return render_template('components/contact-form-partial.html', errors=errors, values=request.form)
                
    seo = get_seo_metadata(
        title="Contact Our Enterprise AI Team",
        description="Start your AI journey. Message our team for custom implementations or pilot assessments."
    )
    return render_template('contact.html', errors=errors, success=success, name=name, seo=seo)

@main_bp.route('/book-consultation', methods=['GET', 'POST'])
def book_consultation():
    errors = {}
    success = False
    name = ""
    date = ""
    time = ""
    code = ""
    
    if request.method == 'POST':
        form = ConsultationForm(request.form)
        if form.validate():
            success = True
            name = request.form.get('name')
            email = request.form.get('email')
            company = request.form.get('company')
            company_size = request.form.get('company_size')
            ai_interest = request.form.get('ai_interest')
            date = request.form.get('date')
            time = request.form.get('time')
            
            import random
            code = f"ALT-{random.randint(1000, 9999)}"
            
            # 1. Dispatch scoping call alert to administrator
            admin_subject = f"New Discovery Consultation Requested by {company}"
            admin_html = f"""
            <h2>New Scoping Call Request</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Company:</strong> {company}</p>
            <p><strong>Company Size:</strong> {company_size}</p>
            <p><strong>AI Interest Focus:</strong> {ai_interest}</p>
            <p><strong>Preferred Date:</strong> {date}</p>
            <p><strong>Preferred Time Slot:</strong> {time} (EST)</p>
            """
            send_notification_email(admin_subject, admin_html)
            
            # 2. Dispatch scheduled session confirmation to the visitor
            smtp_from = os.environ.get('SMTP_FROM', 'altimetaiworld@gmail.com')
            visitor_subject = "Consultation Scheduled | Altimet AI"
            visitor_html = f"""
            <h2>Your Discovery Session is Reserved, {name}!</h2>
            <p>We look forward to meeting with you to discuss custom pipelines for <strong>{company}</strong>.</p>
            <div style="background-color: #f9f9f9; padding: 15px; border-radius: 8px; margin: 15px 0; max-width: 400px; font-family: monospace;">
              <p style="margin: 5px 0;"><strong>Topic:</strong> Technical Scoping Call</p>
              <p style="margin: 5px 0;"><strong>Date:</strong> {date}</p>
              <p style="margin: 5px 0;"><strong>Time Slot:</strong> {time} EST</p>
              <p style="margin: 5px 0;"><strong>Platform:</strong> MS Teams Invite Attached</p>
            </div>
            <p>An engineer will bring a draft architecture outline based on your selected focus area: <strong>{ai_interest}</strong>.</p>
            <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
            <p style="font-size: 11px; color: #777;">This is an automated confirmation sent from Altimet AI ({smtp_from}).</p>
            """
            send_notification_email(visitor_subject, visitor_html, to_email=email)

            if request.headers.get('HX-Request'):
                return render_template('components/booking-success.html', name=name, date=date, time=time, code=code)
            flash("Your discovery consultation has been requested successfully!", "success")
        else:
            errors = form.errors
            if request.headers.get('HX-Request'):
                return render_template('components/booking-form-partial.html', errors=errors, values=request.form)
                
    seo = get_seo_metadata(
        title="Schedule a Discovery Consultation",
        description="Book a 30-minute technical discovery session to review schema options and custom agent pipelines."
    )
    return render_template('book-consultation.html', errors=errors, success=success, name=name, date=date, time=time, code=code, seo=seo)

@main_bp.route('/privacy')
def privacy():
    seo = get_seo_metadata(title="Privacy Policy")
    return render_template('privacy.html', seo=seo)

@main_bp.route('/terms')
def terms():
    seo = get_seo_metadata(title="Terms of Service")
    return render_template('terms.html', seo=seo)

@main_bp.route('/api/search')
def api_search():
    q = request.args.get('q', '').strip()
    results = ContentService.search(q)
    return jsonify(results)

@main_bp.route('/robots.txt')
def robots():
    response = make_response("User-agent: *\nDisallow:\nSitemap: https://altimetai.com/sitemap.xml")
    response.headers["Content-Type"] = "text/plain"
    return response

@main_bp.route('/sitemap.xml')
def sitemap():
    pages = []
    # Add static pages
    pages.append({"loc": url_for('main.index', _external=True), "lastmod": "2026-06-28", "changefreq": "daily", "priority": "1.0"})
    pages.append({"loc": url_for('main.services', _external=True), "lastmod": "2026-06-28", "changefreq": "weekly", "priority": "0.9"})
    pages.append({"loc": url_for('main.industries', _external=True), "lastmod": "2026-06-28", "changefreq": "weekly", "priority": "0.8"})
    pages.append({"loc": url_for('main.case_studies', _external=True), "lastmod": "2026-06-28", "changefreq": "weekly", "priority": "0.8"})
    pages.append({"loc": url_for('main.about', _external=True), "lastmod": "2026-06-28", "changefreq": "monthly", "priority": "0.7"})
    pages.append({"loc": url_for('main.blog', _external=True), "lastmod": "2026-06-28", "changefreq": "daily", "priority": "0.8"})
    pages.append({"loc": url_for('main.contact', _external=True), "lastmod": "2026-06-28", "changefreq": "monthly", "priority": "0.7"})
    pages.append({"loc": url_for('main.book_consultation', _external=True), "lastmod": "2026-06-28", "changefreq": "monthly", "priority": "0.9"})
    
    # Add dynamic pages
    for s in ContentService.get_services():
        pages.append({"loc": url_for('main.service_detail', slug=s['slug'], _external=True), "lastmod": "2026-06-28", "changefreq": "weekly", "priority": "0.80"})
    for ind in ContentService.get_industries():
        pages.append({"loc": url_for('main.industry_detail', slug=ind['slug'], _external=True), "lastmod": "2026-06-28", "changefreq": "weekly", "priority": "0.75"})
    for cs in ContentService.get_case_studies():
        pages.append({"loc": url_for('main.case_study_detail', slug=cs['slug'], _external=True), "lastmod": "2026-06-28", "changefreq": "weekly", "priority": "0.75"})
    for b in ContentService.get_blog_posts():
        pages.append({"loc": url_for('main.blog_detail', slug=b['slug'], _external=True), "lastmod": "2026-06-28", "changefreq": "monthly", "priority": "0.60"})
        
    sitemap_xml = render_template('sitemap_xml.html', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response
