# Altimet AI - Enterprise AI Consulting & Products Website

This is a premium, production-ready enterprise SaaS-style website for **Altimet AI** built using Flask, Python, Jinja2, Tailwind CSS, GSAP, and Vanilla JS.

The project is structured to establish trust with mid-market and enterprise buyers by highlighting measurable business outcomes, clear system architectures, and professional copy, positioning Altimet AI as a leader in **Enterprise AI Consulting, AI Copilots & Agentic Automation**.

## Tech Stack

- **Backend**: Python 3.10+, Flask, python-dotenv
- **Frontend / Styling**: Jinja2, Tailwind CSS v3 (dynamic config)
- **Animations / Interactivity**: GSAP 3 (ScrollTrigger, Custom cursor, Timelines), Vanilla JS, HTMX (asynchronous form validation)

## Getting Started (Local Run)

1. **Verify Python**:
   Ensure you have Python 3.10+ installed.

2. **Setup Environment**:
   Initialize and activate a virtual environment, then install dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # source .venv/bin/activate  # On Unix/Mac
   pip install -r requirements.txt
   ```

3. **Configure Settings**:
   The local configurations are pre-defined in `.env`. Update variables as needed for production specs.

4. **Launch Server**:
   Run the Flask server:
   ```bash
   python app.py
   ```
   The application will be accessible at: [http://localhost:5000](http://localhost:5000).

## Project Structure

```
/project-root
├── app.py                # App runner entrypoint
├── requirements.txt      # Dependency lists
├── config.py             # Configuration properties
├── README.md             # Guide documentation
├── .env                  # Development environment configuration
├── app/
│   ├── __init__.py       # Application Factory setup
│   ├── routes.py         # Views routing blueprinted controllers
│   ├── forms.py          # Corporate validations
│   ├── services.py       # Data copy provider
│   ├── utils.py          # Dynamic SEO/JSON-LD schema tools
│   ├── static/
│   │   ├── css/
│   │   │   ├── main.css        # Variables, font links, cursors, custom selection styles
│   │   │   ├── animations.css  # mesh blob animations, keyframes, logo animations
│   │   │   └── components.css  # glass panels, inputs, faq accordions, custom button settings
│   │   └── js/
│   │       ├── app.js          # Theme switcher, command palette fuzzy index matching
│   │       ├── animations.js   # GSAP scrolling reveals, mouse coordinates mapping
│   │       ├── navigation.js   # responsive mobile toggles, scrolling navigation headers
│   │       ├── counters.js     # numbers rollup animations
│   │       └── faq.js          # sliding FAQs transitions
│   └── templates/
│       ├── base.html           # main layout wrapping CDNs and common overlays
│       ├── index.html          # homepage structures
│       ├── services.html       # list of all capabilities
│       ├── services-detail.html# dynamic detail display
│       ├── industries.html     # industry grids
│       ├── industries-detail.html # industry solutions details
│       ├── case-studies.html   # ROI lists
│       ├── case-studies-detail.html # case study challenge/architecture
│       ├── blog.html           # insights search indexing
│       ├── blog-detail.html    # single post display
│       ├── about.html          # mission statement
│       ├── contact.html        # corporate messaging form
│       ├── book-consultation.html # consultation schedulers
│       ├── 404.html            # error overlay
│       ├── privacy.html        # privacy policy page
│       ├── terms.html          # terms of service page
│       └── components/         # reusable blocks
│           ├── navbar.html     # menu lists
│           ├── footer.html     # footer maps
│           ├── hero.html       # landing showcase
│           ├── faq.html        # accordion panels
│           ├── testimonials.html # client reviews
│           ├── cta.html        # consultation banner
│           └── architecture.html # SVG deployment layout
```

## Features

- **Dark Mode**: Persistent preference toggles.
- **Custom Cursor Follower**: Magnetic interactive coordinates pointer.
- **Command Palette**: `Ctrl+K` searchable fuzzy matches indexing.
- **Dynamic Forms**: Submits validation queries in-place using HTMX hooks.
- **Structured Data**: Automatically injects JSON-LD tags into templates for SEO crawlers.
