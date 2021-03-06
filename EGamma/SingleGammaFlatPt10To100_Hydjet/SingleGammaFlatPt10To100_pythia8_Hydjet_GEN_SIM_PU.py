# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SingleGammaFlatPt10To100_pythia8_cfi.py --pileup_input dbs:/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/HiFall15-75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/GEN-SIM --mc --eventcontent RAWSIM --pileup HiMixGEN --datatier GEN-SIM --conditions 75X_mcRun2_HeavyIon_v14 --beamspot RealisticHICollision2015 --step GEN,SIM --scenario HeavyIons --era Run2_HI -n 20 --no_exec --python_filename SingleGammaFlatPt10To100_pythia8_Hydjet_GEN_SIM_PU.py --fileout SingleGammaFlatPt10To100_pythia8_Hydjet_GEN_SIM_PU.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_HI)

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
process.load('IOMC.EventVertexGenerators.VtxSmearedRealisticHICollision2015_cfi')
process.load('Configuration.StandardSequences.GeneratorMix_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/SingleGammaFlatPt10To100_pythia8_cfi.py nevts:20'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
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
    fileName = cms.untracked.string('SingleGammaFlatPt10To100_pythia8_Hydjet_GEN_SIM_PU.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/005F5115-9BD4-E611-AB73-0025905C431C.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/0062542B-A7D4-E611-BDA2-0025905C2CD0.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/006B6A2A-D4D4-E611-91D0-00269E95B1B8.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/00839502-96D4-E611-B666-02163E013EEB.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/009B5A74-CED4-E611-8F43-20CF3019DEEF.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/00A04E07-D4D4-E611-B9D5-0090FAA58544.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/00B28404-D0D4-E611-907C-001E68862A40.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/00DA17A4-C0D4-E611-885F-1866DAEA7A40.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/00EAE9E5-BFD4-E611-B094-FA163E71C1CA.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/00FF50B2-DBD4-E611-B55F-0025904C63F8.root'])
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_mcRun2_HeavyIon_v14', '')

process.generator = cms.EDFilter("Pythia8PtGun",
    PGunParameters = cms.PSet(
        AddAntiParticle = cms.bool(True),
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MaxPt = cms.double(100.0),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double(10.0),
        ParticleID = cms.vint32(22)
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring()
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single gamma pt 10 to 100')
)


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
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 


