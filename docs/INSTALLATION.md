# Install IntroSkip through Kodi

## One-time repository setup

1. In Kodi 22, open **Settings → File manager → Add source**.
2. Enter `https://zoeywowy.github.io/repository.introskip/`.
3. Give the source a short name, such as **IntroSkip Repository**.
4. Open **Add-ons → Install from zip file**.
5. Select the source you just added, then choose `repository.introskip-1.0.4.zip`.
6. Wait for Kodi to confirm that **IntroSkip Repository** was installed.
7. Open **Add-ons → Install from repository → IntroSkip Repository → Services → IntroSkip** and install it.

## Updating

Once the repository is installed, Kodi checks its index for newer versions. Use **Add-ons → My add-ons → Services → IntroSkip** to view or configure the installed service.

## If Kodi cannot connect

- Check the File Manager source character by character. It must use `repository.introskip`, not `service.introskip`.
- Confirm the repository's latest [GitHub Actions run](https://github.com/zoeywowy/repository.introskip/actions) succeeded.
- Open the [repository index](https://raw.githubusercontent.com/zoeywowy/repository.introskip/main/repo/zips/addons.xml) and [checksum](https://raw.githubusercontent.com/zoeywowy/repository.introskip/main/repo/zips/addons.xml.md5) in a browser.
- If both open, but Kodi still cannot connect, restart Kodi and capture a new Kodi log from the failed refresh.

Do not uninstall the IntroSkip service to troubleshoot the repository. Updating or reinstalling the repository add-on does not require removing your IntroSkip settings.
