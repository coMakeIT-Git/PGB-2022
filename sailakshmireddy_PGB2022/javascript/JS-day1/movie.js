let reviews_container = document.getElementById("reviewsContainer")
let movie_name = document.getElementById("titleInput")
let movie_review = document.getElementById("reviewTextarea")

function onAddReview() {
    let movietitle = movie_name.value
    let moviereview = movie_review.value
    if (movietitle ==="") {
        alert("Please enter a Movie Title")
        return;
    }
    if (moviereview ==="") {
        alert("Please enter a Movie Review")
        return;
    }
    let movieE = document.createElement("h1")
    movieE.textContent = "Movie Title: " + movietitle
    movieE.classList.add("movieE")
    reviews_container.appendChild(movieE)

    let reviewE = document.createElement("p")
    reviewE.textContent = "Review: " + moviereview
    reviewE.classList.add("movieE")
    reviews_container.appendChild(reviewE)

    let hr = document.createElement("hr")
    reviews_container.appendChild(hr)

    movie_name.value = ""
    movie_review.value = ""

}