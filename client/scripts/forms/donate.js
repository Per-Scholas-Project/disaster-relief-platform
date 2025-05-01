// donate.js
// Sends donation form data to AWS backend

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".donate__form");

    form?.addEventListener("submit", async (event) => {
        event.preventDefault();

        const source = document.querySelector("#donate_source")?.value;
        const name = document.querySelector("#donate_name")?.value.trim();
        const expiration = document.querySelector("#donate_expiration")?.value.trim();
        const cvv = document.querySelector("#donate_cvv")?.value.trim();
        const zip = document.querySelector("#donate_zip")?.value.trim();
        const amount = document.querySelector("#donate_amount")?.value.trim();
        const note = document.querySelector("#donate_note")?.value.trim();

        if (!source || source === "select" || !name || !expiration || !cvv || !zip || !amount) {
            alert("Please complete all required fields.");
            return;
        }

        try {
            const response = await fetch("https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/donate", {
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
        } catch (err) {
            console.error("Donation error:", err.message);
            alert("Donation failed: " + err.message);
        }
    });
});
