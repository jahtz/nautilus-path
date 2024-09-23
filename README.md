# nautilus-path
Nautilus (GNOME Files) extension for copying file and directory paths.

>[!IMPORTANT]
> This extension removes any prefixes from network drive paths (tested only with SFTP servers) and returns them as "local" paths.
## Setup
### Requirements
Ubuntu/Debian/Mint: `sudo apt install python3-nautilus python3-gi`

RHEL/Fedora: `sudo dnf install nautilus-python python3-gobject`

Arch: `sudo pacman -S python-nautilus python-gobject`

### Install extension
 ```shell
git clone https://github.com/jahtz/nautilus-path.git
cd nautilus-path
make install
````

### Remove extension
```shell
make uninstall
```

## Modifications
>[!NOTE]
> File to modify: `~/.local/share/nautilus-python/extensions/nautilus-path.py`<br>
> Modifications require Nautilus to be reloaded: `nautilus -q`

### Change separator for multiple selected files:
Default is a _newline_ symbol. Can be changed by changing `FILE_SEPARATOR` (line 36)