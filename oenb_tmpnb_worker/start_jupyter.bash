#! /bin/bash

CONDADIR=/opt/conda

${CONDADIR}/bin/ipython kernel install --user
source activate ${CONDADIR}
ipython kernel install

cp -R /hub_data/notebooks/* ./

chown -R oe-user:oe-user /home/oe-user

RUN find . -name '*.ipynb' -exec ipython2 trust {} \;

jupyter-notebook --no-browser --NotebookApp.ip='*' $*
