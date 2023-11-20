// function toggleLikeClass() {
//   var heartIcon = document.querySelector(".like-icon");
//   heartIcon.classList.toggle("liked");
// }

// function toggleLikeClass() {
//   const likeIcon = document.querySelector(".like-icon");
//   const isLiked = localStorage.getItem('isLiked') === 'true';

//   if (isLiked) {
//     likeIcon.classList.remove("liked");
//     localStorage.setItem('isLiked', 'false');
//   } else {
//     likeIcon.classList.add("liked");
//     localStorage.setItem('isLiked', 'true');
//   }
// }

function toggleLikeClass() {
  const likeIcon = document.querySelector(".like-icon");

  fetch('/like-toggle?is_liked=' + (likeIcon.classList.contains('liked') ? 'false' : 'true'))
    .then(response => response.json())
    .then(data => {
      if (data.isLiked) {
        likeIcon.classList.remove("liked");
      } else {
        likeIcon.classList.add("liked");
      }
    });
}
