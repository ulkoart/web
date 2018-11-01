sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn_hello.conf   /etc/gunicorn.d/hello
sudo ln -s /home/box/web/etc/gunicorn_ask.conf   /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
﻿sudo /etc/init.d/mysql start﻿