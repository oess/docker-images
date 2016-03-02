#! /bin/bash

CONDADIR=/opt/conda

${CONDADIR}/bin/ipython kernel install --user
source activate ${CONDADIR}
ipython kernel install

mkdir -p $HOME/notebooks

cp -R /hub_data/notebooks/* $HOME/notebooks/

chown -R oe-user:oe-user /home/oe-user

RUN find $HOME/notebooks -name '*.ipynb' -exec ipython2 trust {} \;

jupyter-notebook --no-browser --NotebookApp.ip='*' --notebook-dir=$HOME/notebooks $*
