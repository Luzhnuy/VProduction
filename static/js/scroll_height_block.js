const action = document.querySelector('.action')
let hidden = false;
window.addEventListener("scroll",()=> {
    if(window.scrollY > 0 && !hidden) {
        action.classList.add('hidden')
        hidden = true
    } else if(window.scrollY === 0 && hidden) {
        action.classList.remove('hidden');
        hidden = false
    }
})