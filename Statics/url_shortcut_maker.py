import sys
import os


def _make_mac_url_shortcut(url, path):
    url_content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>URL</key>
<string>%s</string>
</dict>
</plist>""" % url

    with open(path + ".webloc", "w") as out_file:
        out_file.write(url_content)


def _make_linux_url_shortcut(url, path):
    name = os.path.split(url)[-1]
    url_content ="""[Desktop Entry]
Encoding=UTF-8
Name=%s
Type=Link
URL=%s
Icon=text-html""" % (name, url)

    with open(path + ".desktop", "w") as out_file:
        out_file.write(url_content)


def _make_windows_url_shortcut(url, path):
    url_content ="""[InternetShortcut]
URL=%s""" % url

    with open(path + ".URL", "w") as out_file:
        out_file.write(url_content)


def make_url_shortcut(url, path):

    system = sys.platform.lower()

    if system == "darwin":
        _make_mac_url_shortcut(url, path)
    elif "linux" in system:
        _make_linux_url_shortcut(url, path)
    else:
        _make_windows_url_shortcut(url, path)
