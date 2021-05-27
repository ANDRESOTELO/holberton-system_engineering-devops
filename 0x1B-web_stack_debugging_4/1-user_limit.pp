# Change the OS configuration so that it is possible to login with
# the holberton user and open a file without any error message.
exec { 'sed -i s/holberton/sotelo/ /etc/security/limits.conf':
  path => ['/usr/bin', '/bin'],
}
