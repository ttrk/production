from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'PAEGJet1_PARun2016C_PromptReco_v1_HLTfilter_SinglePhoton_FOREST'
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pPb_DATA_80X_HLTfilter.py'
# forest_CMSSW_8_0_22
# https://github.com/CmsHI/cmssw/commit/af73978e5aad673186cb56e2610887c98e6d8674
# runForestAOD_pPb_DATA_80X.py commit + HLT filter
# https://github.com/CmsHI/cmssw/commit/5f80b18a63a6006b1e2d2773baa213c88705a5d0

config.section_('Data')
config.Data.inputDataset = '/PAEGJet1/PARun2016C-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
# lumiMask is the manually merged version of these two :
# /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/HI/Cert_285479-285832_HI8TeV_PromptReco_pPb_Collisions16_JSON_NoL1T.txt
# /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/HI/Cert_285952-286009_HI8TeV_PromptReco_Pbp_Collisions16_JSON_NoL1T.txt
# related : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/3626.html
config.Data.lumiMask = '/afs/cern.ch/work/k/katatar/public/forest/CMSSW_8_0_23/src/PAEGJet1_PARun2016C_PromptReco_v1_HLTfilter_SinglePhoton/Cert_285479-286009_HI8TeV_PromptReco_pPb_Pbp_Collisions16_JSON_NoL1T_MERGED.txt'
#config.Data.runRange = '263233-263284'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'PARun2016C_PromptReco_v1_HLTfilter_SinglePhoton_FOREST'
config.Data.outLFNDirBase = '/store/user/katatar/'

# https://github.com/richard-cms/production/commits/2016-03-17-reRECO-foresting/crabConfig.py
config.section_('Site')
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT", "T2_US_Vanderbilt"]
