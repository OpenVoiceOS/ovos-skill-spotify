> # ⚠️ DEPRECATED
>
> This OCP **search skill** is deprecated and unmaintained. OCP search skills
> (`OVOSCommonPlaybackSkill` + `@ocp_search`) are replaced by **MediaProvider**
> plugins loaded in-process by the
> [`ovos-ocp-pipeline-plugin`](https://github.com/OpenVoiceOS/ovos-ocp-pipeline-plugin) —
> the catalog/search half moves to
> [`ovos-media-provider-spotify`](https://github.com/OpenVoiceOS/ovos-media-provider-spotify),
> dispatched in-process by the OCP pipeline, and playback moves to
> [`ovos-media-plugin-spotify`](https://github.com/OpenVoiceOS/ovos-media-plugin-spotify),
> a playback backend that belongs to the `ovos-media` player daemon.
> Both packages are published, but they only do anything once the OCP
> pipeline's MediaProvider dispatch is the default search path and
> `ovos-media` is running as your player — installing them does not replace
> this skill under the legacy OCP/`ovos-audio` stack.
>
> - **How MediaProviders work / how to migrate:** https://github.com/OpenVoiceOS/ovos-media/blob/dev/docs/media-providers.md
> - **Base-class deprecation:** [ovos-workshop#423](https://github.com/OpenVoiceOS/ovos-workshop/pull/423)
>
> This skill keeps working until the OCP pipeline's MediaProvider dispatch
> becomes the default search path and this repository is archived.

# OVOS Spotify skill

OCP skill for spotify

This skill requires additional setup and components

## Setup

Install and configure the companion plugin [ovos-media-plugin-spotify](https://github.com/OpenVoiceOS/ovos-media-plugin-spotify)

`pip install ovos-media-plugin-spotify`

this skill only handles the voice search, plugin is needed to handle playback of spotify uris provided by this skill

## Oauth

Currently Oauth needs to be performed manually

after installing the plugin run `ovos-spotify-oauth` on the command line and follow the instructions

```
$ ovos-spotify-oauth
This script creates the token information needed for running spotify
        with a set of personal developer credentials.

        It requires the user to go to developer.spotify.com and set up a
        developer account, create an "Application" and make sure to whitelist
        "https://localhost:8888".

        After you have done that enter the information when prompted and follow
        the instructions given.
        
YOUR CLIENT ID: xxxxx
YOUR CLIENT SECRET: xxxxx
Go to the following URL: https://accounts.spotify.com/authorize?client_id=xxx&response_type=code&redirect_uri=https%3A%2F%2Flocalhost%3A8888&scope=user-library-read+streaming+playlist-read-private+user-top-read+user-read-playback-state
Enter the URL you were redirected to: https://localhost:8888/?code=.....
ocp_spotify oauth token saved
```

## Examples 

* "play heavy metal"
* "play motorhead"


## Credits

- [@forslund](https://github.com/forslund)
