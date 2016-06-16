from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'forest_dielectron_HighPtPhoton30AndZ'
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pp_DATA_75X.py'
# config.JobType.maxMemoryMB = 3500
# https://github.com/CmsHI/cmssw/commit/4040e9a38ec26f96541a07c17d09efec9c99db51
# runForestAOD_pp_DATA_75X.py commit
# https://github.com/CmsHI/cmssw/commit/3cf8d6b741d1c55284904fada7ed1174ac4daa87

config.section_('Data')
config.Data.inputDataset = '/HighPtPhoton30AndZ/azsigmon-Run2015E-PromptReco-AOD-DielectronSkim-v2-0d8b27ea5ddb998af72cec10f8b38257/USER'
config.Data.inputDBS = 'phys03'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/5TeV/Cert_262081-262328_5TeV_PromptReco_Collisions15_25ns_JSON.txt'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 30
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'HIRun2015E-PromptReco-AOD-dielectron-skim-FOREST'
config.Data.outLFNDirBase = '/store/user/katatar/'

# https://github.com/richard-cms/production/commits/2016-03-17-reRECO-foresting/crabConfig.py
config.section_('Site')
config.Site.storageSite = "T2_US_MIT"
config.Site.whitelist = ["T2_US_MIT", "T2_HU_Budapest"]
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

