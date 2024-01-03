window.addEventListener("load", () => {
    // Handle disabling all relevant inputs if one patient selection method has been interacted with
    const patientInputs = Array.from(
        document.querySelectorAll<HTMLInputElement>(".patient-option input, .patient-option select") || [],
    );
    patientInputs.forEach((input) => {
        input.addEventListener("change", () => {
            const siblings = Array.from(
                input.closest(".patient-option")?.querySelectorAll<HTMLInputElement>("input, select") || [],
            );
            patientInputs.forEach((otherInput) => {
                if (!siblings.includes(otherInput)) {
                    /* eslint-disable-next-line no-param-reassign */
                    otherInput.disabled = true;
                }
            });

            const reset = input.closest(".patient-option")?.querySelector(".form-reset") as HTMLElement;
            reset.classList.remove("hidden");
        });
    });

    // Handle resetting all patient selection input fields
    const resets = document.querySelectorAll<HTMLElement>(".form-reset");
    resets.forEach((reset) => {
        reset.addEventListener("click", () => {
            patientInputs.forEach((input) => {
                /* eslint-disable-next-line no-param-reassign */
                input.value = input.defaultValue;
                /* eslint-disable-next-line no-param-reassign */
                input.disabled = false;
            });
            resets.forEach((reset) => {
                reset.classList.add("hidden");
            });
        });
    });

    // Handle displaying and updating the selected approximate age of emergency patients
    const ageSlider = document.querySelector("#id_unknown-approximate_age") as HTMLInputElement;
    const ageDisplay = document.querySelector("#approximate-age-display") as HTMLElement;
    if (!ageSlider || !ageDisplay) {
        return;
    }
    ageSlider.addEventListener("input", () => {
        ageDisplay.innerHTML = ageSlider.value;
    });
});
