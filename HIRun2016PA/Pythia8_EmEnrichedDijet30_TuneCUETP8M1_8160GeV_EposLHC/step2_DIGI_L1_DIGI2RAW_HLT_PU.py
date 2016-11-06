# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions 80X_mcRun2_asymptotic_v17 --pileup_input dbs:/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/pPb816Spring16GS-80X_mcRun2_asymptotic_v17-v1/GEN-SIM --pileup_dasoption=--limit=100 --eventcontent RAWSIM -s DIGI,L1,DIGI2RAW,HLT:@fake --datatier GEN-SIM-RAW --pileup HiMix --era Run2_2016 -n 10 --no_exec --filein=file:Pythia8_EmEnrichedDijet30_TuneCUETP8M1_8160GeV_SingleParticleFilter_cff_py_GEN_SIM_PU.root
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
    fileNames = cms.untracked.vstring('file:Pythia8_EmEnrichedDijet30_TuneCUETP8M1_8160GeV_SingleParticleFilter_cff_py_GEN_SIM_PU.root'),
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

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('step2_DIGI_L1_DIGI2RAW_HLT_PU.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0015599B-5671-E611-A11A-008CFAFC043A.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0032A97D-6671-E611-ADED-848F69FD2826.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0039E374-6071-E611-AD5B-047D7B2E84EC.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0050A418-7171-E611-887D-14187741013C.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/00618F48-5971-E611-A74A-0CC47A4DEE00.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0071D8A7-5F71-E611-884D-0025905C3DD0.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/00C10B26-6D71-E611-B92D-848F69FD28E3.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/00F467B1-6B71-E611-BBC7-901B0E5427B0.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/00F72BC0-6871-E611-8A98-B499BAAC054A.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/023D4492-6871-E611-8987-002590D6004A.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/024FE11C-5771-E611-9C5E-0025904C66E4.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/025E5458-7671-E611-9C7F-10BF481A0245.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/027D325A-5E71-E611-9B90-0025905C54B8.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/02893F0C-5C71-E611-AFE7-001517EA9DC0.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/02DFA0B3-7071-E611-8D7F-7845C4FC3A13.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/02F02860-5871-E611-A5BD-0025905D1CAE.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0422E697-6B71-E611-9165-44A842CFD5B1.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/042C030F-7371-E611-98EC-20CF305B057C.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/04381CE4-6471-E611-AC14-7845C4FBBD07.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0455DBBA-6B71-E611-A8E4-02163E014A43.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0458DD97-6B71-E611-9558-848F69FD4FB5.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/045B64C0-4F71-E611-84DB-782BCB5301D0.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/048AD6A0-7871-E611-8C36-20CF3027A582.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/04DCC7C2-6871-E611-890A-0CC47A713A04.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/04E72A43-5271-E611-8D25-44A842CFD619.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/04F92BAB-5471-E611-9AD0-901B0E5427A6.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/04FB2524-5871-E611-95D9-008CFAF750B6.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/060851C4-6471-E611-9FAE-44A84225C4EB.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/060FB1FC-6571-E611-8AF3-003048F23D58.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/06142A08-7371-E611-9505-842B2B1811D7.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0616C1F8-6171-E611-8B3D-842B2B42D35D.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/06189A16-7871-E611-A304-001E6739BB01.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/064CA0A4-7871-E611-9184-0025901A9EFC.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/065144A6-6471-E611-B3B8-003048F23D58.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/06663F37-5571-E611-8086-0025905C42A8.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/068D66D9-6471-E611-878A-549F3525DD6C.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/06AD6D98-6071-E611-AACB-003048F3100A.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/06C03C18-5E71-E611-B51E-002590A36084.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/06CEB5B8-6871-E611-86AB-001517EA8BE4.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/06F1E625-6171-E611-A4C8-842B2B42D35D.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/08080B12-7471-E611-A149-1458D04903A8.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/083013B0-6E71-E611-BB9A-00266CF9B59C.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/08394051-5171-E611-B756-FA163E9F9947.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/08722E52-7971-E611-BAEB-02163E01515F.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/087B34C0-6A71-E611-939C-003048F3521E.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/087D8A9D-7671-E611-8101-A0000220FE80.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/088EAFE2-6971-E611-84C9-2C600C7BF9BE.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/089B2D26-7371-E611-90D6-0025904CF764.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0A38E96C-6371-E611-8E99-001E6739AFB9.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0A40F141-6571-E611-A245-02163E01612B.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0A6650F9-5F71-E611-96C5-02163E015F44.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0A78C5B3-6971-E611-B2F8-002481CFE26A.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0A7D0F1E-6F71-E611-8BAB-782BCB2101DC.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0AA314F1-6171-E611-9CCE-20CF300E9EDD.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0AF108F1-6F71-E611-A305-6C3BE5B5A4C8.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0AF3403C-5971-E611-86CB-B499BAAC054A.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0C11C32E-5671-E611-9EE9-28924A38DC1E.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0C250AB2-7271-E611-8921-A0369F7FC83C.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0C8965EF-5771-E611-ADC0-001E67FA403C.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0CB4CF2E-6571-E611-A57F-848F69FD2817.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0CC38C58-4771-E611-9FE1-FA163E4A04FB.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0CC49FA8-5171-E611-AE7B-02163E012D08.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0CC9F403-6A71-E611-AC4E-0025B3268576.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0CF07AED-5F71-E611-BEF1-7845C4FC3623.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0E1DD549-6671-E611-AA78-848F69FD28FE.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0E237FBD-6A71-E611-9F1A-842B2B42B536.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0E46C1B7-6F71-E611-954A-A0369F6367C2.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0E67D175-7671-E611-BB33-842B2B17EE7F.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0EB9F2AB-7771-E611-9D2D-20CF3027A59F.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0ED7E8AB-5471-E611-BF03-001E67F8FA4C.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0EFC96DC-4671-E611-9917-3417EBE64561.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/102F0074-4871-E611-8109-0CC47A4C6FDC.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/1042BCAF-5B71-E611-A6DB-0025905C2CEA.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/1045A492-6F71-E611-932D-00266CFFC6CC.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/104869EF-6D71-E611-91A3-001E6739BB01.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/104EE85A-6971-E611-A0BB-180373FF8D42.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/10767775-7471-E611-947E-1CC1DE1CF622.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/109F665D-6A71-E611-A9D8-6CC2173BB900.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/10D2D93C-7171-E611-AF70-008CFA064884.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/10F53BB9-4771-E611-A546-6CC2173CAAE0.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/1200F24E-7671-E611-8B05-001E67399C89.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/1221C832-5071-E611-A56B-001EC9ADEA41.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/126BA7EE-5671-E611-BDB7-A0369F7F9DE0.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/127466F7-6771-E611-852D-1418774118F6.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/12C28AC2-7571-E611-AC88-D4AE526DEDB7.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/12C328C6-5571-E611-923B-FA163E6627D1.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/12E27E1E-7971-E611-A5DF-008CFAF0842A.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/1404694D-7371-E611-B399-842B2B17EE7F.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/14302121-5771-E611-B64C-FA163E26BF36.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/1435CAD8-4B71-E611-8355-FA163E8FC0DE.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/14BD7562-6171-E611-87C5-001E67F8F9E8.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/14F95F93-6971-E611-A151-001E6739BC29.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/14FA8BB6-7871-E611-A3C3-0CC47A7D9870.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/1668F5A3-4371-E611-BECE-02163E014973.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/1676E8C1-6A71-E611-995D-0025908210E6.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/168BC102-5A71-E611-A790-C4346BC75558.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/16BB6CE9-5B71-E611-A019-0025901A9EFC.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/16D4CAD5-6671-E611-B6EC-001E67398025.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/16D9D8CF-6871-E611-A582-FA163E76145C.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/16E5DE45-6D71-E611-A451-00266CFFC6CC.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_v17', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)

# End of customisation functions

