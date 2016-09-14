# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions 80X_mcRun2_asymptotic_v15 --pileup_input das:/EPOSpPb_MinBias4080_4080_1M/gsfs-GEN_SIM_20160822-d4761a1e86cf6de84555bcb356232d4c/USER --eventcontent FEVTDEBUG -s DIGI,L1,DIGI2RAW,HLT:@fake --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --pileup HiMix --era Run2_2016 -n 10 --no_exec --filein=file:Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV_cff_py_GEN_SIM_PU.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.HiMix_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV_cff_py_GEN_SIM_PU.root'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-HLTDEBUG'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('step2_DIGI_L1_DIGI2RAW_HLT_PU.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
##### manually add private dataset files used in "--pile_input" option #####
process.mix.input.fileNames = cms.untracked.vstring([
'/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_1.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_103.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_104.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_105.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_106.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_107.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_108.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_11.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_110.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_111.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_114.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_116.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_117.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_120.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_122.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_124.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_126.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_128.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_129.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_13.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_130.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_131.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_133.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_136.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_140.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_143.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_145.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_146.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_148.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_149.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_150.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_155.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_161.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_163.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_165.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_168.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_170.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_172.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_174.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_175.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_176.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_177.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_178.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_179.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_18.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_180.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_182.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_183.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_184.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_185.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_186.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_187.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_188.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_189.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_190.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_191.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_192.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_193.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_194.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_195.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_196.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_197.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_198.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_199.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_2.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_200.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_201.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_202.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_203.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_206.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_208.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_21.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_211.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_212.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_215.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_217.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_218.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_220.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_222.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_223.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_224.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_227.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_228.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_231.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_232.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_233.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_24.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_240.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_241.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_244.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_246.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_247.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_248.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_249.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_252.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_253.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_254.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_259.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_266.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_269.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_27.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_270.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_271.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_272.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_275.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_276.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_278.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_28.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_281.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_282.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_286.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_289.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_290.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_291.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_292.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_293.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_294.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_295.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_296.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_297.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_299.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_3.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_30.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_300.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_301.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_302.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_303.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_304.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_305.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_306.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_307.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_308.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_309.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_31.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_310.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_311.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_312.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_313.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_315.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_316.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_317.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_318.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_319.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_32.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_322.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_323.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_324.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_326.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_328.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_329.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_33.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_331.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_332.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_334.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_336.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_341.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_342.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_343.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_345.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_347.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_349.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_352.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_354.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_358.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_361.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_363.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_368.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_372.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_378.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_38.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_382.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_383.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_384.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_385.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_387.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_388.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_389.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_391.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_392.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_395.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_396.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_397.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_398.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_399.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_4.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_40.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_400.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_402.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_403.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_404.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_405.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_406.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_407.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_408.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_410.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_411.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_412.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_414.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_415.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_416.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_417.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_418.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_42.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_420.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_421.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_422.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_423.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_424.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_425.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_426.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_427.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_43.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_430.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_431.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_432.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_435.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_437.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_438.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_44.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_441.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_442.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_443.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_445.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_446.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_449.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_45.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_453.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_457.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_46.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_465.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_467.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_468.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_47.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_470.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_473.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_474.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_475.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_476.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_477.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_478.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_479.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_48.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_480.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_481.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_482.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_483.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_485.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_486.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_487.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_488.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_489.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_49.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_490.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_491.root',
       '/store/user/gsfs/EPOSpPb_MinBias4080_4080_1M/GEN_SIM_20160822/160822_172214/0000/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi_py_GEN_SIM_492.root' 
])
##### manually add private dataset files used in "--pile_input" option - END #####

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_v15', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)

# End of customisation functions

