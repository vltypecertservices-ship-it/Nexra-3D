# Repository AI agent guidance

## What this project is

This repository is a small static website for a 3D printing business.

- Source pages are in `src/`.
- Site styles are in `public/css/style.css`.
- Images and visual assets are in `public/images/`.
- `out/` contains rendered/exported output copies of the site; prefer editing `src/` and `public/` unless the user explicitly asks to update generated output.
- `patch_logo_css.py` is a small helper script that edits a CSS pattern in `public/css/style.css`.

## How to work here

- Edit HTML in `src/*.html` for page content and structure.
- Keep the existing header/footer and navigation conventions.
- Preserve the relative asset paths used in HTML, e.g. `../public/css/style.css` and `../public/images/...`.
- Edit CSS in `public/css/style.css` for styling changes.
- Do not introduce a build system or framework unless the user asks for one.

## Notes for agents

- There is no package manager, build script, or test command in the repo.
- If asked to add a new page, update navigation links consistently in the shared header.
- If asked to fix layout or visual issues, first check `src/layout.html` and `public/css/style.css`.
- Avoid changing `out/` manually if the source files in `src/` or `public/` are still the authoritative source.
