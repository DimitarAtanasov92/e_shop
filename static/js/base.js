let imageUrls = [
      "static/js/pictures/IMG_8495-2.jpg",
      "static/js/pictures/IMG_8528.jpg",
      "static/js/pictures/IMG_8564.jpg",
      "static/js/pictures/IMG_8577.jpg",
        ];
let imageIndex = 0;
let sliderImage = document.getElementById('img1');
 setInterval(() => {
  imageIndex = (imageIndex + 1) % imageUrls.length;
  sliderImage.src = imageUrls[imageIndex];
}, 2000);
 let sliderImage2 = document.getElementById('img2');
 setInterval(() => {
  imageIndex = (imageIndex + 1) % imageUrls.length;
  sliderImage2.src = imageUrls[imageIndex];
}, 2000);