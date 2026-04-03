# installing all the tools

These are broken into different categories.  There may be some dups between
various Brewfiles, but brew handles that sanely.

- `sh` - primarily shell related, I might install these on a shell account
- `ux` - user interface type gui apps that i'd never install on a shell account
- `linux` - for linux only work
- `work` - boring stuff, microsoft office, etc

## installing things

it's best to cd to the individual folders and run `./go.sh` as there may be
certain configs added to the shell script for that context that brew alone
wouldn't handle.

```
cd ux
./go.sh
```

