# Install Nginx web server (w/ Puppet)

package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => 'Holberton School',
}

file_line { 'Redirect_me':
  ensure => 'present',
  after  => 'listen 80 default_server;',
  path   => '/etc/nginx/sites-available/default',
  line   => '	rewrite ^/redirect_me https://youtu.be/LNv9PevSRLo permanent;',
}

service { 'service_start':
  ensure  => 'running',
  require => Package['nginx'],
}
