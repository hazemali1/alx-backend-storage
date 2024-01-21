jQuery(document).ready(function(){

    function PEPFU(){
        var pepFU = jQuery(window).innerHeight() - jQuery('footer').height() - jQuery('#wpadminbar').height();
        jQuery('body > .content').css('min-height', pepFU);   
    }
    PEPFU()

    /*add caret to dropdown menu*/
        /*open on hover or click*/
        jQuery('nav .menu-item-has-children > a').each( function(){
            jQuery(this).append('<span class="caret"></span>')
        })
        jQuery('nav .menu-item-has-children').each( function(){
            jQuery(this).append('<span class="thereCaret"><img src="/wp-content/uploads/2020/04/right-arrow-grey-chevron.png" title="" alt=""/></span>')
        })
        /*open on hover or click*/
        if (jQuery(window).innerWidth() > 1199) {
            jQuery('nav .menu-item-has-children').hover(function(){
                jQuery(this).find('ul:first').stop().slideDown(300);
            }, function(){
                jQuery(this).find('ul:first').stop().slideUp(200);
            });
        }else{
            jQuery('nav .menu-item-has-children .thereCaret').click(function(){
                jQuery(this).parent().find('ul:first').toggleClass('openMenu');
                jQuery(this).toggleClass('active');
            });
        }
        
        if(jQuery(window).innerWidth() > 600){
            var topHP = 0 + jQuery('#wpadminbar').height();    
        }else{
            var topHP = 0; 
        }

        /*Height header*/
        function HH(){
            var heiHeader = jQuery('.fixing').innerHeight();
            jQuery('header').height(heiHeader);            
        }
        HH();
        jQuery('.searchOpen').click(function(){ 
            jQuery('header .headerSearch').stop().slideDown(300);; 
        });
        jQuery('.headerSearch').click(function(){
            setTimeout(function(){
                jQuery("#resortpro_sw_lodging_unit").focus();
            }, 200);             
        }) 

        /*cacl height and position*/
        function FiH(){
            if(window.innerWidth > 600){
                var tpFH = jQuery('.fixing').innerHeight() + jQuery('#wpadminbar').height();    
            }else{
                var chCL = jQuery('.fixing').hasClass('activated');
                if(chCL == false){
                    var tpFH = jQuery('.fixing').height() + jQuery('#wpadminbar').height();    
                }else{
                    var tpFH = jQuery('.fixing').height();
                }
            }
            var formHei = jQuery(window).innerHeight() - tpFH;
            jQuery('header nav').css({'max-height': formHei});                               
        }
        FiH() 

        jQuery(window).scroll(function(){
            /*header fixed pos*/                              
                if(jQuery(window).scrollTop() > 100){
                    jQuery('.fixing').addClass('activated').css({'top': topHP});
                    FiH();
                }else{
                    jQuery('.fixing').removeClass('activated').attr('style', '');
                    FiH(); 
                }
        });/*End Scroll Function*/
        jQuery(window).resize(function(){
            HH();
            FiH();
        });

        /*Trigger Focus*/
        jQuery('.headerSearch').click(function(){
            setTimeout(function(){
                jQuery("#resortpro_sw_lodging_unit").focus();
            }, 200);             
        });

        jQuery('.modal_btn').click(function(e) {
            e.preventDefault();
            jQuery('.modal_search').fadeIn(300);
        });

        jQuery('.modal_search .close_modal').click(function() {
            jQuery('.modal_search').fadeOut(300);
        });
        
        jQuery('.for-widget-toggle').click(function(ev){
             ev.preventDefault(); 
            jQuery('.modal_search').slideToggle(300);
        });
        
    jQuery('#resortpro_sw_bed').change(function() {
        this.form.submit();
    });         

    /*Mail Togling*/
    jQuery('.mobileMenuClose').click(function() {
        jQuery('.CustomMobileMenu').removeClass('open');
    })   
    emailClick = 1
    jQuery('header .mail').click(function() {
        if(emailClick == 1){
            jQuery('.CustomMobileMenu').addClass('open');    
        }
        
    })    
    jQuery(document).mouseup(function (e){
    	var div = jQuery(".CustomMobileMenu");
        var hzCL = jQuery('.CustomMobileMenu').hasClass('open');
    	if (!div.is(e.target) && div.has(e.target).length === 0) {            
            if(hzCL == true){
                jQuery('.CustomMobileMenu').removeClass('open');
                emailClick = 0;     
            }else{
                emailClick = 1;
            }
    	}            
    });
    var header_h = jQuery('header').innerHeight() + jQuery('#wpadminbar').height();
    jQuery(".CustomMobileMenu").css('max-height', 'calc(100vh - '+header_h+'px)');

    if(window.innerWidth < 992){
        jQuery('.footer-links.footer-block h3, footer .center-menu.footer-block h3').on('click', function () {
            jQuery(this).next('ul').slideToggle('slow');
            jQuery(this).toggleClass('openLinks');
        });
    }   
    
     jQuery('#top-property-management').click(function(ev){
       ev.preventDefault();
       jQuery('html, body').animate({scrollTop:0}, 500); 
    });
    

    
     
});/*End Document Ready*/




