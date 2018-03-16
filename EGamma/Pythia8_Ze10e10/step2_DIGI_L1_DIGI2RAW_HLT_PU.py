# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --pileup_input dbs:/MinBias_TuneCUETP8M1_5p02TeV-pythia8/pp502Fall15-MCRUN2_71_V1-v1/GEN-SIM --pileup_dasoption=--limit=0 --mc --eventcontent RAWSIM --pileup pp5TeV_Poisson_1p5 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM-RAW --conditions 75X_mcRun2_asymptotic_ppAt5TeV_v3 --step DIGI,L1,DIGI2RAW,HLT:PRef -n 10 --no_exec --filein root://cms-xrd-global.cern.ch//store/himc/pp502Fall15/Pythia8_Ze10e10/GEN-SIM/MCRUN2_71_V1_ext1-v1/50000/0020CA3E-8C03-E611-B37D-44A842CFD5B1.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_PRef_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/himc/pp502Fall15/Pythia8_Ze10e10/GEN-SIM/MCRUN2_71_V1_ext1-v1/50000/0020CA3E-8C03-E611-B37D-44A842CFD5B1.root'),
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
process.mix.input.nbPileupEvents.averageNumber = cms.double(1.500000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-5)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/020D5E4D-E97E-E511-9681-001EC9ADE587.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/02B1BA24-F37E-E511-9E73-848F69FD29B8.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/0612E37C-D67E-E511-A870-001E67E71CE0.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/0845C6E6-037F-E511-948D-002590A50046.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/08AAC172-0D7F-E511-9F29-0025904E1286.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/0A8795BF-EA7E-E511-8A9E-44A842B298FE.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/0C8D2DEC-097F-E511-B777-002590200B38.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/0E237EDE-D97E-E511-83B3-001E67E6F65C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/0E2A55E4-D77E-E511-83E8-D8D385AF891A.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/0E5EA881-537F-E511-9607-782BCB67826E.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/0E7C8DCB-FC7E-E511-98B6-3417EBE528B5.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/0E931624-EB7E-E511-BC3E-002590A3C96C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/12C74E7F-FC7E-E511-BB55-001E67E6F404.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/1407E72D-F17E-E511-A3D3-3417EBE64402.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/14245DB2-017F-E511-BFA3-001D09FDD7D1.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/148591B6-087F-E511-96EA-02163E00EA13.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/16016E79-047F-E511-9BF1-003048C75802.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/16C4051C-E97E-E511-BB7E-002590FC5ACE.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/180B172A-F97E-E511-97B8-44A842BE8F7E.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/18460443-E57E-E511-9ABE-28924A33B9AA.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/1A35013E-ED7E-E511-9F54-003048C75DE4.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/1A40DB6C-107F-E511-94F4-0025904E4034.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/1ABE2C3C-E57E-E511-8BE1-00266CF3E3C4.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/1C12D421-E47E-E511-8797-44A842B46A98.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/1C2E0C2D-FD7E-E511-8E32-02163E00EABD.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/1C6C598C-DB7E-E511-8DF3-001E67D5D8EF.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/1E638995-CC7E-E511-BD5F-001EC9ADE550.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/1E66A841-D17E-E511-92C3-0025905C96E8.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/2008B030-D27E-E511-AA7F-0025904C66EE.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/204F1463-D17E-E511-9799-0025905C3DD0.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/2074A591-DD7E-E511-AA15-001E673D2261.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/228EDFB0-E07E-E511-9206-00266CF89130.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/2293C821-EB7E-E511-AA67-001EC9ADD78B.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/242FBBBD-DC7E-E511-9F85-001E67E6F864.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/24B3979C-ED7E-E511-B995-9CB654AEAC82.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/2645926D-D97E-E511-828A-34E6D7E05F1B.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/2650805A-EE7E-E511-9AC2-848F69FD12B3.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/2669CEF7-DE7F-E511-B9FF-0019BBEBF35E.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/28270680-F980-E511-9E9A-A0369F7F9EDC.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/28C64FF2-FA7E-E511-A2FB-02163E013719.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/28EAA99E-BB7F-E511-9DBD-00A0D1EC3950.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/2A4F4695-087F-E511-A20D-002590200B38.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/2A9B951C-CD7E-E511-A7E9-001E67E33C10.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/2C556024-E97E-E511-AE01-003048D43988.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/2CA238D6-DF7E-E511-A2F5-9CB654ADA584.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/2CEF3D9D-077F-E511-92D7-002590200838.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/307191EC-D37F-E511-BBB1-00266CF1027C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/323425B5-037F-E511-A840-7845C4FC3A9A.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/32659AF7-ED7E-E511-9205-0025904E42D2.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/32CB4584-E67E-E511-AFCE-001E6739AB19.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/34156DF2-D27E-E511-89B0-0025905C42F2.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/343D737F-537F-E511-AF80-44A842B46A71.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/34AF4BA1-C47E-E511-A6EE-002590200858.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/36EB38DE-DE7E-E511-95EE-001E6739703A.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/38C1D551-737F-E511-B39C-0025904C7F5C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/3AA49ADA-D27E-E511-A550-00269E95B17C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/3AF8A020-E27E-E511-A0A2-0025900EB0C6.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/3C27501E-D77E-E511-A73D-002590A80DE2.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/3CB5E2A0-ED7E-E511-A56A-001EC9ADC343.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/3EA01AFF-D37E-E511-B758-B083FED3F4E3.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/3EB76471-0A7F-E511-B76D-001E673D23F9.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/3EC929CA-E97E-E511-9F5A-001EC9ADDDF3.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/3ECA8668-E87E-E511-8E00-B499BAA67780.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/40291317-E87E-E511-AB9E-001A648F1BFA.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/4093965E-0D7F-E511-85DB-7845C4FC3B8D.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/40A6C854-E17E-E511-9A6A-0025902008FC.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/40D45633-E27E-E511-BCFC-20CF3027A5D4.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/40D8BD70-DF7E-E511-8DFB-002590A3707C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/40E4B3B6-CE7E-E511-AB23-001EC9ADDF6A.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/44414289-D07E-E511-A401-002590A3CA1A.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/445DD6D7-0280-E511-8B80-90E6BA5CBB3C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/448AE563-FA7E-E511-9F03-02163E014948.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/44F04F16-0380-E511-B4E8-001E67E71381.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/46557B8C-F17E-E511-A1D6-02163E00F68E.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/465C695B-E77E-E511-B19E-F04DA23BCE4C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/466FE7FF-F27E-E511-A32C-00237DF2B400.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/4C23C7E2-DF7E-E511-B7CC-B499BAA67F78.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/4C40D721-E77E-E511-8DA0-001EC9ADD812.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/4C6D34AA-D47E-E511-8844-6CC2173D46A0.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/4C992090-DB7E-E511-BA33-001E4F32EAA2.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/4CA6B0E1-D87E-E511-879E-78E7D1217468.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/4CC6FA5D-D97E-E511-9D52-001E67E6F864.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/4E7707CD-D77E-E511-9D2F-001E67E6F404.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/508BDB23-DD7E-E511-97E8-001E67E696A8.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/52A51C2D-E57E-E511-9BBC-0025904CFB76.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/54621BEB-D77E-E511-88D0-B083FED18BA0.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/546D4B02-D67E-E511-8F0A-50465DE43BAC.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/54A2B3AC-1A7F-E511-AB71-02163E00CA3F.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/54B2AC73-E67E-E511-8632-001EC9ADDF51.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/56CE6828-D57E-E511-90A5-0025904C6622.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/583AB1F2-E07E-E511-83D2-0025B3E02292.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/5867A655-1E80-E511-8376-00505602077E.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/5A30DFEE-D27E-E511-B6F0-0025904C66EE.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/5A59C828-EB7E-E511-822C-68B599B94F60.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/5A95D9C3-E97E-E511-B980-003048C7B924.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/5AAD8C6F-047F-E511-9B15-7845C4F91495.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/5C3D5FBB-D67E-E511-80CB-001E67E6F65C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/5C3FBEE9-E77E-E511-8D6C-BCEE7B2FE069.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/5E2BEACF-F17E-E511-9FEE-78E7D1239AB8.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/5E74C491-F37E-E511-AE4A-02163E016BEE.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/5ED3815F-097F-E511-8052-180373FF8446.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/60FEC49F-1581-E511-B182-001EC9ADC9B5.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/624B6C21-EB7E-E511-B72D-002481DE4A28.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/62B2C5B2-D07E-E511-9843-0025905C3DD0.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/64263D80-0B7F-E511-8AB2-78E7D12293A0.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/649E21E5-BC7F-E511-8B98-6CC2173DBFB0.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/66DF60E8-2C80-E511-8A41-00215A491916.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/684EBF68-E87E-E511-BB43-001EC9ADE258.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/68598032-D07E-E511-895A-0025905C431C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/685C72FB-D07E-E511-9F80-002219560D70.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/6A176423-DC7E-E511-83F1-001E67E6F65C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/6A3A245A-087F-E511-B73C-002590200B20.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/6A7558A0-D47F-E511-9A46-002618943C31.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/6A8CDD97-EC7E-E511-8457-00215A45F8B6.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/6A9064BD-DC7E-E511-900C-001E67E6F404.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/6C0A63F9-D57E-E511-BF00-0025904C66EE.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/6C65C856-037F-E511-8520-008CFA001EE4.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/6C8465BC-EB7E-E511-A16F-002590A3C96C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/6C95FB4E-CB7E-E511-8982-001EC9ADDDDF.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/6CE10285-057F-E511-BFFE-F04DA275C328.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/6E0192D3-E77E-E511-85CC-001EC9ADDF51.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/6E908EC1-0880-E511-849C-28924A3504DA.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/701691EF-0A7F-E511-8F78-0025904B2AB8.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/7089E2EB-B27F-E511-96E8-782BCB3BCA77.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/70F04A38-ED7E-E511-BEDF-7845C4FC35E1.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/723F40B7-FA7E-E511-BC7D-34E6D7E05F1B.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/74A3C2B9-007F-E511-93C5-02163E0148C4.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/74E6B0B3-DA7E-E511-B2EA-001E67E71BF5.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/762D415C-087F-E511-9B91-002590200974.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/76867E55-0A7F-E511-AB6C-02163E016928.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/76D2E3EC-D57E-E511-9A14-28924A35056A.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/78690E47-537F-E511-81DD-E0DB55FC100D.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/7886BD42-137F-E511-9DA1-02163E00B3FD.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/788EF370-D47E-E511-BD27-B083FED3F4E3.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/7A30CE57-D37E-E511-B927-0025904C4E2A.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/7A93902F-F97E-E511-B380-00259021A0E2.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/7AADC1E1-D87E-E511-ABDD-0025B3E02292.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/7AD4EA81-FC7E-E511-A642-3417EBE33927.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/7CA99F47-0F7F-E511-81A5-001EC9AE1AE3.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/7E1AC74B-CB7E-E511-B5C6-002590A88806.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/7E856FBE-E57E-E511-AB67-001E67D5D8EF.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/7EEEFA2A-F87E-E511-84AA-34E6D7E05F1B.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/80327527-EB7E-E511-A832-BC305B390A73.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/80841F3E-827F-E511-9951-02163E014F8B.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/80844ED5-257F-E511-9A01-001E67396DEC.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/8210C02E-2C7F-E511-90B3-9CB654AD7810.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/82FED53B-027F-E511-A842-02163E00F44F.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/8A107C23-DD7E-E511-B0D1-90B11CBCFF8F.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/8A3AECF9-D57E-E511-9B58-001E67E71CC7.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/8A4712A3-1180-E511-89E2-00259090765E.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/8A76E63F-D27E-E511-94D4-0025905C42F2.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/8ABC1528-DE7E-E511-AC44-002590D60004.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/8C0C5499-0E7F-E511-BAA5-0025904E1286.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/8C38EAC3-E57E-E511-9427-001EC9ADE1E0.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/9017E1E3-047F-E511-9B57-002590200838.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/920EBDD4-DF7E-E511-AF7E-002590A88810.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/92403F11-E57E-E511-B7AF-002590DD7C9E.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/941AEFAB-FA7E-E511-936D-7845C4F91537.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/945D519F-487F-E511-90B5-002590DE39F0.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/94FD13F6-B67F-E511-A7BF-001E6742FF8D.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/9602F09E-EA7E-E511-BC93-001E67396E28.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/984ACDBE-F37E-E511-8B95-00259021A14E.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/98F15CC0-F77E-E511-9F8F-7845C4FC364D.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/98F92588-F07E-E511-836F-00266CFAE684.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/98FD82B4-E07E-E511-BB0A-20CF3019DF00.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/9A21BE64-E87E-E511-843C-002590A37120.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/9A4C8A57-D17E-E511-81DB-0025905C2C84.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/9C902DF6-EE7E-E511-BD17-002590796302.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/9E038598-E47E-E511-94AD-002590C14B42.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/A055C1E0-C47F-E511-A555-001E672488D1.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/A233764F-E57E-E511-99A5-003048F23868.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/A26D3546-FF7E-E511-A0A6-C81F66C8BA4C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/A282166E-C87E-E511-9E8C-001EC9ADDC63.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/A4323A46-157F-E511-85AB-00266CF85908.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/A66ACAE0-DD7E-E511-8F78-FA163E008318.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/A6A3FC3B-E57E-E511-A7D7-002590DE6E30.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/A6A53653-0E80-E511-9102-001A648F12C2.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/A6B26D77-A17F-E511-894D-0025905C2CBE.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/A85C07FE-EE7E-E511-9F0E-02163E010DB4.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/AA571332-437F-E511-9592-00259073E390.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/AAE9B035-ED7E-E511-B149-002590A80E08.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/AC928A80-2B80-E511-A34B-C81F66C8BA4C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/ACB18E23-F87E-E511-90F7-0025905C42D2.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/AE47D5B2-E97E-E511-9F71-002590147CA2.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/AE7E1F98-B47F-E511-9642-9C8E9931E1E0.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/AE9BBA96-F97E-E511-BD7E-7845C4FC3A13.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/AEABCCEF-0A7F-E511-816E-0026B93F4112.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/AEE32934-D27E-E511-87DE-00269E95B17C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/B082D794-AE7F-E511-9AF4-002590AC50C2.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/B290B77C-E67E-E511-9845-002590FC5ACE.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/B41FC364-077F-E511-ABEE-02163E01146B.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/B423AB02-057F-E511-84EA-02163E01147F.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/B4B71CB3-037F-E511-B87B-848F69FD2907.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/B4E86CF4-E67E-E511-8879-001EC9ADE67C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/B6A9C339-3C7F-E511-A48A-38EAA7A6DC58.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/B849F375-E87E-E511-9B55-02163E013EB8.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/B883DB44-2D80-E511-B608-C81F66B7864D.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/B88F2A35-067F-E511-9318-7845C4FC3C80.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/BC5E42EC-097F-E511-B3F4-0026B95A4D42.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/BCC4F038-E57E-E511-9AD0-D8D385FF3201.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/BE2F7971-4280-E511-BD81-002590DE6E2E.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/BE4AC6B3-DA7E-E511-86E1-38EAA78D8F98.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/BE96A24E-087F-E511-8126-7845C4FC3B7B.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/C039F087-F07E-E511-A87B-002590A81DAC.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/C070CBB0-D87E-E511-88A0-001E67E6F404.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/C07474C6-F77E-E511-9BA7-34E6D7E3879B.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/C0F122EA-FD7E-E511-93DC-02163E014D90.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/C290A954-077F-E511-A6FD-0025901E1158.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/C4E4F6AA-DB7E-E511-B1E6-002590D60068.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/C6C07975-EC7E-E511-957E-001E67396ACC.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/C80BC297-E47E-E511-BCB6-20CF3027A59A.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/C893F738-E57E-E511-A4C6-02163E0168A5.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/CA0EA55A-EE7E-E511-835C-001E67398458.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/CC2FBD96-F97E-E511-A3BA-D8D385AE8BD0.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/CE132F54-027F-E511-B670-7845C4FC38ED.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/CE2DB92E-DE7E-E511-8197-0025B3268576.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/CE42C622-DC7E-E511-BBFD-001E67E71BF5.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/D2BB297B-DF7E-E511-B468-0025907DC9C4.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/D2BC5F78-B880-E511-964A-02163E00EAB3.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/D45BB724-DE7E-E511-8EF9-002590A80DDA.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/D47F135C-037F-E511-B38F-34E6D7E387A8.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/D688A1C3-0C7F-E511-A425-02163E014217.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/D84B6240-F17E-E511-A53B-44A842BFA94B.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/D865D9BE-DC7E-E511-9EC1-0CC47A124574.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/DA4BD256-367F-E511-8DBD-02163E012EFC.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/DCAD4E76-F57E-E511-84F6-7845C4FC35D8.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/DCC28E25-DD7E-E511-B3E6-001E67E6F8E6.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/DCC50B56-E17E-E511-A101-0026B94DBE31.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/E02C96F5-1E7F-E511-8520-02163E01156F.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/E0A007C9-ED7E-E511-A9D2-002590A80E08.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/E0C1C166-247F-E511-8ABB-02163E01692A.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/E4AE249F-1A7F-E511-BC54-0025904C7A60.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/E4E759E1-D87E-E511-9DAF-001E67E6F65C.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/E4F66306-187F-E511-AEC5-02163E016740.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/E603C527-0E7F-E511-B67B-02163E00F706.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/E8FF6323-E97E-E511-BA44-002590DD7E50.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/EC3CF275-127F-E511-AF70-44A842B4CC71.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/EC5F704F-D97E-E511-92F6-38EAA78D8F98.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/ECC6AED9-EF7E-E511-8F02-3417EBE2EEC6.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/F40B5E6C-D47E-E511-ADBC-0025904C6622.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/F473C48D-EE7E-E511-9FEB-002590A80E08.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/F4D36A72-3E80-E511-9E69-D4AE526A1010.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/F657C08E-D47E-E511-B37F-001E67E6F512.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/F6C09D50-FE7E-E511-BBC9-34E6D7E05F28.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/F6C6F716-3C7F-E511-99BE-001EC9ADDC9F.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/F6CD5EC5-C47F-E511-A77E-74867AD4BE94.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/F6E9EA3D-D77E-E511-8522-002590D60098.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/F6F94A8E-F87E-E511-B0D2-02163E016BEE.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/F82A3304-7080-E511-AAA6-002590DE3AC0.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/F8722969-E27E-E511-83C0-02163E0168C5.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/F892DAC8-FC7E-E511-A5D2-34E6D7E38781.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/FC341896-DD7E-E511-9168-0023AEEEB559.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/FC512085-057F-E511-AEE6-001E67E6F819.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/FC690BE2-D77E-E511-B34E-0023AEEEB559.root', '/store/himc/pp502Fall15/MinBias_TuneCUETP8M1_5p02TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/80000/FEF21A89-DC7E-E511-BA4C-001E4F33E1FD.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_mcRun2_asymptotic_ppAt5TeV_v3', '')

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

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)

# End of customisation functions
