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

## 2024-07-23 - Add explicit labels to form inputs and disable during submission
**Learning:** For accessibility, form inputs like emails need explicitly bound labels (via `for` and `id`), along with hidden indicators (like `aria-hidden="true"` on asterisks) so screen readers parse required fields correctly without reading out decorative characters. Additionally, disabling all inputs during an asynchronous submission explicitly informs the user that the form is processing and prevents double-submissions.
**Action:** When creating or modifying forms, ensure all inputs have a properly associated label, and bind all interactive form fields (inputs, selects, textareas) and visually custom elements (like proxy checkboxes) to the reactive `isSubmitting` state using the `:disabled` attribute and appropriate Tailwind CSS variants (`disabled:opacity-50`, `peer-disabled:opacity-50`).
