from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_AllQCDPhoton30_Hydjet_Cymbal_MB_FOREST_extendEC_pfSC_phiWidth0p40"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MIX_75X_ggHi_doRecHits.py"
config.JobType.maxMemoryMB = 2750    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2880    # request longer runtime, 48 hours.
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/f61094f7a81de65dc1f9796236b8ed94fca888a6
# runForestAOD_PbPb_MIX_75X.py commit + change gen particle pt and eta cuts + enable rechitanalyzer
# https://github.com/CmsHI/cmssw/commit/336108879815bf68a856f23a7a47254ef87347fd
# add rechits correspoding to a photon SC :
# <PUT THE COMMIT HERE>

config.section_("Data")
config.Data.inputDataset = "/Pythia8_AllQCDPhoton30_Hydjet_Cymbal_MB/katatar-HiFall15-75X_mcRun2_HeavyIon_v14-v1_RAW2DIGI_L1Reco_RECO_extendEC_pfSC_phiWidth0p40-7983486ae4f50b1e6045975dc5453e26/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "HiFall15-75X_mcRun2_HeavyIon_v14-v1_FOREST_extendEC_pfSC_phiWidth0p40"
config.Data.outLFNDirBase = "/store/user/katatar/EGamma/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

