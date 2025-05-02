// volunteer.js
// Handles volunteer form submission to backend

import { VOLUNTEER_API_URL } from "../utils/config.js";

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".volunteer__form");

    if (!form) return;

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const getValue = (selector) => document.querySelector(selector)?.value.trim();
        const getChecked = (selector) => document.querySelector(selector)?.checked;

        const firstName = getValue("#volunteer_firstname");
        const lastName = getValue("#volunteer_lastname");
        const email = getValue("#volunteer_email");
        const city = getValue("#volunteer_city");
        const state = getValue("#volunteer_state");
        const willingToTravel = getChecked("#volunteer_travel");
        const message = getValue("#volunteer_message");

        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!firstName || !lastName || !email || !city || !state) {
            alert("Please complete all required fields.");
            return;
        }

        if (!emailPattern.test(email)) {
            alert("Please enter a valid email address.");
            return;
        }

        const submitButton = form.querySelector("button[type='submit']");
        submitButton.disabled = true;
        submitButton.textContent = "Submitting...";

        try {
            const response = await fetch(VOLUNTEER_API_URL, {
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
                    willingToTravel,
                    message
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || "Submission failed. Please try again.");
            }

            alert("Thank you for volunteering with UnitedRelief!");
            form.reset();
            window.location.href = "../../index.html"; // ✅ Redirect after success
        } catch (error) {
            console.error("Submission error:", error);
            alert(`Could not submit your form: ${error.message}`);
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = "Submit";
        }
    });
});
