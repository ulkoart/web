sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn_hello.conf   /etc/gunicorn.d/hello
sudo ln -s /home/box/web/etc/gunicorn_ask.conf   /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
﻿sudo /etc/init.d/mysql start﻿

mysql -uroot -e "CREATE DATABASE aks;"
mysql -uroot -e "CREATE USER 'aks' IDENTIFIED BY 'aks';"
mysql -uroot -e "GRANT ALL ON aks.* TO 'aks';"
mysql -uroot -e "GRANT USAGE ON *.* TO 'aks';"
mysql -uroot -e "FLUSH PRIVILEGES;"
