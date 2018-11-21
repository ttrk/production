#!/bin/bash

# instructions : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/5498.html

set -x
export PATH=$HOME/.local/bin:/cvmfs/cms-bril.cern.ch/brilconda/bin:$PATH
pip install --install-option="--prefix=$HOME/.local" brilws
set +x
