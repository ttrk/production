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

grep --color -i "   HLT_HIGEDPhoton20_v1" $inputFile
echo "#####"
grep --color -i "   HLT_HIGEDPhoton20_L1EG7_v1" $inputFile
echo "#####"
grep --color -i "   HLT_HIGEDPhoton20_L1Seeded_v1" $inputFile
echo "#####"
grep --color -i "   HLT_HIGEDPhoton20_EB_v1" $inputFile
echo "#####"
grep --color -i "   HLT_HIGEDPhoton20_EB_L1EG7_v1" $inputFile
echo "#####"
grep --color -i "   HLT_HIGEDPhoton20_EB_L1Seeded_v1" $inputFile
echo "#####"


#FastReport       289.1 ms HLT_HIGEDPhoton30_v1
######
#FastReport       176.8 ms HLT_HIGEDPhoton30_L1EG15_v1
######
#FastReport       174.7 ms HLT_HIGEDPhoton30_L1Seeded_v1
######
#FastReport       289.1 ms HLT_HIGEDPhoton30_EB_v1
######
#FastReport       176.8 ms HLT_HIGEDPhoton30_EB_L1EG15_v1
######
#FastReport       174.7 ms HLT_HIGEDPhoton30_EB_L1Seeded_v1
######

