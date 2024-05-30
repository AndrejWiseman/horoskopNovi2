
window.addEventListener('load', () => {
    const spinner = document.getElementById('spinner');

    spinner.classList.add('loader-hidden');

    spinner.addEventListener('transitionend', () => {
        document.body.removeChild('spinner')
    })
})





// const spinner = document.getElementById("spinner")
// const list = document.getElementById('list')
//
// $.ajax({
//     type:'GET',
//     url:'http://127.0.0.1:8000/horoskop/vodolija/',
//     success: function(res){
//         setTimeout(() => {
//             spinner.classList.add('no-display')
//         }, 4000)
//     },
//     error: function(er){
//         console.log('Error')
//     }
// })
