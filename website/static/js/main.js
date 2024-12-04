document.getElementById('predict-form').addEventListener('submit', function (e) {
  e.preventDefault();  // Prevent form submission

    // Collect form data into a JSON object
    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = parseFloat(value);  // Ensure values are sent as floats
    });

  // Send the form data to the Flask server
  fetch('/predict', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
      // Display the prediction result
      document.getElementById('prediction-result').innerText = 'Prediction: ' + data.prediction;
  })
  .catch(error => {
      console.error('Error:', error);
  });
});
