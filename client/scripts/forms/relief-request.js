// relief-request.js
// Sends aid request data + optional images to your backend

import { RELIEF_API_URL } from "../utils/config.js";

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".relief__form");
    if (!form) return;

    const imageInput = document.querySelector("#relief_images");
    const previewContainer = document.querySelector(".relief__image-preview");

    let selectedImages = [];

    imageInput?.addEventListener("change", () => {
        const newFiles = Array.from(imageInput.files || []);
        const maxImages = 2;
        const maxSizeMB = 2;

        // === Estimate total size including new files ===
        const combinedFiles = [...selectedImages, ...newFiles].slice(0, maxImages);
        const totalRawSize = combinedFiles.reduce((sum, file) => sum + file.size, 0);
        const estimatedPayloadSize = totalRawSize * 1.4; // Base64 & form overhead

        if (estimatedPayloadSize > 9_000_000) {
            alert("Combined image size is too large. Upload fewer or smaller images.");
            return;
        }

        for (const file of newFiles) {
            if (selectedImages.length >= maxImages) {
                alert(`You can only upload up to ${maxImages} images (under 2MB each).`);
                break;
            }

            if (file.size > maxSizeMB * 1024 * 1024) {
                alert(`"${file.name}" exceeds the 2MB limit and was skipped.`);
                continue;
            }

            if (selectedImages.some(existing => existing.name === file.name && existing.size === file.size)) {
                alert(`"${file.name}" is already selected.`);
                continue;
            }

            selectedImages.push(file);
        }

        renderImagePreviews();
        imageInput.value = ""; // reset file input
    });

    function renderImagePreviews() {
        previewContainer.innerHTML = "";

        selectedImages.forEach((file, index) => {
            const reader = new FileReader();
            reader.onload = (e) => {
                if (typeof e.target?.result === "string") {
                    const wrapper = document.createElement("div");
                    wrapper.classList.add("relief__preview-wrapper");

                    const img = document.createElement("img");
                    img.src = e.target.result;
                    img.alt = file.name;
                    img.classList.add("relief__preview-thumb");

                    const deleteBtn = document.createElement("button");
                    deleteBtn.classList.add("relief__delete-btn");
                    deleteBtn.textContent = "✖";
                    deleteBtn.title = "Remove image";
                    deleteBtn.onclick = () => {
                        selectedImages.splice(index, 1);
                        renderImagePreviews();
                    };

                    wrapper.appendChild(img);
                    wrapper.appendChild(deleteBtn);
                    previewContainer.appendChild(wrapper);
                }
            };
            reader.readAsDataURL(file);
        });
    }

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const getValue = (selector) => document.querySelector(selector)?.value.trim();
        const getChecked = (selector) => document.querySelector(selector)?.checked;

        const fields = {
            firstName: getValue("#relief_first_name"),
            lastName: getValue("#relief_last_name"),
            email: getValue("#relief_email"),
            phone: getValue("#relief_phone"),
            city: getValue("#relief_city"),
            state: getValue("#relief_state"),
            assistanceType: getValue("#relief_type"),
            description: getValue("#relief_description"),
            confirmed: getChecked("#relief_confirm")
        };

        // === Highlight missing fields ===
        const requiredSelectors = [
            "#relief_first_name",
            "#relief_last_name",
            "#relief_email",
            "#relief_phone",
            "#relief_city",
            "#relief_state",
            "#relief_type",
            "#relief_description"
        ];

        requiredSelectors.forEach(selector => {
            const input = document.querySelector(selector);
            input?.classList.remove("relief__input--error");
            if (input && !input.value.trim()) {
                input.classList.add("relief__input--error");
            }
        });

        if (Object.values(fields).some(v => !v) || !fields.confirmed) {
            alert("Please complete all required fields and confirm.");
            return;
        }

        const formData = new FormData();
        Object.entries(fields).forEach(([key, value]) => {
            if (key !== "confirmed") formData.append(key, value);
        });

        selectedImages.slice(0, 3).forEach(file => {
            formData.append("images", file);
        });

        const submitButton = form.querySelector("button[type='submit']");
        submitButton.disabled = true;
        submitButton.textContent = "Submitting...";

        // === Optional debug: actual raw size of files ===
        const totalSize = selectedImages.reduce((sum, f) => sum + f.size, 0);
        console.log("Total raw file size (bytes):", totalSize);

        try {
            const response = await fetch(RELIEF_API_URL, {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.message || "Submission failed.");
            }

            console.log("✅ Relief request submitted:", {
                name: `${fields.firstName} ${fields.lastName}`,
                email: fields.email,
                city: fields.city,
                state: fields.state
            });

            alert("Relief request submitted successfully.");
            form.reset();
            previewContainer.innerHTML = "";
            window.location.href = "../../index.html";
        } catch (err) {
            console.error("❌ Error:", err.message);
            alert("Something went wrong: " + err.message);
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = "Submit";
        }
    });
});
