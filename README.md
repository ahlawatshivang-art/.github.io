# Shivang Ahlawat — Portfolio

Personal portfolio for ECE 1100. Plain HTML + CSS, no build step, hosted free on GitHub Pages.

**Live at:** https://ahlawatshivang-art.github.io

---

## File layout

```
index.html        → Home tab (cover + contact)
about.html        → About tab (story, education, experience, goals, hobbies)
projects.html     → Projects tab
resume.html       → Resume tab (embedded PDF + download)
assets/
  css/style.css   → ALL design settings (colors, fonts, spacing)
  js/main.js      → tab highlighting + fade-in animation
  images/         → photos
  resume/         → resume PDF
.nojekyll         → tells GitHub Pages to serve files as-is
```

---

## Publishing (first time)

1. On GitHub, create a **new public repository** named exactly **`ahlawatshivang-art.github.io`**.
2. Upload these files, either way:
   - **Browser:** on the new repo page click *uploading an existing file*, drag in everything from this folder (including the `assets` folder and `.nojekyll`), and commit.
   - **Command line:**
     ```bash
     cd portfolio
     git init
     git add .
     git commit -m "Initial portfolio"
     git branch -M main
     git remote add origin https://github.com/ahlawatshivang-art/ahlawatshivang-art.github.io.git
     git push -u origin main
     ```
3. In the repo go to **Settings → Pages**, set *Source* to **Deploy from a branch**, branch **main**, folder **/ (root)**, then save.
4. Wait a minute or two, then visit https://ahlawatshivang-art.github.io.

After that, every change you commit goes live automatically within a minute or two.

> `.nojekyll` starts with a dot, so it may be hidden on Mac/Windows. If it gets left out, the site still works; it just makes Pages a little faster and more predictable.

---

## Editing

You can edit any file directly on GitHub (open the file → pencil icon → *Commit changes*) or locally in VS Code. To preview locally, just double-click `index.html`.

Look for `<!-- EDIT: ... -->` comments in the HTML; they mark the spots meant for your text.

### Replace a placeholder
Placeholder lines look like:
```html
<p class="placeholder">[Describe this experience.]</p>
```
Replace with normal text (drop `class="placeholder"`, which makes text grey and italic):
```html
<p>Fabricated GaN-on-Si prototypes using photolithography and PECVD...</p>
```

### Add a text box (a new section)
Paste this anywhere inside `<main>`:
```html
<section class="block reveal">
  <h2>Section Title</h2>
  <p>Your text here.</p>
</section>
```
Want it inside a panel? Wrap the text in `<div class="card"> ... </div>`.

### Add bullet points
```html
<ul>
  <li>First point</li>
  <li>Second point</li>
</ul>
```

### Add an experience entry (about.html)
Copy one whole `<div class="card reveal" ...>` block under **EXPERIENCE** and change the title, dates, organization and text.

### Add a project (projects.html)
Copy one whole `<article class="card project reveal"> ... </article>` block.
- Status badge: `class="status"` → *In Progress*, `class="status done"` → *Completed*.
- Tags: add or remove `<li>` items in the `<ul class="tags">` list.

### Add or swap an image
1. Put the image in `assets/images/` (JPG or PNG; keep it under ~1 MB — around 1200 px wide is plenty).
2. Reference it:
   ```html
   <img src="assets/images/my-photo.jpg" alt="Short description of the photo">
   ```
- **Project image:** replace the `Image coming soon` text inside `<div class="thumb">` with the `<img>` tag.
- **Image with a caption:**
  ```html
  <figure>
    <img src="assets/images/my-photo.jpg" alt="...">
    <figcaption>Caption text</figcaption>
  </figure>
  ```
- **Swap the headshot:** replace `assets/images/headshot.jpg` with a new file of the same name.
- **Remove an image:** delete the `<img>` (or `<figure>`) tag.

### Update the resume
Replace `assets/resume/Shivang-Ahlawat-Resume.pdf` with your new PDF, keeping the same file name.

### Add a new tab/page
1. Copy `about.html`, rename it (e.g. `leadership.html`), and change the content inside `<main>`.
2. Add a link to the tab list in **every** page's header:
   ```html
   <li><a href="leadership.html">Leadership</a></li>
   ```

### Fade-in animation
Any element with `reveal` in its class fades in on scroll. Remove `reveal` to keep something static.

---

## Changing the design

Open `assets/css/style.css`. Everything at the top under `:root` controls the whole site:

| Variable     | What it controls                        | Current     |
|--------------|-----------------------------------------|-------------|
| `--bg`       | Page background (deep navy)             | `#0e1524`   |
| `--surface`  | Cards / panels                          | `#151e31`   |
| `--border`   | Thin divider lines                      | `#26324d`   |
| `--text`     | Main text                               | `#e7eaf3`   |
| `--muted`    | Secondary text                          | `#9aa4bb`   |
| `--accent`   | Peach — links, buttons, active tab      | `#f2bfa8`   |
| `--accent-2` | Soft blue — tags, labels                | `#a9c3ea`   |
| `--font`     | Font family (Inter)                     |             |
| `--max-width`| Content width                           | `1040px`    |
| `--radius`   | Corner roundness                        | `14px`      |

Some alternative pastel accents to try: lavender `#c9b8f0`, sage `#b5d3bd`, rose `#f0b8c8`, mint `#a8e0d1`.

To change the font: pick one at [fonts.google.com](https://fonts.google.com), replace the `<link href="https://fonts.googleapis.com/...">` line in each HTML file, and update `--font`.
