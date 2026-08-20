## 2025-05-27 - Booking Form Accessibility
**Learning:** Custom checkbox implementations using `display: none` (Tailwind `hidden`) remove the input from the tab order, breaking keyboard accessibility.
**Action:** Always use `sr-only` (screen reader only) for the input and ensure the visual proxy element has `peer-focus` styles to indicate focus state.

## 2025-05-27 - Interaction Feedback
**Learning:** Using `window.alert()` for form submission success is disruptive and looks unprofessional.
**Action:** Implement inline success messages and button loading states (text change + disabled) for smoother interaction.

## 2025-05-27 - Keyboard Accessible Dropdowns
**Learning:** Hover-only dropdowns are inaccessible to keyboard users. Tailwind's `group-hover` should almost always be paired with `group-focus-within`.
**Action:** Automatically add `group-focus-within` variants whenever `group-hover` is used for visibility toggling.

## 2026-02-02 - Mobile Toggle Accessibility
**Learning:** Icon-only toggles (like hamburger menus) require explicit `aria-label` and `aria-expanded` states to be usable by screen readers.
**Action:** Ensure all toggle buttons have dynamic ARIA attributes and visible focus rings (`focus-visible`).

## 2026-02-03 - Async Interaction Patterns
**Learning:** Simple forms often lack loading states, leaving users unsure if their action registered.
**Action:** Always implement `isLoading` state, disable inputs/buttons during submission, and provide textual feedback on the button.

## 2026-10-24 - Input Labeling
**Learning:** Inputs relying solely on placeholders for identification are inaccessible to screen readers.
**Action:** Always include an `aria-label` matching the placeholder if a visible `<label>` is not design-compliant.

## 2026-02-05 - Tactile Feedback in Quizzes
**Learning:** Static selection cards feel dull and lack affordance. Keyboard users often get lost without clear focus rings.
**Action:** Combine `hover:-translate-y-1` for mouse users with `focus-visible:ring-2` for keyboard users to make selection steps feel alive and accessible.

## 2026-10-25 - Horizontal Scroll Accessibility
**Learning:** Horizontal scroll areas with hidden scrollbars are inaccessible to mouse users without touchpads and undiscoverable.
**Action:** Add explicit "Previous" and "Next" buttons that appear on hover AND on focus (using `group-focus-within`), ensuring keyboard users can also access them.

## 2026-10-26 - Multi-step Process Accessibility
**Learning:** Visual-only step indicators (divs) leave screen reader users lost in multi-step forms.
**Action:** Use semantic `<nav>` and `<ol>` with `aria-label`, `aria-current="step"`, and hidden status text for each step.

## 2026-10-27 - Accessible Accordions
**Learning:** Accordion toggles lacking `aria-expanded` and `aria-controls` do not convey state or relationship to screen reader users. In Vue/Nuxt, mapping IDs dynamically in `v-for` loops without a unique prefix can cause ID collisions if the component is reused.
**Action:** Use Nuxt 3's `useId()` (or Vue 3.5+) to generate a unique prefix for accordion item IDs. Always implement `aria-expanded` on the trigger, `aria-controls` linking to the content, and `role="region"` with `aria-labelledby` on the collapsible content container. Hide decorative icons inside the toggle with `aria-hidden="true"`.

## 2026-10-28 - Skip to Main Content Link Target Focus
**Learning:** When linking to a main content area (`#main-content`) via a "Skip to main content" link, simply assigning the ID is not enough. Without `tabindex="-1"` and `focus:outline-none` on the target container, the browser might not programmatically transfer focus correctly, or it will display an undesirable focus ring around the entire main layout.

## 2026-10-29 - Repeating Visual Elements Accessibility (Star Ratings)
**Learning:** Rendering repeating visual elements like a 5-star rating using a loop of `aria-hidden="true"` icons leaves the rating completely invisible to screen readers, missing a crucial piece of social proof or feedback.
**Action:** When implementing repeating visual elements representing a single combined value (like a star rating), wrap the elements in a container with `role="img"` and a descriptive `aria-label` (e.g., `aria-label="Ocena 5 od 5 zvezdic"`), while keeping the individual child elements `aria-hidden="true"`.
## 2026-10-30 - Form Input Disabled States and Labels
**Learning:** Using placeholder text alone for form inputs is an accessibility violation, and inputs often lack disabled states during asynchronous submission, which leaves users uncertain if their actions registered.
**Action:** Always provide explicit visual or `aria-label` labels for inputs and pair form submissions with disabled states using `disabled:opacity-50 disabled:cursor-not-allowed` to improve user feedback.

## 2026-10-31 - Async Interaction Feedback
**Learning:** Adding an inline SVG spinner directly within the submit button during the `isSubmitting` state (using Tailwind's `animate-spin` and `flex gap-2`) provides crucial immediate visual feedback and improves the perceived performance of async forms.
**Action:** Always provide a loading indicator (spinner) and pair it with disabled states for async buttons.
## 2026-08-07 - Use get_by_role instead of get_by_label for form inputs with nested elements\n**Learning:** Playwright's `get_by_label` can fail to interact with form inputs if the associated `<label>` contains nested elements (like `<span aria-hidden="true">*</span>`).\n**Action:** Use `get_by_role('textbox', name='...')` with `exact=False` or `exact=True` (omitting the nested text) to reliably target form inputs for interaction in Playwright scripts.
## 2024-10-27 - [Add loading state to order form]
**Learning:** For a11y and consistency across the app, loading state spinners in buttons should ideally be paired with `disabled` forms so the user is prevented from firing multiple submissions simultaneously. Utilizing SVG classes like `animate-spin` is highly effective when paired with standard Tailwind utilities.
**Action:** When adding spinners, make sure they are visually hidden or unannounced (e.g., using `aria-hidden="true"`) to prevent verbose SR reading, and ensure flex wrappers keep the text and icon aligned well.
## 2026-10-31 - Dynamic Accordion Accessibility with useId()
**Learning:** In Nuxt 3 applications, accordion or toggle components rendered inside `v-for` loops can suffer from ID collisions if they don't use unique IDs per instance, breaking `aria-controls` and `aria-labelledby` relationships.
**Action:** Use the `useId()` composable in the `<script setup>` block to generate a unique prefix for the component instance, and append the loop index to it to create robust, globally unique IDs for accessibility attributes.
## 2025-05-27 - Generic Button Labels
**Learning:** E-commerce list pages often have generic repeating buttons (like "Kupi" or "Add to Cart") which are completely inaccessible to screen reader users scanning the page by buttons, as they lack context.
**Action:** Always add a dynamic `aria-label` appending the item name (e.g., `:aria-label="'Kupi ' + product.name"`) to provide necessary context for assistive technologies.
## 2026-10-31 - Async Interaction Feedback with Spinners
**Learning:** For a11y and consistency across the app, loading state spinners in buttons should ideally be paired with `disabled` forms so the user is prevented from firing multiple submissions simultaneously. Utilizing SVG classes like `animate-spin` is highly effective when paired with standard Tailwind utilities.
**Action:** When adding spinners, make sure they are visually hidden or unannounced (e.g., using `aria-hidden="true"`) to prevent verbose SR reading, and ensure flex wrappers keep the text and icon aligned well.

## 2026-08-14 - Icon-only Social Links Accessibility
**Learning:** Icon-only social links (like Instagram icons) in the footer often lack accessible names, making them unannounced by screen readers, and frequently miss explicit focus states for keyboard users.
**Action:** Always provide an `aria-label` (localized) on the `<a>` tag and pair it with Tailwind's `focus-visible:ring-2` utilities to ensure the link is perceivable by all users.

## 2026-08-17 - Instagram Feed Link Keyboard Accessibility
**Learning:** Icon-only social links (like Instagram icons) often lack accessible names or proper focus states. An icon + text link might have hover animation (e.g. `group-hover:translate-x-1`) but misses the same feedback for keyboard users.
**Action:** Add `group-focus:translate-x-1` and `focus-visible:ring-2` for keyboard users. Apply `aria-hidden="true"` to the decorative SVG to prevent redundant reading by screen readers since the visible text already provides context.

## 2026-10-31 - Keyboard Accessibility on Informational Links
**Learning:** Links and NuxtLinks used as CTAs (like "Oglejte si Cenik", "Rezerviraj Termin", or external links like Google reviews) often lack keyboard focus states (`focus-visible:ring-2`), making them hard to use for keyboard navigators, even if they have nice hover states for mouse users.
**Action:** Always add standard focus styling (`focus-visible:ring-2 focus-visible:ring-accent focus:outline-none rounded-sm`) to interactive elements. Also, if they use `group-hover` for internal element changes (like arrow movement), pair it with `group-focus-within` to mirror the interaction for keyboard users.

## 2026-08-20 - Focus States on Primary CTAs
**Learning:** The primary calls-to-action (CTAs) across the application, including hero buttons, form submit buttons, and mobile sticky buttons, were missing explicit keyboard focus states, hindering accessibility for keyboard navigation users.
**Action:** Standardize focus states on all interactive elements (buttons, links) by explicitly appending the `focus-visible:ring-2 focus-visible:ring-accent focus:outline-none rounded-sm` Tailwind pattern to ensure clear visibility without interfering with mouse usage.
