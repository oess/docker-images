FROM ubuntu:14.04

MAINTAINER OpenEye <mattg@eyesopen.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -yq --no-install-recommends \
    wget \
    libcairo2-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Configure environment
ENV CONDA_DIR /home/oetester/conda
ENV PATH $CONDA_DIR/bin:$PATH
ENV SHELL /bin/bash

# Create oetester user with UID=1000 and in the 'users' group
RUN useradd -m -s /bin/bash -N -u 1000 oetester

USER oetester

# Install Conda with Python3
RUN cd /tmp && \
    wget --quiet http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_DIR && \
    rm Miniconda3-latest-Linux-x86_64.sh && \
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
