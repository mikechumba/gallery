
$('.image-card').on('click', () => {
   $('.modal').fadeIn(1000)
})

$('.close').on('click', () => {
   $('.modal').fadeOut()
})


$('.selectfield').on('change', () => {
   (this).submit()
})