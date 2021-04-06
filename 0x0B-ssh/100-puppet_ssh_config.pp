# Client configuration file (w/ Puppet)

file_line { 'Refuse password auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	PasswordAuthentication no',
}
file_line { 'To use private key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	IdentityFile ~/.ssh/holberton',
}
