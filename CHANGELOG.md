# Repository release notes

**Current packaged IntroSkip service:** 0.0.30.

## 1.0.5 — Kodi 22 File Manager installation

**12 November 2026**

- Separated the repository installer and package feed from the service source.
- Uses the standard Kodi repository layout: `addons.xml`, matching `addons.xml.md5`, and versioned ZIP packages.
- Uses `datadir zip="true"` for the package directory.
- Publishes the first-install ZIP on GitHub Pages with a Kodi 22-compatible relative link.
- Adds automated checks for the generated page, deployed page, repository metadata, checksums and ZIP contents.
- Includes IntroSkip service 0.0.28, the low-resource Kodi 22 pre-release.

Earlier combined-repository experiments are superseded by this separate layout.
