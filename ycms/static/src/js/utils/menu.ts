window.addEventListener("load", () => {
    const sidebarToggle = document.getElementById("sidebarToggle");
    const sidebar = document.getElementById("sidebar");
    const menuIcon = document.getElementById("menuIcon");
    const closeIcon = document.getElementById("closeIcon");

    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener("click", () => {
            sidebar.classList.toggle("-translate-x-full");
            menuIcon?.classList.toggle("hidden");
            closeIcon?.classList.toggle("hidden");
        });
    }
});
