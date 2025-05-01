// signup.js
// Handles account creation via backend API

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".signup__form");

    form?.addEventListener("submit", async (event) => {
        event.preventDefault();

        const firstName = document.querySelector("#signup_firstname")?.value.trim();
        const lastName = document.querySelector("#signup_lastname")?.value.trim();
        const email = document.querySelector("#signup_email")?.value.trim();
        const password = document.querySelector("#signup_password")?.value;
        const confirmPassword = document.querySelector("#signup_confirm_password")?.value;

        // Validation
        if (!firstName || !lastName || !email || !password || !confirmPassword) {
            alert("Please fill in all required fields.");
            return;
        }

        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            return;
        }

        try {
            const response = await fetch("https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/signup", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    firstName,
                    lastName,
                    email,
                    password
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || "Signup failed.");
            }

            alert("Account created successfully! You can now log in.");
            window.location.href = "signin.html";
        } catch (err) {
            console.error("Signup error:", err.message);
            alert("Signup failed: " + err.message);
        }
    });
});
