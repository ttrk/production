#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

#inputFile="root://xrootd.cmsaf.mit.edu//store/user/clindsey/Pythia8_AllQCDPhoton15_Hydjet_Quenched_Cymbal5Ev8/RAWSIM_20180630/180630_163544/0000/step1_DIGI_L1_DIGI2RAW_HLT_PU_863.root"
#inputFile="root://xrootd-cms.infn.it//store/user/mnguyen/AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8_5020GeV_DIGI2RAW_103X_upgrade2018_realistic_HI_v4/Pythia8_AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8/crab_AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8_5020GeV_DIGI2RAW_103X_upgrade2018_realistic_HI_v4/181013_203555/0000/step1_private_DIGI_L1_DIGI2RAW_HLT_PU_99.root"
inputFile="root://xrootd.cmsaf.mit.edu//store/user/rbi/Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV/crab_Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV_DIGI2RAW_PU_1030_v1/181030_234244/0001/step1_DIGI_L1_DIGI2RAW_HLT_PU_1652.root"

$runCmd edmDumpEventContent --all $inputFile &> edmDEC_Pythia8_AllQCDPhoton15_Hydjet_Quenched_Cymbal5Ev8_RAW.log

