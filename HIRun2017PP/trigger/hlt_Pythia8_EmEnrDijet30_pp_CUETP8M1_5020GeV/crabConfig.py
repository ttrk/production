from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "hlt_Pythia8_EmEnrDijet30_pp_CUETP8M1_5020GeV_HIHighPtRefPP5TeVPhoton_V2"
config.General.transferLogs = False
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "hlt.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines, 2500 is the maximum guaranteed number.
config.JobType.maxJobRuntimeMin = 2800 # request longer runtime, ~47 hours. 2800 is the maximum guaranteed number.
# CMSSW_9_2_12
# HLT instructions : https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGlobalHLT?rev=3071#Running_the_HLT_with_CMSSW_9_2_0
# hlt.py is the result of ./createHLT.sh + turn off process.dqmOutput

config.section_("Data")
config.Data.inputDataset = "/Pythia8_EmEnrDijet30_pp_CUETP8M1_5020GeV/gsfs-RAW_20171002-f5c51db4d3712eae044fcbfa9ecb19c0/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10 
config.Data.totalUnits = -1
config.Data.publication = False
config.JobType.outputFiles = ["openHLT.root"]
config.JobType.numCores = 4
config.Data.outputDatasetTag = "hlt_HIHighPtRefPP5TeVPhoton_V2"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]
#config.Site.ignoreGlobalBlacklist = True

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
