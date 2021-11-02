#!/bin/bash

# software : CMSSW_10_3_2

events="events.txt"

inputFiles="inputFiles.txt"

outDirBase="/eos/cms/store/group/phys_heavyions_ops/"
outputFile=$outDirBase"/event/pbpb18/edmCPM_out_txt_input.root"
outDir=$(dirname "${outputFile}")
mkdir -p $outDir

logFile="${outputFile/.root/.log}"

edmCopyPickMerge outputFile=$outputFile eventsToProcess_load=$events inputFiles_load=$inputFiles &> $logFile &
echo "edmCopyPickMerge outputFile=$outputFile eventsToProcess_load=$events inputFiles_load=$inputFiles &> $logFile &"

