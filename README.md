# github-hooks


Github-hooks is a service to consume Github [push webhooks event](https://developer.github.com/v3/activity/events/types/#pushevent) and trigger an action on it.

It currently only supports git pulling a local git clone.



## Configuration

Configuration must be placed in either `/etc/githubhooks` or `~/.githubhooksrc`. Configuration is in `json`, an example can be found at `extras/config.ex`.

Repoistories are configured in the following way:

```
"repos": {
  "<reponame>": {
    "<full_branch_name>": {
      "action": "gitpull",
      "repodir": "<path_to_local_clone>"
    }
  }
}
```

The listen port can be customised:

```
"port": 4123
```

You can validate the github signature by setting a secret in the github webhook and locally:

```
"secret": "hunter2"
```
