document.addEventListener("DOMContentLoaded", function () {
    const toggleSwitch = document.querySelector('#dark-mode-switch');
    const body = document.body;

    // Check localStorage for dark mode preference
    if (localStorage.getItem('darkMode') === 'enabled') {
        body.classList.add('dark-mode');
        toggleSwitch.checked = true; // Make sure the toggle switch is checked
    }

    // Toggle dark mode and update localStorage
    toggleSwitch.addEventListener('change', function () {
        if (toggleSwitch.checked) {
            body.classList.add('dark-mode'); // Enable dark mode
            localStorage.setItem('darkMode', 'enabled'); // Save to localStorage
        } else {
            body.classList.remove('dark-mode'); // Disable dark mode
            localStorage.setItem('darkMode', 'disabled'); // Save to localStorage
        }
    });
});




// Rating System
const stars = document.querySelectorAll('.star');
const ratingResult = document.getElementById('rating-result');
let currentRating = 0;

if (stars.length > 0 && ratingResult) {
    stars.forEach(star => {
        star.addEventListener('click', () => {
            currentRating = star.getAttribute('data-value');
            ratingResult.textContent = currentRating;
            updateStarRating(currentRating);
        });

        star.addEventListener('mouseover', () => {
            const hoverValue = star.getAttribute('data-value');
            updateStarRating(hoverValue, true);
        });

        star.addEventListener('mouseout', () => {
            updateStarRating(currentRating);
        });
    });

    function updateStarRating(rating, isHover = false) {
        stars.forEach(star => {
            if (parseInt(star.getAttribute('data-value')) <= rating) {
                star.classList.add(isHover ? 'hover' : 'selected');
            } else {
                star.classList.remove('hover', 'selected');
            }
        });
    }
}

// Social Media Sharing
const memeImage = document.getElementById('meme-image');
const facebookBtn = document.getElementById('share-facebook');
const twitterBtn = document.getElementById('share-twitter');
const whatsappBtn = document.getElementById('share-whatsapp');

if (memeImage && facebookBtn && twitterBtn && whatsappBtn) {
    // Ensure the meme image has a valid src
    const memeURL = memeImage.src;

    
        // Update the href attributes for each social media share button
        facebookBtn.href = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(memeURL)}`;
        twitterBtn.href = `https://twitter.com/intent/tweet?url=${encodeURIComponent(memeURL)}&text=Check out this hilarious meme!`;
        whatsappBtn.href = `https://api.whatsapp.com/send?text=Check out this hilarious meme: ${encodeURIComponent(memeURL)}`;
}




// Download Meme Button
const downloadBtn = document.getElementById('download-btn');

if (downloadBtn && memeImage) {
    downloadBtn.addEventListener('click', () => {
        const link = document.createElement('a');
        link.href = memeImage.src;
        link.download = 'meme.png';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });
}

function filterCategory() {
    var category = document.getElementById('category').value;
    var chosenCategoryText = "Chosen category: " + category;

    // Display chosen category above meme
    document.getElementById('chosen-category').textContent = chosenCategoryText;

    // Optional: Make an AJAX request to filter memes based on the category selected
    // For example, you could use the selected category to filter memes from your database.
}

function filterCategory() {
    var category = document.getElementById('category').value;

    // Redirect to the same page with the selected category as a query parameter
    window.location.href = "?category=" + category;
}




