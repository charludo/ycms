window.addEventListener("load", () => {
    const sidebarToggle = document.getElementById("sidebarToggle");
    const sidebar = document.getElementById("sidebar");
    const menuIcon = document.getElementById("menuIcon");
    const closeIcon = document.getElementById("closeIcon");
    const leftToggle = document.getElementById("leftToggle");
    const mainContent = document.getElementById("mainContent");

    // if  localStorage isSidebarOpen not set, set it to true
    if (localStorage.getItem("isSidebarOpen") === null) {
        localStorage.setItem("isSidebarOpen", "true");
    }

    const isSidebarOpen = localStorage.getItem("isSidebarOpen") === "true";

    if (!isSidebarOpen && sidebar) {
        sidebar?.classList.toggle("lg:translate-x-0");
        mainContent?.classList.toggle("lg:ml-64");
    }

    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener("click", () => {
            sidebar.classList.toggle("-translate-x-full");
            menuIcon?.classList.toggle("hidden");
            closeIcon?.classList.toggle("hidden");
        });
    }

    leftToggle?.addEventListener("click", () => {
        menuIcon?.classList.toggle("hidden");
        closeIcon?.classList.toggle("hidden");
        sidebar?.classList.toggle("lg:translate-x-0");
        mainContent?.classList.toggle("lg:ml-64");

        // Update localStorage with the current state
        const isOpen = sidebar?.classList.contains("lg:translate-x-0");
        localStorage.setItem("isSidebarOpen", String(isOpen));
    });
});
