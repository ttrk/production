#!/bin/bash

# must be run after ./runPickEvents.sh

output="copypickmerge_photonJet_run326XXX.root"
events="326381:4730826,326392:10890664,326392:7592041,326398:13815238,326476:17621247,326478:8881667,326482:34963120,326482:38331029,326483:12754564,326483:17814407,326483:26476731,326483:48608769"
input="/store/hidata/HIRun2018A/HIHardProbes/AOD/PromptReco-v1/000/326/476/00000/A91811C0-2204-544C-B11B-78F2B721894F.root"

edmCopyPickMerge outputFile=$output eventsToProcess=$events inputFiles=$input

