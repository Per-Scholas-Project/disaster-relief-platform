// volunteer.js
// Submits volunteer application to backend

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".volunteer__form");

    form?.addEventListener("submit", async (event) => {
        event.preventDefault();

        const firstName = document.querySelector("#volunteer_firstname")?.value.trim();
        const lastName = document.querySelector("#volunteer_lastname")?.value.trim();
        const email = document.querySelector("#volunteer_email")?.value.trim();
        const city = document.querySelector("#volunteer_city")?.value.trim();
        const state = document.querySelector("#volunteer_state")?.value.trim();
        const travel = document.querySelector("#volunteer_travel")?.checked;
        const message = document.querySelector("#volunteer_message")?.value.trim();

        if (!firstName || !lastName || !email || !city || !state) {
            alert("Please complete all required fields.");
            return;
        }

        try {
            const response = await fetch("https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/volunteer", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    firstName,
                    lastName,
                    email,
                    city,
                    state,
                    willingToTravel: travel,
                    message
                })
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.message || "Submission failed");
            }

            alert("Thank you for volunteering with UnitedRelief!");
            form.reset();
        } catch (err) {
            console.error("Submission error:", err.message);
            alert("Could not submit your form: " + err.message);
        }
    });
});
