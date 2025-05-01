// signin.js
// Triggered on form submission and sends credentials to your AWS backend

import { SIGNIN_API_URL } from "../utils/config.js";

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".login__form");

    if (!form) return;

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const email = document.querySelector("#login_email")?.value.trim();
        const password = document.querySelector("#login_password")?.value;

        if (!email || !password) {
            alert("Please enter both email and password.");
            return;
        }

        const submitButton = form.querySelector("button[type='submit']");
        submitButton.disabled = true;
        submitButton.textContent = "Signing in...";

        try {
            const response = await fetch(SIGNIN_API_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email, password })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || "Login failed");
            }

            const data = await response.json();
            console.log("Login successful:", data);

            // Save token to localStorage (or cookie) if needed
            localStorage.setItem("accessToken", data.token);

            // Redirect to dashboard or homepage
            window.location.href = "/";
        } catch (err) {
            console.error("Login error:", err.message);
            alert("Login failed: " + err.message);
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = "Sign In";
        }
    });
});
