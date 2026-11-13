# IntroSkip Kodi Repository

Install and update [IntroSkip](https://github.com/zoeywowy/service.introskip) through Kodi 22's normal add-on manager.

## Install

No browser download or manual file transfer is needed.

1. In Kodi, open **Settings → File manager → Add source**.
2. Enter `https://zoeywowy.github.io/repository.introskip/`.
3. Name the source **IntroSkip Repository**.
4. Open **Add-ons → Install from zip file**.
5. Select **IntroSkip Repository** and install the repository ZIP Kodi lists.
6. Open **Add-ons → Install from repository → IntroSkip Repository → Services → IntroSkip**.
7. Select **Install**.

The [installation guide](docs/INSTALLATION.md) includes update and troubleshooting steps.

## How it works

- GitHub Pages hosts the small first-install repository ZIP.
- The installed repository add-on reads the generated `addons.xml` index, matching MD5 checksum and versioned packages from this repository.
- The service source and its installable ZIP are built from [service.introskip](https://github.com/zoeywowy/service.introskip).
- Kodi handles normal add-on installation and updates after the repository is installed.

## Maintain the feed

Run **Actions → Build Kodi repository → Run workflow** after a new service release. The workflow packages the service, regenerates the Kodi index and checksum, validates the ZIPs, and deploys the Pages installer.

See [MAINTAINING.md](docs/MAINTAINING.md) for the build details.

[Service source](https://github.com/zoeywowy/service.introskip) · [Releases](https://github.com/zoeywowy/service.introskip/releases) · [Issues](https://github.com/zoeywowy/service.introskip/issues)
