# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/Pythia8_Dijet15_pp_TuneCUETP8M1_8160GeV_cff.py --conditions 80X_mcRun2_asymptotic_v15 -s GEN,SIM --pileup_input das:/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/pPb816Spring16GS-80X_mcRun2_asymptotic_v17-v1/GEN-SIM --era Run2_2016 --eventcontent RAWSIM --pileup HiMixGEN --datatier GEN-SIM --beamspot Match5TeVPPbBoost --scenario HeavyIons -n -1 -o 10 --no_exec --python_filename=Pythia8_Dijet15_pp_TuneCUETP8M1_8160GeV_EposLHC_GEN_SIM_PU.py
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.HiMixGEN_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.HiGenCommon.VtxSmearedMatch5TeVPPbBoost_cff')
process.load('Configuration.StandardSequences.GeneratorMix_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('PYTHIA 8 (unquenched) dijets in NN (pt-hat > 15 GeV) at sqrt(s) = 8.16 TeV')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('Pythia8_Dijet15_pp_TuneCUETP8M1_8160GeV_cff_py_GEN_SIM_PU.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0015599B-5671-E611-A11A-008CFAFC043A.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0032A97D-6671-E611-ADED-848F69FD2826.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0039E374-6071-E611-AD5B-047D7B2E84EC.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0050A418-7171-E611-887D-14187741013C.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/00618F48-5971-E611-A74A-0CC47A4DEE00.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0071D8A7-5F71-E611-884D-0025905C3DD0.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/00C10B26-6D71-E611-B92D-848F69FD28E3.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/00F467B1-6B71-E611-BBC7-901B0E5427B0.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/00F72BC0-6871-E611-8A98-B499BAAC054A.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/023D4492-6871-E611-8987-002590D6004A.root'])
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_v15', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'processParameters'),
        processParameters = cms.vstring('HardQCD:all = on', 
            'PhaseSpace:pTHatMin = 15.', 
            'PhaseSpace:pTHatMax = 9999.'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    comEnergy = cms.double(8160.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 


