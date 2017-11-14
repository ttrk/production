from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "LowEGJet_Run306462_RECO_94X_GT_Prompt_forHIN"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "Reco_9_4_0.py"
config.JobType.maxMemoryMB = 2400
config.JobType.maxJobRuntimeMin = 2400
# CMSSW_9_2_14_patch1

config.section_("Data")
config.Data.userInputFiles = ["root://eoscms//eos/cms/tier0/store/backfill/1/data/Tier0_REPLAY_vocms047/LowEGJet/RAW/v215/000/306/462/00000/52D37C2A-14C7-E711-B21A-02163E011DD0.root",
"root://eoscms//eos/cms/tier0/store/backfill/1/data/Tier0_REPLAY_vocms047/LowEGJet/RAW/v215/000/306/462/00000/440A48A5-3CC6-E711-827B-02163E01A230.root",
"root://eoscms//eos/cms/tier0/store/backfill/1/data/Tier0_REPLAY_vocms047/LowEGJet/RAW/v215/000/306/462/00000/D6B0EAB0-3CC6-E711-B119-02163E01A61A.root",
"root://eoscms//eos/cms/tier0/store/backfill/1/data/Tier0_REPLAY_vocms047/LowEGJet/RAW/v215/000/306/462/00000/7C8A8EB0-3CC6-E711-9A3C-02163E01A583.root",
"root://eoscms//eos/cms/tier0/store/backfill/1/data/Tier0_REPLAY_vocms047/LowEGJet/RAW/v215/000/306/462/00000/10FE8EA3-3CC6-E711-AC63-02163E019E4E.root"]
#config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.outputPrimaryDataset = "dataProcessing"
config.Data.outputDatasetTag = "LowEGJet_Run306462_RECO_94X_GT_Prompt_forHIN"
config.Data.outLFNDirBase = "/store/group/phys_heavyions/katatar/HIRun2017PP/"

config.section_("Site")
config.Site.storageSite = "T2_CH_CERN"
config.Site.whitelist = ["T2_CH_CERN"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
