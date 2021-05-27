# Fix code Puppet

exec { 'fix-ulimit':
  command => 'sudo sed -i s/15/4096/ /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/:/usr/bin/env'
}

->exec { 'restart-service':
  command => 'sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/:/usr/bin/env'
}
