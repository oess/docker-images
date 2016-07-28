FROM centos:5

MAINTAINER OpenEye <mattg@eyesopen.com>

RUN yum install -yq \
    wget \
    bzip2 \
    cairo-devel \
    libXrender-devel \
    && yum clean all

# Configure environment
ENV CONDA_DIR /home/oetester/conda
ENV PATH $CONDA_DIR/bin:$PATH
ENV SHELL /bin/bash

# Create oetester user with UID=1000 and in the 'users' group
RUN useradd -m -s /bin/bash -u 1000 oetester

USER oetester

# Install Conda with Python2
RUN cd /tmp && \
    wget --quiet http://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh && \
    bash Miniconda2-latest-Linux-x86_64.sh -b -p $CONDA_DIR && \
    rm Miniconda2-latest-Linux-x86_64.sh && \
    $CONDA_DIR/bin/conda update --quiet --yes conda && \
    $CONDA_DIR/bin/conda config --system --add channels conda-forge && \
    $CONDA_DIR/bin/conda install --yes pip && \
    $CONDA_DIR/bin/pip install --upgrade pip && \
    conda clean -tipsy

ENV OE_LICENSE /tmp/oe_license.txt

# Install OE TKs
# COPY requirements.txt /tmp/requirements.txt
RUN pip install --extra-index-url https://pypi.anaconda.org/OpenEye/simple OpenEye-toolkits


CMD python -m openeye.examples.openeye_tests
