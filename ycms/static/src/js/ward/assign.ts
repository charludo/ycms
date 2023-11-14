import { Modal, ModalOptions } from "flowbite";

let selectedBedAssignmentId: string | null = "";

export const handleAssign = (button: HTMLElement): void => {
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

export const handleButtonAssign = (): void => {
    const buttons = document.querySelectorAll('button[id*="assignButton"]');

    buttons.forEach((element) => {
        const button = element as HTMLElement;
        button.addEventListener("click", () => {
            handleAssign(button);
        });
    });
};
