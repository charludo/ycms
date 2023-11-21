import "tom-select/dist/css/tom-select.css";
import "./css/style.scss";
import "./js/messages";
import "./js/patient_select_or_create";
import "./js/utils/autocomplete";
import "./js/utils/timetravel";
import "./js/utils/menu";
import { initFlowbite } from "flowbite";
import { handleConfirmDischarge, handleButtonDischarge, handleModalClose } from "./js/ward/discharge";
import { createIconsAt } from "./js/utils/create-icons";

window.addEventListener("DOMContentLoaded", () => {
    createIconsAt(document.documentElement);
    handleButtonDischarge();
    handleConfirmDischarge();
    handleModalClose();
    const event = new Event("icon-load");
    window.dispatchEvent(event);
    initFlowbite();
});
