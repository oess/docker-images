# OENB_JupyterHub Image: Multi-User Notebook Server
* Ubuntu
* scientific python stack
* IPython/Jupyter
* JupyterHub
* OE toolkits
* OENotebook

----

**Example Commands**
* Launch a multi-user notebook server:

```
docker run -v /path/to/hub_data:/opt/hub_data -p 80:80 -it openeye/oenotebook
```
