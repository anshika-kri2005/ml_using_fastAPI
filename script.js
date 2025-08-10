document.getElementById("predictionForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        sepal_length: parseFloat(document.getElementById("sepal_length").value),
        sepal_width: parseFloat(document.getElementById("sepal_width").value),
        petal_length: parseFloat(document.getElementById("petal_length").value),
        petal_width: parseFloat(document.getElementById("petal_width").value)
    };

    const response = await fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("result").textContent = "🌼 Prediction: " + result.prediction;
});
