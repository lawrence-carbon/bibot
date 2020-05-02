#! /bin/sh

cp listen-for-shutdown.py /usr/local/bin
chmod +x /usr/local/bin/listen-for-shutdown.py

cp listen-for-shutdown.sh /etc/init.d
chmod +x /etc/init.d/listen-for-shutdown.sh

update-rc.d listen-for-shutdown.sh defaults
