# IntroSkip Kodi Repository — Release Notes

## 1.0.4 — Separate repository installer
**12 November 2026**

- Published the Kodi repository from its own project, separate from the IntroSkip service source.
- Followed the established Kodi layout demonstrated by [drinfernoo/repository.example](https://github.com/drinfernoo/repository.example).
- Uses raw GitHub for `addons.xml`, the matching `addons.xml.md5`, and versioned ZIPs under `addon.id/addon.id-version.zip`.
- Declares `datadir zip="true"` in the repository add-on manifest.
- Bumped the installer above the legacy 1.0.3 version so existing installations can upgrade in place.
- Automated builds validate both packages, regenerate the index and checksum, and deploy the GitHub Pages bootstrap page.
- Included service version: IntroSkip **0.0.25**.

## 1.0.0–1.0.3 — Earlier combined-repository experiments

These versions were created while the repository feed and service source were still being hosted together. They are superseded by the separate repository layout in 1.0.4.
