const popup = document.querySelector("#popup-container");
const table = document.querySelector("#table");
const tableBtn = document.querySelector("#tableBtn");
const content = document.getElementById("content");
const search = document.querySelector("#search");
const searchBtn = document.querySelector("#searchBtn");

function showPopup(data) {
  popup.innerHTML = data;
  popup.style.display = "block";
}

function hidePopup() {
  popup.style.display = "none";
  document.removeEventListener("click", hidePopupOnClickOutside);
}

function hideTable() {
  table.style.display = "none";
  tableBtn.style.display = "block";
}

function hideSearch() {
  search.style.display = "none";
  searchBtn.style.display = "block";
}

function showTable() {
  table.style.display = "block";
  tableBtn.style.display = "none";
}

function showSerach() {
  search.style.display = "block";
  searchBtn.style.display = "none";
}

function hidePopupOnClickOutside(event) {
  if (!popup.contains(event.target)) {
    hidePopup();
  }
}

document.getElementById("btnCloseColorTab").addEventListener("click", () => {
  document.querySelector(".colorTab").style.display = "none";
  document.querySelector("#btnColorTab").style.display = "block";
});

document.getElementById("btnColorTab").addEventListener("click", () => {
  document.querySelector(".colorTab").style.display = "block";
  document.querySelector("#btnColorTab").style.display = "none";
});
