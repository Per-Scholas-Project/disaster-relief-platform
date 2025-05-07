const container = document.querySelector('.partners__logos-container');
const slides = document.querySelector('.logos-slides');

if (container && slides && !container.querySelector('.logos-slides + .logos-slides')) {
    const copy = slides.cloneNode(true);
    container.appendChild(copy);
}
