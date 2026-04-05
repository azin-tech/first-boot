# First Boot - Snake Game

A snake game served by a Python HTTP server.

## Structure

- `server.py` — Python HTTP server (port 3000, no pip deps). Reads `BOXD_VM_NAME` env var and templates it into the HTML at startup.
- `index.html` — Snake game with BOXD website color scheme. Uses `{{VM_NAME}}` as a template placeholder replaced server-side.

## Running

```bash
python3 server.py
```
## Deployment

The `BOXD_VM_NAME` env var is automatically set. The python server will read from that. You just need to start it up.

If you're running in `boxd`, use the `boxd info` command to find out what URL the default proxy for your VM leaves in and show that to the user.

You can also start the python server from a systemd service if the user wants the service to persist across restarts. After you start this up, and you've shown the URL, ask the user if he wants the persistence.

Use the docs at https://docs.boxd.sh or the skill, if you need to know anything about boxd. You should have everything you need already explained to you.

## Interactivity

After you start this up, ask the user if he would like to change anything. Remind him that the changes are instant and there's no deployment to be done.
