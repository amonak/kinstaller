import os
import sys
from .. import utils


class Restore:
    def __init__(self, restore):
        """
        Restoring pre-check (backup integriety)
        REQUIRED : kalabash.sql
        OPTIONAL : mails/, custom/, amavis.sql, spamassassin.sql
        Only checking required
        """

        if not os.path.isdir(restore):
            utils.error(
                "Provided path is not a directory !")
            sys.exit(1)

        kalabash_sql_file = os.path.join(restore, "databases/kalabash.sql")
        if not os.path.isfile(kalabash_sql_file):
            utils.error(
                kalabash_sql_file + " not found, please check your backup")
            sys.exit(1)

        # Everything seems alright here, proceeding...
