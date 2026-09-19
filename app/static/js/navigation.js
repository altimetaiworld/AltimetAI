/* app/static/js/navigation.js */

document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('header');
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileMenuIconOpen = mobileMenuBtn?.querySelector('.menu-icon-open');
  const mobileMenuIconClose = mobileMenuBtn?.querySelector('.menu-icon-close');
  
  // 1. Sticky Navigation Scroll Handler
  const handleScroll = () => {
    if (window.scrollY > 20) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }
  };
  
  window.addEventListener('scroll', handleScroll);
  handleScroll(); // Trigger immediately to check position on refresh
  
  // 2. Mobile Nav Hamburger Toggle
  const toggleMobileMenu = () => {
    if (!mobileMenu) return;
    const isExpanded = mobileMenu.classList.contains('hidden');
    
    if (isExpanded) {
      mobileMenu.classList.remove('hidden');
      // Animate slide-down
      gsap.fromTo(mobileMenu, { y: -20, opacity: 0 }, { y: 0, opacity: 1, duration: 0.3, ease: "power2.out" });
      mobileMenuIconOpen?.classList.add('hidden');
      mobileMenuIconClose?.classList.remove('hidden');
      document.body.style.overflow = 'hidden'; // Lock background scrolling
    } else {
      gsap.to(mobileMenu, {
        y: -20,
        opacity: 0,
        duration: 0.2,
        ease: "power2.in",
        onComplete: () => {
          mobileMenu.classList.add('hidden');
        }
      });
      mobileMenuIconOpen?.classList.remove('hidden');
      mobileMenuIconClose?.classList.add('hidden');
      document.body.style.overflow = ''; // Unlock background
    }
  };
  
  mobileMenuBtn?.addEventListener('click', toggleMobileMenu);
  
  // Close mobile menu on clicking a link
  const mobileLinks = mobileMenu?.querySelectorAll('a');
  mobileLinks?.forEach(link => {
    link.addEventListener('click', () => {
      if (!mobileMenu.classList.contains('hidden')) {
        toggleMobileMenu();
      }
    });
  });
  
  // 3. Highlight Current Route
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link-item');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath.startsWith(href) && href !== '/')) {
      link.classList.add('text-indigo-600', 'dark:text-indigo-400');
      link.classList.remove('text-gray-600', 'dark:text-gray-300');
    }
  });
});
