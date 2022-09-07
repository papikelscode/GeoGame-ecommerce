// Gets the Mobile Nav icon by its ID
let bars = document.getElementById('bars');

// Gets the Mobile Nav container
let mobileMenu = document.getElementById('mobileMenu');

// Displays the Mobile Nav when clicked and changes the Nav Icon from three bars to an 'X'
bars.addEventListener('click', function(){
  mobileMenu.classList.toggle('show');
  bars.classList.toggle('fa-times');
});