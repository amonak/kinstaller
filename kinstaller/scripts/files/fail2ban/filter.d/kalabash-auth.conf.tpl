# Fail2Ban filter Kalabash authentication

[INCLUDES]

before = common.conf

[Definition]

failregex = kalabash\.auth: WARNING Failed connection attempt from \'<HOST>\' as user \'.*?\'$
