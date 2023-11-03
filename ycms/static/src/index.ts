import "tom-select/dist/css/tom-select.css";
import "./css/style.scss";
import "./js/messages";
import "./js/patient_select_or_create";
import "./js/utils/autocomplete";
import { createIconsAt } from "./js/utils/create-icons";

window.addEventListener("DOMContentLoaded", () => {
    createIconsAt(document.documentElement);
    const event = new Event("icon-load");
    window.dispatchEvent(event);
});
