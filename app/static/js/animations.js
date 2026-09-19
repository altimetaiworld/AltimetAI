/* app/static/js/animations.js */

// Execute when DOM is ready
function initAnimations() {
  // 1. Hero Entrance Animations
  function triggerHeroEntrance() {
    if (typeof gsap === 'undefined') return;
    const tl = gsap.timeline();
    
    // Check elements
    if (document.querySelector('.hero-title')) {
      tl.from('.hero-title', 
        { y: 24, opacity: 0, duration: 0.7, ease: "power3.out" }
      );
    }
    
    if (document.querySelector('.hero-desc')) {
      tl.from('.hero-desc', 
        { y: 16, opacity: 0, duration: 0.6, ease: "power3.out" }, 
        "-=0.4"
      );
    }
    
    if (document.querySelector('.hero-ctas')) {
      tl.from('.hero-ctas', 
        { y: 12, opacity: 0, duration: 0.5, ease: "power3.out" }, 
        "-=0.3"
      );
    }
    
    if (document.querySelector('.hero-dashboard')) {
      tl.from('.hero-dashboard', 
        { scale: 0.98, opacity: 0, y: 20, duration: 0.8, ease: "power2.out" }, 
        "-=0.3"
      );
    }
  }

  // Invoke hero entrance immediately
  triggerHeroEntrance();
  
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
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initAnimations);
} else {
  initAnimations();
}
