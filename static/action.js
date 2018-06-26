 /*
    1.Make the page can have the correct response, such as the dropdown element
    2.Get the elements to be rendered ahead of time
    */
  var all_book;
  $(document)
    .ready(function() {
      $('.ui.menu .ui.dropdown').dropdown({
        on: 'hover'
      });
      $('.ui.menu a.item')
        .on('click', function() {
          $(this)
            .addClass('active')
            .siblings()
            .removeClass('active')
          ;
          var tab = $(this).attr('data-tab');
          $('.ui.tab').each(function(i){
            if($(this).attr('data-tab') == tab){
              $(this)
                .addClass('active')
                .siblings()
                .removeClass('active')
            }
          });
        })
      ;
    })
  ;