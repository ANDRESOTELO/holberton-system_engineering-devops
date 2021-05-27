# Fix code Puppet
exec { '/usr/bin/env sed -i s/15/4096/ /etc/default/nginx':
  path => ['/usr/bin', '/bin'],
}
-> exec { '/usr/bin/env service nginx restart':
  path => ['/usr/bin', '/bin'],
}
