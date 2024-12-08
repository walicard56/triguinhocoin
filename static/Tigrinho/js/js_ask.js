document.addEventListener('DOMContentLoaded', function() {
    const faqs = document.querySelectorAll('.faq');

    faqs.forEach(faq => {
        faq.addEventListener('click', () => {
            faq.classList.toggle('active');
            const answer = faq.querySelector('.answer');
            const toggle = faq.querySelector('.toggle');
            if (faq.classList.contains('active')) {
                answer.style.display = 'block';
                toggle.textContent = '-';
            } else {
                answer.style.display = 'none';
                toggle.textContent = '+';
            }
        });
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('.carousel');
    const partners = document.querySelector('.partners');
    const prevBtn = document.querySelector('.carousel-btn.prev');
    const nextBtn = document.querySelector('.carousel-btn.next');

    let currentIndex = 0;
    const partnerCount = document.querySelectorAll('.partner').length;
    const partnerWidth = document.querySelector('.partner').offsetWidth + 20; // Width + gap

    // Move carousel to the desired index
    const updateCarousel = () => {
        const offset = -currentIndex * partnerWidth;
        carousel.style.transform = `translateX(${offset}px)`;
    };

    // Event listener for next button
    nextBtn.addEventListener('click', () => {
        if (currentIndex < partnerCount - 1) {
            currentIndex++;
            updateCarousel();
        }
    });

    // Event listener for previous button
    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateCarousel();
        }
    });

    // Ensure carousel resets on window resize
    window.addEventListener('resize', () => {
        updateCarousel();
    });
});
