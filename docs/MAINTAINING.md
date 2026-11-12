# Maintaining the IntroSkip Kodi repository

This repository is deliberately separate from the add-on source.

## Layout

```text
repository.introskip/
├── .github/workflows/build-repository.yml
├── _repo_generator.py
├── index.html
├── repo/
│   └── repository.introskip/
│       └── addon.xml
└── repo/zips/                 # generated and committed by Actions
    ├── addons.xml
    ├── addons.xml.md5
    ├── repository.introskip/
    └── service.introskip/
```

The service folder is downloaded from `zoeywowy/service.introskip` during the workflow. It is not maintained as a second copy here.

## Build and publish

1. Open **Actions → Build Kodi repository**.
2. Select **Run workflow** to package the latest service source.
3. The workflow runs the upstream-style repository generator, checks the XML, checksum and ZIP contents, commits generated packages, and deploys the installer page.
4. Check the workflow's final public URL tests before installing the update in Kodi. The GitHub Pages URL is a human-facing download page, not a Kodi File Manager source. Users download the bootstrap ZIP in a browser and install it from local storage or a network share.

A daily scheduled run also checks the add-on source for a newer manifest version. For a new service release, bump the version in the service repository's `addon.xml` before running the workflow.

## Important Kodi details

The repository add-on manifest uses the standard pattern:

- `info compressed="false"` points to the generated `addons.xml`.
- `checksum` points to the matching `addons.xml.md5`.
- `datadir zip="true"` points to the directory containing the per-add-on ZIP folders.
- Each package is stored at `<addon-id>/<addon-id>-<version>.zip`.

Do not replace these URLs with GitHub Pages URLs. The Pages site is only the human-facing bootstrap download page; the Kodi index and packages use raw GitHub URLs.

## Reference

The layout and generator are based on [drinfernoo/repository.example](https://github.com/drinfernoo/repository.example). The generator is kept in this repository with its upstream implementation and attribution.
