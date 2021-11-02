#!/bin/bash

# software : CMSSW_10_3_2

events="327402:37:22650440,327402:37:22762759,327402:37:22402182"

inputFiles="/store/hidata/HIRun2018A/HIMinimumBias2/RAW/v1/000/327/402/00000/EF63C0AC-B746-2342-A63E-6556A99AB432.root,/store/hidata/HIRun2018A/HIMinimumBias2/RAW/v1/000/327/402/00000/D7B27BE2-6F2D-2540-A90B-3EF8E6370190.root"

outDirBase="/eos/cms/store/group/phys_heavyions_ops/"
outputFile=$outDirBase"/event/pbpb18/edmCPM_out.root"
outDir=$(dirname "${outputFile}")
mkdir -p $outDir

logFile="${outputFile/.root/.log}"

edmCopyPickMerge outputFile=$outputFile eventsToProcess=$events inputFiles=$inputFiles &> $logFile &
echo "edmCopyPickMerge outputFile=$outputFile eventsToProcess=$events inputFiles=$inputFiles &> $logFile &"

