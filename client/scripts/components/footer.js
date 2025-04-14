document.addEventListener("DOMContentLoaded", () => {
    fetch("./components/footer.html")
        .then(res => res.text())
        .then(data => {
            document.getElementById("footer").innerHTML = data;
        })
        .catch(err => console.error("Failed to load footer:", err));
});
