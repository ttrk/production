from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'HIHardProbes_HIRun2018A_PbPbZEE_PromptReco_v1_FOREST_userInputFiles'
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pponAA_DATA_103X.py'
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
## software : CMSSW_10_3_1
# forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/ed4cc2a144a2435767daabdea0ecfff168d3bc27
# runForestAOD_pponAA_DATA_103X.py commit + turn off ZDC
# https://github.com/CmsHI/cmssw/commit/6e3b5960dc4ad1ca695bd3fc1eb1d93ec0119c7a

config.section_('Data')
#config.Data.inputDataset = '/HIHardProbes/HIRun2018A-PbPbZEE-PromptReco-v1/RAW-RECO'
#config.Data.inputDBS = 'global'
config.Data.userInputFiles = open('inputFiles_das_FOREST.txt').readlines()
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputPrimaryDataset = "HIHardProbes"
config.Data.outputDatasetTag = 'HIRun2018A-PbPbZEE-PromptReco-v1-FOREST-userInputFiles'
config.Data.outLFNDirBase = '/store/group/phys_heavyions/katatar/HIRun2018PbPb/'

config.section_('Site')
config.Site.storageSite = "T2_CH_CERN"
config.Site.whitelist = ["T1_US_FNAL"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
