# Fix code Puppet

exec { 'fix-ulimit':
  user     => 'root',
  provider => 'shell',
  command  => 'sudo sed -i s/15/4096/g /etc/default/nginx',
  path     => '/usr/local/bin/:/bin/'
}

exec { 'restart-service':
  user    => 'root',
  command => 'sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}
