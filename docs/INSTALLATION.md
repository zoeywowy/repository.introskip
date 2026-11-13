# Install IntroSkip on Kodi 22

The repository is a one-time installation. After it is installed, Kodi can install and update IntroSkip normally.

## First installation

1. Open **Settings → File manager → Add source**.
2. Enter `https://zoeywowy.github.io/repository.introskip/`.
3. Name the source **IntroSkip Repository**.
4. Open **Add-ons → Install from zip file**.
5. Select **IntroSkip Repository**. Kodi should list the current `repository.introskip-<version>.zip`.
6. Select the ZIP and wait for Kodi to confirm that the repository add-on is installed.
7. Open **Add-ons → Install from repository → IntroSkip Repository → Services → IntroSkip** and select **Install**.

No browser download, manual ZIP transfer or extraction is required.

## Updates

Once installed, Kodi reads the repository's add-on index and checksum, then retrieves service packages from the configured ZIP directory. IntroSkip updates are delivered through Kodi's normal add-on manager.

The bootstrap ZIP is only needed for the initial repository installation or if the repository add-on itself must be reinstalled.

## If Kodi shows an empty source

If the source shows only `..` and **0 items**:

1. Confirm the [Build Kodi repository workflow](https://github.com/zoeywowy/repository.introskip/actions) completed successfully.
2. Remove and re-add the File Manager source to refresh a stale entry.
3. Restart Kodi and try again.

Kodi 22 reads the bootstrap ZIP from a relative HTML link. The link must begin with `<a href="...">`, and its visible text must match the ZIP filename. The automated build checks both the generated page and the deployed public page.

If the source is still empty, capture a fresh Kodi log after opening it and report the result in an [issue](https://github.com/zoeywowy/service.introskip/issues/new). Do not switch to a manual download unless you intentionally want to bypass repository-based updates.
