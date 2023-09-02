const openModalButton = document.getElementById("openModal");
const registerModal = document.getElementById("register1");
const closeButton = registerModal.querySelector(".close");

openModalButton.addEventListener("click", function() {
    registerModal.style.display = "block";
    registerModal.style.zIndex = "2";
    document.body.style.overflow = "hidden"; // Sayfanın kaydırmasını engelle
});

function closeModal() {
    registerModal.style.display = "none";
    document.body.style.overflow = "auto"; // Sayfanın kaydırmasını tekrar etkinleştir
}

registerModal.addEventListener("click", function(event) {
    if (event.target === registerModal || event.target === closeButton) {
        closeModal();
    }
});

document.addEventListener("click", function(event) {
    if (!registerModal.contains(event.target) && !openModalButton.contains(event.target)) {
        closeModal();
    }
});

// login icin
const openModalButtons = document.getElementById("openLogin");
const registerModals = document.getElementById("loginAna");
const closeButtons = registerModal.querySelector(".closes");

openModalButtons.addEventListener("click", function() {
  registerModals.style.display = "block";
  registerModals.style.zIndex = "2";
    document.body.style.overflow = "hidden"; // Sayfanın kaydırmasını engelle
});

function closeModals() {
  registerModals.style.display = "none";
    document.body.style.overflow = "auto"; // Sayfanın kaydırmasını tekrar etkinleştir
}

registerModals.addEventListener("click", function(event) {
    if (event.target === registerModals || event.target === closeButtons) {
        closeModals();
    }
});

document.addEventListener("click", function(event) {
    if (!registerModals.contains(event.target) && !openModalButtons.contains(event.target)) {
      closeModals();
    }
});



// slider1 icin 

const slides = document.querySelectorAll(".slide");
let currentIndex = 0;

function showSlide(index) {
    slides.forEach(slide => slide.classList.remove("active"));
    slides[index].classList.add("active");
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    showSlide(currentIndex);
}

showSlide(currentIndex);
setInterval(nextSlide, 2000); // Her 2 saniyede bir resim değiştir


const slides2 = document.querySelectorAll(".slide2");
let currentIndex2 = 0;

function showSlide2(index) {
    slides2.forEach(slide2r => slide2r.classList.remove("active"));
    slides2[index].classList.add("active"); // .active sınıfını ekle
}

function nextSlide2() {
    currentIndex2 = (currentIndex2 + 1) % slides2.length;
    showSlide2(currentIndex2);
}

showSlide2(currentIndex2);




