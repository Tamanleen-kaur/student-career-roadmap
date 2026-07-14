
const submitButton = document.getElementById("submit");
console.log(submitButton)
if (submitButton) {

    submitButton.addEventListener("click", function () {
        

        let careerCount = {
            fullstack: 0,
            datascience: 0,
            uiux: 0,
            cybersecurity: 0
        };

        const selectedAnswers = document.querySelectorAll('input[type="radio"]:checked');
        console.log("selected:",selectedAnswers.length)
        if (selectedAnswers.length < 7) {
            alert("Please answer all questions before submitting.");
            return;
}

        selectedAnswers.forEach(answer => {
            careerCount[answer.value]++;
        });

        let recommendedCareer = "";
        let maxCount = 0;

        for (let career in careerCount) {
            if (careerCount[career] > maxCount) {
                maxCount = careerCount[career];
                recommendedCareer = career;
            }
        }

        let careerName = "";

        if (recommendedCareer === "fullstack") {
            careerName = "Full Stack Developer";
        } else if (recommendedCareer === "datascience") {
            careerName = "Data Scientist";
        } else if (recommendedCareer === "uiux") {
            careerName = "UI/UX Designer";
        } else if (recommendedCareer === "cybersecurity") {
            careerName = "Cyber Security Analyst";
        }

        document.getElementById("quiz-card-result").innerHTML =
            "<h2>🎉 Quiz Result</h2>" +
            "<p><strong>Your Recommended Career:</strong> " + careerName + "</p>";

    });

}