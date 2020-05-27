$(document).ready(function() {

    $(".owl-carousel").owlCarousel({
    
    autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:true,
    items : 8,
    itemsDesktop : [1199,3],
    itemsDesktopSmall : [979,3],
    center: false,
    nav:true,
    loop:true,
    responsive: {
      0:{ items:1 },
      600:{ items:3 },
      992:{ items:4 }
    }
    
    });
  
});