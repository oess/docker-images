# oenotebook Docker Image
* Ubuntu
* scientific python stack
* IPython/Jupyter
* OE toolkits
* OENotebook

----

**Example Commands**
* Launch a notebook server with notebooks from the current directory.


```
    docker run -v /full/path/to/oe_license.txt:/tmp/oe_license.txt -v `pwd`:/tmp/notebooks -p 8888:8888 -it oenb
```
