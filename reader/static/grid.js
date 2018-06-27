// namespace
window.semantic = {
  handler: {}
};

semantic.grid = {};

// ready event
semantic.grid.ready = function() {

  $('#all_checkbox.animation.checkbox')
    .checkbox({
      onChecked: function() {
        $('#example').addClass('animated');
      },
      onUnchecked: function() {
        $('#example').removeClass('animated');
      }
    })
  ;
  $('#finished_checkbox.animation.checkbox')
    .checkbox({
      onChecked: function() {
        $('#finished').addClass('animated');
      },
      onUnchecked: function() {
        $('#finished').removeClass('animated');
      }
    })
  ;

};


// attach ready event
$(document)
  .ready(semantic.grid.ready)
;