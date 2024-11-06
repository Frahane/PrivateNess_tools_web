$(document).ready(function() {
    // You can add interactivity here if needed
   // Toggle the scaled class on image click
   $('.repo-map').on('click', function() {
    $(this).toggleClass('scaled');
});
    console.log("Document is ready!");

    $(document).ready(function() {
        // Navigation toggle functionality
        $('.nav-toggle').click(function() {
            $(this).toggleClass('active');
            $('.nav-menu').slideToggle(300);
        });
    
        // Close menu when clicking outside
        $(document).click(function(event) {
            if (!$(event.target).closest('.quick-nav').length) {
                $('.nav-menu').slideUp(300);
                $('.nav-toggle').removeClass('active');
            }
        });
    
        // Handle responsive behavior
        $(window).resize(function() {
            if ($(window).width() > 768) {
                $('.nav-menu').show();
            } else {
                $('.nav-menu').hide();
                $('.nav-toggle').removeClass('active');
            }
        });
    });

});