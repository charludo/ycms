const editPatient = (id: string) => {
    const row = document.querySelector(`[data-patient-id='${id}']`);
    if (row != null) {
        for (const column of row.children) {
            for (const child of column.children) {
                child.classList.toggle("hidden");
            }
        }
    }
};

const searchPatients = (name: string) => {
    const filter = name.toUpperCase();
    const table = document.getElementById("patients") as HTMLTableElement;
    const tr = table.getElementsByTagName("tr");

    for (let i = 2; i < tr.length; i++) {
        const td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            const txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
};

window.addEventListener("load", () => {
    const editPatientButtons = document.querySelectorAll(".edit-patient-button");
    editPatientButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const id = button.parentElement?.parentElement?.parentElement?.getAttribute("data-patient-id") as string;
            editPatient(id);
        });
    });

    const searchPatientInput = document.querySelector("#search-patient-input") as HTMLInputElement;
    searchPatientInput.addEventListener("keyup", () => {
        const name = searchPatientInput.value;
        searchPatients(name);
    });
});
