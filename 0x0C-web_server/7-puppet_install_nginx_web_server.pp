# Install Nginx web server (w/ Puppet)

package { 'nginx':
  ensure   => installed,
  name     => 'nginx',
  provider => 'apt'
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Holberton School'
}

file_line { 'Redirect_me':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => '	rewrite ^/redirect_me https://youtu.be/LNv9PevSRLo permanent;'
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx']
}
