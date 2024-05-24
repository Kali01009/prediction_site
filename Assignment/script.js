<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Revenue Prediction</title>
</head>
<body>
    <h1>Revenue Prediction</h1>
    <form id="prediction-form">
        <label for="revenue-category">Revenue Category:</label>
        <input type="text" id="revenue-category" name="revenue-category" required><br><br>
        <label for="year">Year to Predict For:</label>
        <input type="number" id="year" name="year" required><br><br>
        <button type="submit">Predict</button>
    </form>
    <div id="result"></div>

    <script>
        document.getElementById('prediction-form').addEventListener('submit', async function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const revenueCategory = formData.get('revenue-category');
            const year = formData.get('year');
            
            const response = await fetch(`https://your-netlify-app-url/.netlify/functions/predict?revenue_category=${revenueCategory}&year=${year}`);
            const data = await response.json();

            document.getElementById('result').innerHTML = `
                <p>Predicted Value for ${year}: ${data.prediction}</p>
                <p>Model Accuracy (R-squared): ${data.accuracy.toFixed(2)} %</p>
            `;
        });
    </script>
</body>
</html>
