# Using puppet create a manifest that kills a process

exec { 'kill_process':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
}
