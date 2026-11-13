# Install IntroSkip on Kodi 22

The intended installation uses Kodi's File Manager source. You do not need to download the ZIP in a separate browser, move it to Kodi, or browse local storage.

## One-time repository installation

1. In Kodi, open **Settings → File manager → Add source**.
2. Enter `https://zoeywowy.github.io/repository.introskip/`.
3. Name the source **IntroSkip Repository** and save it.
4. Open **Add-ons → Install from zip file**.
5. Select the **IntroSkip Repository** source. Kodi should list `repository.introskip-1.0.5.zip`.
6. Select that ZIP and wait for Kodi to confirm that **IntroSkip Repository** is installed.
7. Open **Add-ons → Install from repository → IntroSkip Repository → Services → IntroSkip** and select **Install**.

The bootstrap ZIP is linked with a relative filename from the GitHub Pages root. This mirrors the working A4K repository pattern: the Kodi File Manager source points to the website root, and Kodi enumerates the ZIP link on that page.

## Updating

After the repository add-on is installed, Kodi reads the feed's `addons.xml` and matching checksum, then downloads service packages from the configured ZIP data directory. Future IntroSkip releases are installed through Kodi's normal repository update mechanism. The bootstrap ZIP is only needed for the initial repository installation or if the repository add-on itself must be reinstalled.

## If Kodi shows an empty source

If selecting **IntroSkip Repository** under **Install from zip file** shows only `..` and **0 items`, do not download a ZIP manually yet. That means Kodi is not seeing the relative ZIP link from the published page.

- Confirm the GitHub Actions **Build Kodi repository** workflow succeeded: [Actions](https://github.com/zoeywowy/repository.introskip/actions).
- Confirm the Pages site has deployed the latest commit: [Deployments](https://github.com/zoeywowy/repository.introskip/deployments).
- Remove and re-add the File Manager source to clear a stale source entry.
- Restart Kodi and try again.

If it remains empty, capture a fresh `kodi.log` after opening the source. The relevant lines will show whether Kodi received the HTML page and whether it parsed the relative ZIP link.

## Repository feed troubleshooting

After the bootstrap repository add-on is installed, Kodi uses:

- [Kodi add-on index](https://raw.githubusercontent.com/zoeywowy/repository.introskip/main/repo/zips/addons.xml)
- [Matching checksum](https://raw.githubusercontent.com/zoeywowy/repository.introskip/main/repo/zips/addons.xml.md5)
- [ZIP package directory](https://github.com/zoeywowy/repository.introskip/tree/main/repo/zips)

The repository add-on declares the index, checksum, and `datadir zip="true"` using the standard Kodi layout. If the repository cannot connect after installation, check these endpoints and provide a fresh Kodi log.

