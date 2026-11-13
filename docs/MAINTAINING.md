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
4. Check the workflow's final public URL tests before asking users to refresh Kodi. The GitHub Pages root is also the Kodi File Manager source; it must expose the bootstrap ZIP as a parseable HTML link.

A daily scheduled run also checks the add-on source for a newer manifest version. For a new service release, bump the version in the service repository's `addon.xml` before running the workflow.

## Important Kodi details

The repository add-on manifest uses the standard pattern:

- `info compressed="false"` points to the generated `addons.xml`.
- `checksum` points to the matching `addons.xml.md5`.
- `datadir zip="true"` points to the directory containing the per-add-on ZIP folders.
- Each package is stored at `<addon-id>/<addon-id>-<version>.zip`.

Do not replace these URLs with GitHub Pages URLs. The Pages site exposes the bootstrap ZIP to Kodi's HTTP directory browser. The Kodi index and service packages use raw GitHub URLs.

## Kodi HTTP directory parsing

Kodi 22's `CHTTPDirectory` does not treat an arbitrary HTML page as a general web page. It extracts links using an anchor pattern that starts with `<a href="...">`. Therefore the bootstrap link must follow these rules:

- `href` must be the first attribute after `<a` (a CSS class may follow it, not precede it).
- The visible anchor text must exactly match the relative filename in `href`.
- The ZIP itself must be published in the GitHub Pages root beside `index.html`.
- Keep the link relative, for example `<a href="repository.introskip-1.0.5.zip">repository.introskip-1.0.5.zip</a>`.

The workflow runs a regression check using Kodi's `CHTTPDirectory` anchor pattern against both the generated page and the deployed public page, and downloads/tests the ZIP. This catches attribute-order or filename mismatches before release. See [Kodi's HTTPDirectory implementation](https://github.com/xbmc/xbmc/blob/Piers/xbmc/filesystem/HTTPDirectory.cpp) and the [repository.example template](https://github.com/drinfernoo/repository.example).

## Reference

The layout and generator are based on [drinfernoo/repository.example](https://github.com/drinfernoo/repository.example). The generator is kept in this repository with its upstream implementation and attribution.
