const setTime = (time: string) => {
    const urlParams = new URLSearchParams(window.location.search);
    urlParams.set("time", time);
    const newUrl = `${window.location.pathname}?${urlParams.toString().replace(".000+00:00", "Z")}`;
    window.history.replaceState({}, "", newUrl);
    window.location.reload();
};

window.addEventListener("load", () => {
    const urlParams = new URLSearchParams(window.location.search);
    const timeParameter = urlParams.get("time");
    if (!timeParameter) {
        return;
    }
    const dateTime = new Date(timeParameter.replace("Z", "+00:00"));

    const startTimetravel = document.querySelector<HTMLElement>("#timetravel-start");
    const stopTimetravel = document.querySelector<HTMLElement>("#timetravel-stop");
    if (startTimetravel && stopTimetravel) {
        startTimetravel.classList.add("hidden");
        stopTimetravel.classList.remove("hidden");
    }

    const controls = document.querySelector<HTMLElement>("#timetravel-controls");
    const buttons = document.querySelectorAll<HTMLButtonElement>("#timetravel-controls button");
    const dateInput = document.querySelector<HTMLInputElement>("#timetravel-controls input");

    if (!controls || !buttons || !dateInput) {
        return;
    }

    controls.classList.remove("hidden");

    const datestringLength = 16;
    dateInput.value = dateTime.toISOString().slice(0, datestringLength);

    dateInput.addEventListener("change", () => {
        setTime(dateInput.value);
    });

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            const minutes = button.getAttribute("data-minutes") ?? "0";
            const minutesInt = parseInt(minutes, 10) ?? 0;
            dateTime.setMinutes(dateTime.getMinutes() + minutesInt);
            setTime(dateTime.toISOString());
        });
    });
});
