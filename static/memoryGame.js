// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
  // Get the <p> element containing the numbers
  var numbersEl = document.getElementById('numbers');

  // Hide the element after 0.7 seconds
  setTimeout(function() {
    numbersEl.style.display = 'none';
  }, 700);
});
