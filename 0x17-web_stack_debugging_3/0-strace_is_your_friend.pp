# Fix code Puppet

exec { 'fix-type':
  user     => 'root',
  provider => 'shell'
  command  => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php',
  path     => '/usr/local/bin/:/bin/'
}
