/* app/static/js/faq.js */

document.addEventListener('DOMContentLoaded', () => {
  const faqItems = document.querySelectorAll('.faq-accordion-item');
  
  faqItems.forEach(item => {
    const header = item.querySelector('.faq-accordion-header');
    const content = item.querySelector('.faq-accordion-content');
    const icon = item.querySelector('.faq-accordion-icon');
    
    header?.addEventListener('click', () => {
      const isOpen = content.classList.contains('open');
      
      // Close all other accordions first (optional, but creates a cleaner layout)
      faqItems.forEach(otherItem => {
        const otherContent = otherItem.querySelector('.faq-accordion-content');
        const otherIcon = otherItem.querySelector('.faq-accordion-icon');
        if (otherContent && otherContent !== content) {
          otherContent.classList.remove('open');
          otherContent.style.maxHeight = null;
          if (otherIcon) {
            gsap.to(otherIcon, { rotation: 0, duration: 0.25 });
          }
        }
      });
      
      // Toggle current accordion
      if (isOpen) {
        content.classList.remove('open');
        content.style.maxHeight = null;
        if (icon) {
          gsap.to(icon, { rotation: 0, duration: 0.25 });
        }
      } else {
        content.classList.add('open');
        content.style.maxHeight = content.scrollHeight + "px";
        if (icon) {
          gsap.to(icon, { rotation: 45, duration: 0.25 }); // rotate plus sign to x
        }
      }
    });
  });
});
