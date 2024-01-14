import TomSelect from "tom-select";

const newTomSelect = (element: string, endpoint: string) => {
    const domElement = document.querySelector(element) as HTMLSelectElement;
    if (!domElement) {
        return;
    }
    /* eslint-disable-next-line no-new */
    new TomSelect(element, {
        valueField: "id",
        labelField: "name",
        searchField: ["id", "name"],
        selectOnTab: true,
        items: [...domElement.options].map((el) => el.value),
        /* eslint-disable-next-line @typescript-eslint/no-explicit-any */
        load: (query: string, callback: any) => {
            const url = `/autocomplete/${endpoint}/?q=${encodeURIComponent(query)}`;
            fetch(url)
                .then((response) => response.json())
                .then((json) => {
                    callback(json.suggestions);
                });
        },
    });
};

window.addEventListener("load", () => {
    const diagnosisInputs = document.querySelectorAll<HTMLInputElement>(".async_diagnosis_code");
    const autosuggestionConfig = [["#id_patient", "patient"]];
    diagnosisInputs.forEach((input) => {
        autosuggestionConfig.push([`#${input.id}`, "icd10"]);
    });
    autosuggestionConfig.forEach((element) => {
        newTomSelect(element[0], element[1]);
    });
});
