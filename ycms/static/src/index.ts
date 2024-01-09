import "tom-select/dist/css/tom-select.css";
import "./css/style.scss";
import "./js/messages";
import "./js/patient_select_or_create";
import "./js/utils/autocomplete";
import "./js/utils/persistent-drawers";
import "./js/utils/timetravel";
import "./js/utils/menu";
import "./js/ward/discharge";
import "./js/ward/assign";
import "./js/ward/toggle-edit-mode";
import "./js/ward/progress";
import { createIconsAt } from "./js/utils/create-icons";
import "./js/patients_list";
import "./js/utils/loader";
import "./js/utils/set-language";

window.addEventListener("DOMContentLoaded", () => {
    createIconsAt(document.documentElement);
    const event = new Event("icon-load");
    window.dispatchEvent(event);
});
