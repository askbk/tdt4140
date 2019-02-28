document.getElementById("preview-image").style.display = "block";
document.getElementById("id_image").onchange = function() {
    const reader = new FileReader();

    reader.onload = e => {
        document.getElementById("preview-image").src = e.target.result;
    };

    reader.readAsDataURL(this.files[0]);
}
