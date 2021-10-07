$(function() {
    $('.showSingle').click(function() {
      $('.targetDiv').not('#div' + $(this).attr('target')).hide();
      $('#div' + $(this).attr('target')).toggle();
    });
});