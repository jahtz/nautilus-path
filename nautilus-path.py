# Copyright (C) 2024 Janik Haitz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from urllib.parse import unquote, urlparse
from pathlib import Path

from gi import require_version
try:
    require_version('Nautilus', '4.0')
    require_version('Gtk', '4.0')
    require_version('Gdk', '4.0')
    gi_version = 4
except:
    require_version('Nautilus', '3.0')
    require_version('Gtk', '3.0')
    require_version('Gdk', '3.0')
    gi_version = 3
from gi.repository import GObject, Nautilus, Gtk, Gdk


FILE_SEPARATOR = '\n'


class NautilusPath(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        if gi_version == 4:
            self.clipboard = Gdk.Display.get_default().get_clipboard()
        else:
            self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

    def get_file_items(self, selected_files: list[Nautilus.FileInfo]):
        copy_menu = Nautilus.MenuItem(name=f'PathExtension::CopyFile{"s" if len(selected_files) != 1 else ""}',
                                      label=f'Copy Path{"s" if len(selected_files) != 1 else ""}',
                                      tip='Copy selected file path(s).')
        copy_menu.connect('activate', self._copy_path, selected_files)
        return (copy_menu, )

    def get_background_items(self, current_directory: Nautilus.FileInfo):
        copy_menu = Nautilus.MenuItem(name='PathExtension::CopyDirectory',
                                      label='Copy Path',
                                      tip='Copy selected directory path')
        copy_menu.connect('activate', self._copy_path, [current_directory])
        return (copy_menu, )

    def _copy_path(self, _menu, selected_files: list[Nautilus.FileInfo]):
        posix_list: list[str] = []
        for file in selected_files:
            fp = Path(unquote(urlparse(file.get_uri()).path))  # strip fileinfo to plain paths
            posix = fp.as_posix()
            if ' ' in posix:
                posix = f'"{posix}"'
            posix_list.append(posix)
        posix_string = FILE_SEPARATOR.join(posix_list)
        if posix_string is not None:
            if gi_version == 4:
                self.clipboard.set(posix_string)
            else:
                self.clipboard.set_text(posix_string, -1)
