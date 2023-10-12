"""fail2ban related functions."""

from . import base


class Fail2ban(base.Installer):
    """Fail2ban installer."""

    appname = "fail2ban"
    packages = {
        "deb": ["fail2ban"],
        "rpm": ["fail2ban"]
    }
    config_files = [
        "jail.d/kalabash.conf",
        "filter.d/kalabash-auth.conf",
    ]
