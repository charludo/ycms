window.addEventListener("load", () => {
    const patientSelect = document.querySelector("#id_patient") as HTMLInputElement;
    const patientCreate = document.querySelector("#patient-create") as HTMLElement;

    if (!patientSelect || !patientCreate) {
        return;
    }

    patientSelect.addEventListener("change", () => {
        patientCreate.querySelectorAll("input, select").forEach((node: Element) => {
            /* eslint-disable-next-line no-param-reassign */
            (node as HTMLInputElement).disabled = !!patientSelect.value;
        });
    });
});
