async function getWeather() {
    const city = document.getElementById('city').value;
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = ''; // Clear previous results

    if (!city) {
        resultDiv.innerHTML = `<p style="color: red;">Please enter a city!</p>`;
        return;
    }

    try {
        const response = await fetch(`/weather?city=${city}`);
        const data = await response.json();

        if (response.ok) {
            // Capitalize each word in the description
            const description = data.description.charAt(0).toUpperCase() + data.description.slice(1);

            // Update the web app with weather data
            resultDiv.innerHTML = `
                <h2>Current weather in ${data.city}:</h2>
                <img src="http://openweathermap.org/img/wn/${data.icon}@4x.png" alt="Weather icon" class="weather-icon">
                <p>Temperature: ${data.temperature} °C - ${description}</p>
                <p>Humidity: ${data.humidity}%</p>
                <p>Wind Speed: ${data.wind_speed} km/h</p>
            `;
        } else {
            resultDiv.innerHTML = `<p style="color: red;">Error: ${data.error}</p>`;
        }
    } catch (error) {
        resultDiv.innerHTML = `<p style="color: red;">Failed to fetch data. Please try again.</p>`;
    }
}
