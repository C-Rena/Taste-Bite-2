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



