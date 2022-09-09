from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "run3_pp22_privateMC_QCDDijet15_pythia8_5p36TeV_DIGI_userInput" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time.
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step2_DIGI.py"
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000   # Allowed maximum for a 8 core(s) job is 20000.
config.JobType.maxJobRuntimeMin = 2880 # request longer runtime, 48 hours.

# software : CMSSW_12_5_0_pre5

config.section_("Data")
#config.Data.inputDataset = "########################"
#config.Data.inputDBS = "phys03"
config.Data.userInputFiles = open('inputFiles_DIGI.txt').readlines()
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
#config.Data.outputDatasetTag = "run3_pp22_privateMC_QCDDijet15_pythia8_5p36TeV_DIGI"
#config.Data.outLFNDirBase = "/store/user/katatar/"
config.Data.outputDatasetTag = ""
config.Data.outLFNDirBase = "/store/user/katatar/run3/run3_pp22_privateMC_QCDDijet15_pythia8_5p36TeV_DIGI/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

##### Notes
#### The GEN-SIM dataset did not get published somehow. GEN-SIM job got stuck in the status copied below, I ended up running DIGI on an input specified as file list :
# Task name:			220905_135834:katatar_crab_run3_pp22_privateMC_QCDDijet15_pythia8_5p36TeV_GEN_SIM
# Grid scheduler - Task Worker:	crab3@vocms0194.cern.ch - crab-prod-tw01
# Task URL to use for HELP:	https://cmsweb.cern.ch/crabserver/ui/task/220905_135834%3Akatatar_crab_run3_pp22_privateMC_QCDDijet15_pythia8_5p36TeV_GEN_SIM
# Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=katatar&var-task=220905_135834%3Akatatar_crab_run3_pp22_privateMC_QCDDijet15_pythia8_5p36TeV_GEN_SIM&from=1662382714000&to=now
# Status on the scheduler:	COMPLETED
# Jobs status:                    finished     		100.0% (53/53)
# Output dataset:			/run3/katatar-run3_pp22_privateMC_QCDDijet15_pythia8_5p36TeV_GEN_SIM-00000000000000000000000000000000/USER
# No publication information available yet
