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

        // TODO 4:
        // Send a POST request to /api/ask
        // with JSON:
        //
        // {
        //     "question": question
        
        const response = await fetch("http://127.0.0.1:800/api/ask", {
            method: "POST",
            headers: {
                "content.type": "application/json"
            },

            // Convert the response to JSON

            body: JSON.stringify({ question })
        });
        data = await response.json();
        



        // and display data.answer in answerBox.

        const data = null;

        answerBox.textContent = "TODO: display the answer";

    } catch (error) {

        console.error(error);
        statusBox.textContent = "Request failed.";
        statusBox.classList.add("error");

    } finally {

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
