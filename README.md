# IntroSkip Kodi Repository

This repository is the **Kodi repository installer and package feed** for [IntroSkip](https://github.com/zoeywowy/service.introskip). The first published feed contains **IntroSkip 0.0.24** and repository installer **1.0.4**.

The actual add-on source code lives in a separate repository. Keeping the two projects separate makes the installer, package index and updates easier to maintain.

## Install in Kodi 22

1. Open **Settings → File manager → Add source**.
2. Enter this address:

   `https://zoeywowy.github.io/repository.introskip/`

3. Name the source **IntroSkip Repository**.
4. Open **Add-ons → Install from zip file → IntroSkip Repository**.
5. Select `repository.introskip-1.0.4.zip`.
6. Open **Add-ons → Install from repository → IntroSkip Repository → Services → IntroSkip**.
7. Select **Install**.

If Kodi does not show the repository immediately after installation, wait for its refresh or restart Kodi.

## How the repository works

This project follows the established GitHub-hosted Kodi layout demonstrated by [drinfernoo/repository.example](https://github.com/drinfernoo/repository.example).

- `repo/repository.introskip/` contains the small repository add-on and its `addon.xml`.
- The build workflow downloads and packages the add-on from [service.introskip](https://github.com/zoeywowy/service.introskip).
- `repo/zips/addons.xml` is the generated Kodi add-on index.
- `repo/zips/addons.xml.md5` is the matching MD5 checksum.
- `repo/zips/<addon-id>/<addon-id>-<version>.zip` contains each installable add-on.
- `repository.introskip-1.0.4.zip` in the repository root is the first-install ZIP served by GitHub Pages.

The repository add-on points Kodi directly to the raw GitHub index and package directory. Its `datadir` uses `zip="true"`, as in the reference layout.

## Updating IntroSkip

The **Build Kodi repository** workflow checks out the current `main` branch of `service.introskip`, builds its Kodi ZIP, generates the repository index and checksum, and publishes the installer page.

- Run it manually from **Actions → Build Kodi repository → Run workflow**.
- A daily scheduled run also checks for a newer add-on version.
- The workflow only commits generated packages when they change.

When releasing a new add-on version, update the version in the add-on's own `addon.xml`. The repository generator uses that version to create the package path Kodi expects.

## GitHub Pages setup

Open **Settings → Pages** and set **Build and deployment → Source** to **GitHub Actions**. The workflow publishes the installer page and bootstrap ZIP. Kodi's package index and add-on ZIPs are served from `raw.githubusercontent.com`.

## Troubleshooting

- The File Manager source must be exactly `https://zoeywowy.github.io/repository.introskip/`.
- Do not use the old `service.introskip` Pages address.
- Confirm the latest workflow run completed successfully in [GitHub Actions](https://github.com/zoeywowy/repository.introskip/actions).
- Check that these files open in a browser:
  - [Kodi add-on index](https://raw.githubusercontent.com/zoeywowy/repository.introskip/main/repo/zips/addons.xml)
  - [Matching MD5 checksum](https://raw.githubusercontent.com/zoeywowy/repository.introskip/main/repo/zips/addons.xml.md5)

If Kodi still reports a connection error, capture a fresh Kodi log and share it with the exact time of the failed repository refresh.

## Related projects

- [IntroSkip add-on source](https://github.com/zoeywowy/service.introskip)
- [Kodi repository layout reference](https://github.com/drinfernoo/repository.example)

## Credits

The repository layout and generator are based on the public [repository.example](https://github.com/drinfernoo/repository.example) project by drinfernoo. IntroSkip is an unofficial Kodi add-on and is not part of Kodi's official add-on repository.
