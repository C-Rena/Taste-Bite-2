document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.home-page-section-2 .card');
    let activeIndex = 0;
  
    function updateCards() {
      cards.forEach((card, index) => {
        card.classList.remove('center', 'side');
  
        if (index === activeIndex) {
          card.classList.add('center');
        } else {
          card.classList.add('side');
        }
      });
    }
  
    function rotateCards() {
      activeIndex = (activeIndex + 1) % cards.length; 
      updateCards();
    }
  
    updateCards();
    setInterval(rotateCards, 3000); 
  });
  
// #################################################

document.addEventListener('DOMContentLoaded', function () {
  const itemsPerPage = 4; 
  let currentPage = 1;

  const recipeItems = document.querySelectorAll('.recipe-item');
  const loadMoreButton = document.getElementById('loadMore');

  
  function showItems() {
      const start = (currentPage - 1) * itemsPerPage;
      const end = start + itemsPerPage;
      recipeItems.forEach((item, index) => {
          if (index >= start && index < end) {
              item.style.display = 'block';
          }
      });

     
      if (end >= recipeItems.length) {
          loadMoreButton.style.display = 'none';
      }
  }


  loadMoreButton.addEventListener('click', function (e) {
      e.preventDefault(); 
      currentPage++;
      showItems();
  });

  showItems();
});
