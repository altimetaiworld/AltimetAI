# app/__init__.py
from flask import Flask, render_template
from config import Config
from datetime import datetime

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Configure logs directory and files rotating handlers
    import os
    import logging
    from logging.handlers import RotatingFileHandler
    
    if not os.path.exists('logs'):
        try:
            os.makedirs('logs')
        except OSError:
            pass
            
    log_level = logging.DEBUG if app.config.get('DEBUG', True) else logging.INFO
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )
    
    # File Handler
    try:
        file_handler = RotatingFileHandler('logs/app.log', maxBytes=1024*1024*10, backupCount=5)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(log_level)
        app.logger.addHandler(file_handler)
    except Exception:
        pass
        
    # Stream Handler (Stdout)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(log_level)
    app.logger.addHandler(stream_handler)
    
    app.logger.setLevel(log_level)
    app.logger.info("Altimet AI Logger Initialized: Output configured to terminal and logs/app.log")
    
    # Import routes blueprint and register it
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    # Context Processor for sharing common parameters across pages
    @app.context_processor
    def inject_global_data():
        return {
            'year': datetime.utcnow().year,
            'site_name': app.config.get('SITE_NAME'),
            'site_domain': app.config.get('SITE_DOMAIN')
        }
        
    # Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        from app.utils import get_seo_metadata
        seo = get_seo_metadata(title="404 Page Not Found")
        return render_template('404.html', seo=seo), 404
        
    @app.errorhandler(500)
    def internal_server_error(e):
        from app.utils import get_seo_metadata
        seo = get_seo_metadata(title="500 Internal Server Error")
        return render_template('404.html', error_msg="Internal Server Error", seo=seo), 500
        
    return app
