const searchIcon = document.getElementById('search');
const searchDiv = document.getElementById('search_div');
const searchInput = document.getElementById('s_input');
const navLinks = document.getElementById('nav-links');

searchIcon.addEventListener('click', () => {
    if (searchDiv.style.display === 'none' || searchDiv.style.display === '') {
        navLinks.style.display = 'none';
        searchDiv.style.display = 'block';
        searchInput.focus();
    } else {
        navLinks.style.display = 'flex';
        searchDiv.style.display = 'none';
    }
});document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('s_input');
    const resultsDiv = document.getElementById('results');

    searchInput.addEventListener('input', function() {
        const keyword = searchInput.value.trim();  

        if (keyword.length > 0) {
            fetch(`/recipes/?keyword=${keyword}`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                resultsDiv.innerHTML = ''; 
                resultsDiv.style.display = 'block'; 

                if (data.recipes.length > 0) {
                    data.recipes.forEach(recipe => {
                       
                        const recipeDiv = document.createElement('div');
                        recipeDiv.classList.add('recipe-card');
                        recipeDiv.style.cursor = 'pointer';  

                   
                        const recipeImg = document.createElement('img');
                        recipeImg.src = recipe.image; 
                        recipeImg.classList.add('recipe-image');

                      
                        const recipeName = document.createElement('div');
                        recipeName.textContent = recipe.recipe_name;
                        recipeName.classList.add('recipe-name');

                        recipeDiv.addEventListener('click', function() {
                            window.location.href = `/recipe_detail/${recipe.id}`; 
                        });

                        recipeDiv.appendChild(recipeImg);
                        recipeDiv.appendChild(recipeName);
                        resultsDiv.appendChild(recipeDiv);
                    });
                } else {
                    resultsDiv.innerHTML = '<div>No results found...</div>';
                }
            })
            .catch(error => {
                console.error('Veri getirme hatası:', error);
                resultsDiv.innerHTML = '<div>An error occurred while fetching results.</div>';
            });
        } else {
            resultsDiv.innerHTML = ''; 
            resultsDiv.style.display = 'none';  
        }
    });

    searchInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();  
            const keyword = searchInput.value.trim();  

            if (keyword.length > 0) {
                fetch(`/recipes/?keyword=${keyword}`, {
                    method: 'GET',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.recipes.length > 0) {
                        window.location.href = `/recipe_detail/${data.recipes[0].id}`;
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }
        }
    });
});




  document.addEventListener('DOMContentLoaded', function() {
    const dropbtn = document.querySelector('.dropbtn');
    const dropdownContent = document.querySelector('.dropdown-contentt');

    dropbtn.addEventListener('click', function() {
      dropdownContent.classList.toggle('show'); 
    });
  });




document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('mobile-menu-icon');
    const navDropdownLinks = document.getElementById('nav-dropdown-links');

    menuIcon.addEventListener('click', function() {
        navDropdownLinks.classList.toggle('show');
    });
});




const moonIcon = document.getElementById('moonIcon');
const sunIcon = document.getElementById('sunIcon');
const darkModeToggle = document.querySelector('.dark_light');

darkModeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');

 
    if (document.body.classList.contains('dark-mode')) {
        moonIcon.style.display = 'none';
        sunIcon.style.display = 'inline';
        localStorage.setItem('theme', 'dark'); 
    } else {
        moonIcon.style.display = 'inline';
        sunIcon.style.display = 'none';
        localStorage.setItem('theme', 'light');
    }
});


window.addEventListener('load', () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        moonIcon.style.display = 'none';
        sunIcon.style.display = 'inline';
    } else {
        moonIcon.style.display = 'inline';
        sunIcon.style.display = 'none';
    }
});










