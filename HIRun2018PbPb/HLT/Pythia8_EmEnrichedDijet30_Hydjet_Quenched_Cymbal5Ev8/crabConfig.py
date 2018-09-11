from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_EmEnrichedDijet30_Hydjet_Quenched_Cymbal5Ev8_hltTestEgamma_V32"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "hltConfig.py"
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, 48 hours.
# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT?rev=26
# software : CMSSW_10_1_2
# L1 tag : cms-l1t-offline:l1t-integration-v97.27.1-CMSSW_10_1_2

# Samples are listed here : https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018PrivateMC?rev=20#Tunes
config.section_("Data")
config.Data.inputDataset = "/Pythia8_EmEnrichedDijet30_Hydjet_Quenched_Cymbal5Ev8/clindsey-RAWSIM_20180630-d863108fee469c130ddd2763f36829bb/USER"
config.Data.inputDBS = "phys03"
# Code crashes in event with lumi=80527 in the following file. Skip that event by using masking its lumi.
# root://xrootd.cmsaf.mit.edu//store/user/clindsey/Pythia8_EmEnrichedDijet30_Hydjet_Quenched_Cymbal5Ev8/RAWSIM_20180630/180630_162218/0000/step1_DIGI_L1_DIGI2RAW_HLT_PU_405.root
config.Data.lumiMask = "customLumiMask.txt"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 30
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = "hltTestEgamma_V32"
config.Data.outLFNDirBase = "/store/user/katatar/HIRun2018PbPb/HLT/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]

