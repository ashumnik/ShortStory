$(function() {


/*-------------------------------------------
Load Page
---------------------------------------------*/

	$('body').waitForImages({
		finished: function() {
				Website();
				$('body').jKit();
		},
		waitForAll: true
	});


/*-------------------------------------------
Ajax link page transitions
---------------------------------------------*/

	$("a.ajax-link").live("click", function(){
		$this = $(this);
		var link = $this.attr('href');
		var current_url = $(location).attr('href');

		if( link != current_url && link != '#' ) {
		$.ajax({
			url:link,
			processData:true,
			dataType:'html',
			success:function(data){
				document.title = $(data).filter('title').text();
				current_url = link;
        if (typeof history.pushState != 'undefined') history.pushState(data, 'Page', link);

          setTimeout(function(){
          $('#preloader').delay(50).fadeIn(600);
          $('html, body').delay(1000).animate({ scrollTop:  0  },1000);

					setTimeout(function(){

            $('#ajax-content').html($(data).filter('#ajax-content').html());
            $('#ajax-sidebar').html($(data).filter('#ajax-sidebar').html());

						$('body').waitForImages({
							finished: function() {
								Website();
								backLoading();
								$('.opacity-nav').delay(50).fadeOut(600);
              },
              waitForAll: true
						});
					},1000);
					},0);
			}
		});
    }
    return false;
	});

/*-------------------------------------------
Ajax Like button
---------------------------------------------*/

$('.like-form').submit(function(e){
	e.preventDefault()

	const story_id = $(this).attr('id')

  const likeText = $(`.like-btn${story_id}`).text()
	const trim = $.trim(likeText)

	const url = $(this).attr('action')

	const likes = $(`.like-btn${story_id}`).text()
	const trimCount = parseInt(likes)

	$.ajax({
		type: 'POST',
		url: url,
		data: {
			'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
			'story_id':story_id,
		},
		success: function(response) {
                        if(response.value === true) {
														$(`.like-btn${story_id}`).text(trimCount + 1 + ' нравится')
                        } else {
                            $(`.like-btn${story_id}`).text(trimCount - 1 + ' нравится')
                        }
											},
											error: function(response) {
												console.log('error', response)
											}
	})
});

/*-------------------------------------------
When you click back arrow
---------------------------------------------*/


function backLoading() {
    $(window).on("popstate", function () {
        $('body').fadeOut('slow',function(){
            location.reload();
        });
        $('body').fadeIn();
    });
}

/*-------------------------------------------
Load Page - next Open Site
---------------------------------------------*/

function Website() {
		CheckScripts();
		Masonry();
		$('body').jKit();
		backgroundmenu();
		setTimeout(function(){
			$(".preloader").fadeOut(500);
		},2000);
		setTimeout(function(){
			$('header').fadeIn();
		},500);
}


/*-------------------------------------------
Init and check list scripts
---------------------------------------------*/

function CheckScripts() {

  $(document).ready(function(){
    preloaderCheck();
    Typewriting();
    sidebarhero();
  });

}


/*-------------------------------------------
Masonry Check Script
---------------------------------------------*/

function Masonry() {
       var $container = $('.portfolio-grid');

       $container.imagesLoaded( function(){
         $container.masonry({
           itemSelector : 'li'
         });
       });
}


/*-------------------------------------------
Multi purpose init Background menu
---------------------------------------------*/

function backgroundmenu() {

  $(document).ready(function(){
     if($("#header-fade").length) {

         $(window).scroll(function(){
            if ($(this).scrollTop() > 10) {
                $('header').fadeOut();
            } else {
                $('header').fadeIn();
            }
        });
     }

     if($("#header-white").length) {

         $(window).scroll(function(){
            if ($(this).scrollTop() > 10) {
                $('header').css( "background", "white" );
                $('header .logo > a').css( "borderBottom", "0" );

            } else {
                $('header').css( "background", "none" );
            }
        });
     }


  });

}

/*-------------------------------------------
Typewriting init script
---------------------------------------------*/

function Typewriting() {


$(document).ready(function(){
	setTimeout( function(){
		if($("#site-type").length) {
        $(".typewrite span").typed({
            strings: ["strings ", "huings "],  //заменить для слов
            typeSpeed: 100,
            backDelay: 500,
            loop: false,
            contentType: 'html', // or text
            // defaults to false for infinite loop
            loopCount: false,
        });
    }
	}, 3000);
});
}


/*-------------------------------------------
Amazing Fade with scroll Sidebar
---------------------------------------------*/

function sidebarhero() {

  if($("#hero").length) {
    var fadeStart=100,fadeUntil=800,fading = $('#hero');

    $(window).bind('scroll', function(){
        var offset = $(document).scrollTop()
            ,opacity=0
        ;
        if( offset<=fadeStart ){
            opacity=1;
        }else if( offset<=fadeUntil ){
            opacity=1-offset/fadeUntil;
        }
        fading.css('opacity',opacity);
    });
  }
}


/*-------------------------------------------
Open Check Scription
---------------------------------------------*/

function OpenCheck() {
    setTimeout(function() {
        hidePreloader();
    }, 1000);
}


/*-------------------------------------------
Check Preloader
---------------------------------------------*/

function preloaderCheck() {
    showPreloader();
    $(window).load(function() {
        hidePreloader();
    });
}

/*-------------------------------------------
Functions Show / Hide Preloader
---------------------------------------------*/

function showPreloader() {
  $(".preloader").fadeIn("slow");
}

function hidePreloader() {
  $(".preloader").delay(2000).fadeOut("slow");
}


/*-------------------------------------------
Like button
---------------------------------------------*/

$(document).ready(function(){

    $('.like-button').click(function(){
        $(this).toggleClass('is-active');
    })

})


})//End
