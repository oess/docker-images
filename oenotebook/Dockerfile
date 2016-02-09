FROM ubuntu:14.04
#FROM jupyter/scipy-notebook
#FROM ipython/scipystack

MAINTAINER OpenEye <mattg@eyesopen.com>

RUN apt-get update && apt-get upgrade -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN apt-get update && apt-get install -y wget libcairo2-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Configure environment
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH
ENV SHELL /bin/bash

# Install Conda
# RUN cd /tmp && \
#     mkdir -p $CONDA_DIR && \
#     wget --quiet https://repo.continuum.io/miniconda/Miniconda3-3.9.1-Linux-x86_64.sh && \
#     echo "6c6b44acdd0bc4229377ee10d52c8ac6160c336d9cdd669db7371aa9344e1ac3 *Miniconda3-3.9.1-Linux-x86_64.sh" | sha256sum -c - && \
#     /bin/bash Miniconda3-3.9.1-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
#     rm Miniconda3-3.9.1-Linux-x86_64.sh && \
#     $CONDA_DIR/bin/conda install --yes conda==3.14.1

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda-3.16.0-Linux-x86_64.sh && \
    /bin/bash /Miniconda-3.16.0-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda-3.16.0-Linux-x86_64.sh && \
    /opt/conda/bin/conda install --yes conda==3.19.1 && \
    /opt/conda/bin/pip install --upgrade pip

RUN conda install --yes \
    'jupyter' \
    'ipywidgets=4.0*' \
    'pandas=0.17*' \
    'matplotlib=1.4*' \
    'scipy=0.16*' \
    'seaborn=0.6*' \
    'scikit-learn=0.16*' \
    'sympy=0.7*' \
    'patsy=0.4*' \
    'statsmodels=0.6*' \
    'bokeh=0.10*' \
    && conda clean -yt



# Dependencies for OE Example Notebooks
# Commented for local install because of pip problems. DNS resolution of devpi.eyesopen.com, even if static IP passed

# RUN source activate python2

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
#RUN pip install -i https://pypi.anaconda.org/OpenEye/simple -r /tmp/requirements.txt


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

CMD jupyter notebook --no-browser --ip=*
