import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import { SimpleSlug } from "./quartz/util/path"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
    head: Component.Head(),
    header: [],
    afterBody: [],
    footer: Component.Footer({
        links: {
            GitHub: "https://github.com/jackyzha0/quartz"
        },
    }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
    beforeBody: [
        Component.Breadcrumbs(),
        Component.ArticleTitle(),
        Component.ContentMeta(),
        Component.TagList(),
    ],
    left: [
        Component.PageTitle(),
        Component.MobileOnly(Component.Spacer()),
        Component.Flex({
            components: [
                { Component: Component.Search() },
                { Component: Component.Darkmode() },
                { Component: Component.ReaderMode() },
            ],
            gap: "unset",
        }),
        Component.Divider(),
        Component.DesktopOnly(Component.RecentNotes({
            title: "Most recent",
            limit: 3,
            linkToMore: "tags/" as SimpleSlug,
        })),
        Component.Explorer(),
    ],
    right: [
        Component.Graph(),
        Component.DesktopOnly(Component.TableOfContents()),
        Component.Backlinks(),
    ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
    beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
    left: [
        Component.PageTitle(),
        Component.MobileOnly(Component.Spacer()),
        Component.Flex({
            components: [
                { Component: Component.Search() },
                { Component: Component.Darkmode() },
                { Component: Component.ReaderMode() },
            ],
            gap: "unset",
        }),
        Component.Divider(),
        Component.Explorer(),
    ],
    right: [],
}