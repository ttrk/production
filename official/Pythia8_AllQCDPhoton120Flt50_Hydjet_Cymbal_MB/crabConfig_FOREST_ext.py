from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton120Flt50_Hydjet_Cymbal_MB_FOREST_ext"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MIX_75X.py"
# config.JobType.maxMemoryMB = 3500
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/f61094f7a81de65dc1f9796236b8ed94fca888a6
# runForestAOD_PbPb_MIX_75X.py commit + change gen particle pt and eta cuts
# https://github.com/CmsHI/cmssw/commit/336108879815bf68a856f23a7a47254ef87347fd

config.section_("Data")
config.Data.inputDataset = "/Pythia8_AllQCDPhoton120Flt50_Hydjet_Cymbal_MB/HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v14_ext1-v1/AODSIM"
config.Data.allowNonValidInputDataset = True
### related message from CRAB
# Failure message from the server:        CRAB refuses to proceed in getting the details of the dataset /Pythia8_AllQCDPhoton120Flt50_Hydjet_Cymbal_MB/HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v14_ext1-v1/AODSIM from DBS, because the dataset is not 'VALID' but 'PRODUCTION'. To allow CRAB to consider a dataset that is not 'VALID', set Data.allowNonValidInputDataset = True in the CRAB configuration. Notice that this will not force CRAB to run over all files in the dataset; CRAB will still check if there are any valid files in the dataset and run only over those files. 
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HINPbPbWinter16DR-75X_mcRun2_HeavyIon_v14_ext1-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
