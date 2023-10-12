#!/bin/sh

DBNAME=%kalabash_dbname DBUSER=%kalabash_dbuser DBPASSWORD=%kalabash_dbpassword

echo "UPDATE core_user SET last_login=now() WHERE username='$USER'" | mysql -u $DBUSER -p$DBPASSWORD $DBNAME

exec "$@"
