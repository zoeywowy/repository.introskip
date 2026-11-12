# Install the IntroSkip Kodi repository

The GitHub Pages address is an information page, not a ZIP directory. Kodi’s **Install from zip file** browser cannot open a webpage or click its download button. Download the bootstrap ZIP directly in a normal browser first.

## One-time installation

1. Open the [IntroSkip download page](https://zoeywowy.github.io/repository.introskip/) in a web browser.
2. Download `repository.introskip-1.0.4.zip`. Keep it as a ZIP; do not extract it.
3. Make the downloaded ZIP available to Kodi:
   - **Windows:** leave it in your Downloads folder.
   - **Android / Fire TV:** download it on the device if a browser is available, or copy it from a computer using USB or a shared network folder.
   - **Other devices:** use a local folder, USB drive or network share Kodi can browse.
4. In Kodi, open **Add-ons → Install from zip file**.
5. Browse to the downloaded ZIP and select `repository.introskip-1.0.5.zip`.
6. Wait for Kodi to confirm **IntroSkip Repository** was installed.
7. Open **Add-ons → Install from repository → IntroSkip Repository → Services → IntroSkip** and select **Install**.

The repository ZIP is a small bootstrap installer. Once it is installed, Kodi reads the add-on index and packages from the separate repository feed and can receive future IntroSkip updates normally.

## Updating

After the repository is installed, Kodi can check its feed for newer versions. You do not need to download the bootstrap ZIP again for ordinary IntroSkip service updates.

## If Kodi shows an empty folder

If the Install from zip file browser shows only `..` and `0 items`, Kodi is looking at a location that contains no downloadable ZIP file.

1. Cancel the empty browser.
2. Download the ZIP using the direct link in this guide.
3. Open Install from zip file again and select the ZIP from Downloads, USB or a network share.

## If Kodi cannot connect after installation

- Confirm the repository add-on is installed and enabled.
- Confirm the latest [GitHub Actions build](https://github.com/zoeywowy/repository.introskip/actions) succeeded.
- Open the [repository index](https://raw.githubusercontent.com/zoeywowy/repository.introskip/main/repo/zips/addons.xml) and [matching MD5 checksum](https://raw.githubusercontent.com/zoeywowy/repository.introskip/main/repo/zips/addons.xml.md5) in a browser.
- If both are reachable but Kodi still cannot connect, restart Kodi and capture a fresh `kodi.log` immediately after the failed refresh.

Do not uninstall the IntroSkip service or clear its settings to troubleshoot the repository. Reinstalling the repository add-on does not require removing IntroSkip.

## Official Kodi instructions

Kodi's [Install add-ons from ZIP files](https://kodi.wiki/view/Archive%3AInstall_add-ons_from_zip_files) guide explains that the ZIP can be stored on local storage or a network share.
