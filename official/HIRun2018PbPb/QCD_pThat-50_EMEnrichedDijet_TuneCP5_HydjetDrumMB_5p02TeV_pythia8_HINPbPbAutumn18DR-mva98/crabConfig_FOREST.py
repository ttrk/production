from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "QCD_pThat-50_EMEnrichedDijet_TuneCP5_HydjetDrumMB_5p02TeV_pythia8_HINPbPbAutumn18DR-mva98_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
#config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_3_patch1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/1519b69f556c8db08a3f177d372026193358432d
# runForestAOD_pponAA_MIX_103X.py commit + ggHi.doEffectiveAreas + enable ggHiNtuplizerGED doRecHits, doPhoERegression, doEleERegression, doSuperClusters, and doEvtPlane + activate l1object + add event plane info
# https://github.com/CmsHI/cmssw/commit/1f9264da586b55e0424c6a66b66d893af792e5f6
config.JobType.inputFiles = ["HeavyIonRPRcd_PbPb2018_offline.db"]

config.section_("Data")
config.Data.inputDataset = "/QCD_pThat-50_EMEnrichedDijet_TuneCP5_HydjetDrumMB_5p02TeV_pythia8/HINPbPbAutumn18DR-mva98_103X_upgrade2018_realistic_HI_v11-v2/AODSIM"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HINPbPbAutumn18DR-mva98_103X_upgrade2018_realistic_HI_v11-v2-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/official/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

#The server answered with an error.
#Server answered with: Invalid input parameter
#Reason is: ERROR: CMSSW_10_3_3_patch1 on slc7_amd64_gcc700 is not among supported releases; Use config.JobType.allowUndistributedCMSSW = True if you are sure of what you are doing
config.JobType.allowUndistributedCMSSW = True

