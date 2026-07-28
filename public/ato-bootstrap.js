try {
  const storedTheme = window.localStorage.getItem("excalidraw-theme");
  const theme =
    storedTheme === "system"
      ? window.matchMedia("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light"
      : storedTheme || "light";
  document.documentElement.classList.toggle("dark", theme === "dark");
} catch (error) {
  console.error("Error setting dark mode", error);
}

window.EXCALIDRAW_ASSET_PATH = window.location.origin;
window.name = "_excalidraw";
