/**
 * Keep application fonts in the Vite asset graph for isolated hosting.
 * @returns {import("vite").PluginOption}
 */
module.exports.woff2BrowserPlugin = () => {
  let isDev;
  return {
    name: "woff2BrowserPlugin",
    enforce: "pre",
    config(_, { command }) {
      isDev = command === "serve";
    },
    transform(code, id) {
      // Leave fonts.css intact so Vite emits every referenced font and rewrites
      // its URL. A CSS-relative fallback to the JS assets directory is invalid.
      if (!isDev && id.endsWith("excalidraw-app/index.html")) {
        return code.replace(
          "<!-- PLACEHOLDER:EXCALIDRAW_APP_FONTS -->",
          '<script>window.EXCALIDRAW_ASSET_PATH = "/";</script>',
        );
      }
    },
  };
};
