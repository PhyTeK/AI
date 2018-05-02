function hide(id) {
      elm = document.getElementById(id);
      elm.style.display = 'none'
}

$(document).ready(function() {
       // Create the tooltips only on document load
        $('[id^=slickbox]').hide();
       // hides the slickbox as soon as the DOM is ready
       // (a little sooner than page load)

       // toggles the slickbox on clicking the noted link
        $('a#slick-toggle').click(function() {
            var $this = $(this);
            var x = $this.attr("name");

            // change the link text
                if ($('a#slick-toggle').text()=='show more info') {
                    $('a#slick-toggle').text('show less info');
                    }

                else {
                    $('a#slick-toggle').text('show more info');
                    }

            if (x) {
             $('#slickbox' + x ).toggle();
            }
            else {
             $('#slickbox').toggle();
            }
             return false;
        });

       // toggles. Use the name attribute (e.g.:toggleme) of a an <a> unit with class="toggle" to toggle a class of that name attribute
        $('a.toggle').click(function() {
            var $this = $(this);
            var x = $this.attr("name");
             $('.'+ x).toggle();
             return false;
        });

        $('.show-long').click(function(){
            $('.more-long').css('display', 'inline');
            $('.more-short').css('display', 'none');
        });
        $('.show-short').click(function(){
            $('.more-short').css('display', 'inline');
            $('.more-long').css('display', 'none');
        });

      });
