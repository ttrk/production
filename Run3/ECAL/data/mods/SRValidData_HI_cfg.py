import FWCore.ParameterSet.Config as cms

process = cms.Process("EcalSelectiveReadoutValid")
process.options = cms.untracked.PSet( allowUnscheduled = cms.untracked.bool(True) )
###process.load('Configuration.StandardSequences.GeometryRecoDB_cff')

#Number of events to process
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    #input = cms.untracked.int32(10)
    #input = cms.untracked.int32(1000)
)
#Input files
process.source = cms.Source("PoolSource",
      fileNames = cms.untracked.vstring(
# RAW runs 2018
# HLTPHYSICS RUN 324747 Fill=7309, Colliding bunches:, PU=?, DT=7% Date:
#'file:/wk_cms/paganis/data/HLTPhysicsRun2018D/324/747/A2A5C20E-D62F-594D-A2E2-0CF532189346.root',#LS=875-890, PU=31
#
# Special High PU RUN 325310 Fill=7358, Colliding bunches:26, PU=?:, HLTPhysics DT=7%
#'file:/wk_cms/paganis/data/HLTPhysicsRun2018E/325/310/B78CE309-9B47-8B4C-BA21-400928224A43.root',#LS=33-34, PU=98
'file:/wk_cms/paganis/data/HLTPhysicsRun2018E/325/310/BAF43ACB-24C6-D04A-9EEA-FA1481CDBFC7.root',#LS=91-92, PU=95
#'file:/wk_cms/paganis/data/HLTPhysicsRun2018E/325/310/',#LS=, PU=
#
# Special High PU RUN 325308 Fill=7358, Colliding bunches:26, PU=108:, HLTPhysics DT=7%
#'file:/wk_cms/paganis/data/HLTPhysicsRun2018E/325/308/025FAAF8-485A-0543-9436-DBD269137CD5.root',#LS=98, PU=107
#'file:/wk_cms/paganis/data/HLTPhysicsRun2018E/325/308/07D447CA-64BA-7B43-BB08-1DDEBAFF7BE7.root',#LS=89, PU=102
#
        )
)

# initialize  MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")

# initialize magnetic field
process.load("Configuration.StandardSequences.MagneticField_cff")

# Added by Stathes
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')

# DQM services
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.dqmSaver.workflow = "/Run2015C/Commissioning/RAW"
#process.load("CalibCalorimetry.Configuration.Ecal_FakeConditions_cff")
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
##process.load("DQM.Integration.config.FrontierCondition_GT_Offline_cfi")
process.load("DQM.Integration.config.FrontierCondition_GT_cfi")

# Local database for emulator setup (to change ZS thresholds!)
#----------------------------------------------------------------------
#To overwrite Selective readout settings with settings from a local DB (sqlite file): 
#process.load("CondCore.CondDB.CondDB_cfi")
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string("EcalSRSettingsRcd"),
# 2019 Strategy:
# Check1:
#              tag = cms.string("EcalSRSettings_LTH2.0_HTH4.0GeV_ZS5.0_5.5ADC_mc"),
#              connect = cms.string("sqlite_file:EcalSRSettings_LTH2.0_HTH4.0GeV_ZS5.0_5.5ADC_mc.db")
# Check2:
              tag = cms.string("EcalSRSettings_LTH2.0_HTH4.0GeV_ZS5.0_5.0ADC_mc"),
              connect = cms.string("sqlite_file:EcalSRSettings_LTH2.0_HTH4.0GeV_ZS5.0_5.0ADC_mc.db")
# Check3:
#              tag = cms.string("EcalSRSettings_LTH2.0_HTH4.0GeV_ZS5.5_5.5ADC_mc"),
#              connect = cms.string("sqlite_file:EcalSRSettings_LTH2.0_HTH4.0GeV_ZS5.5_5.5ADC_mc.db")
# 2018 Strategy:
# Default:
#              tag = cms.string("EcalSRSettings_LTH2.0_HTH4.0GeV_ZS5.5_6.0ADC_mc"),
#              connect = cms.string("sqlite_file:EcalSRSettings_LTH2.0_HTH4.0GeV_ZS5.5_6.0ADC_mc.db")
# Check1: 1ADC tighter in EB
#             tag = cms.string("EcalSRSettings_LTH2.5_HTH4.5GeV_ZS5.5_6.5ADC_mc"),
#             connect = cms.string("sqlite_file:EcalSRSettings_LTH2.5_HTH4.5GeV_ZS5.5_6.5ADC_mc.db")
             )
    )

#----------------------------------------------------------------------

# Sequence info:
# 0. ecalEBunpacker runs: 
#    - it will provide the Trigger Prims (i.e. LI, HI trigger towers, their Et etc).
#    - the name of the output is "EcalTriggerPrimitives"
#    - if input file is data, then the TPs are data
# 1. ecalDigiSequence defined but only "simEcalDigis" runs:
# ecalDigiSequence = cms.Sequence(simEcalTriggerPrimitiveDigis*simEcalDigis*simEcalPreshowerDigis)
#    - Here the simEcalDigis, reads EB and EE digis and TPs from the unpacker
#    - Output names are "egDigis" and "eeDigis"
#    - simEcalDigis also output the "ebSrFlags" and "eeSrFlags"
#    - The user may invoke emulation (EcalSelectiveReadoutSuppressor.cc) uncommenting
#    the flags at the end of this macro.
#    The difference is that the simEcalDigis re-does zero suppression from scratch.
#    It uses the input TTPrimitives getting from there the suppressed Et(), but then
#    it redefines LI,MI,HI etc. Of course I would hope nothing changes as far as the 
#    TTPrims are concerned, but the ZS being repeated should cut more data and 
#    reduce the DCC load!
# 2. ecalSelectiveReadoutValidation runs:
#    Its input can be the output of the unpacker, or the output of the simEcalDigis.
#    - It simply makes a number of SR validation histograms based on the input digis.
#    - If we want to plot the emulated ADC FIR histograms, these histograms are calculated 
#      in the validation code by applying the FIR weights on ADC samples coming from the 
#      input digis. So the ADC FIR histograms depend on the input ebDigis eeDigis.
#

# ECAL Unpacker:
process.load("EventFilter.EcalRawToDigi.EcalUnpackerMapping_cfi")
process.load("EventFilter.EcalRawToDigi.EcalUnpackerData_cfi")
process.ecalEBunpacker.silentMode = cms.untracked.bool(True)

#
# ECAL digitization sequence
#
process.load("SimCalorimetry.Configuration.ecalDigiSequence_cff")
process.simEcalDigis.trigPrimProducer = cms.string('ecalEBunpacker')# Label name of input ECAL trigger primitive collection
process.simEcalDigis.trigPrimCollection =  cms.string('EcalTriggerPrimitives')# Input trigger prim collection
process.simEcalDigis.digiProducer = cms.string('ecalEBunpacker')#Input Label of EB EE digi collections
process.simEcalDigis.EBdigiCollection = cms.string('ebDigis')#Input Digis
process.simEcalDigis.EEdigiCollection = cms.string('eeDigis')#Input Digis
process.simEcalDigis.EBSRPdigiCollection = cms.string('SRebDigis')#output Digis (emulated)
process.simEcalDigis.EESRPdigiCollection = cms.string('SReeDigis')#output Digis (emulated)
#Note that the output flags have names (default): ebSrFlags,eeSrFlags


#
# Ecal selective readout validation module, ecalSelectiveReadoutValidation:
#
process.load("Validation.EcalDigis.ecalSelectiveReadoutValidation_cfi")
process.ecalSelectiveReadoutValidation.outputFile = 'srvalid_hists.root'
process.ecalSelectiveReadoutValidation.verbose = cms.untracked.bool(False);

#INPUTS:
process.ecalSelectiveReadoutValidation.EbUnsuppressedDigiCollection = cms.InputTag("simEcalUnsuppressedDigis")
process.ecalSelectiveReadoutValidation.EeUnsuppressedDigiCollection = cms.InputTag("simEcalUnsuppressedDigis")

#Stathes changes:
#DQM: here we use straight the data (no emulator)
#     the output of the unpacker will be used by the ecalSelectiveReadoutValidation.
#process.ecalSelectiveReadoutValidation.EbDigiCollection = cms.InputTag("ecalEBunpacker","ebDigis")#input digis to SRValid
#process.ecalSelectiveReadoutValidation.EeDigiCollection = cms.InputTag("ecalEBunpacker","eeDigis")#input digis to SRValid
#process.ecalSelectiveReadoutValidation.EbSrFlagCollection = cms.InputTag("ecalEBunpacker","")#input flags
#process.ecalSelectiveReadoutValidation.EeSrFlagCollection = cms.InputTag("ecalEBunpacker","")#input flags
#process.ecalSelectiveReadoutValidation.TrigPrimCollection = cms.InputTag("ecalEBunpacker", "EcalTriggerPrimitives")
#
# My MC script: (if you turn on the emulator uncomment the following).
# Here we force the simEcalDigis to do the zero suppression and their output will go 
# to the ecalSelectiveReadoutValidation.
process.ecalSelectiveReadoutValidation.EbDigiCollection = cms.InputTag("simEcalDigis","SRebDigis")#input digis to SRValid
process.ecalSelectiveReadoutValidation.EeDigiCollection = cms.InputTag("simEcalDigis","SReeDigis")#input digis to SRValid
process.ecalSelectiveReadoutValidation.EbSrFlagCollection = cms.InputTag("simEcalDigis","ebSrFlags")#input is the output of simEcalDigis
process.ecalSelectiveReadoutValidation.EeSrFlagCollection = cms.InputTag("simEcalDigis","eeSrFlags")#input
process.ecalSelectiveReadoutValidation.TrigPrimCollection = cms.InputTag("simEcalDigis", "simEcalTriggerPrimitives")
# end

#process.ecalSelectiveReadoutValidation.ecalDccZs1stSample = 2
#process.ecalSelectiveReadoutValidation.dccWeights = [ -0.374, -0.374, -0.3629, 0.2721, 0.4681, 0.3707 ]
process.ecalSelectiveReadoutValidation.histDir = ''
process.ecalSelectiveReadoutValidation.histograms = [ 'all' ]
#process.ecalSelectiveReadoutValidation.useEventRate = False
process.ecalSelectiveReadoutValidation.LocalReco = cms.bool(False) # local pulse Ampl reco
process.ecalSelectiveReadoutValidation.IsDATA    = cms.bool(True)
process.ecalSelectiveReadoutValidation.ebZsThrADCCount = 4.5
process.ecalSelectiveReadoutValidation.eeZsThrADCCount = 6.5


process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")

process.tpparams12 = cms.ESSource("EmptyESSource",
    recordName = cms.string('EcalTPGPhysicsConstRcd'),
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.vuint32(1)
)

#process.load("pgras.ListCollection.ListCollection_cfi")

process.p1 = cms.Path(process.ecalEBunpacker*process.simEcalDigis*process.ecalSelectiveReadoutValidation*process.dqmSaver)

#
# switch Modify ECAL SR
#
# to work you need (1) to uncomment the bypass flags below,
# (2) you need to uncomment the 4 lines above (see "turn on the emulator" above)
from SimCalorimetry.EcalSimProducers.ecaldigi_cfi import *
from SimCalorimetry.EcalSelectiveReadoutProducers.ecalDigis_cfi import *
simEcalDigis.trigPrimBypass = cms.bool(True) # uncomment to bypass
simEcalDigis.trigPrimBypassMode = cms.int32(1) #bypass mode (uncomment)
simEcalDigis.trigPrimBypassLTH = cms.double(3.0)# 2xGeV C1 DEFAULT
simEcalDigis.trigPrimBypassHTH = cms.double(7.0)# 2xGeV C1 DEFAULT
#simEcalDigis.trigPrimBypassLTH = cms.double(4.0)# 2xGeV C1 //2GeV Et 2018 Default
#simEcalDigis.trigPrimBypassHTH = cms.double(8.0)# 2xGeV C1 //4GeV Et 2018 Default
#simEcalDigis.trigPrimBypassLTH = cms.double(0.0)# 2xGeV C1
#simEcalDigis.trigPrimBypassHTH = cms.double(0.0)# 2xGeV C1
#switch to apply selective readout decision on the digis and produce
simEcalDigis.produceDigis = cms.untracked.bool(True)

