[program:kalabash-dkim-worker]
autostart=true
autorestart=true
command=%{venv_path}/bin/python %{home_dir}/instance/manage.py rqworker dkim
directory=%{home_dir}
user=%{opendkim_user}
redirect_stderr=true
numprocs=1
stopsignal=TERM
