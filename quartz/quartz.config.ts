import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4.0 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
    configuration: {
        pageTitle: "Personal Second Brain",
        enableSPA: true,
        enablePopovers: false, // https://github.com/jackyzha0/quartz/issues/890
        analytics: null,
        locale: "en-US",
        // baseUrl: "url.com",
        ignorePatterns: ["private", "**/templates", ".obsidian"],
        defaultDateType: "created",
        theme: {
            fontOrigin: "local",
            cdnCaching: false,
            typography: {
                header: "Schibsted Grotesk",
                body: "Inter",
                code: "Fira Code",
            },
            colors: {
                lightMode: {
                    light: "#fafafa",
                    lightgray: "#e0e0e0",
                    gray: "#9e9e9e",
                    darkgray: "#212121",
                    dark: "#000000",
                    secondary: "#4271AE",
                    tertiary: "#B48EAD",
                    highlight: "rgba(66, 113, 174, 0.1)",
                    textHighlight: "#fff23688",
                },
                darkMode: {
                    light: "#212121",
                    lightgray: "#424242",
                    gray: "#65737E",
                    darkgray: "#dadada",
                    dark: "#dadada",
                    secondary: "#8FA1B3",
                    tertiary: "#B48EAD",
                    highlight: "rgba(143, 161, 179, 0.15)",
                    textHighlight: "#b3aa0288",
                },
            },
        },
    },
    plugins: {
        transformers: [
            Plugin.FrontMatter(),
            Plugin.CreatedModifiedDate({
                priority: ["frontmatter"],
            }),
            Plugin.SyntaxHighlighting({
                theme: {
                    light: "github-light",
                    dark: "nord",
                },
                keepBackground: false,
            }),
            Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
            Plugin.GitHubFlavoredMarkdown(),
            Plugin.TableOfContents(),
            Plugin.CrawlLinks({
                markdownLinkResolution: "shortest",
            }),
            Plugin.Description(),
            Plugin.Latex({ renderEngine: "katex" })
        ],
        filters: [Plugin.RemoveDrafts()],
        emitters: [
            Plugin.AliasRedirects(),
            Plugin.ComponentResources(),
            Plugin.ContentPage(),
            Plugin.FolderPage(),
            Plugin.TagPage(),
            Plugin.ContentIndex({
                enableSiteMap: true,
                enableRSS: true,
            }),
            Plugin.Assets(),
            Plugin.Static(),
            Plugin.NotFoundPage(),
            // Comment out CustomOgImages to speed up build time
            Plugin.CustomOgImages(),
        ],
    },
}

export default config