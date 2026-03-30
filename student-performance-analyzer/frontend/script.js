// LOGIN FUNCTION
function login() {
    let user = document.getElementById("username").value;
    let pass = document.getElementById("password").value;

    if (user === "" || pass === "") {
        alert("Please enter username and password");
        return;
    }

    alert("Login Successful");
    window.location.href = "dashboard.html";
}

// SIGNUP FUNCTION
function signup() {
    let user = document.getElementById("newUser").value;
    let pass = document.getElementById("newPass").value;

    if (user === "" || pass === "") {
        alert("Please fill all fields");
        return;
    }

    alert("Signup Successful");
    window.location.href = "index.html";
}

// ANALYSIS FUNCTION
function analyze() {
    let cgpa = parseFloat(document.getElementById("cgpa").value);
    let attendance = parseFloat(document.getElementById("attendance").value);
    let coding = parseFloat(document.getElementById("coding").value);
    let internships = parseInt(document.getElementById("internships").value);
    let projects = parseInt(document.getElementById("projects").value);
    let certifications = parseInt(document.getElementById("certifications").value);
    let backlogs = parseInt(document.getElementById("backlogs").value);

    if (isNaN(cgpa) || isNaN(attendance) || isNaN(coding)) {
        alert("Please fill all fields correctly");
        return;
    }

    // Placement Probability Logic
    let score = (cgpa * 10) + (attendance * 0.3) + coding +
                (internships * 5) + (projects * 5) +
                (certifications * 3) - (backlogs * 10);

    let probability = Math.min(100, Math.max(0, score / 2));

    let placement = probability > 60 ? "Placed ✅" : "Not Placed ❌";

    // Academic Risk
    let risk = (cgpa < 6 || attendance < 75 || backlogs > 0)
        ? "High Risk ⚠️"
        : "Low Risk ✅";

    // Skill Gaps
    let gaps = [];

    if (coding < 60) gaps.push("Coding");
    if (internships === 0) gaps.push("Industry Exposure");
    if (projects < 2) gaps.push("Projects");
    if (certifications < 1) gaps.push("Certifications");

    if (gaps.length === 0) gaps.push("No major gaps 🎉");

    // Store results
    localStorage.setItem("placement", placement);
    localStorage.setItem("probability", probability.toFixed(2));
    localStorage.setItem("risk", risk);
    localStorage.setItem("gaps", gaps.join(", "));

    window.location.href = "result.html";
}

// DISPLAY RESULT
window.onload = function () {
    let resultBox = document.getElementById("resultText");

    if (resultBox) {
        resultBox.innerHTML =
            "Placement: " + localStorage.getItem("placement") + "<br><br>" +
            "Probability: " + localStorage.getItem("probability") + "%<br><br>" +
            "Academic Risk: " + localStorage.getItem("risk") + "<br><br>" +
            "Skill Gaps: " + localStorage.getItem("gaps");
    }
};

// BACK BUTTON
function goBack() {
    window.location.href = "dashboard.html";
}