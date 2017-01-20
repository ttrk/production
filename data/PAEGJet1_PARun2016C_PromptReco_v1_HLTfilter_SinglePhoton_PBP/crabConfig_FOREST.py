from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'PAEGJet1_PARun2016C_PromptReco_v1_HLTfilter_SinglePhoton_PBP_FOREST'
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pPb_DATA_80X_HLTfilter.py'
# forest_CMSSW_8_0_22
# https://github.com/CmsHI/cmssw/commit/8e55358ae9a5842cb986078b5db42fac7e5b95ad
# runForestAOD_pPb_DATA_80X.py commit + HLT filter
# https://github.com/CmsHI/cmssw/commit/5f80b18a63a6006b1e2d2773baa213c88705a5d0

config.section_('Data')
config.Data.inputDataset = '/PAEGJet1/PARun2016C-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
# related : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/3677.html
# /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/HI/Cert_285952-286496_HI8TeV_PromptReco_Pbp_Collisions16_JSON_NoL1T.txt
config.Data.lumiMask = 'Cert_285952-286496_HI8TeV_PromptReco_Pbp_Collisions16_JSON_NoL1T.txt'
#config.Data.runRange = '263233-263284'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'PARun2016C_PromptReco_v1_HLTfilter_SinglePhoton_PBP_FOREST'
config.Data.outLFNDirBase = '/store/user/katatar/'

# https://github.com/richard-cms/production/commits/2016-03-17-reRECO-foresting/crabConfig.py
config.section_('Site')
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT", "T2_US_Vanderbilt"]
