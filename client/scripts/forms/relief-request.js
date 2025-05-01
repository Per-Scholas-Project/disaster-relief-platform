// relief-request.js
// Sends aid request data + optional images to your backend

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".relief__form");

    form?.addEventListener("submit", async (event) => {
        event.preventDefault();

        const firstName = document.querySelector("#relief_first_name")?.value.trim();
        const lastName = document.querySelector("#relief_last_name")?.value.trim();
        const email = document.querySelector("#relief_email")?.value.trim();
        const phone = document.querySelector("#relief_phone")?.value.trim();
        const city = document.querySelector("#relief_city")?.value.trim();
        const state = document.querySelector("#relief_state")?.value.trim();
        const assistanceType = document.querySelector("#relief_type")?.value.trim();
        const description = document.querySelector("#relief_description")?.value.trim();
        const confirmed = document.querySelector("#relief_confirm")?.checked;
        const images = document.querySelector("#relief_images")?.files;

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

        // Attach up to 6 images
        if (images?.length > 0) {
            Array.from(images).slice(0, 6).forEach((file, index) => {
                formData.append("images", file); // backend should handle multiple 'images' fields
            });
        }

        try {
            const response = await fetch("https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/relief-request", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.message || "Submission failed.");
            }

            alert("Relief request submitted successfully.");
            form.reset();
        } catch (err) {
            console.error("Error:", err.message);
            alert("Something went wrong: " + err.message);
        }
    });
});
