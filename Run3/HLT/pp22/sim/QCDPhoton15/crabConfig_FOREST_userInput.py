from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "run3_pp22_privateMC_QCDPhoton15_pythia8_5p36TeV_FOREST_mAOD_userInput"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "forest_miniAOD_run3_ppref_MC.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
# software : CMSSW_12_5_0_pre5
## forest_CMSSW_12_5_0
# https://github.com/CmsHI/cmssw/commit/c20cc75a948b5817c1c4f53485d10df45fb7374a
# forest_miniAOD_run3_ppref_MC.py commit + turn off electrons + disable ggHi.doEffectiveAreas RecHits
# https://github.com/CmsHI/cmssw/commit/4ee95825626b40695415f875b1912c980ad7b5f9

config.section_("Data")
#config.Data.inputDataset = "########################"
#config.Data.inputDBS = "phys03"
config.Data.userInputFiles = open('inputFiles_FOREST_mAOD.txt').readlines()
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = ""
config.Data.outLFNDirBase = "/store/user/katatar/run3/run3_pp22_privateMC_QCDPhoton15_pythia8_5p36TeV_FOREST_mAOD/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

