#!/bin/bash

dataset="/HIHardProbes/HIRun2018A-PromptReco-v1/AOD"
eventList="events_photonJet_run326XXX.txt"
output="edmPE_photonJet_run326XXX.log"

edmPickEvents.py --printInteractive --maxEventsInteractive=50 $dataset $eventList &> $output
