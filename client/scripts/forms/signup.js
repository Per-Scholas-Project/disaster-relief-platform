// signup.js
// Handles account creation via backend API

import { SIGNUP_API_URL } from "../utils/config.js";

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".signup__form");

    if (!form) return;

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const getValue = (selector) => document.querySelector(selector)?.value.trim();

        const firstName = getValue("#signup_firstname");
        const lastName = getValue("#signup_lastname");
        const email = getValue("#signup_email");
        const password = document.querySelector("#signup_password")?.value;
        const confirmPassword = document.querySelector("#signup_confirm_password")?.value;

        if (!firstName || !lastName || !email || !password || !confirmPassword) {
            alert("Please fill in all required fields.");
            return;
        }

        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            return;
        }

        const submitButton = form.querySelector("button[type='submit']");
        submitButton.disabled = true;
        submitButton.textContent = "Creating account...";

        try {
            const response = await fetch(SIGNUP_API_URL, {
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
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = "Sign Up";
        }
    });
});
