$(document).ready(function() {
    // Toggle the scaled class on image click
    $('.repo-map').on('click', function() {
        $(this).toggleClass('scaled');
    });
    console.log("Document is ready!");

    // Navigation toggle functionality
    $('.nav-toggle').click(function(e) {
        e.stopPropagation(); // Prevent event bubbling
        $(this).toggleClass('active');
        
        const $menu = $('.nav-menu');
        const $quickNav = $('.quick-nav'); // Reference to the quick-nav element

        if ($menu.is(':visible')) {
            $menu.removeClass('showing').addClass('hiding');
            $quickNav.addClass('hidden'); // Add hidden class when hiding menu
            setTimeout(() => {
                $menu.hide().removeClass('hiding');
            }, 300);
        } else {
            $menu.show().addClass('showing');
            $quickNav.removeClass('hidden'); // Remove hidden class when showing menu
            setTimeout(() => {
                $menu.removeClass('showing');
            }, 300);
        }
    });

    // Close menu when clicking outside
    $(document).click(function(event) {
        if (!$(event.target).closest('.quick-nav').length) {
            const $menu = $('.nav-menu');
            const $toggle = $('.nav-toggle');
            const $quickNav = $('.quick-nav'); // Reference to the quick-nav element
            
            if ($menu.is(':visible')) {
                $menu.removeClass('showing').addClass('hiding');
                $toggle.removeClass('active');
                $quickNav.addClass('hidden'); // Add hidden class when hiding menu
                setTimeout(() => {
                    $menu.hide().removeClass('hiding');
                }, 300);
            }
        }
    });

    // Handle responsive behavior
    $(window).resize(function() {
        if ($(window).width() > 768) {
            $('.nav-menu').show().css('display', 'flex');
            $('.nav-toggle').removeClass('active');
            $('.quick-nav').removeClass('hidden'); // Ensure hidden class is removed on resize
        } else {
            $('.nav-menu').hide();
        }
    });

    // Prevent menu links from closing immediately on click
    $('.nav-menu a').click(function(e) {
        e.stopPropagation();
        if ($(window).width() <= 768) {
            setTimeout(() => {
                $('.nav-menu').hide();
                $('.nav-toggle').removeClass('active');
                $('.quick-nav').addClass('hidden'); // Add hidden class when hiding menu
            }, 300);
        }
    });
});