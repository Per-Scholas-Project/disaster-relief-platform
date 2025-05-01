// signin.js
// Triggered on form submission and sends credentials to your AWS backend

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".login__form");

    form?.addEventListener("submit", async (event) => {
        event.preventDefault();

        const email = document.querySelector("#login_email")?.value.trim();
        const password = document.querySelector("#login_password")?.value;

        if (!email || !password) {
            alert("Please enter both email and password.");
            return;
        }

        try {
            const response = await fetch("https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/signin", {
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
            window.location.href = "/dashboard.html";
        } catch (err) {
            console.error("Login error:", err.message);
            alert("Login failed: " + err.message);
        }
    });
});
