from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'forest_dielectron_HIPhoton40AndZ'
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_PbPb_DATA_75X.py'
config.JobType.maxMemoryMB = 2500    # request high memory machines, 2500 is the maximum guaranteed number.
config.JobType.maxJobRuntimeMin = 2800    # request longer runtime, ~47 hours. 2800 is the maximum guaranteed number.
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/c32f0fc41c29226dc80cac56a4ef063f4ea4b2df
# runForestAOD_PbPb_DATA_75X.py commit
# https://github.com/CmsHI/cmssw/commit/c32f0fc41c29226dc80cac56a4ef063f4ea4b2df

config.section_('Data')
config.Data.inputDataset = '/HIPhoton40AndZ/katatar-HIRun2015-PromptReco-v1-AOD-dielectron-skim-f8ca4a1d94c645c1a352f0d31009e079/USER'
config.Data.inputDBS = 'phys03'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 5
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'HIRun2015-PromptReco-v1-AOD-dielectron-skim-FOREST'
config.Data.outLFNDirBase = '/store/user/katatar/'

# https://github.com/richard-cms/production/commits/2016-03-17-reRECO-foresting/crabConfig.py
config.section_('Site')
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT"]

config.section_("Debug")
config.Debug.extraJDL = ["+CMS_ALLOW_OVERFLOW=False"]
