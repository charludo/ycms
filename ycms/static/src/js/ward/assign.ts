import { Modal, ModalOptions } from "flowbite";

let selectedBedAssignmentId: string | null = "";
let selectedBedId: string | null = "";
let selectedWardId: string | null = "";

export const handleAssignModalClose = (): void => {
    document.getElementById("cancelAssignButton")?.addEventListener("click", () => {
        const modal = FlowbiteInstances.getInstance("Modal", "assign-modal");
        modal.hide();
    });
    document.getElementById("closeAssignButton")?.addEventListener("click", () => {
        const modal = FlowbiteInstances.getInstance("Modal", "assign-modal");
        modal.hide();
    });
};

export const handleAssignModalConfirm = (): void => {
    document.getElementById("confirmAssignButton")?.addEventListener("click", () => {
        const modal = FlowbiteInstances.getInstance("Modal", "assign-modal");

        const getCookie = (name: string): string | null => {
            let cookieValue = null;
            if (document.cookie && document.cookie !== "") {
                const cookies = document.cookie.split(";");
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Check if the cookie name matches the provided name
                    if (cookie.substring(0, name.length + 1) === `${name}=`) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        };

        fetch(`/patients/assign/${selectedWardId}/${selectedBedAssignmentId}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken") || "",
            },
            body: JSON.stringify({ bed_id: selectedBedId }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    modal.hide();
                    window.location.href = `/ward/${selectedWardId}/`;
                } else {
                    console.error("POST request failed");
                }
            });

        modal.hide();
    });
};

export const handleAssign = (card: HTMLElement): void => {
    selectedBedId = card.getAttribute("data-bed-id");
    selectedWardId = card.getAttribute("data-ward-id");
    selectedBedAssignmentId = card.getAttribute("data-bedassignment-id");
    const roomNumber = card.getAttribute("data-room-number");
    const genderWarning = card.getAttribute("data-room-gender-warning");
    const ageWarning = card.getAttribute("data-room-age-warning");
    const insuranceWarning = card.getAttribute("data-room-insurance-warning");

    let warningList = "";

    if (genderWarning) {
        warningList += `<li>${genderWarning}</li>`;
    }
    if (ageWarning) {
        warningList += `<li>${ageWarning}</li>`;
    }
    if (insuranceWarning) {
        warningList += `<li>${insuranceWarning}</li>`;
    }

    const targetEl = document.getElementById("assign-modal");
    const assignContent = document.getElementById("assign-modal-content");

    const options: ModalOptions = {
        placement: "center-center" as ModalOptions["placement"],
        backdrop: "dynamic",
        backdropClasses: "bg-gray-900 bg-opacity-10 dark:bg-opacity-80 fixed inset-0 z-40",
        closable: true,
    };

    if (!targetEl) {
        return;
    }
    if (!assignContent) {
        return;
    }
    if (!genderWarning && !ageWarning && !insuranceWarning) {
        assignContent.innerHTML = `
        <h3 class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">Are you sure you want to assign the patient to Room ${roomNumber}?</h3>
    `;
    } else {
        assignContent.innerHTML = `
    <div
    class="mb-5 bg-yellow-50 text-yellow-800 p-4 rounded-lg shadow dark:bg-gray-800 dark:text-yellow-300 flex flex-col justify-between h-full">
    <h2 class="text-xl font-semibold text-gray-900 dark:text-white">Assigning to Room ${roomNumber} may cause:</h2>
    <ul class="max-w-md space-y-2 mt-2 list-disc list-inside dark:text-gray-400">
    ${warningList}
    </ul>
</div>

    <h3 class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">Are you sure you want to assign the patient to Room ${roomNumber}?</h3>
        `;
    }

    const modal = new Modal(targetEl, options);
    modal.show();
};

export const handleRoomCardAssign = (): void => {
    const cards = document.querySelectorAll('div[id*="assignRoomCard"]');

    cards.forEach((element) => {
        const button = element as HTMLElement;
        button.addEventListener("click", () => {
            handleAssign(button);
        });
    });
};

export const handleEdit = (button: HTMLElement): void => {
    selectedBedAssignmentId = button.getAttribute("data-bedassignment-id");
    const targetEl = document.getElementById("update-modal");
    if (!targetEl) {
        return;
    }
    const options: ModalOptions = {
        placement: "center-center" as ModalOptions["placement"],
        backdrop: "dynamic",
        backdropClasses: "bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40",
        closable: true,
    };

    fetch(`/bed-assignments/update-modal/${selectedBedAssignmentId}/`)
        .then((response) => response.text())
        .then((data) => {
            if (!targetEl) {
                return;
            }
            targetEl.innerHTML = data;
        })
        .catch((error) => console.error("Error:", error));
    const modal = new Modal(targetEl, options);
    modal.show();
};

export const handleButtonEdit = (): void => {
    const buttons = document.querySelectorAll('button[id*="editButton"]');

    buttons.forEach((element) => {
        const button = element as HTMLElement;
        button.addEventListener("click", () => {
            handleEdit(button);
        });
    });
};
