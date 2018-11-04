#!/bin/bash

inputFile="hltConfig.log"

grep --color -i "   HLT_HIGEDPhoton30_v1" $inputFile
echo "#####"
grep --color -i "   HLT_HIGEDPhoton30_L1EG15_v1" $inputFile
echo "#####"
grep --color -i "   HLT_HIGEDPhoton30_L1Seeded_v1" $inputFile
echo "#####"
grep --color -i "   HLT_HIGEDPhoton30_EB_v1" $inputFile
echo "#####"
grep --color -i "   HLT_HIGEDPhoton30_EB_L1EG15_v1" $inputFile
echo "#####"
grep --color -i "   HLT_HIGEDPhoton30_EB_L1Seeded_v1" $inputFile
echo "#####"
