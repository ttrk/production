from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "L1Ntuple_Pythia8_EmEnrichedDijet30_Hydjet_Quenched_Cymbal5Ev8"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "l1Ntuple_RAW2DIGI.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines, 2500 is the maximum guaranteed number.
config.JobType.maxJobRuntimeMin = 2750 # request longer runtime, ~47 hours. 2750 is the maximum guaranteed number.
## Software
# CMSSW_10_2_1, l1t-integration-v99.0
# This integration contains the new L1 EG bypass flags : https://github.com/cms-l1t-offline/cmssw/pull/708
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TStage2Instructions?rev=140#Environment_Setup_with_Integrati
## Driver
# https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce?rev=42#Offline_SW_setup
# l1Ntuple_RAW2DIGI.py is created after calling ./createConfigs.sh

# Samples are listed here : https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018PrivateMC?rev=19#Tunes
config.section_("Data")
config.Data.inputDataset = "/Pythia8_EmEnrichedDijet30_Hydjet_Quenched_Cymbal5Ev8/clindsey-RAWSIM_20180630-d863108fee469c130ddd2763f36829bb/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 120
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "L1Ntuple_egHOverEcut_EB1_EE1_egEtaCut24"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/L1T/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
