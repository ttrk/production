from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_QCDPhoton_pThat15_Run3_HydjetEmbedded_pbpb22_hltTest_cmssw_12_3_0_HIon_V8"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "hltConfig.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, 48 hours.
# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2021HLT?rev=83#HLT_trees_CMSSW_12_3_X_Version_w
# software : CMSSW_12_3_0

# Obsolete samples are listed here : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2021HLT#Simulations
config.section_("Data")
config.Data.inputDataset = "/QCDPhoton_pThat15_Run3_HydjetEmbedded/mnguyen-QCDPhoton_pThat15_Run3_HydjetEmbedded_DIGI-752b0cc9d22f4a7f20eccfe0d5df0682/USER"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
#config.Data.outputDatasetTag = "cmssw_12_3_0_HIon_V84"
config.Data.outputDatasetTag = "pbpb22_hltTest_cmssw_12_3_0_HIon_V8"
config.Data.outLFNDirBase = "/store/user/katatar/run3/HLT/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT"]

#config.section_("Debug")
#config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

