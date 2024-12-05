// Star rating functionality for review form
let stars = document.getElementsByClassName("rating-star");

// Initialize stars based on pre-filled rating value
let ratingField = document.getElementsByClassName("rating-field")[0];
let initialRating = parseInt(ratingField?.value || 0);
for (let j = 0; j < stars.length; j++) {
    if (j < initialRating) {
        stars[j].classList.add("rating-star-selected");
    }
}

// Loop through stars
for (let i = 0; i < stars.length; i++) {
    // Attach click event for rating select
    stars[i].addEventListener("click", function (e) {
        e.preventDefault(); // Prevent form submission on click

        // Get selected rating
        let selectedStar = parseInt(this.getAttribute("data-star"));

        // Set the hidden input value
        if (ratingField) {
            ratingField.value = selectedStar;
        }

        // Highlight selected stars and remove highlight from others
        for (let j = 0; j < stars.length; j++) {
            if (j < selectedStar) {
                stars[j].classList.add("rating-star-selected");
            } else {
                stars[j].classList.remove("rating-star-selected");
            }
        }
    });

    // Optional: Attach hover effect to preview rating
    stars[i].addEventListener("mouseover", function () {
        let hoverStar = parseInt(this.getAttribute("data-star"));
        for (let j = 0; j < stars.length; j++) {
            if (j < hoverStar) {
                stars[j].classList.add("rating-star-hover");
            } else {
                stars[j].classList.remove("rating-star-hover");
            }
        }
    });

    // Remove hover effect when mouse leaves
    stars[i].addEventListener("mouseout", function () {
        for (let j = 0; j < stars.length; j++) {
            stars[j].classList.remove("rating-star-hover");
        }
    });
}