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
});

document.addEventListener('DOMContentLoaded', function() {
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
                        recipeDiv.textContent = recipe.recipe_name;
                        recipeDiv.style.cursor = 'pointer';  

                       
                        recipeDiv.addEventListener('click', function() {
                            window.location.href = `/recipe_detail/${recipe.id}`; 
                        });

                        resultsDiv.appendChild(recipeDiv);
                    });
                } else {
                    resultsDiv.innerHTML = '<div>Result not found.</div>';
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                resultsDiv.innerHTML = '<div>Error fetching results.</div>';
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
                    console.error('Error fetching data:', error);
                });
            }
        }
    });
});

