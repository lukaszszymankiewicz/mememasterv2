const maxPage = 25;
const prevBtn = document.getElementById('prevButton');
const nextBtn = document.getElementById('nextButton');
const container = document.getElementById('imageContainer');

let memes;

async function loadMemes(pageChange) {

  try {
    const response = await fetch('memes.json');

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    memes = await response.json();
    
    let currentPage = parseInt(sessionStorage.getItem('currentPage')) || 0;
    let newPage = 0;
    let requestedPage = currentPage + pageChange; 

    if (requestedPage > 0 && requestedPage < maxPage) {
        newPage = requestedPage;
    }

    sessionStorage.setItem('currentPage', newPage);

    container.innerHTML = "";

    memes[newPage].forEach(url => {
      const img = document.createElement('img');
      img.src = url;
      img.className = "img-responsive";
      container.appendChild(img);
    });
  } 
  catch (error) {
    console.error('No memes for you buddy...', error);
  }
}

loadMemes(0);

nextBtn.addEventListener('click', () => { loadMemes(1); });
prevBtn.addEventListener('click', () => { loadMemes(-1); });
