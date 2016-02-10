# Configuration file for Jupyter Hub

c = get_config()

c.JupyterHub.port = 80

c.JupyterHub.log_level = 10

c.Authenticator.whitelist = whitelist = set()
c.Authenticator.admin_users = admin = set()

import os
import sys
import subprocess

join = os.path.join

here = os.path.dirname(__file__)
root = os.environ.get('OAUTHENTICATOR_DIR', here)
sys.path.insert(0, root)

print(subprocess.call(["bash", "/tmp/add_user.sh", "/opt/hub_data/userlist"]))

with open('/opt/hub_data/userlist') as f:
    for line in f:
        if not line:
            continue
        parts = line.strip().split(",")
        name = parts[0]
        whitelist.add(name)
        if name in ['nbadmin']:
            admin.add(name)

os.remove("/opt/hub_data/userlist")
os.remove("/tmp/add_user.sh")


c.Spawner.env_keep = ['PATH', 'PYTHONPATH', 'CONDA_ROOT', 'CONDA_DEFAULT_ENV',
                      'VIRTUAL_ENV', 'LANG', 'LC_ALL', 'OE_LICENSE']

c.MultiKernelManager.default_kernel_name = 'python2'

# ssl config
ssl = join(root, 'ssl')
keyfile = join(ssl, 'ssl.key')
certfile = join(ssl, 'ssl.cert')
if os.path.exists(keyfile):
    c.JupyterHub.ssl_key = keyfile
if os.path.exists(certfile):
    c.JupyterHub.ssl_cert = certfile
