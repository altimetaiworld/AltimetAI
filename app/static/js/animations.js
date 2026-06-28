/* app/static/js/animations.js */

// Wait until page assets loaded
window.addEventListener('load', () => {
  // 1. Loading Screen dismissal
  const loader = document.getElementById('loader-overlay');
  if (loader) {
    gsap.to(loader, {
      opacity: 0,
      duration: 0.5,
      ease: "power2.out",
      onComplete: () => {
        loader.style.visibility = 'hidden';
        triggerHeroEntrance();
      }
    });
  } else {
    triggerHeroEntrance();
  }
  
  // 2. Custom Cursor Follower using GSAP (Only on desktop size)
  if (window.innerWidth > 1024) {
    const cursor = document.querySelector('.custom-cursor');
    const glow = document.querySelector('.custom-cursor-glow');
    
    if (cursor && glow) {
      // Setup position setter helpers
      const setCursorX = gsap.quickTo(cursor, "x", { duration: 0.1, ease: "power2.out" });
      const setCursorY = gsap.quickTo(cursor, "y", { duration: 0.1, ease: "power2.out" });
      const setGlowX = gsap.quickTo(glow, "x", { duration: 0.4, ease: "power2.out" });
      const setGlowY = gsap.quickTo(glow, "y", { duration: 0.4, ease: "power2.out" });
      
      window.addEventListener('mousemove', (e) => {
        setCursorX(e.clientX);
        setCursorY(e.clientY);
        setGlowX(e.clientX);
        setGlowY(e.clientY);
      });
      
      // Make cursor expand and highlight on hoverable items
      const interactiveEls = document.querySelectorAll('a, button, [role="button"], input, select, textarea, .hover-trigger');
      interactiveEls.forEach(el => {
        el.addEventListener('mouseenter', () => {
          gsap.to(cursor, {
            scale: 2.2,
            backgroundColor: 'rgba(79, 70, 229, 0.15)',
            borderColor: 'transparent',
            duration: 0.2
          });
        });
        el.addEventListener('mouseleave', () => {
          gsap.to(cursor, {
            scale: 1,
            backgroundColor: 'transparent',
            borderColor: '#4F46E5',
            duration: 0.2
          });
        });
      });
    }
  }
  
  // 3. Hero Entrance Animations Timeline
  function triggerHeroEntrance() {
    const tl = gsap.timeline();
    
    // Check elements
    if (document.querySelector('.hero-title')) {
      tl.fromTo('.hero-title', 
        { y: 30, opacity: 0 }, 
        { y: 0, opacity: 1, duration: 0.8, ease: "power3.out" }
      );
    }
    
    if (document.querySelector('.hero-desc')) {
      tl.fromTo('.hero-desc', 
        { y: 20, opacity: 0 }, 
        { y: 0, opacity: 1, duration: 0.6, ease: "power3.out" }, 
        "-=0.5"
      );
    }
    
    if (document.querySelector('.hero-ctas')) {
      tl.fromTo('.hero-ctas', 
        { y: 15, opacity: 0 }, 
        { y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }, 
        "-=0.4"
      );
    }
    
    if (document.querySelector('.hero-dashboard')) {
      tl.fromTo('.hero-dashboard', 
        { scale: 0.96, opacity: 0, y: 30 }, 
        { scale: 1, opacity: 1, y: 0, duration: 1.0, ease: "power2.out" }, 
        "-=0.3"
      );
    }
  }
  
  // 4. Scroll Reveal Animations (ScrollTrigger)
  if (typeof ScrollTrigger !== 'undefined') {
    // Register scrolltrigger plugin
    gsap.registerPlugin(ScrollTrigger);
    
    // Batch reveal elements
    const revealSections = document.querySelectorAll('.reveal-on-scroll');
    revealSections.forEach(section => {
      gsap.fromTo(section, 
        { opacity: 0, y: 40 },
        {
          opacity: 1,
          y: 0,
          duration: 0.8,
          ease: "power2.out",
          scrollTrigger: {
            trigger: section,
            start: "top 85%",
            toggleActions: "play none none none"
          }
        }
      );
    });
    
    // Stagger reveal grid cards
    const cardGrids = document.querySelectorAll('.stagger-cards-grid');
    cardGrids.forEach(grid => {
      const cards = grid.querySelectorAll('.stagger-card-item');
      if (cards.length > 0) {
        gsap.fromTo(cards, 
          { opacity: 0, y: 30 },
          {
            opacity: 1,
            y: 0,
            duration: 0.6,
            stagger: 0.1,
            ease: "power2.out",
            scrollTrigger: {
              trigger: grid,
              start: "top 80%"
            }
          }
        );
      }
    });
    
    // Left-Right Split Reveals
    const splitReveals = document.querySelectorAll('.split-reveal-trigger');
    splitReveals.forEach(trigger => {
      const left = trigger.querySelector('.split-reveal-left');
      const right = trigger.querySelector('.split-reveal-right');
      
      if (left) {
        gsap.fromTo(left, { opacity: 0, x: -30 }, {
          opacity: 1, x: 0, duration: 0.7, ease: "power2.out",
          scrollTrigger: { trigger: trigger, start: "top 80%" }
        });
      }
      if (right) {
        gsap.fromTo(right, { opacity: 0, x: 30 }, {
          opacity: 1, x: 0, duration: 0.7, ease: "power2.out",
          scrollTrigger: { trigger: trigger, start: "top 80%" }
        });
      }
    });
  }
  
  // 5. Back to Top Button Actions
  const backToTopBtn = document.getElementById('back-to-top');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        backToTopBtn.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-4');
      } else {
        backToTopBtn.classList.add('opacity-0', 'pointer-events-none', 'translate-y-4');
      }
    });
    
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
});
