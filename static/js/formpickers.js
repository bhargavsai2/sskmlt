(function($) {
  'use strict';
  if ($("#timepicker-example").length) {
    $('#timepicker-example').datetimepicker({
      format: 'LT'
    });
  }
  if ($(".color-picker").length) {
    $('.color-picker').asColorPicker();
  }
  if ($("#datepicker-popup,#datepicker-popup1,#datepicker-popup2").length) {
    $('#datepicker-popup,#datepicker-popup1').datepicker({
       dateFormat: 'yy-mm-dd',
      enableOnReadonly: true,
      todayHighlight: true,
    });
  }
  if ($("#datepicker-popup2").length) {
   $('#datepicker-popup2').datepicker({
       format: 'yyyy-mm-dd',
     
    });
   /*$('#datepicker-popup2').datepicker();
    $( "#datepicker-popup2" ).datepicker( "option", "format", 'dd.mm.yy' ); */
  }
  if ($("#inline-datepicker").length) {
    $('#inline-datepicker').datepicker({
      enableOnReadonly: true,
      todayHighlight: true,
    });
  }
  if ($(".datepicker-autoclose").length) {
    $('.datepicker-autoclose').datepicker({
      autoclose: true
    });
  }
  if ($('input[name="date-range"]').length) {
    $('input[name="date-range"]').daterangepicker();
  }
  if ($('input[name="date-time-range"]').length) {
    $('input[name="date-time-range"]').daterangepicker({
      timePicker: true,
      timePickerIncrement: 30,
      locale: {
        format: 'MM/DD/YYYY h:mm A'
      }
    });
  }
})(jQuery);