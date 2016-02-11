# OENB_JupyterHub Image
#### Multi-User Notebook Server
* Ubuntu
* scientific python stack
* IPython/Jupyter
* JupyterHub
* OE toolkits
* OENotebook

----

### Requirements
You must create a folder to be passed into the container with three components:
```
example_hub_data/
├── notebooks
│   └── Example_NB.ipynb
├── oe_license.txt
└── userlist
```

#### **notebooks**
Any contents of this subfolder are copied into each user's home directory and are available to a user on login.

#### **oe_license.txt**
Your license file for OpenEye toolkits.

#### **userlist**
A comma-separated list of users and passwords to create on the server. The first user in this list will be granted administrative rights on JupyterHub, as well as any user named ***nbadmin***.

Here's an example file for Seinfeld characters:
```
jerry,sup3rman
kramer,C0smo
george,bosco
elaine,JohnJohn
```

---

### Example Commands
* Launch a multi-user notebook server:
```
docker run -v /path/to/hub_data:/opt/hub_data -p 80:80 -it openeye/oenb_jupyterhub
```


* Launch a multi-user notebook server where user work will persist after shutdown:
```
docker run -v /path/to/hub_data:/opt/hub_data -v /path/to/nb_storage:/home -p 80:80 -it openeye/oenb_jupyterhub
```
