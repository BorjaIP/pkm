import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

interface BackToSiteOptions {
    /**
     * Where the link points to (the main site this garden is served under)
     */
    href: string
    /**
     * Visible name of the main site
     */
    label: string
}

const defaultOptions: BackToSiteOptions = {
    href: "https://borjaip.github.io/",
    label: "BorjaIP",
}

export default ((userOpts?: Partial<BackToSiteOptions>) => {
    const opts = { ...defaultOptions, ...userOpts }

    const BackToSite: QuartzComponent = ({ displayClass }: QuartzComponentProps) => {
        // The main site shares this site's origin, so Quartz's SPA router would try to
        // fetch and morph its HTML into this page. `data-router-ignore` forces a normal
        // full-page navigation instead.
        return (
            <a
                class={classNames(displayClass, "back-to-site")}
                href={opts.href}
                data-router-ignore
                aria-label={`Back to ${opts.label}`}
            >
                <span class="back-arrow" aria-hidden="true">←</span>
                <span class="back-label">{opts.label}</span>
            </a>
        )
    }

    return BackToSite
}) satisfies QuartzComponentConstructor
