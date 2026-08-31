## 💡 What

Added keyboard focus states (`focus-visible:ring-2 focus-visible:ring-accent focus:outline-none rounded-sm`) to the primary Call-To-Action (CTA) links (`<NuxtLink>`) on the "O Nas" (About Us) page.

## 🎯 Why

Previously, these interactive elements relied on browser default focus outlines (which were often stripped by global styles) or only had mouse-specific hover states (`hover:-translate-y-1` and `hover:text-white`). This lack of visual feedback made it extremely difficult for users navigating with a keyboard (using the `Tab` key) to identify which link was currently focused, negatively impacting the site's accessibility and usability for these users.

## 📸 Before/After

*See the attached visual verification screenshots and video demonstrating the new explicit focus rings when tabbing through the page.*

## ♿ Accessibility

*   **Keyboard Navigation:** Improved keyboard operability and perceivability by providing clear, standardized visual indicators for focused interactive elements, adhering to WCAG 2.1 Success Criterion 2.4.7 (Focus Visible).
