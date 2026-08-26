# Bambie Digital Works — brand pack

Canonical logo assets for the Bambie Digital Works organization. Optimized
exports from the isometric 3D wordmark for websites, apps, and GitHub.

**Palette:** navy + cyan · **Masters:** lockup (wordmark) + mark (stack icon)

This folder lives in the org [`.github`](https://github.com/Bambie-Digital-Works/.github)
repository so every project can reuse the same brand drop.

## Quick pick

| Use | File |
|-----|------|
| Browser tab icon | `web/favicon.ico` |
| Site header (light) | `web/logo-lockup.png` (+ `@2x`) |
| Site header (dark UI) | `web/logo-lockup-dark.png` (+ `@2x`) |
| Open Graph / Twitter card | `web/og-image.png` |
| PWA / Android icons | `web/icon-192.png`, `web/icon-512.png` |
| iOS home screen | `web/apple-touch-icon.png` |
| App store master | `app/icon-1024.png` |
| GitHub profile / org avatar | `github/avatar.png` |
| Repo social preview | `github/social-preview.png` |
| README header | `github/readme-banner.png` |

Dark-theme twins: `*-dark.png` next to the light files above.

---

## Folder map

```
brand/
  source/          Master art (do not resize by hand — re-run build_pack.py)
  web/             Favicon, PWA, header lockups, OG
  app/             Square app icons
  github/          Avatar, social preview, README banner
  build_pack.py    Regenerates sized exports from source/
```

There is no SVG — this brand mark is 3D CGI and stays raster.

---

## Website

Copy the `web/` files into your site (e.g. `/public/`). Add to `<head>`:

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">

<meta property="og:image" content="https://example.com/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://example.com/og-image.png">
```

Example `site.webmanifest` icons:

```json
{
  "name": "Bambie Digital Works",
  "short_name": "Bambie",
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ],
  "display": "standalone",
  "background_color": "#E8EEF5",
  "theme_color": "#0B1220"
}
```

Header image:

```html
<img
  src="/logo-lockup.png"
  srcset="/logo-lockup.png 1x, /logo-lockup@2x.png 2x"
  width="800"
  alt="Bambie Digital Works"
>
```

Use `logo-lockup-dark.png` on dark backgrounds.

---

## Apps

| Platform | Start from |
|----------|------------|
| iOS / App Store | `app/icon-1024.png` (export remaining sizes in Xcode / Transporter) |
| Android / Play | `app/icon-512.png` (adaptive icon foreground); keep `icon-1024` as master |
| General / Electron | `app/icon-256.png`, `icon-128.png`, `icon-64.png` |

The square **mark** (stack only) is used for app icons so the mark stays legible at small sizes. Do not use the wide lockup as an app icon.

---

## GitHub

1. **Avatar** — Organization → Settings → Profile → Profile picture → upload `github/avatar.png` (or `avatar-dark.png`). Git cannot set the avatar from this repo alone.
2. **Repo social preview** — Repo → Settings → General → Social preview → upload `github/social-preview.png` (1280×640).
3. **README banner** — reference the files in this pack (as used on the org profile):

```html
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="brand/github/readme-banner-dark.png">
    <img src="brand/github/readme-banner.png" alt="Bambie Digital Works" width="640">
  </picture>
</p>
```

From `profile/README.md`, use `../brand/github/...` paths instead.

---

## Regenerating sizes

After replacing files in `source/`:

```powershell
pip install Pillow
python ".\build_pack.py"
```

Source masters:

| File | Role |
|------|------|
| `source/lockup-light.png` | Full wordmark, light studio |
| `source/lockup-dark.png` | Full wordmark, dark studio |
| `source/mark-square.png` | Stack icon only, light |
| `source/mark-square-dark.png` | Stack icon only, dark |
