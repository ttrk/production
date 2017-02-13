from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'GJets_1j_Gpt15_5f_NLO_TuneCUETP8M1_5020GeV_amcatnloFXFX_pythia8_FOREST'
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pp_MC_75X.py'
# config.JobType.maxMemoryMB = 3500
# forest_CMSSW_7_5_8_patch3
# https://github.com/CmsHI/cmssw/commit/9ead9d0df8c6df3da912116100bfeee5774b3fac
# runForestAOD_pp_MC_75X.py commit + change gen particle pt and eta cuts
# https://github.com/CmsHI/cmssw/commit/746b5cde271c0e27629823699677aaf5d2162f26

config.section_('Data')
config.Data.inputDataset = '/GJets_1j_Gpt15_5f_NLO_TuneCUETP8M1_5020GeV-amcatnloFXFX-pythia8/HINppWinter16DR-75X_mcRun2_asymptotic_ppAt5TeV_v3-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'HINppWinter16DR-75X_mcRun2_asymptotic_ppAt5TeV_v3-v1-FOREST'
config.Data.outLFNDirBase = '/store/user/katatar/official/'

# https://github.com/richard-cms/production/commits/2016-03-17-reRECO-foresting/crabConfig.py
config.section_('Site')
config.Site.storageSite = 'T2_US_MIT'

