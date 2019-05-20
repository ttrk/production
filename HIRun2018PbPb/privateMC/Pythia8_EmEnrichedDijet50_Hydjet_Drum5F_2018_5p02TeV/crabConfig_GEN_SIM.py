from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = "Pythia8_EmEnrichedDijet50_Hydjet_Drum5F_2018_5p02TeV_PbPb2018_GEN_SIM_PU"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "step_GEN_SIM.py"
config.JobType.pyCfgParams=["maxEventsOutput=350"]
config.JobType.maxMemoryMB = 2500    # request high memory machines.
config.JobType.maxJobRuntimeMin = 2750    # request longer runtime, ~48 hours.

## CMSSW_10_3_3_patch1
## gen fragment :https://github.com/CmsHI/genproductions/blob/master/python/HI/photon_analysis/PbPb/5020GeV/Pythia8_EmEnrichedDijet50_TuneCP5_5020GeV_SingleParticleFilter_cff.py

config.section_("Data")
config.Data.outputPrimaryDataset = "EGamma"
config.Data.splitting = "EventBased"
## https://twiki.cern.ch/twiki/bin/view/CMS/MCFor2018PbPb5TeV
## Filter efficiency = 3.463E-02
## Assumption : 30 trials will give 1 events. Try 7500 units per job to output 250 events per job
TRIALPEROUTPUTEVT = 30
OUTPUTEVTSPERJOB = 250
config.Data.unitsPerJob = TRIALPEROUTPUTEVT * OUTPUTEVTSPERJOB
NJOBS = 4000  # try total output events = 1 M
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
## increase the number of "tried" events per lumi to avoid this problem : https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_submit_fails_with_Block_con
#config.JobType.eventsPerLumi = 100 * TRIALPEROUTPUTEVT

config.Data.outputDatasetTag = "Pythia8_EmEnrichedDijet50_Hydjet_Drum5F_2018_5p02TeV_PbPb2018_GEN_SIM_PU"
config.Data.outLFNDirBase = "/store/user/katatar/"

config.section_("Site")
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
