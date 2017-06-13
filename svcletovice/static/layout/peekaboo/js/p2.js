/*jQuery.noConflict();*/
jQuery(document).ready(function($){ 
		

/*===================================================================================*/
/*	Superfish - http://users.tpg.com.au/j_birch/plugins/superfish/
/*===================================================================================*/

		$("ul.sf-menu").supersubs({ 
			minWidth:    10,   // minimum width of sub-menus in em units 
			maxWidth:    45,   // maximum width of sub-menus in em units 
			extraWidth:  1     // extra width can ensure lines don't sometimes turn over 
							   // due to slight rounding differences and font-family 
		}).superfish({
			delay:			300,
			dropShadows:    false
		});  // call supersubs first, then superfish, so that subs are 
						 // not display:none when measuring. Call before initialising 
						 // containing tabs for same reason. 
	
/*===================================================================================*/
/*	ColorBox
/*===================================================================================*/
	$(".video_modal").colorbox({iframe:true, innerWidth:"50%", innerHeight:"50%"});
	$("a[rel='cb-image'], a[rel='cb-thumb'], .cb-single, .cb").colorbox({transition:"fade"});
	
/*===================================================================================*/
/*	Scroll to Top
/*===================================================================================*/
	$('#toTop').click(function() {
		$('#content-wrapper').animate({scrollTop:0},600);
	});	
	
/*-----------------------------------------------------------------------------------*/
/* Tabs
/*-----------------------------------------------------------------------------------*/
	if($().tabs) {
		$(".tabs").tabs({ 
			fx: { opacity: 'toggle', duration: 150} 
		});		
	};
	
/*-----------------------------------------------------------------------------------*/
/* Features
/*-----------------------------------------------------------------------------------*/	
	if($().tabs) {
		$('.features .nav a').click( function (e) {
			e.preventDefault();
		});
		$(".features").tabs({ 
			fx: { opacity: 'toggle', duration: 150} 
		});
	}

/*-----------------------------------------------------------------------------------*/
/* Toggle
/*-----------------------------------------------------------------------------------*/

	$(".toggle_inner").hide(); //Hide on load

	$("h4.toggler").click(function(){
	$(this).toggleClass("active").next().slideToggle();
	return false; //Prevent the browser jump to the link anchor
	});
	
	
/*-----------------------------------------------------------------------------------*/
/* Accordion
/*-----------------------------------------------------------------------------------*/

	//Set default open/close settings
	$('.acc_inner').hide(); //Hide/close all containers
	$('.acc_toggler:first').addClass('active').next().show();
	
	//On Click
	$('.acc_toggler').click(function(){
		if( $(this).next().is(':hidden') ) { 
			$('.acc_toggler').removeClass('active').next().slideUp(); 
			$(this).toggleClass('active').next().slideDown(); 
		}
		return false; 
	});
	
/*-----------------------------------------------------------------------------------*/
/* Tooltip
/*-----------------------------------------------------------------------------------*/

	$(function(){
		$(".tooltip").tipTip({maxWidth: 'auto', edgeOffset: 10 });
	});
	
/*===================================================================================*/
/*	Tiny Carousel
/*===================================================================================*/
	if ($().tinycarousel) {
		$('#quickmenu').tinycarousel({ 
			axis: 'y',
			display: 3, 
			duration: 500
		});
	};

/*===================================================================================*/
/*	Isotope
/*===================================================================================*/
	
	if ($().isotope) {

		$(function(){
		  
			var $container = $('#module-wrapper '); 
			
			$container.isotope({
			itemSelector : '.module'
			});
			
			
			var $optionSets = $('#filter-bar-container #filter-bar'),  
			  $optionLinks = $optionSets.find('a'); 
			
			$optionLinks.click(function(){
				var $this = $(this);
				// don't proceed if already selected
				if ( $this.hasClass('selected') ) {
				  return false;
				}
				var $optionSet = $this.parents('#filter-bar');
				$optionSet.find('.selected').removeClass('selected');
				$this.addClass('selected');
			
				// make option object dynamically, i.e. { filter: '.my-filter-class' }
				var options = {},
					key = $optionSet.attr('data-option-key'),
					value = $this.attr('data-option-value');
				// parse 'false' as false boolean
				value = value === 'false' ? false : value;
				options[ key ] = value;
				if ( key === 'layoutMode' && typeof changeLayoutMode === 'function' ) {
				  // changes in layout modes need extra logic
				  changeLayoutMode( $this, options )
				} else {
				  // otherwise, apply new options
				  $container.isotope( options );
				}
				
				return false;
			});
			  
		});
	
	};
	
	
});

