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

## 2026-10-27 - Scroll Container Semantics
**Learning:** Scrollable containers without semantics are invisible to screen readers and keyboard inaccessible if they lack `tabindex`.
**Action:** Add `tabindex="0"`, `role="region"`, `aria-label`, and `aria-controls` on buttons to make the scroll area fully accessible.
