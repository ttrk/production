from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018_hltTestEgamma_V70_L1_SK1212"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "hltConfig.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, 48 hours.
# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=47#Instructions_as_of_2018_10_26_in
## obsolete instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT?rev=26
# software : CMSSW_10_3_0
# no L1 tag

# Obsolete samples are listed here : https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018PrivateMC?rev=20#Tunes
config.section_("Data")
config.Data.inputDataset = "/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/katatar-HINPbPbSpring18GS_103X_upgrade2018_realistic_HI_v7_DIGI_L1_DIGI2RAW_HLT_PU-1c389861083a146d75ac332e7b4016f6/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "103X_upgrade2018_realistic_HI_v7_hltTestEgamma_V70_L1_SK1212"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/HLT/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

