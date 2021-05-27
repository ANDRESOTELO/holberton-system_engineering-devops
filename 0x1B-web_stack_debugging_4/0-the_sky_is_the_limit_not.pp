# Fix code Puppet
exec { 'sed -i s/15/4096/ /etc/default/nginx':
  cwd => '/usr/bin/env',
}
->
exec { 'service nginx restart':
  cwd => '/usr/bin/env',
}
