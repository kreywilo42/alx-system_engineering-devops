# Fix the limit in nginx default.
exec { 'changeLimit':
    command => 'sed -i "s/15/4096/g" /etc/default/nginx; service nginx restart',
    path    => '/usr/bin/:/bin/',
}
