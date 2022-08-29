from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "run3_pbpb22_privateMC_QCDDijet15_pythia8_RECO_userInput" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time.
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RECO.py"
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000   # Allowed maximum for a 8 core(s) job is 20000.
config.JobType.maxJobRuntimeMin = 2880 # request longer runtime, 48 hours.

## CMSSW_10_3_3_patch1

config.section_("Data")
#config.Data.inputDataset = "########################"
#config.Data.inputDBS = "phys03"
config.Data.userInputFiles = open('inputFiles_RECO.txt').readlines()
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 2
config.Data.totalUnits = -1
config.Data.publication = False
#config.Data.outputDatasetTag = "run3_pbpb22_privateMC_QCDDijet15_pythia8_RECO"
#config.Data.outLFNDirBase = "/store/user/katatar/"
config.Data.outputDatasetTag = ""
config.Data.outLFNDirBase = "/store/user/katatar/run3/run3_pbpb22_privateMC_QCDDijet15_pythia8_RECO/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

##### Notes
#### The DIGI dataset did not published somehow. DIGI job got stuck in the status copied below, I ended up running RECO on an input specified as file list :
# Task name:			220812_132309:katatar_crab_run3_pbpb22_privateMC_QCDDijet15_pythia8_DIGI
# Task URL to use for HELP:	https://cmsweb.cern.ch/crabserver/ui/task/220812_132309%3Akatatar_crab_run3_pbpb22_privateMC_QCDDijet15_pythia8_DIGI
# Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=katatar&var-task=220812_132309%3Akatatar_crab_run3_pbpb22_privateMC_QCDDijet15_pythia8_DIGI&from=1660306990000&to=now
# Status on the scheduler:	COMPLETED
# Grid scheduler - Task Worker:	crab3@vocms0144.cern.ch - crab-prod-tw01
# Jobs status:                    finished     		100.0% (5195/5195)
# Output dataset:			/run3/katatar-run3_pbpb22_privateMC_QCDDijet15_pythia8_DIGI-00000000000000000000000000000000/USER
# No publication information available yet
