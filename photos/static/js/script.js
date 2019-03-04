

$('.image-card').on('click', () => {
   let $id = $(this.event.currentTarget).attr('id');
   $('#image-'+$id).fadeIn(600);
})

$('.close').on('click', () => {
   $('.modal').fadeOut();
})

$('.selectfield').on('change', () => {
   (this).submit();
})


$('.fa-clipboard').on('click', () => {
   let $id = $(this.event.currentTarget).attr('id');
   let link = document.getElementById('url-'+$id);
   link.select();
   document.execCommand("copy");
   alert("Link has been copied! "+link);
})