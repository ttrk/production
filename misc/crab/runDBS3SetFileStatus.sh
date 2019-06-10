#!/bin/bash

#runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
runCmd=""

# https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling#Changing_a_dataset_or_file_statu
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCrabForPublication#Invalidate_individual_files_in_a

# echo $DBS3_CLIENT_ROOT gives
# /cvmfs/cms.cern.ch/crab3/slc6_amd64_gcc493/cms/dbs3-client/3.5.1//

progCode=${DBS3_CLIENT_ROOT}"/examples/DBS3SetFileStatus.py"

set -x

file1="/store/user/katatar/EGamma/Pythia8_AllQCDPhoton30_Filter30GeV_Hydjet_Drum5F_2018_5p02TeV_PbPb2018_DIGI_L1_DIGI2RAW_HLT_PU/190607_211039/0000/step2_DIGI_L1_DIGI2RAW_HLT_PU_8.root"
file2="/store/user/katatar/EGamma/Pythia8_AllQCDPhoton30_Filter30GeV_Hydjet_Drum5F_2018_5p02TeV_PbPb2018_DIGI_L1_DIGI2RAW_HLT_PU/190607_211039/0000/step2_DIGI_L1_DIGI2RAW_HLT_PU_10.root"
file3="/store/user/katatar/EGamma/Pythia8_AllQCDPhoton30_Filter30GeV_Hydjet_Drum5F_2018_5p02TeV_PbPb2018_DIGI_L1_DIGI2RAW_HLT_PU/190607_211039/0000/step2_DIGI_L1_DIGI2RAW_HLT_PU_213.root"
logFile="DBS3SetFileStatus_invalid_Pythia8_AllQCDPhoton30_Filter30GeV_Hydjet_Drum5F_2018_5p02TeV_PbPb2018_DIGI_L1_DIGI2RAW_HLT_PU.log"

invalidFiles=${file1}","${file2}","${file3}

${runCmd} python ${progCode} --url=https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter --status=invalid --recursive=False --files=$invalidFiles &> ${logFile} &

