let currentPage = 1;

function toggleClass(e, toggleClassName) {
  if(e.className.includes(toggleClassName)) {
    e.className = e.className.replace(' ' + toggleClassName, '');
  } else {
    e.className += ' ' + toggleClassName;
  }
}

function movePage(e, page) {
  const character = document.getElementById('character');
  const thought = document.getElementById('thought')
  if (currentPage !== 0) {
    document.addEventListener('click', function(event) {
      if (event.target !== character) {
        character.style.display = 'none';
        thought.style.display = 'none';
      }
    })
  }

  if (page == currentPage) {
    currentPage+=2;
    toggleClass(e, "left-side");
    toggleClass(e.nextElementSibling, "left-side");
    
  }

  else if (page = currentPage - 1) {
    currentPage-=2;
    toggleClass(e, "left-side");
    toggleClass(e.previousElementSibling, "left-side");
  }

  
}


