// donate.js
// Sends donation form data to AWS backend

import { DONATE_API_URL } from "../utils/config.js";

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".donate__form");

    if (!form) return;

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const getValue = (selector) => document.querySelector(selector)?.value.trim();

        const source = document.querySelector("#donate_source")?.value;
        const name = getValue("#donate_name");
        const expiration = getValue("#donate_expiration");
        const cvv = getValue("#donate_cvv");
        const zip = getValue("#donate_zip");
        const amount = getValue("#donate_amount");
        const note = getValue("#donate_note");

        if (!source || source === "select" || !name || !expiration || !cvv || !zip || !amount) {
            alert("Please complete all required fields.");
            return;
        }

        const submitButton = form.querySelector("button[type='submit']");
        submitButton.disabled = true;
        submitButton.textContent = "Processing...";

        try {
            const response = await fetch(DONATE_API_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    source,
                    name,
                    expiration,
                    cvv,
                    zip,
                    amount: parseFloat(amount),
                    note
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || "Donation failed");
            }

            const data = await response.json();
            console.log("Donation successful:", data);

            alert("Thank you for your donation!");
            form.reset();
            window.location.href = "/index.html"; // Redirect after alert
        } catch (err) {
            console.error("Donation error:", err.message);
            alert("Donation failed: " + err.message);
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = "Submit";
        }
    });
});
