const checkPassword = (password, validatePassword) => {
    if (password.length < 8)
        return false;

    if (password !== validatePassword)
        return false;

    return true;
}

document.addEventListener('DOMContentLoaded', () => {

    const validatePassword = document.getElementById('validate-password');
    const submitButton = document.getElementById('submit-button');
    const password = document.getElementById('password');

    submitButton.disabled = true;

    validatePassword.onkeyup = () => {
        if (checkPassword(password.value, validatePassword.value)) {
            validatePassword.style.border = "1px solid green";
            submitButton.disabled = false;
        } else {
            validatePassword.style.border = "1px solid red";
            submitButton.disabled = true;
        }
    };

});
