cp gitremind/gitremind.py /usr/bin/gitremind.py
cp systemd/gitremind.service /lib/systemd/system/gitremind.service
systemctl enable gitremind.service
systemctl start gitremind.service
systemctl status gitremind.service


