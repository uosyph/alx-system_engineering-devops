# Increase the maximum number of concurrent connections to Nginx to improve performance under high load.

exec {'nginx_connection_limit':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['nginx_restart'],
}

exec {'nginx_restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
