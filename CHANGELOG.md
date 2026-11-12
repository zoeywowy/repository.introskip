# IntroSkip Kodi Repository — Release Notes

## 1.0.0 — First separate Kodi repository
**12 November 2026**

- Created a dedicated repository project, separate from the IntroSkip service source.
- Followed the established Kodi repository layout demonstrated by [drinfernoo/repository.example](https://github.com/drinfernoo/repository.example).
- Added a repository installer with raw GitHub `addons.xml`, matching `addons.xml.md5`, and `datadir zip="true"`.
- Published the first versioned packages for `repository.introskip` and `service.introskip`.
- Added an automated build that validates package layout, checks the public endpoints, and deploys the GitHub Pages bootstrap page.

The included service add-on is IntroSkip **0.0.24**.
