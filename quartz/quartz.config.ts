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
                    light: "#faf8f8",
                    lightgray: "#e5e5e5",
                    gray: "#b8b8b8",
                    darkgray: "#4e4e4e",
                    dark: "#2b2b2b",
                    secondary: "#284b63",
                    tertiary: "#84a59d",
                    highlight: "rgba(143, 159, 169, 0.15)",
                    textHighlight: "#fff23688",
                },
                darkMode: {
                    light: "#2B303B", // background
                    lightgray: "rgba(192, 197, 206, 0.15)", // "#C0C5CE"
                    gray: "#65737E",
                    darkgray: "#E8E8E8", // paragraph
                    dark: "#DFE1E8", // title
                    secondary: "#7CAFC2", // links
                    tertiary: "#B48EAD", // hover
                    highlight: "rgba(143, 159, 169, 0.15)",
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