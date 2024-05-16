document.addEventListener('DOMContentLoaded', () => {

    const num1Input = document.getElementById("num1");
    const num2Input = document.getElementById("num2");
    const submitInput = document.getElementById("submit");

    const answerText = document.getElementById("answer");

    submitInput.onclick = () => {
        const num1 = parseInt(num1Input.value); 
        const num2 = parseInt(num2Input.value); 
        answerText.innerText = `Answer: ${num1 + num2}`;
    };
});