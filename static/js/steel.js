$(document).ready(function () {

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.back-to-top-steel').addClass('show');
        } else {
            $('.back-to-top-steel').removeClass('show');
        }
    });

    $('.back-to-top-steel').click(function (e) {
        e.preventDefault();
        $('html, body').animate({ scrollTop: 0 }, 600);
    });

    // Testimonial carousel
    if ($('.testimonial-carousel').length) {
        $('.testimonial-carousel').owlCarousel({
            loop: true,
            margin: 20,
            autoplay: true,
            autoplayTimeout: 5000,
            smartSpeed: 800,
            dots: true,
            nav: false,
            responsive: {
                0:    { items: 1 },
                768:  { items: 2 },
                1024: { items: 3 }
            }
        });
    }

    // Smooth scroll for anchor links
    $('a[href^="#"]').on('click', function (e) {
        var target = $(this.getAttribute('href'));
        if (target.length) {
            e.preventDefault();
            $('html, body').animate({ scrollTop: target.offset().top - 80 }, 600);
        }
    });

});
