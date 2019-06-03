# simple code to make L1Ntuple, no emulation is done

import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('MyL1Ntuple')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
#process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
#process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
#process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/himc/HINPbPbAutumn18DR/MinBias_Hydjet_Drum5F_2018_5p02TeV/AODSIM/NoPU_103X_upgrade2018_realistic_HI_v11-v1/80000/F21D1792-30BA-0249-B451-3F33E8186955.root'),
    secondaryFileNames = cms.untracked.vstring()
)

#process.options = cms.untracked.PSet(
#)

# Production Info

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_realistic_hi', '')

process.schedule = cms.Schedule()

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
#from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleEMU,L1NtupleGEN
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleEMU 

#call to customisation function L1NtupleEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleEMU(process)

#call to customisation function L1NtupleGEN imported from L1Trigger.L1TNtuples.customiseL1Ntuple
#process = L1NtupleGEN(process)

process.l1UpgradeEmuTree.egToken = cms.untracked.InputTag("caloStage2Digis","EGamma")
process.l1UpgradeEmuTree.jetToken = cms.untracked.InputTag("caloStage2Digis","Jet")
process.l1UpgradeEmuTree.maxL1Upgrade = cms.uint32(60)
process.l1UpgradeEmuTree.muonToken = muonToken = cms.untracked.InputTag("gmtStage2Digis","Muon")
process.l1UpgradeEmuTree.sumToken = cms.untracked.InputTag("caloStage2Digis","EtSum")
process.l1UpgradeEmuTree.tauTokens = cms.untracked.VInputTag(cms.InputTag("caloStage2Digis","Tau"))

# Schedule definition
#process.endjob_step = cms.EndPath(process.L1NtupleEMU+process.L1NtupleGEN)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need

# End adding early deletion
