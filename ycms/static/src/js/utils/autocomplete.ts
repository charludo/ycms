import TomSelect from "tom-select";

const newTomSelect = (element: string, endpoint: string) => {
    /* eslint-disable-next-line no-new */
    new TomSelect(element, {
        valueField: "id",
        labelField: "name",
        searchField: ["id", "name"],
        selectOnTab: true,
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
    const autosuggestionConfig = [
        ["#id_diagnosis_code", "icd10"],
        ["#id_patient", "patient"],
    ];
    autosuggestionConfig.forEach((element) => {
        if (!document.querySelector(element[0])) {
            return;
        }
        newTomSelect(element[0], element[1]);
    });
});
