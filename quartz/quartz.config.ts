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
        baseUrl: "borjaip.github.io/pkm",
        ignorePatterns: ["private", "**/templates", ".obsidian"],
        defaultDateType: "created",
        theme: {
            fontOrigin: "googleFonts",
            cdnCaching: true,
            typography: {
                header: "Inconsolata",
                body: "Inconsolata",
                code: "Inconsolata",
            },
            // Palette matched to borjaip.github.io (pink accent on near-black).
            colors: {
                lightMode: {
                    light: "#fafafa",
                    lightgray: "#e0e0e0",
                    gray: "#888888",
                    darkgray: "#2B303B",
                    dark: "#0a0a0a",
                    secondary: "#2B303B",
                    tertiary: "#de73be",
                    highlight: "rgba(222, 115, 190, 0.1)",
                    textHighlight: "#de73be55",
                },
                darkMode: {
                    light: "#0a0a0a",
                    lightgray: "#262626",
                    gray: "#666666",
                    darkgray: "#d4d4d4",
                    dark: "#e8e8e8",
                    secondary: "#bbbbbb",
                    tertiary: "#de73be",
                    highlight: "rgba(222, 115, 190, 0.12)",
                    textHighlight: "#de73be55",
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