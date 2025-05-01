// relief-request.js
// Sends aid request data + optional images to your backend

import { RELIEF_API_URL } from "../utils/config.js";

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".relief__form");

    if (!form) return;

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const getValue = (selector) => document.querySelector(selector)?.value.trim();
        const getChecked = (selector) => document.querySelector(selector)?.checked;
        const getFiles = (selector) => document.querySelector(selector)?.files;

        const firstName = getValue("#relief_first_name");
        const lastName = getValue("#relief_last_name");
        const email = getValue("#relief_email");
        const phone = getValue("#relief_phone");
        const city = getValue("#relief_city");
        const state = getValue("#relief_state");
        const assistanceType = getValue("#relief_type");
        const description = getValue("#relief_description");
        const confirmed = getChecked("#relief_confirm");
        const images = getFiles("#relief_images");

        if (!firstName || !lastName || !email || !phone || !city || !state || !assistanceType || !description || !confirmed) {
            alert("Please fill out all required fields and confirm the checkbox.");
            return;
        }

        const formData = new FormData();
        formData.append("firstName", firstName);
        formData.append("lastName", lastName);
        formData.append("email", email);
        formData.append("phone", phone);
        formData.append("city", city);
        formData.append("state", state);
        formData.append("assistanceType", assistanceType);
        formData.append("description", description);

        if (images?.length > 0) {
            Array.from(images).slice(0, 6).forEach(file => {
                formData.append("images", file);
            });
        }

        const submitButton = form.querySelector("button[type='submit']");
        submitButton.disabled = true;
        submitButton.textContent = "Submitting...";

        try {
            const response = await fetch(RELIEF_API_URL, {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.message || "Submission failed.");
            }

            alert("Relief request submitted successfully.");
            form.reset();
            window.location.href = "/index.html";
        } catch (err) {
            console.error("Error:", err.message);
            alert("Something went wrong: " + err.message);
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = "Submit";
        }
    });
});
