import { Modal, ModalOptions } from "flowbite";

let selectedBedAssignmentId: string | null = "";

export const handleModalClose = (): void => {
    document.getElementById("cancelDischargeButton")?.addEventListener("click", () => {
        const modal = FlowbiteInstances.getInstance("Modal", "modalEl");
        modal.hide();
    });
    document.getElementById("closeModalButton")?.addEventListener("click", () => {
        const modal = FlowbiteInstances.getInstance("Modal", "modalEl");
        modal.hide();
    });
};

export const handleConfirmDischarge = (): void => {
    document.getElementById("confirmDischargeButton")?.addEventListener("click", () => {
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

        fetch(`/patients/discharge/${selectedBedAssignmentId}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken") || "",
            },
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    handleModalClose();
                    window.location.reload();
                } else {
                    console.error("POST request failed");
                }
            });

        handleModalClose();
    });
};

export const handleDischarge = (button: HTMLElement): void => {
    selectedBedAssignmentId = button.getAttribute("data-bedassignment-id");

    const targetEl = document.getElementById("modalEl");

    const options: ModalOptions = {
        placement: "center-center" as ModalOptions["placement"],
        backdrop: "dynamic",
        backdropClasses: "bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40",
        closable: true,
    };
    const modal = new Modal(targetEl, options);
    modal.show();
};

export const handleButtonDischarge = (): void => {
    const buttons = document.querySelectorAll('button[id*="dischargeButton"]');

    buttons.forEach((element) => {
        const button = element as HTMLElement;
        button.addEventListener("click", () => {
            handleDischarge(button);
        });
    });
};
