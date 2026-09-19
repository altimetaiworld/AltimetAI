/* app/static/js/counters.js */

document.addEventListener('DOMContentLoaded', () => {
  // If ScrollTrigger is not present, render static values
  if (typeof ScrollTrigger === 'undefined' || typeof gsap === 'undefined') return;
  
  const counters = document.querySelectorAll('.stat-counter-val');
  
  counters.forEach(counter => {
    const rawVal = counter.getAttribute('data-target'); // e.g. "80", "15", "99.4", "-65"
    if (!rawVal) return;
    
    // Parse numeric characters vs non-numeric characters
    const numericPart = parseFloat(rawVal.replace(/[^\d.-]/g, ''));
    const suffix = rawVal.replace(/[\d.-]/g, ''); // %, x, ms, etc.
    const isDecimal = rawVal.includes('.');
    
    const obj = { val: 0 };
    
    gsap.fromTo(obj, 
      { val: 0 },
      {
        val: numericPart,
        duration: 1.5,
        ease: "power2.out",
        scrollTrigger: {
          trigger: counter,
          start: "top 90%",
          toggleActions: "play none none none"
        },
        onUpdate: () => {
          if (isDecimal) {
            counter.textContent = obj.val.toFixed(1) + suffix;
          } else {
            counter.textContent = Math.floor(obj.val) + suffix;
          }
        }
      }
    );
  });
});
