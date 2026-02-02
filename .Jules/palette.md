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
