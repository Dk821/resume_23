// disapper the mesage 
document.addEventListener("DOMContentLoaded", function () {
    const alertMessage = document.getElementById("alertMessage");
    if (alertMessage) {
        setTimeout(function () {
            alertMessage.style.display = "none";
        }, 5000); // 5000ms = 5 seconds
    }
});

// check the pass regx
document.addEventListener("DOMContentLoaded", function () {
    const passwordField = document.getElementById("floatingPassword");
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#()!%*?&])[A-Za-z\d@$#()!%*?&]{8,}$/;

    passwordField.addEventListener("input", function () {
        if (passwordRegex.test(passwordField.value)) {
            passwordField.classList.remove("invalid");
            passwordField.classList.add("valid");
        } else {
            passwordField.classList.remove("valid");
            passwordField.classList.add("invalid");
        }
    });
});

// check the email regx
document.addEventListener("DOMContentLoaded", function () {
    const passwordField = document.getElementById("floatingInput");
    const passwordRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/u;

    passwordField.addEventListener("input", function () {
        if (passwordRegex.test(passwordField.value)) {
            passwordField.classList.remove("invalid");
            passwordField.classList.add("valid");
        } else {
            passwordField.classList.remove("valid");
            passwordField.classList.add("invalid");
        }
    });
});

// eye function

function togglePasswordVisibility() {
    const passwordInput = document.getElementById("floatingPassword");
    const eyeIcon = document.querySelector(".eye-icon i");

    // Toggle password visibility
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIcon.classList.remove("bi-eye");
        eyeIcon.classList.add("bi-eye-slash");
    } else {
        passwordInput.type = "password";
        eyeIcon.classList.remove("bi-eye-slash");
        eyeIcon.classList.add("bi-eye");
    }
}