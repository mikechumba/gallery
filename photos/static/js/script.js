

$('.image-card').on('click', () => {
   let $id = $(this.event.currentTarget).attr('id');
   let $src = $(this.event.currentTarget).attr('src');
   $('#image-'+$id).fadeIn(600);
})

$('.close').on('click', () => {
   $('.modal').fadeOut();
})

$('.selectfield').on('change', () => {
   (this).submit();
})


$('.clipboard').on('click', () => {
   var $temp = $("<input>");
   $("body").append($temp);
   $temp.val($(element).text()).select();
   document.execCommand("copy");
   $temp.remove();
   $('.alert-copied').show()
})