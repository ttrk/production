from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_Ze10e10_Hydjet_Quenched_Cymbal5Ev8_pp_on_AA_FOREST"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_MC_101X.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, 48 hours.
# forest setup : https://twiki.cern.ch/twiki/bin/view/CMS/HiForestSetup?rev=52#Setup_for_10_1_0_pre2_For_PbPb_2
# forest_CMSSW_10_1_0_pre2
# https://github.com/bi-ran/cmssw/commit/f2808ca5cf8aac5e6d33d493cc6e1f1479132d3d
# runForestAOD_PbPb_MC_101X.py commit
# https://github.com/bi-ran/cmssw/commit/f2808ca5cf8aac5e6d33d493cc6e1f1479132d3d

# Samples are listed here : https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018PrivateMC?rev=18#Tunes
config.section_("Data")
config.Data.inputDataset = "/Pythia8_Ze10e10_Hydjet_Quenched_Cymbal5Ev8/clindsey-AODSIM_20180723_pp_on_AA-b7cacae03ea78f1a9a439e6efe1e6356/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "pp_on_AA_FOREST"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

