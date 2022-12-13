# configuring the SSH config file so that we can connect to the server without using a password

include stdlib
file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '	IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/sss_config',
  line    => '	PasswordAuthentication no',
  replace => true,
}
