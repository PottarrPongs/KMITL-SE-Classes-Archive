const studentName = document.getElementById("student_name");
const studentDOB = document.getElementById("date_of_birth");
const studentID = document.getElementById("student_id");
const studentDOA = document.getElementById("date_of_admission");
const studentDOG = document.getElementById("date_of_graduation");
const studentDeg = document.getElementById("degree");
const studentMaj = document.getElementById("major");
const contentBody = document.getElementById("content_body");


function handleFileSelect(event) {
    const file = event.target.files[0]; // Get the first selected file
    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            const jsonString = e.target.result;
            const jsonData = JSON.parse(jsonString); // Parse the JSON string into a JavaScript object
            render(jsonData);
        };
        reader.onerror = function(e) {
            const error = e.target.error;
            console.error("Error parsing JSON file:", error);
        }
        reader.readAsText(file); // Read the file content as text
    }
}

function render (jsonData) {
    studentName.value = jsonData.student_name;
    studentDOB.value = jsonData.date_of_birth;
    studentID.value = jsonData.student_id;
    studentDOA.value = jsonData.date_of_admission;
    studentDOG.value = jsonData.date_of_graduation;
    studentDeg.value = jsonData.degree;
    studentMaj.value = jsonData.major;

    let accNumerator = 0.0;
    let accDenominator = 0.0;
    for (const yr in jsonData.credit) {
        const yrHeaderRow = document.createElement("tr");
        const yrHeaderCol0 = document.createElement("td");
        const yrHeaderCol2 = document.createElement("td");
        const yrHeaderCol1 = document.createElement("td");
        yrHeaderCol0.innerText = yr;
        yrHeaderRow.appendChild(yrHeaderCol0);
        yrHeaderRow.appendChild(yrHeaderCol1);
        yrHeaderRow.appendChild(yrHeaderCol2);
        contentBody.appendChild(yrHeaderRow);

        for (const sem in jsonData.credit[yr]) {
            const semRow = document.createElement("tr");
            const semCol0 = document.createElement("td");
            const semCol1 = document.createElement("td");
            const semCol2 = document.createElement("td");
            semCol0.innerText = sem;
            semRow.appendChild(semCol0);
            semRow.appendChild(semCol1);
            semRow.appendChild(semCol2);
            contentBody.appendChild(semRow);

            let semNumerator = 0.0;
            let semDenominator = 0.0;
            for (const subIdx in jsonData.credit[yr][sem]) {
                const subjRow = document.createElement("tr");
                let subjName = "";
                let temp = 0.0;
                for (const subjData in jsonData.credit[yr][sem][subIdx]) {
                    if (subjData === "name") {
                        subjName = jsonData.credit[yr][sem][subIdx][subjData];
                    } else if (subjData === "subject_id") {
                        subjName = `${jsonData.credit[yr][sem][subIdx][subjData]} ${subjName}`;
                        const subjDataCol = document.createElement("td");
                        subjDataCol.style = "text-align: left;"
                        subjDataCol.innerText = subjName;
                        subjRow.appendChild(subjDataCol);
                        contentBody.appendChild(subjDataCol);
                    } else {
                        if (subjData === "credit") {
                            temp += parseFloat(jsonData.credit[yr][sem][subIdx][subjData]);
                            semDenominator += parseFloat(jsonData.credit[yr][sem][subIdx][subjData]);
                            accDenominator += parseFloat(jsonData.credit[yr][sem][subIdx][subjData]);
                        } else {
                            temp *= findGrade(jsonData.credit[yr][sem][subIdx][subjData]);
                            semNumerator += temp;
                            accNumerator += temp;
                        }
                        const subjDataCol = document.createElement("td");
                        subjDataCol.innerText = jsonData.credit[yr][sem][subIdx][subjData];
                        subjRow.appendChild(subjDataCol);
                        contentBody.appendChild(subjDataCol);
                    }
                }
                contentBody.appendChild(subjRow);
            }
            const gps = semNumerator/semDenominator;
            const gpa = accNumerator/accDenominator;
            const gradeSummary = `GPS: ${gps.toFixed(2)} &emsp; GPA: ${gpa.toFixed(2)}`;
            const gradeSummaryRow = document.createElement("tr");
            const gradeSummayCol0 = document.createElement("td");
            const gradeSummayCol1 = document.createElement("td");
            const gradeSummayCol2 = document.createElement("td");
            gradeSummayCol0.innerHTML = gradeSummary;
            gradeSummaryRow.appendChild(gradeSummayCol0);
            gradeSummaryRow.appendChild(gradeSummayCol1);
            gradeSummaryRow.appendChild(gradeSummayCol2);
            contentBody.appendChild(gradeSummaryRow);
        }
    }
}

function findGrade(gradeLetter) {
    if (gradeLetter === "A") {
        return 4;
    } else if (gradeLetter === "B+") {
        return 3.5;
    } else if (gradeLetter === "B") {
        return 3.0;
    } else if (gradeLetter === "C+") {
        return 2.5;
    } else if (gradeLetter === "C") {
        return 2.0;
    } else if (gradeLetter === "D+") {
        return 1.5;
    } else if (gradeLetter === "D+") {
        return 1.0;
    } else {
        return 0.0;
    }
}
