# Fix code Puppet
exec { 'sed -i s/15/4096/ /etc/default/nginx':
  path    => ['/usr/local/bin/', '/bin/', '/usr/bin/env'],
}
-> exec { 'service nginx restart':
  path    => ['/usr/local/bin/', '/bin/', '/usr/bin/env'],
}
