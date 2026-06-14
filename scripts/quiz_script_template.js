
<script>
    const sectionId = "__SECTION_ID__";
    const correctAnswers = __CORRECT_ANSWERS__;
    const explanations = __EXPLANATIONS__;

    function submitQuiz() {
        let score = 0;
        for (let i = 1; i <= 10; i++) {
            const selected = document.querySelector("input[name=\"q" + i + "\"]:checked");
            const explanationEl = document.getElementById("q" + i + "-explanation");
            if (selected) {
                const selectedValue = selected.value;
                const correctValue = correctAnswers["q" + i];
                if (selectedValue === correctValue) {
                    score++;
                    explanationEl.innerHTML = '<span class="correct">对！</span> ' + explanations["q" + i];
                    selected.parentElement.classList.add("correct");
                } else {
                    explanationEl.innerHTML = '<span class="wrong">错！</span> ' + explanations["q" + i];
                    selected.parentElement.classList.add("incorrect");
                    const correctOption = document.querySelector("input[name=\"q" + i + "\"][value=\"" + correctValue + "\"]");
                    if (correctOption) correctOption.parentElement.classList.add("correct");
                }
            } else {
                explanationEl.innerHTML = '<span style="color:#999;">未作答</span> - ' + explanations["q" + i];
            }
            explanationEl.classList.add("show");
        }
        document.getElementById("scoreDisplay").textContent = score + "/10";
        document.getElementById("quizResult").classList.add("show");
        const quizResult = { sectionId: sectionId, score: score, total: 10, answers: {} };
        for (let i = 1; i <= 10; i++) {
            const selected = document.querySelector("input[name=\"q" + i + "\"]:checked");
            quizResult.answers["q" + i] = selected ? selected.value : null;
        }
        localStorage.setItem("quiz-" + sectionId, JSON.stringify(quizResult));
        document.getElementById("quizResult").scrollIntoView({ behavior: "smooth", block: "center" });
    }

    function resetQuiz() {
        for (let i = 1; i <= 10; i++) {
            const options = document.querySelectorAll("input[name=\"q" + i + "\"]");
            options.forEach(opt => {
                opt.checked = false;
                opt.parentElement.classList.remove("correct", "incorrect");
            });
            const explanationEl = document.getElementById("q" + i + "-explanation");
            explanationEl.classList.remove("show");
            explanationEl.innerHTML = "";
        }
        document.getElementById("quizResult").classList.remove("show");
        document.getElementById("scoreDisplay").textContent = "0/10";
    }

    function toggleSidebar() {
        document.body.classList.toggle("sidebar-open");
    }

    document.addEventListener("DOMContentLoaded", function() {
        const saved = localStorage.getItem("quiz-" + sectionId);
        if (saved) {
            const quizResult = JSON.parse(saved);
            for (let i = 1; i <= 10; i++) {
                const answer = quizResult.answers["q" + i];
                if (answer) {
                    const radio = document.querySelector("input[name=\"q" + i + "\"][value=\"" + answer + "\"]");
                    if (radio) radio.checked = true;
                }
            }
            document.getElementById("scoreDisplay").textContent = quizResult.score + "/10";
            document.getElementById("quizResult").classList.add("show");
        }
        if (window.innerWidth < 768) {
            const sidebarLinks = document.querySelectorAll(".sidebar a");
            sidebarLinks.forEach(link => {
                link.addEventListener("click", () => {
                    document.body.classList.remove("sidebar-open");
                });
            });
        }
    });
</script>
