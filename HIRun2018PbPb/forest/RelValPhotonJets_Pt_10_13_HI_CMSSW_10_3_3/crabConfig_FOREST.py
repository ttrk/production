from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "RelValPhotonJets_Pt_10_13_HI_CMSSW_10_3_3_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_pponAA_MIX_103X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
## software : CMSSW_10_3_1
## forest_CMSSW_10_3_1
# https://github.com/CmsHI/cmssw/commit/c5058c956d1bb5cc638843508c0911e3585d1f2f
## runForestAOD_pponAA_MIX_103X.py commit
# https://github.com/CmsHI/cmssw/commit/b9ff187623bc36f16c23ac31de736b00e3130838
## related : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/5731.html

## Sample is pp_on_AA reco and not embedded.
config.section_("Data")
config.Data.inputDataset = "/RelValPhotonJets_Pt_10_13_HI/CMSSW_10_3_3-PU_103X_upgrade2018_realistic_HI_v11-v1/GEN-SIM-RECO"
#config.Data.allowNonValidInputDataset = True
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "CMSSW_10_3_3-PU_103X_upgrade2018_realistic_HI_v11-v1-FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/relval/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

