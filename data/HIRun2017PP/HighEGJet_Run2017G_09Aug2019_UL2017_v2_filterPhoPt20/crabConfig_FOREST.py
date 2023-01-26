from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "HighEGJet_Run2017G_09Aug2019_UL2017_v2_306546_306826_filterPhoPt20_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pp_DATA_106X.py"
#config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime.
## software : CMSSW_10_6_29
## forest_CMSSW_10_6_29
# https://github.com/CmsHI/cmssw/commit/6605d4e0cffbccbe8be3fffee9ee4f86bd1588a7
## runForestAOD_pp_DATA_106X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits, doPhoERegression, and doEleERegression + activate l1object
# https://github.com/CmsHI/cmssw/commit/6605d4e0cffbccbe8be3fffee9ee4f86bd1588a7
# dataset summary on DAS
#   output :  Number of blocks: 21 Number of events: 373368064 Number of files: 6140 Number of lumis: 31259 sum(file_size): 22519265148710 (22.5TB)

config.section_("Data")
config.Data.inputDataset = "/HighEGJet/Run2017G-09Aug2019_UL2017-v2/AOD"
config.Data.inputDBS = "global"
config.Data.lumiMask = "Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt" # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/5TeV/ReReco/Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt
#config.Data.runRange = "326500-326886"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 2
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "Run2017G-09Aug2019_UL2017-v2-Cert-306546-306826-filterPhoPt20-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_BE_UCL"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
