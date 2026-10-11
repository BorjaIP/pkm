import { QuartzComponentConstructor, QuartzComponentProps } from "./types"

function Divider(_props: QuartzComponentProps) {
    return <hr />
}

export default (() => Divider) satisfies QuartzComponentConstructor