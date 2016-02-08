FROM jupyter/scipy-notebook
#FROM ipython/scipystack

MAINTAINER OpenEye <mattg@eyesopen.com>

# Dependencies for OE Example Notebooks
# Commented for local install because of pip problems. DNS resolution of devpi.eyesopen.com, even if static IP passed

RUN pip2 install -U pip

COPY requirements.txt /tmp/requirements.txt
RUN pip2 install -i https://devpi.eyesopen.us/oe/dev/ -r /tmp/requirements.txt

# oe-user is our user
# RUN useradd -m -s /bin/bash oeuser

# USER oeuser
# RUN ipython2 profile create

# Workaround for issue with ADD permissions
# USER root
# ADD ipython_notebook_config.py /home/oe-user/.ipython/profile_default/
# ADD custom.js /home/oe-user/.ipython/profile_default/static/custom/

# License should be provided in the run command
# COPY oe_license.txt /tmp/

# ADD notebooks/ /home/oe-user/

# RUN chown oe-user:oe-user /home/oe-user -R

EXPOSE 8888

# USER oeuser
# ENV HOME /home/oeuser
# ENV SHELL /bin/bash
# ENV USER oeuser
ENV OE_LICENSE /tmp/oe_license.txt

WORKDIR /tmp/notebooks/


# RUN chown -R oeuser:oeuser /home/oe-user

# RUN find . -name '*.ipynb' -exec ipython2 trust {} \;

CMD ipython2 notebook --no-browser --ip=*
