const btn = document.getElementById('btn');
const main = document.getElementById('main');
const btnOpen = document.getElementById('btnOpen');

btn.addEventListener('click', ()  => {
    main.classList.toggle('hidden');
})

btnOpen.addEventListener('click', ()  => {
    main.classList.toggle('hidden');
})