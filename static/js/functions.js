/*------------------------------------
	Theme Name: Minimag
	Start Date :
	End Date : 
	Last change: 
	Version: 1.0
	Assigned to:
	Primary use:
---------------------------------------*/
/*	

	+ Blog Masonry
	+ Responsive Caret*
	+ Expand Panel Resize*
	+ Sticky Menu*
	
	+ Document On Ready
		- Scrolling Navigation*
		- Set Sticky Menu*
		- Responsive Caret*
		- Expand Panel*
		- Collapse Panel*
		- Revolution Slider
		- Slider Carousel 4
		- Slider Section 6
		- Slider Section 7
		- Instagram Carousel
		- Trending Post
		- Related Post
		- Quick Contact Form*
	
	+ Window On Scroll
		- Set Sticky Menu
		
	+ Window On Resize
		- Expand Panel Resize
		
	+ Window On Load
		- Site Loader
		- Largest Post
		
*/

(function($) {

	"use strict"
	
	/* + Blog Masonry */
	function blog_masonry() {
		if($(".blog-masonry-list").length) {
			var $container = $(".blog-masonry-list");
			$container.isotope({
				layoutMode: 'masonry',
				percentPosition: true,				
				itemSelector: ".blog-masonry-box"
			});
		}
	}
	
	/* + Responsive Caret* */
	function menu_dropdown_open(){
		var width = $(window).width();
		if($(".ownavigation .navbar-nav li.ddl-active").length ) {
			if( width > 991 ) {
				$(".ownavigation .navbar-nav > li").removeClass("ddl-active");
				$(".ownavigation .navbar-nav li .dropdown-menu").removeAttr("style");
			}
		} else {
			$(".ownavigation .navbar-nav li .dropdown-menu").removeAttr("style");
		}
	}
	
	/* + Expand Panel Resize* */
	function panel_resize(){
		var width = $(window).width();
		if( width > 991 ) {
			if($(".header_s .slidepanel").length ) {
				$(".header_s .slidepanel").removeAttr("style");
			}
		}
	}

	/* + Sticky Menu* */
	function sticky_menu() {
		var menu_scroll = $("body").offset().top;
		var scroll_top = $(window).scrollTop();
		var height = $(window).height();
		var body_height = $("body").height();
		var header_height = $(".header-fix").height();
		var a = height + header_height + header_height;
		if( body_height > a  ){	
			if ( scroll_top > menu_scroll ) {
				$(".header-fix").addClass("fixed-top animated fadeInDown");
				$("body").css("padding-top",header_height);
			} else {
				$(".header-fix").removeClass("fixed-top animated fadeInDown"); 
				$("body").css("padding-top","0");
			}
		} else {
			$(".header-fix").removeClass("fixed-top animated fadeInDown"); 
			$("body").css("padding-top","0");
		}
	}
	
	/* + Document On Ready */
	$(document).on("ready", function() {

		/* - Scrolling Navigation* */
		var width	=	$(window).width();
		var height	=	$(window).height();
		
		/* - Set Sticky Menu* */
		if( $(".header-fix").length ) {
			sticky_menu();
		}
		
		$('.navbar-nav li a[href*="#"]:not([href="#"]), .site-logo a[href*="#"]:not([href="#"])').on("click", function(e) {
	
			var $anchor = $(this);
			
			$("html, body").stop().animate({ scrollTop: $($anchor.attr("href")).offset().top - 49 }, 1500, "easeInOutExpo");
			
			e.preventDefault();
		});

		/* - Responsive Caret* */
		$(".ddl-switch").on("click", function() {
			var li = $(this).parent();
			if ( li.hasClass("ddl-active") || li.find(".ddl-active").length !== 0 || li.find(".dropdown-menu").is(":visible") ) {
				li.removeClass("ddl-active");
				li.children().find(".ddl-active").removeClass("ddl-active");
				li.children(".dropdown-menu").slideUp();
			}
			else {
				li.addClass("ddl-active");
				li.children(".dropdown-menu").slideDown();
			}
		});
		
		/* - Expand Panel* */
		$( "[id*='slideit-']" ).each(function (index) { 
			index++;
			$("[id*='slideit-"+index+"']").on("click", function() {
				$("[id*='slidepanel-"+index+"']").slideDown(1000);
				$("header").animate({ scrollTop: 0 }, 1000);
			});
		});

		/* - Collapse Panel * */
		$( "[id*='closeit-']" ).each(function (index) {
			index++;			
			$("[id*='closeit-"+index+"']").on("click", function() {
				$("[id*='slidepanel-"+index+"']").slideUp("slow");			
				$("header").animate({ scrollTop: 0 }, 1000);
			});
		});
		
		/* Switch buttons from "Log In | Register" to "Close Panel" on click * */
		$( "[id*='toggle-']" ).each(function (index) { 
			index++;
			$("[id*='toggle-"+index+"'] a").on("click", function() {
				$("[id*='toggle-"+index+"'] a").toggle();
			});
		});		
		
		panel_resize();
		
		
		/* - Revolution Slider */
		if($("#mm-slider-1").length){
			var tpj=jQuery;
			var revapi9;
			if(tpj("#mm-slider-1").revolution == undefined){
				revslider_showDoubleJqueryError("#mm-slider-1");
			}else{
				revapi9 = tpj("#mm-slider-1").show().revolution({
					sliderType:"standard",
					sliderLayout:"fullwidth",
					dottedOverlay:"none",
					delay:9000,
					navigation: {
						onHoverStop:"off",
					},
					responsiveLevels:[1920,1200,768,480],
					visibilityLevels:[1920,1200,768,480],
					gridwidth:[1920,1200,768,480],
					gridheight:[600,425,320,250],
					lazyType:"none",
					shadow:0,
					spinner:"spinner0",
					stopLoop:"off",
					stopAfterLoops:-1,
					stopAtSlide:-1,
					shuffle:"off",
					autoHeight:"off",
					disableProgressBar:"on",
					hideThumbsOnMobile:"off",
					hideSliderAtLimit:0,
					hideCaptionAtLimit:0,
					hideAllCaptionAtLilmit:0,
					debugMode:false,
					fallbacks: {
						simplifyAll:"off",
						nextSlideOnWindowFocus:"off",
						disableFocusListener:false,
					}
				});
			}
		}
		/* - Slider Carousel 4 */
		if( $(".slider-carousel-4").length ) {
			$(".slider-carousel-4").owlCarousel({
				loop: true,
				margin: 4,
				nav: false,
				dots: false,
				autoplay: true,
				responsive:{
					0:{
						items: 1
					},
					477:{
						items: 2
					},
					768:{
						items: 3
					},
					992:{
						items: 4
					}
				}
			});
		}
		/* - Slider Carousel 5 */
		if( $(".slider-carousel-5").length ) {
			$(".slider-carousel-5").owlCarousel({
				loop: true,
				margin: 0,
				nav: false,
				dots: false,
				autoplay: true,
				responsive:{
					0:{
						items: 1
					}
				}
			});
		}
		
		/* - Slider Section 6 */
		if( $(".slider-section6").length ) {
			$(".slider-carousel-6").slick({
				centerMode: true,
				centerPadding: '250px',
				autoplay: true,
				slidesToShow: 2,
				responsive: [{
					breakpoint: 1366,
						settings: {
							arrows: false,
							centerMode: true,
							centerPadding: '200px',
							slidesToShow: 2
						}
					},{
					breakpoint: 1201,
						settings: {
							arrows: false,
							centerMode: true,
							centerPadding: '100px',
							slidesToShow: 2
						}
					},{
					breakpoint: 992,
						settings: {
							arrows: false,
							centerMode: true,
							centerPadding: '60px',
							slidesToShow: 2
						}
					},{
					breakpoint: 768,
						settings: {
							arrows: false,
							centerMode: true,
							centerPadding: '25px',
							slidesToShow: 2
						}
					},{
					breakpoint: 640,
						settings: {
							arrows: false,
							centerMode: true,
							centerPadding: '25px',
							slidesToShow: 1
						}
					},{
					breakpoint: 480,
						settings: {
						arrows: false,
						centerMode: true,
						centerPadding: '15px',
						slidesToShow: 1
					}
				}]
			});
		}
		
		/* - Slider Section 7 */
		if( $(".slider-section7").length ) {
			$(".slider-carousel-7").slick({
				centerMode: true,
				centerPadding: '373px',
				autoplay: true,
				slidesToShow: 1,
				responsive: [{
					breakpoint: 1600,
						settings: {
							arrows: false,
							centerMode: true,
							centerPadding: '200px',
							slidesToShow: 1
						}
					},{
					breakpoint: 1366,
						settings: {
							arrows: false,
							centerMode: true,
							centerPadding: '150px',
							slidesToShow: 1
						}
					},{
					breakpoint: 1201,
						settings: {
							arrows: false,
							centerMode: true,
							centerPadding: '100px',
							slidesToShow: 1
						}
					},{
					breakpoint: 992,
						settings: {
							arrows: false,
							centerMode: true,
							centerPadding: '60px',
							slidesToShow: 1
						}
					},{
					breakpoint: 768,
						settings: {
							arrows: false,
							centerMode: true,
							centerPadding: '25px',
							slidesToShow: 1
						}
					},{
					breakpoint: 640,
						settings: {
							arrows: false,
							centerMode: true,
							centerPadding: '25px',
							slidesToShow: 1
						}
					},{
					breakpoint: 480,
						settings: {
						arrows: false,
						centerMode: true,
						centerPadding: '15px',
						slidesToShow: 1
					}
				}]
			});
		}
		
		/* - Instagram Carousel */
		if( $(".instagram-carousel").length ) {
			$(".instagram-carousel").owlCarousel({
				loop: true,
				margin: 0,
				nav: false,
				dots: false,
				autoplay: true,
				responsive:{
					0:{
						items: 2
					},
					480:{
						items: 3
					},
					575:{
						items: 4
					},
					768:{
						items: 5
					},
					992:{
						items: 6
					}
				}
			});
		}
		
		/* - Trending Post */
		if( $(".trending-carousel").length ) {
			$(".trending-carousel").owlCarousel({
				loop: true,
				margin: 30,
				nav: false,
				dots: false,
				autoplay: true,
				responsive:{
					0:{
						items: 1
					},
					400:{
						items: 2
					},
					768:{
						items: 3
					},
					992:{
						items: 4
					}
				}
			});
		}
		/* - Related Post */
		if( $(".related-post-block").length ) {
			$(".related-post-block").owlCarousel({
				loop: true,
				margin: 30,
				nav: false,
				dots: false,
				autoplay: false,
				responsive:{
					0:{
						items: 2
					},
					480:{
						items: 2
					},
					575:{
						items: 3
					},
					768:{
						items: 2
					},
					992:{
						items: 4
					}
				}
			});
		}
		
		/* - Quick Contact Form* */
		$( "#btn_submit" ).on( "click", function(event) {
			event.preventDefault();
			var mydata = $("form").serialize();
			$.ajax({
				type: "POST",
				dataType: "json",
				url: "contact.php",
				data: mydata,
				success: function(data) {
					if( data["type"] == "error" ){
						$("#alert-msg").html(data["msg"]);
						$("#alert-msg").removeClass("alert-msg-success");
						$("#alert-msg").addClass("alert-msg-failure");
						$("#alert-msg").show();
					} else {
						$("#alert-msg").html(data["msg"]);
						$("#alert-msg").addClass("alert-msg-success");
						$("#alert-msg").removeClass("alert-msg-failure");
						$("#input_name").val("");
						$("#input_email").val("");
						$("#input_subject").val("");
						$("#textarea_message").val("");
						$("#alert-msg").show();
					}			
				},
				error: function(xhr, textStatus, errorThrown) {
					alert(textStatus);
				}
			});
		});
		
	});	/* - Document On Ready /- */
	
	/* + Window On Scroll */
	$(window).on("scroll",function() {
		/* - Set Sticky Menu* */
		if( $(".header-fix").length ) {
			sticky_menu();
		}
	});
	
	/* + Window On Resize */ 
	$( window ).on("resize",function() {
		var width	=	$(window).width();
		var height	=	$(window).height();
		
		sticky_menu();
		
		/* - Expand Panel Resize */
		panel_resize();
		menu_dropdown_open();
		blog_masonry();
	});
	
	/* + Window On Load */
	$(window).on("load",function() {
		/* - Site Loader* */
		if ( !$("html").is(".ie6, .ie7, .ie8") ) {
			$("#site-loader").delay(1000).fadeOut("slow");
		}
		else {
			$("#site-loader").css("display","none");
		}
		blog_masonry();
	});

})(jQuery);