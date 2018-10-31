#!/bin/bash

# https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling#Changing_a_dataset_or_file_statu
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCrabForPublication#Invalidate_individual_files_in_a

## Run ./dasQueryOutput.sh to get the list of files in the output dataset. Pick the files to be invalidated from that list.
## Following two files needed to be removed from dataset because they are duplicates. Duplication happened due to partial processing of the input dataset.
file1="/store/user/katatar/HIRun2018PbPb/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/HINPbPbSpring18GS_103X_upgrade2018_realistic_HI_v7_DIGI_L1_DIGI2RAW_HLT_PU/181026_193506/0000/step2_DIGI_L1_DIGI2RAW_HLT_PU_6.root"
file2="/store/user/katatar/HIRun2018PbPb/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/HINPbPbSpring18GS_103X_upgrade2018_realistic_HI_v7_DIGI_L1_DIGI2RAW_HLT_PU/181026_193506/0000/step2_DIGI_L1_DIGI2RAW_HLT_PU_7.root"

set -x
invalidFiles=${file1}","${file2}

# echo $DBS3_CLIENT_ROOT gives
# /cvmfs/cms.cern.ch/crab3/slc6_amd64_gcc493/cms/dbs3-client/3.5.1//

python $DBS3_CLIENT_ROOT/examples/DBS3SetFileStatus.py --url=https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter --status=invalid --recursive=False  --files=$invalidFiles &> DBS3SetFileStatus.log &

