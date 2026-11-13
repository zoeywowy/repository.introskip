# IntroSkip Kodi Repository

The official third-party Kodi repository feed for [IntroSkip](https://github.com/zoeywowy/service.introskip). This project keeps the repository installer and package feed separate from the add-on source.

## Install on Kodi 22

**No browser download or file transfer is required.** Add the repository website as a Kodi File Manager source. The website exposes the bootstrap ZIP as a relative file link, following the same approach used by the [A4K repository](https://github.com/a4k-openproject/a4k-openproject.github.io).

1. In Kodi, open **Settings → File manager → Add source**.
2. Enter this exact address: `https://zoeywowy.github.io/repository.introskip/`
3. Name the source **IntroSkip Repository**.
4. Open **Add-ons → Install from zip file**.
5. Select **IntroSkip Repository**. Kodi should show `repository.introskip-1.0.5.zip`.
6. Select the ZIP to install the repository add-on.
7. Open **Add-ons → Install from repository → IntroSkip Repository → Services → IntroSkip** and install IntroSkip.

If the source opens but Kodi shows only `..` and **0 items**, the published page or Kodi's cached copy is not exposing the relative ZIP link. Check the [latest build](https://github.com/zoeywowy/repository.introskip/actions) and reload the source after a successful deployment. Do not switch to a manual download as the intended installation method.

## How it works

- `repo/repository.introskip/` contains the repository add-on manifest.
- `repo/zips/addons.xml` and `addons.xml.md5` provide Kodi's add-on index and checksum.
- `repo/zips/<addon-id>/<addon-id>-<version>.zip` stores installable add-on packages.
- The GitHub Pages root publishes the bootstrap ZIP and a relative link that Kodi can enumerate through File Manager.
- The installed repository add-on then reads the raw GitHub index and ZIP package directory for normal installation and updates.

The service source lives in [zoeywowy/service.introskip](https://github.com/zoeywowy/service.introskip). The repository build workflow packages that source, updates the index/checksum, publishes the bootstrap ZIP, and deploys the Kodi-facing landing page.

## Development

Run **Actions → Build Kodi repository → Run workflow** to rebuild. A scheduled run also checks for changes. See [MAINTAINING.md](docs/MAINTAINING.md) and [INSTALLATION.md](docs/INSTALLATION.md).

