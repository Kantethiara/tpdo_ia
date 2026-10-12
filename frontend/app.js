const questionInput = document.getElementById("question");
const askButton = document.getElementById("askButton");
const answerBox = document.getElementById("answer");
const statusBox = document.getElementById("status");
const exampleButtons = document.querySelectorAll(".example");


async function askQuestion() {

    const question = questionInput.value.trim();

    if (!question) {
        answerBox.textContent = "Please enter a question.";
        return;
    }

    askButton.disabled = true;
    statusBox.textContent = "Loading...";
    statusBox.classList.remove("error");

    try {
        const response = await fetch("http://127.0.0.1:800/api/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Display the answer in answerBox
        answerBox.textContent = data.answer || "No answer received.";

    } catch (error) 
    {
        console.error(error);
        statusBox.textContent = "Request failed.";
        statusBox.classList.add("error");

    } finally 
    {
        askButton.disabled = false;
    }
}


askButton.addEventListener("click", askQuestion);


questionInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        askQuestion();
    }
});


exampleButtons.forEach((button) => {
    button.addEventListener("click", () => {
        questionInput.value = button.dataset.question;
        questionInput.focus();
    });
});
