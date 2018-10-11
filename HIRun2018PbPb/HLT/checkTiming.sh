#!/bin/bash

inputFile="Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/hltConfig.log"

grep --color -i "   hltParticleFlowRecHitECAL" $inputFile
echo "#####"
grep --color -i "   hltParticleFlowClusterECALUncorrected" $inputFile
echo "#####"
grep --color -i "   hltParticleFlowClusterECAL" $inputFile
echo "#####"
grep --color -i "   hltParticleFlowSuperClusterECAL" $inputFile
echo "#####"
