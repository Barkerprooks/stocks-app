document.addEventListener('DOMContentLoaded', () => {

    // HTML Tags
    const passwordErrorText = document.getElementById("password-error");
    const validateErrorText = document.getElementById("validate-error");
    
    // User input
    const passwordInput = document.getElementById('password');
    const validatePasswordInput = document.getElementById('validate-password');

    // submit form
    const submitButton = document.getElementById('submit-button');

    submitButton.disabled = true;

    const passwordLength = 8;

    // When the password field is being typed in
    passwordInput.onkeyup = () => {
        let password = passwordInput.value;

        if (password.length >= passwordLength) {
            passwordInput.style.border = "1px solid green";
            passwordErrorText.innerText = "";
        } else {
            passwordInput.style.border = "1px solid red";
            passwordErrorText.innerText = `password must be ${passwordLength} characters long`;
            submitButton.disabled = true;
        }
    };

    validatePasswordInput.onkeyup = () => {
        let password = passwordInput.value;
        let validatePassword = validatePasswordInput.value;

        if (password.length >= passwordLength && password == validatePassword) {
            validatePasswordInput.style.border = "1px solid green";
            validateErrorText.innerText = "";
            submitButton.disabled = false;
        } else {
            validatePasswordInput.style.border = "1px solid red";
            validateErrorText.innerText = "passwords do not match";
            submitButton.disabled = true;
        }
    }; 
});