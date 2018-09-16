from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018_hltTestEgamma_V34"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "hltConfig.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.
# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT?rev=26
# software : CMSSW_10_1_2
# L1 tag : cms-l1t-offline:l1t-integration-v97.27.1-CMSSW_10_1_2

# Samples are listed here : https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018OfficialMC?rev=15#Available_Samples_AN1
config.section_("Data")
#config.Data.allowNonValidInputDataset = True    # because the dataset is not 'VALID' but 'PRODUCTION'.
config.Data.inputDataset = "/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/HINPbPbSpring18DR-NoPU_100X_upgrade2018_realistic_v10_ext1-v1/GEN-SIM-RAW"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 20
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "hltTestEgamma_V34"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/HLT/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

