# Install Nginx web server

package { 'nginx':
  ensure   => installed,
  name     => 'nginx',
  provider => 'apt'
}
->
file_line { 'custom HTTP header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx']
}
