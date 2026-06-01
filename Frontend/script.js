async function predictWeather() {

    const humidity =
        parseFloat(
            document.getElementById("humidity").value
        );

    const wind_speed =
        parseFloat(
            document.getElementById("wind_speed").value
        );

    const soil_temperature =
        parseFloat(
            document.getElementById("soil_temperature").value
        );

    if (
        isNaN(humidity) ||
        isNaN(wind_speed) ||
        isNaN(soil_temperature)
    ) {
        alert("Please fill all fields correctly.");
        return;
    }

    try {

        const apiBaseUrl = "http://127.0.0.1:8000";
        const response = await fetch(
            `${apiBaseUrl}/predict`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    humidity: humidity,
                    wind_speed: wind_speed,
                    soil_temperature: soil_temperature
                })
            }
        );

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Server returned ${response.status}: ${errorText}`);
        }

        const data = await response.json();

        document.getElementById(
            "prediction"
        ).innerText =
            data.predicted_temperature.toFixed(2) + " °C";

    }
    catch (error) {

        console.error(error);

        alert(
            "Failed to connect to FastAPI server."
        );
    }
}