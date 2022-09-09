from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "run3_pp22_privateMC_QCDPhoton15_pythia8_5p36TeV_RECO_userInput" # Defaults to <time-stamp>, where the time stamp is of the form <YYYYMMDD>_<hhmmss> and corresponds to the submission time.
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RECO.py"
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000   # Allowed maximum for a 8 core(s) job is 20000.
config.JobType.maxJobRuntimeMin = 2880 # request longer runtime, 48 hours.

# software : CMSSW_12_5_0_pre5

config.section_("Data")
#config.Data.inputDataset = "########################"
#config.Data.inputDBS = "phys03"
config.Data.userInputFiles = open('inputFiles_RECO.txt').readlines()
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 2
config.Data.totalUnits = -1
config.Data.publication = False
#config.Data.outputDatasetTag = "run3_pp22_privateMC_QCDPhoton15_pythia8_5p36TeV_RECO"
#config.Data.outLFNDirBase = "/store/user/katatar/"
config.Data.outputDatasetTag = ""
config.Data.outLFNDirBase = "/store/user/katatar/run3/run3_pp22_privateMC_QCDPhoton15_pythia8_5p36TeV_RECO/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

