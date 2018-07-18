# hltGetConfiguration /users/davidlw/HLT_PbPb2018_FullTrackv2/V23 --globaltag 100X_dataRun2_v1 --input root://xrootd.cmsaf.mit.edu//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/898/00000/A0E925FB-89AF-E711-8C82-02163E0144E9.root --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2017DtUnpacking --setup /dev/CMSSW_10_1_0/GRun --customise L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAW --customise L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU --customise L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo --customise FWCore/ParameterSet/MassReplace.massReplaceInputTag --process MyHLT --full --offline --data --unprescale --l1-emulator Full --max-events 100

# /users/davidlw/HLT_PbPb2018_FullTrackv2/V23 (CMSSW_10_1_4)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "MyHLT" )
process.load("setup_dev_CMSSW_10_1_0_GRun_cff")

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/davidlw/HLT_PbPb2018_FullTrackv2/V23')
)

process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::GTSetup" ),
    MinFeds = cms.uint32( 0 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    TMTCheck = cms.bool( True ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1404 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
process.hltGtStage2ObjectMap = cms.EDProducer( "L1TGlobalProducer",
    L1DataBxInEvent = cms.int32( 5 ),
    JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    AlgorithmTriggersUnmasked = cms.bool( True ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    PrintL1Menu = cms.untracked.bool( False ),
    Verbosity = cms.untracked.int32( 0 ),
    EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    ProduceL1GtDaqRecord = cms.bool( True ),
    PrescaleSet = cms.uint32( 1 ),
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    TriggerMenuLuminosity = cms.string( "startup" ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    PrescaleCSVFile = cms.string( "prescale_L1TGlobal.csv" ),
    TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    BstLengthBytes = cms.int32( -1 ),
    MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
process.hltL1sZeroBias = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_ZeroBias" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIFullTracks2018HighPt8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEcalDigis = cms.EDProducer( "EcalRawToDigi",
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    FedLabel = cms.InputTag( "listfeds" ),
    eventPut = cms.bool( True ),
    srpUnpacking = cms.bool( True ),
    syncCheck = cms.bool( True ),
    headerUnpacking = cms.bool( True ),
    feUnpacking = cms.bool( True ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    tccUnpacking = cms.bool( True ),
    numbTriggerTSamples = cms.int32( 1 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    numbXtalTSamples = cms.int32( 10 ),
    feIdCheck = cms.bool( True ),
    FEDs = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    silentMode = cms.untracked.bool( True ),
    DoRegional = cms.bool( False ),
    forceToKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( True )
)
process.hltEcalUncalibRecHit = cms.EDProducer( "EcalUncalibRecHitProducer",
    EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    EBhitCollection = cms.string( "EcalUncalibRecHitsEB" ),
    algo = cms.string( "EcalUncalibRecHitWorkerMultiFit" ),
    algoPSet = cms.PSet( 
      outOfTimeThresholdGain61pEB = cms.double( 5.0 ),
      EBtimeFitParameters = cms.vdouble( -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 91.01147, -50.35761, 11.05621 ),
      activeBXs = cms.vint32( -5, -4, -3, -2, -1, 0, 1, 2, 3, 4 ),
      amplitudeThresholdEE = cms.double( 10.0 ),
      EBtimeConstantTerm = cms.double( 0.6 ),
      EEtimeFitLimits_Lower = cms.double( 0.2 ),
      outOfTimeThresholdGain61pEE = cms.double( 1000.0 ),
      ebSpikeThreshold = cms.double( 1.042 ),
      EBtimeNconst = cms.double( 28.5 ),
      ampErrorCalculation = cms.bool( False ),
      kPoorRecoFlagEB = cms.bool( True ),
      EBtimeFitLimits_Lower = cms.double( 0.2 ),
      kPoorRecoFlagEE = cms.bool( False ),
      chi2ThreshEB_ = cms.double( 65.0 ),
      EEtimeFitParameters = cms.vdouble( -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 140.7432, -75.41106, 16.20277 ),
      useLumiInfoRunHeader = cms.bool( False ),
      outOfTimeThresholdGain12mEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12mEB = cms.double( 5.0 ),
      EEtimeFitLimits_Upper = cms.double( 1.4 ),
      prefitMaxChiSqEB = cms.double( 100.0 ),
      EEamplitudeFitParameters = cms.vdouble( 1.89, 1.4 ),
      prefitMaxChiSqEE = cms.double( 10.0 ),
      EBamplitudeFitParameters = cms.vdouble( 1.138, 1.652 ),
      EBtimeFitLimits_Upper = cms.double( 1.4 ),
      timealgo = cms.string( "None" ),
      amplitudeThresholdEB = cms.double( 10.0 ),
      outOfTimeThresholdGain12pEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12pEB = cms.double( 5.0 ),
      EEtimeNconst = cms.double( 31.8 ),
      outOfTimeThresholdGain61mEB = cms.double( 5.0 ),
      outOfTimeThresholdGain61mEE = cms.double( 1000.0 ),
      EEtimeConstantTerm = cms.double( 1.0 ),
      chi2ThreshEE_ = cms.double( 50.0 ),
      doPrefitEE = cms.bool( True ),
      doPrefitEB = cms.bool( True )
    )
)
process.hltEcalDetIdToBeRecovered = cms.EDProducer( "EcalDetIdToBeRecoveredProducer",
    ebIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebDetIdToBeRecovered = cms.string( "ebDetId" ),
    integrityTTIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityTTIdErrors' ),
    eeIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    ebFEToBeRecovered = cms.string( "ebFE" ),
    ebIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    eeDetIdToBeRecovered = cms.string( "eeDetId" ),
    eeIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    eeIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    ebSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    eeSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    integrityBlockSizeErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityBlockSizeErrors' ),
    eeFEToBeRecovered = cms.string( "eeFE" )
)
process.hltEcalRecHit = cms.EDProducer( "EcalRecHitProducer",
    recoverEEVFE = cms.bool( False ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    recoverEBIsolatedChannels = cms.bool( False ),
    recoverEBVFE = cms.bool( False ),
    laserCorrection = cms.bool( True ),
    EBLaserMIN = cms.double( 0.5 ),
    killDeadChannels = cms.bool( True ),
    dbStatusToBeExcludedEB = cms.vint32( 14, 78, 142 ),
    EEuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEE' ),
    EBLaserMAX = cms.double( 3.0 ),
    EELaserMIN = cms.double( 0.5 ),
    ebFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebFE' ),
    EELaserMAX = cms.double( 8.0 ),
    recoverEEIsolatedChannels = cms.bool( False ),
    eeDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeDetId' ),
    recoverEBFE = cms.bool( True ),
    algo = cms.string( "EcalRecHitWorkerSimple" ),
    ebDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebDetId' ),
    singleChannelRecoveryThreshold = cms.double( 8.0 ),
    ChannelStatusToBeExcluded = cms.vstring(  ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    singleChannelRecoveryMethod = cms.string( "NeuralNetworks" ),
    recoverEEFE = cms.bool( True ),
    triggerPrimitiveDigiCollection = cms.InputTag( 'hltEcalDigis','EcalTriggerPrimitives' ),
    dbStatusToBeExcludedEE = cms.vint32( 14, 78, 142 ),
    flagsMapDBReco = cms.PSet( 
      kGood = cms.vstring( 'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy' ),
      kNeighboursRecovered = cms.vstring( 'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE' ),
      kDead = cms.vstring( 'kNoDataNoTP' ),
      kNoisy = cms.vstring( 'kNNoisy',
        'kFixedG6',
        'kFixedG1' ),
      kTowerRecovered = cms.vstring( 'kDeadFE' )
    ),
    EBuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    skipTimeCalib = cms.bool( False ),
    algoRecover = cms.string( "EcalRecHitWorkerRecover" ),
    eeFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeFE' ),
    cleaningConfig = cms.PSet( 
      e6e2thresh = cms.double( 0.04 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 ),
      cThreshold_endcap = cms.double( 15.0 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      cThreshold_double = cms.double( 10.0 )
    ),
    logWarningEtThreshold_EB_FE = cms.double( 50.0 ),
    logWarningEtThreshold_EE_FE = cms.double( 50.0 )
)
process.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
    saveQIE10DataNSamples = cms.untracked.vint32(  ),
    ExpectedOrbitMessageTime = cms.untracked.int32( -1 ),
    FilterDataQuality = cms.bool( True ),
    silent = cms.untracked.bool( True ),
    saveQIE11DataNSamples = cms.untracked.vint32(  ),
    HcalFirstFED = cms.untracked.int32( 700 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ComplainEmptyData = cms.untracked.bool( False ),
    ElectronicsMap = cms.string( "" ),
    UnpackCalib = cms.untracked.bool( True ),
    UnpackUMNio = cms.untracked.bool( True ),
    FEDs = cms.untracked.vint32(  ),
    saveQIE11DataTags = cms.untracked.vstring(  ),
    UnpackTTP = cms.untracked.bool( False ),
    UnpackZDC = cms.untracked.bool( True ),
    saveQIE10DataTags = cms.untracked.vstring(  ),
    lastSample = cms.int32( 9 ),
    UnpackerMode = cms.untracked.int32( 0 ),
    firstSample = cms.int32( 0 )
)
process.hltHbhePhase1Reco = cms.EDProducer( "HBHEPhase1Reconstructor",
    tsFromDB = cms.bool( False ),
    setPulseShapeFlagsQIE8 = cms.bool( True ),
    digiLabelQIE11 = cms.InputTag( "hltHcalDigis" ),
    saveDroppedInfos = cms.bool( False ),
    setNoiseFlagsQIE8 = cms.bool( True ),
    saveEffectivePedestal = cms.bool( True ),
    digiLabelQIE8 = cms.InputTag( "hltHcalDigis" ),
    sipmQTSShift = cms.int32( 0 ),
    processQIE11 = cms.bool( True ),
    pulseShapeParametersQIE11 = cms.PSet(  ),
    algoConfigClass = cms.string( "" ),
    saveInfos = cms.bool( False ),
    flagParametersQIE11 = cms.PSet(  ),
    makeRecHits = cms.bool( True ),
    pulseShapeParametersQIE8 = cms.PSet( 
      UseDualFit = cms.bool( True ),
      LinearCut = cms.vdouble( -3.0, -0.054, -0.054 ),
      TriangleIgnoreSlow = cms.bool( False ),
      TS4TS5LowerThreshold = cms.vdouble( 100.0, 120.0, 160.0, 200.0, 300.0, 500.0 ),
      LinearThreshold = cms.vdouble( 20.0, 100.0, 100000.0 ),
      RightSlopeSmallCut = cms.vdouble( 1.08, 1.16, 1.16 ),
      TS4TS5UpperThreshold = cms.vdouble( 70.0, 90.0, 100.0, 400.0 ),
      TS3TS4ChargeThreshold = cms.double( 70.0 ),
      R45PlusOneRange = cms.double( 0.2 ),
      TS4TS5LowerCut = cms.vdouble( -1.0, -0.7, -0.5, -0.4, -0.3, 0.1 ),
      RightSlopeThreshold = cms.vdouble( 250.0, 400.0, 100000.0 ),
      TS3TS4UpperChargeThreshold = cms.double( 20.0 ),
      MinimumChargeThreshold = cms.double( 20.0 ),
      RightSlopeCut = cms.vdouble( 5.0, 4.15, 4.15 ),
      RMS8MaxThreshold = cms.vdouble( 20.0, 100.0, 100000.0 ),
      MinimumTS4TS5Threshold = cms.double( 100.0 ),
      LeftSlopeThreshold = cms.vdouble( 250.0, 500.0, 100000.0 ),
      TS5TS6ChargeThreshold = cms.double( 70.0 ),
      TrianglePeakTS = cms.uint32( 10000 ),
      TS5TS6UpperChargeThreshold = cms.double( 20.0 ),
      RightSlopeSmallThreshold = cms.vdouble( 150.0, 200.0, 100000.0 ),
      RMS8MaxCut = cms.vdouble( -13.5, -11.5, -11.5 ),
      TS4TS5ChargeThreshold = cms.double( 70.0 ),
      R45MinusOneRange = cms.double( 0.2 ),
      LeftSlopeCut = cms.vdouble( 5.0, 2.55, 2.55 ),
      TS4TS5UpperCut = cms.vdouble( 1.0, 0.8, 0.75, 0.72 )
    ),
    flagParametersQIE8 = cms.PSet( 
      hitEnergyMinimum = cms.double( 1.0 ),
      pulseShapeParameterSets = cms.VPSet( 
        cms.PSet(  pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )        )
      ),
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 )
    ),
    setNegativeFlagsQIE8 = cms.bool( False ),
    setNegativeFlagsQIE11 = cms.bool( False ),
    processQIE8 = cms.bool( True ),
    algorithm = cms.PSet( 
      ts4Thresh = cms.double( 0.0 ),
      meanTime = cms.double( 0.0 ),
      nnlsThresh = cms.double( 1.0E-11 ),
      nMaxItersMin = cms.int32( 500 ),
      timeSigmaSiPM = cms.double( 2.5 ),
      applyTimeSlew = cms.bool( True ),
      timeSlewParsType = cms.int32( 3 ),
      ts4Max = cms.vdouble( 100.0, 20000.0, 30000.0 ),
      samplesToAdd = cms.int32( 2 ),
      deltaChiSqThresh = cms.double( 0.001 ),
      applyTimeConstraint = cms.bool( False ),
      timeSigmaHPD = cms.double( 5.0 ),
      useMahi = cms.bool( True ),
      correctForPhaseContainment = cms.bool( True ),
      respCorrM3 = cms.double( 1.0 ),
      pulseJitter = cms.double( 1.0 ),
      applyPedConstraint = cms.bool( False ),
      fitTimes = cms.int32( 1 ),
      nMaxItersNNLS = cms.int32( 500 ),
      applyTimeSlewM3 = cms.bool( True ),
      meanPed = cms.double( 0.0 ),
      ts4Min = cms.double( 0.0 ),
      applyPulseJitter = cms.bool( False ),
      useM2 = cms.bool( False ),
      timeMin = cms.double( -12.5 ),
      useM3 = cms.bool( False ),
      chiSqSwitch = cms.double( 15.0 ),
      dynamicPed = cms.bool( True ),
      tdcTimeShift = cms.double( 0.0 ),
      correctionPhaseNS = cms.double( 6.0 ),
      firstSampleShift = cms.int32( 0 ),
      activeBXs = cms.vint32( -1, 0, 1 ),
      ts4chi2 = cms.vdouble( 15.0, 15.0 ),
      timeMax = cms.double( 12.5 ),
      Class = cms.string( "SimpleHBHEPhase1Algo" )
    ),
    setLegacyFlagsQIE8 = cms.bool( False ),
    sipmQNTStoSum = cms.int32( 3 ),
    setPulseShapeFlagsQIE11 = cms.bool( False ),
    setLegacyFlagsQIE11 = cms.bool( False ),
    setNoiseFlagsQIE11 = cms.bool( False ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True )
)
process.hltHbhereco = cms.EDProducer( "HBHEPlan1Combiner",
    hbheInput = cms.InputTag( "hltHbhePhase1Reco" ),
    usePlan1Mode = cms.bool( True ),
    ignorePlan1Topology = cms.bool( False ),
    algorithm = cms.PSet(  Class = cms.string( "SimplePlan1RechitCombiner" ) )
)
process.hltHfprereco = cms.EDProducer( "HFPreReconstructor",
    soiShift = cms.int32( 0 ),
    sumAllTimeSlices = cms.bool( False ),
    dropZSmarkedPassed = cms.bool( True ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    tsFromDB = cms.bool( False ),
    forceSOI = cms.int32( -1 )
)
process.hltHfreco = cms.EDProducer( "HFPhase1Reconstructor",
    setNoiseFlags = cms.bool( True ),
    PETstat = cms.PSet( 
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_R_29 = cms.vdouble( 0.8 ),
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      short_R_29 = cms.vdouble( 0.8 ),
      long_R = cms.vdouble( 0.98 ),
      short_R = cms.vdouble( 0.8 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    algoConfigClass = cms.string( "HFPhase1PMTParams" ),
    inputLabel = cms.InputTag( "hltHfprereco" ),
    S9S1stat = cms.PSet( 
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      isS8S1 = cms.bool( False ),
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    checkChannelQualityForDepth3and4 = cms.bool( False ),
    useChannelQualityFromDB = cms.bool( False ),
    algorithm = cms.PSet( 
      tfallIfNoTDC = cms.double( -101.0 ),
      triseIfNoTDC = cms.double( -100.0 ),
      rejectAllFailures = cms.bool( True ),
      energyWeights = cms.vdouble( 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 1.0 ),
      soiPhase = cms.uint32( 1 ),
      timeShift = cms.double( 0.0 ),
      tlimits = cms.vdouble( -1000.0, 1000.0, -1000.0, 1000.0 ),
      Class = cms.string( "HFFlexibleTimeCheck" )
    ),
    S8S1stat = cms.PSet( 
      shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      isS8S1 = cms.bool( True ),
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    )
)
process.hltHoreco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    digistat = cms.PSet(  ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    setSaturationFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    recoParamsFromDB = cms.bool( True ),
    Subdetector = cms.string( "HO" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    setPulseShapeFlags = cms.bool( False ),
    firstSample = cms.int32( 4 )
)
process.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    HEDThreshold1 = cms.double( 0.8 ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.7 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HESThreshold1 = cms.double( 0.8 ),
    HEDWeights = cms.vdouble(  ),
    EBWeight = cms.double( 1.0 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0E-99 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.8 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    HF2Weight = cms.double( 1.0 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HF1Threshold = cms.double( 0.5 ),
    HcalPhase = cms.int32( 0 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.8 ),
    UseRejectedHitsOnly = cms.bool( False ),
    EBThreshold = cms.double( 0.07 ),
    HEDGrid = cms.vdouble(  ),
    UseHcalRecoveredHits = cms.bool( False ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HOThreshold0 = cms.double( 3.5 ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
process.hltPuAK4CaloJets = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 1 ),
    useMassDropTagger = cms.bool( False ),
    doAreaFastjet = cms.bool( True ),
    muMin = cms.double( -1.0 ),
    Ghost_EtaMax = cms.double( 6.5 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    subtractorName = cms.string( "MultipleAlgoIterator" ),
    dRMax = cms.double( -1.0 ),
    useExplicitGhosts = cms.bool( False ),
    puWidth = cms.double( 0.0 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    R0 = cms.double( -1.0 ),
    jetType = cms.string( "CaloJet" ),
    muCut = cms.double( -1.0 ),
    subjetPtMin = cms.double( -1.0 ),
    csRParam = cms.double( -1.0 ),
    MinVtxNdof = cms.int32( 5 ),
    minSeed = cms.uint32( 14327 ),
    voronoiRfact = cms.double( -0.9 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    writeCompound = cms.bool( False ),
    muMax = cms.double( -1.0 ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    restrictInputs = cms.bool( False ),
    useDynamicFiltering = cms.bool( False ),
    nExclude = cms.uint32( 0 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    yMin = cms.double( -1.0 ),
    jetCollInstanceName = cms.string( "" ),
    useFiltering = cms.bool( False ),
    maxInputs = cms.uint32( 1 ),
    rFiltFactor = cms.double( -1.0 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    rFilt = cms.double( -1.0 ),
    yMax = cms.double( -1.0 ),
    zcut = cms.double( -1.0 ),
    useTrimming = cms.bool( False ),
    puCenters = cms.vdouble(  ),
    MaxVtxZ = cms.double( 15.0 ),
    rParam = cms.double( 0.4 ),
    csRho_EtaMax = cms.double( -1.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    dRMin = cms.double( -1.0 ),
    gridSpacing = cms.double( -1.0 ),
    doFastJetNonUniform = cms.bool( False ),
    usePruning = cms.bool( False ),
    maxDepth = cms.int32( -1 ),
    yCut = cms.double( -1.0 ),
    useSoftDrop = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    UseOnlyOnePV = cms.bool( False ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    correctShape = cms.bool( False ),
    rcut_factor = cms.double( -1.0 ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    gridMaxRapidity = cms.double( -1.0 ),
    sumRecHits = cms.bool( False ),
    jetPtMin = cms.double( 10.0 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "NotUsed" ),
    verbosity = cms.int32( 0 ),
    inputEtMin = cms.double( 0.3 ),
    useConstituentSubtraction = cms.bool( False ),
    beta = cms.double( -1.0 ),
    trimPtFracMin = cms.double( -1.0 ),
    radiusPU = cms.double( 0.5 ),
    nFilt = cms.int32( -1 ),
    useKtPruning = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    useCMSBoostedTauSeedingAlgorithm = cms.bool( False ),
    doPUOffsetCorr = cms.bool( True ),
    writeJetsWithConst = cms.bool( False ),
    inputEMin = cms.double( 0.0 )
)
process.hltPuAK4CaloJetsIDPassed = cms.EDProducer( "HLTCaloJetIDProducer",
    min_N90 = cms.int32( -2 ),
    min_N90hits = cms.int32( 2 ),
    min_EMF = cms.double( 1.0E-6 ),
    jetsInput = cms.InputTag( "hltPuAK4CaloJets" ),
    JetIDParams = cms.PSet( 
      useRecHits = cms.bool( True ),
      hbheRecHitsColl = cms.InputTag( "hltHbhereco" ),
      hoRecHitsColl = cms.InputTag( "hltHoreco" ),
      hfRecHitsColl = cms.InputTag( "hltHfreco" ),
      ebRecHitsColl = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      eeRecHitsColl = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' )
    ),
    max_EMF = cms.double( 999.0 )
)
process.hltFixedGridRhoFastjetAllCalo = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 5.0 ),
    pfCandidatesTag = cms.InputTag( "hltTowerMakerForAll" )
)
process.hltAK4CaloFastJetCorrector = cms.EDProducer( "L1FastjetCorrectorProducer",
    srcRho = cms.InputTag( "hltFixedGridRhoFastjetAllCalo" ),
    algorithm = cms.string( "AK4CaloHLT" ),
    level = cms.string( "L1FastJet" )
)
process.hltAK4CaloRelativeCorrector = cms.EDProducer( "LXXXCorrectorProducer",
    algorithm = cms.string( "AK4CaloHLT" ),
    level = cms.string( "L2Relative" )
)
process.hltAK4CaloAbsoluteCorrector = cms.EDProducer( "LXXXCorrectorProducer",
    algorithm = cms.string( "AK4CaloHLT" ),
    level = cms.string( "L3Absolute" )
)
process.hltPuAK4CaloCorrector = cms.EDProducer( "ChainedJetCorrectorProducer",
    correctors = cms.VInputTag( 'hltAK4CaloRelativeCorrector','hltAK4CaloAbsoluteCorrector' )
)
process.hltPuAK4CaloJetsCorrected = cms.EDProducer( "CorrectedCaloJetProducer",
    src = cms.InputTag( "hltPuAK4CaloJets" ),
    correctors = cms.VInputTag( 'hltPuAK4CaloCorrector' )
)
process.hltPuAK4CaloJetsCorrectedIDPassed = cms.EDProducer( "CorrectedCaloJetProducer",
    src = cms.InputTag( "hltPuAK4CaloJetsIDPassed" ),
    correctors = cms.VInputTag( 'hltPuAK4CaloCorrector' )
)
process.hltJetsForCoreTracking = cms.EDFilter( "CandPtrSelector",
    src = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    cut = cms.string( "pt > 100 && abs(eta) < 2.5" )
)
process.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    UseQualityInfo = cms.bool( False ),
    UsePilotBlade = cms.bool( False ),
    UsePhase1 = cms.bool( True ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    IncludeErrors = cms.bool( True ),
    ErrorList = cms.vint32( 29 ),
    Regions = cms.PSet(  ),
    Timing = cms.untracked.bool( False ),
    CablingMapLabel = cms.string( "" ),
    UserErrorList = cms.vint32(  )
)
process.hltSiPixelClustersPPOnAA = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigis" ),
    ChannelThreshold = cms.int32( 250 ),
    maxNumberOfClusters = cms.int32( -1 ),
    ClusterThreshold_L1 = cms.int32( 2000 ),
    MissCalibrate = cms.untracked.bool( True ),
    VCaltoElectronGain = cms.int32( 47 ),
    VCaltoElectronGain_L1 = cms.int32( 50 ),
    VCaltoElectronOffset = cms.int32( -60 ),
    SplitClusters = cms.bool( False ),
    payloadType = cms.string( "Offline" ),
    SeedThreshold = cms.int32( 1000 ),
    VCaltoElectronOffset_L1 = cms.int32( -670 ),
    ClusterThreshold = cms.int32( 4000 )
)
process.hltSiPixelClustersCachePPOnAA = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    onDemand = cms.bool( False )
)
process.hltSiPixelRecHitsPPOnAA = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltSiStripExcludedFEDListProducer = cms.EDProducer( "SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
process.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripClusterizerFromRaw",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    DoAPVEmulatorCheck = cms.bool( False ),
    Algorithms = cms.PSet( 
      CommonModeNoiseSubtractionMode = cms.string( "Median" ),
      useCMMeanMap = cms.bool( False ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( False ),
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      PedestalSubtractionFedMode = cms.bool( True )
    ),
    Clusterizer = cms.PSet( 
      QualityLabel = cms.string( "" ),
      ClusterThreshold = cms.double( 5.0 ),
      SeedThreshold = cms.double( 3.0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      ChannelThreshold = cms.double( 2.0 ),
      MaxAdjacentBad = cms.uint32( 0 ),
      setDetId = cms.bool( True ),
      MaxSequentialHoles = cms.uint32( 0 ),
      RemoveApvShots = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
      MaxSequentialBad = cms.uint32( 1 )
    ),
    onDemand = cms.bool( True )
)
process.hltSiStripClustersPPOnAA = cms.EDProducer( "MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(  ),
    Phase2TrackerCluster1DProducer = cms.string( "" ),
    measurementTracker = cms.string( "hltESPMeasurementTracker" ),
    pixelClusterProducer = cms.string( "hltSiPixelClustersPPOnAA" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag(  ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    skipClusters = cms.InputTag( "" ),
    pixelCablingMapLabel = cms.string( "" ),
    stripClusterProducer = cms.string( "hltSiStripRawToClustersFacility" )
)
process.hltFullIter0PixelQuadrupletsPreSplittingPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3+BPix4',
      'BPix1+BPix2+BPix3+FPix1_pos',
      'BPix1+BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos+FPix2_pos',
      'BPix1+BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_neg+FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter0PixelTrackingRegionsPreSplitting = cms.EDProducer( "GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet( 
      nSigmaZ = cms.double( 4.0 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      ptMin = cms.double( 0.5 ),
      originHalfLength = cms.double( 0.0 ),
      originRadius = cms.double( 0.02 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
)
process.hltFullIter0PixelClusterCheckPreSplittingPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripRawToClustersFacility" )
)
process.hltFullIter0PixelHitDoubletsPreSplittingPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter0PixelTrackingRegionsPreSplitting" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "hltFullIter0PixelClusterCheckPreSplittingPPOnAA" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter0PixelQuadrupletsPreSplittingPPOnAA" )
)
process.hltFullIter0PixelHitQuadrupletsPreSplittingPPOnAA = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.0012 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter0PixelHitDoubletsPreSplittingPPOnAA" ),
    fitFastCircle = cms.bool( True ),
    CAHardPtCut = cms.double( 0.0 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 50.0 ),
      value1 = cms.double( 200.0 ),
      pt1 = cms.double( 0.7 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.2 ),
    useBendingCorrection = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True )
)
process.hltFullIter0PixelSeedsPreSplittingPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet( 
      FilterStripHits = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      FilterAtHelixStage = cms.bool( False ),
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter0PixelHitQuadrupletsPreSplittingPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter0CkfTrackCandidatesPreSplittingPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter0PixelSeedsPreSplittingPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltFullIter0CtfWithMaterialTracksPreSplittingPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter0CkfTrackCandidatesPreSplittingPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "initialStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltFullIter0PrimaryVerticesPreSplittingPPOnAA = cms.EDProducer( "PrimaryVertexProducer",
    vertexCollections = cms.VPSet( 
      cms.PSet(  chi2cutoff = cms.double( 2.5 ),
        label = cms.string( "" ),
        useBeamConstraint = cms.bool( False ),
        minNdof = cms.double( 0.0 ),
        maxDistanceToBeam = cms.double( 1.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" )
      )
    ),
    verbose = cms.untracked.bool( False ),
    TkFilterParameters = cms.PSet( 
      maxEta = cms.double( 2.4 ),
      minPt = cms.double( 0.0 ),
      minSiliconLayersWithHits = cms.int32( 5 ),
      minPixelLayersWithHits = cms.int32( 2 ),
      maxNormalizedChi2 = cms.double( 20.0 ),
      trackQuality = cms.string( "any" ),
      algorithm = cms.string( "filter" ),
      maxD0Significance = cms.double( 5.0 )
    ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltFullIter0CtfWithMaterialTracksPreSplittingPPOnAA" ),
    TkClusParameters = cms.PSet( 
      TkDAClusParameters = cms.PSet( 
        zmerge = cms.double( 0.01 ),
        Tstop = cms.double( 0.5 ),
        d0CutOff = cms.double( 3.0 ),
        dzCutOff = cms.double( 4.0 ),
        vertexSize = cms.double( 0.01 ),
        coolingFactor = cms.double( 0.6 ),
        Tpurge = cms.double( 2.0 ),
        Tmin = cms.double( 2.4 ),
        uniquetrkweight = cms.double( 0.9 )
      ),
      algorithm = cms.string( "DA_vect" )
    )
)
process.hltSiPixelClustersAfterSplittingPPOnAA = cms.EDProducer( "JetCoreClusterSplitter",
    verbose = cms.bool( False ),
    deltaRmax = cms.double( 0.05 ),
    forceXError = cms.double( 100.0 ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPreSplittingPPOnAA" ),
    chargePerUnit = cms.double( 2000.0 ),
    forceYError = cms.double( 150.0 ),
    centralMIPCharge = cms.double( 26000.0 ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    ptMin = cms.double( 200.0 ),
    chargeFractionMin = cms.double( 2.0 ),
    cores = cms.InputTag( "hltJetsForCoreTracking" ),
    fractionalWidth = cms.double( 0.4 ),
    pixelCPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltSiPixelClustersCacheAfterSplittingPPOnAA = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    onDemand = cms.bool( False )
)
process.hltSiPixelRecHitsAfterSplittingPPOnAA = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltSiStripRawToClustersFacilityFull = cms.EDProducer( "SiStripClusterizerFromRaw",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    DoAPVEmulatorCheck = cms.bool( False ),
    Algorithms = cms.PSet( 
      CommonModeNoiseSubtractionMode = cms.string( "Median" ),
      useCMMeanMap = cms.bool( False ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( False ),
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      PedestalSubtractionFedMode = cms.bool( True )
    ),
    Clusterizer = cms.PSet( 
      QualityLabel = cms.string( "" ),
      ClusterThreshold = cms.double( 5.0 ),
      SeedThreshold = cms.double( 3.0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      ChannelThreshold = cms.double( 2.0 ),
      MaxAdjacentBad = cms.uint32( 0 ),
      setDetId = cms.bool( True ),
      MaxSequentialHoles = cms.uint32( 0 ),
      RemoveApvShots = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
      MaxSequentialBad = cms.uint32( 1 )
    ),
    onDemand = cms.bool( False )
)
process.hltSiStripClustersFullPPOnAA = cms.EDProducer( "MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(  ),
    Phase2TrackerCluster1DProducer = cms.string( "" ),
    measurementTracker = cms.string( "hltESPMeasurementTracker" ),
    pixelClusterProducer = cms.string( "hltSiPixelClustersPPOnAA" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag(  ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    skipClusters = cms.InputTag( "" ),
    pixelCablingMapLabel = cms.string( "" ),
    stripClusterProducer = cms.string( "hltSiStripRawToClustersFacilityFull" )
)
process.hltSiStripMatchedRecHitsFull = cms.EDProducer( "SiStripRecHitConverter",
    StripCPE = cms.ESInputTag( 'hltESPStripCPEfromTrackAngle','hltESPStripCPEfromTrackAngle' ),
    stereoRecHits = cms.string( "stereoRecHit" ),
    useSiStripQuality = cms.bool( False ),
    matchedRecHits = cms.string( "matchedRecHit" ),
    ClusterProducer = cms.InputTag( "hltSiStripRawToClustersFacilityFull" ),
    VerbosityLevel = cms.untracked.int32( 1 ),
    rphiRecHits = cms.string( "rphiRecHit" ),
    Matcher = cms.ESInputTag( 'SiStripRecHitMatcherESProducer','StandardMatcher' ),
    siStripQualityLabel = cms.ESInputTag( "" ),
    MaskBadAPVFibers = cms.bool( False )
)
process.hltFullIter0PixelQuadrupletsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3+BPix4',
      'BPix1+BPix2+BPix3+FPix1_pos',
      'BPix1+BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos+FPix2_pos',
      'BPix1+BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_neg+FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter0PixelTrackingRegions = cms.EDProducer( "GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet( 
      nSigmaZ = cms.double( 4.0 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      ptMin = cms.double( 0.5 ),
      originHalfLength = cms.double( 0.0 ),
      originRadius = cms.double( 0.02 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
)
process.hltFullIter0PixelClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripRawToClustersFacilityFull" )
)
process.hltFullIter0PixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter0PixelTrackingRegions" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "hltFullIter0PixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter0PixelQuadrupletsPPOnAA" )
)
process.hltFullIter0PixelHitQuadrupletsPPOnAA = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.0012 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter0PixelHitDoubletsPPOnAA" ),
    fitFastCircle = cms.bool( True ),
    CAHardPtCut = cms.double( 0.0 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 50.0 ),
      value1 = cms.double( 200.0 ),
      pt1 = cms.double( 0.7 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.2 ),
    useBendingCorrection = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True )
)
process.hltFullIter0PixelSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet( 
      FilterStripHits = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      FilterAtHelixStage = cms.bool( False ),
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter0PixelHitQuadrupletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter0CkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter0PixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersFullPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltFullIter0CtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter0CkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "initialStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltFullIter0PrimaryVerticesPPOnAA = cms.EDProducer( "PrimaryVertexProducer",
    vertexCollections = cms.VPSet( 
      cms.PSet(  chi2cutoff = cms.double( 2.5 ),
        label = cms.string( "" ),
        useBeamConstraint = cms.bool( False ),
        minNdof = cms.double( 0.0 ),
        maxDistanceToBeam = cms.double( 1.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" )
      )
    ),
    verbose = cms.untracked.bool( False ),
    TkFilterParameters = cms.PSet( 
      maxEta = cms.double( 2.4 ),
      minPt = cms.double( 0.0 ),
      minSiliconLayersWithHits = cms.int32( 5 ),
      minPixelLayersWithHits = cms.int32( 2 ),
      maxNormalizedChi2 = cms.double( 20.0 ),
      trackQuality = cms.string( "any" ),
      algorithm = cms.string( "filter" ),
      maxD0Significance = cms.double( 5.0 )
    ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltFullIter0CtfWithMaterialTracksPPOnAA" ),
    TkClusParameters = cms.PSet( 
      TkDAClusParameters = cms.PSet( 
        zmerge = cms.double( 0.01 ),
        Tstop = cms.double( 0.5 ),
        d0CutOff = cms.double( 3.0 ),
        dzCutOff = cms.double( 4.0 ),
        vertexSize = cms.double( 0.01 ),
        coolingFactor = cms.double( 0.6 ),
        Tpurge = cms.double( 2.0 ),
        Tmin = cms.double( 2.4 ),
        uniquetrkweight = cms.double( 0.9 )
      ),
      algorithm = cms.string( "DA_vect" )
    )
)
process.hltFullIter0TrackMVAClassifierPPOnAA = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltFullIter0CtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.95, -0.85, -0.75 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorInitialStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter0HighPurityTracksPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter0CtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltFullIter0TrackMVAClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter0TrackMVAClassifierPPOnAA','MVAValues' )
)
process.hltFullIter1ClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter0HighPurityTracksPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacilityFull" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter1MaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter1ClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter1PixelQuadrupletsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3+BPix4',
      'BPix1+BPix2+BPix3+FPix1_pos',
      'BPix1+BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos+FPix2_pos',
      'BPix1+BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_neg+FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter1ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter1ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter1PixelTrackingRegionsPPOnAA = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 0.5 ),
      maxNVertices = cms.int32( -1 ),
      sigmaZVertex = cms.double( 4.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.3 ),
      originRadius = cms.double( 0.02 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
)
process.hltFullIter1PixelClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripRawToClustersFacilityFull" )
)
process.hltFullIter1PixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter1PixelTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "hltFullIter1PixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter1PixelQuadrupletsPPOnAA" )
)
process.hltFullIter1PixelHitQuadrupletsPPOnAA = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.0017 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter1PixelHitDoubletsPPOnAA" ),
    fitFastCircle = cms.bool( True ),
    CAHardPtCut = cms.double( 0.0 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 150.0 ),
      value1 = cms.double( 1000.0 ),
      pt1 = cms.double( 0.7 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.3 ),
    useBendingCorrection = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True )
)
process.hltFullIter1PixelSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter1PixelHitQuadrupletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter1CkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter1PixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPLowPtQuadStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter1MaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtQuadStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltFullIter1CtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter1CkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter1MaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "lowPtQuadStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltFullIter1TrackMVAClassifierPPOnAA = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltFullIter1CtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.65, -0.35, -0.15 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorLowPtQuadStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter1HighPurityTracksPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter1CtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltFullIter1TrackMVAClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter1TrackMVAClassifierPPOnAA','MVAValues' )
)
process.hltFullIter2ClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter1HighPurityTracksPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter1ClustersRefRemovalPPOnAA" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacilityFull" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter2MaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter2ClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter2PixelTripletsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix1+BPix3+BPix4',
      'BPix1+BPix2+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+BPix3+FPix1_pos',
      'BPix1+BPix3+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg',
      'BPix1+BPix2+FPix2_pos',
      'BPix1+BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg',
      'BPix1+FPix2_pos+FPix3_pos',
      'BPix1+FPix2_neg+FPix3_neg',
      'BPix1+FPix1_pos+FPix3_pos',
      'BPix1+FPix1_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter2ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter2ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter2PixelTrackingRegionsPPOnAA = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 0.2 ),
      maxNVertices = cms.int32( -1 ),
      sigmaZVertex = cms.double( 4.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.7 ),
      originRadius = cms.double( 0.02 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
)
process.hltFullIter2PixelClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripRawToClustersFacilityFull" )
)
process.hltFullIter2PixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter2PixelTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "hltFullIter2PixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter2PixelTripletsPPOnAA" )
)
process.hltFullIter2PixelHitTripletsPPOnAA = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.3 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter2PixelHitDoubletsPPOnAA" ),
    CAThetaCut = cms.double( 0.004 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 6.0 ),
      value1 = cms.double( 100.0 ),
      pt1 = cms.double( 0.8 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 8.0 )
    ),
    CAPhiCut = cms.double( 0.07 ),
    useBendingCorrection = cms.bool( True )
)
process.hltFullIter2PixelSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter2PixelHitTripletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter2CkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter2PixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter2MaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetHighPtTripletStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltFullIter2CtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter2CkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter2MaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "highPtTripletStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltFullIter2TrackMVAClassifierPPOnAA = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltFullIter2CtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( 0.2, 0.3, 0.4 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorHighPtTripletStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter2HighPurityTracksPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter2CtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltFullIter2TrackMVAClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter2TrackMVAClassifierPPOnAA','MVAValues' )
)
process.hltFullIter3ClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter2HighPurityTracksPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter2ClustersRefRemovalPPOnAA" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacilityFull" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter3MaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter3ClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter3PixelTripletsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix1+BPix3+BPix4',
      'BPix1+BPix2+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+BPix3+FPix1_pos',
      'BPix1+BPix3+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg',
      'BPix1+BPix2+FPix2_pos',
      'BPix1+BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg',
      'BPix1+FPix2_pos+FPix3_pos',
      'BPix1+FPix2_neg+FPix3_neg',
      'BPix1+FPix1_pos+FPix3_pos',
      'BPix1+FPix1_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter3ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter3ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter3PixelTrackingRegionsPPOnAA = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( False ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 0.2 ),
      maxNVertices = cms.int32( -1 ),
      sigmaZVertex = cms.double( 4.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.3 ),
      originRadius = cms.double( 0.02 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
)
process.hltFullIter3PixelClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripRawToClustersFacilityFull" )
)
process.hltFullIter3PixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter3PixelTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "hltFullIter3PixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter3PixelTripletsPPOnAA" )
)
process.hltFullIter3PixelHitTripletsPPOnAA = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.3 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter3PixelHitDoubletsPPOnAA" ),
    CAThetaCut = cms.double( 0.002 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 8.0 ),
      value1 = cms.double( 70.0 ),
      pt1 = cms.double( 0.8 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.05 ),
    useBendingCorrection = cms.bool( True )
)
process.hltFullIter3PixelSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter3PixelHitTripletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter3CkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter3PixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPLowPtTripletStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter3MaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtTripletStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltFullIter3CtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter3CkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter3MaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "lowPtTripletStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltFullIter3TrackMVAClassifierPPOnAA = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltFullIter3CtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( 0.0, 0.2, 0.4 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorLowPtTripletStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter3HighPurityTracksPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter3CtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltFullIter3TrackMVAClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter3TrackMVAClassifierPPOnAA','MVAValues' )
)
process.hltFullIter4ClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter3HighPurityTracksPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter3ClustersRefRemovalPPOnAA" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacilityFull" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter4MaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter4ClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter4PixelQuadrupletsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3+BPix4',
      'BPix1+BPix2+BPix3+FPix1_pos',
      'BPix1+BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos+FPix2_pos',
      'BPix1+BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_neg+FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter4ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter4ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter4PixelTrackingRegionsPPOnAA = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 3.75 ),
      maxNVertices = cms.int32( -1 ),
      sigmaZVertex = cms.double( 4.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.9 ),
      originRadius = cms.double( 1.5 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
)
process.hltFullIter4PixelClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripRawToClustersFacilityFull" )
)
process.hltFullIter4PixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter4PixelTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "hltFullIter4PixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter4PixelQuadrupletsPPOnAA" )
)
process.hltFullIter4PixelHitQuadrupletsPPOnAA = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.0011 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter4PixelHitDoubletsPPOnAA" ),
    fitFastCircle = cms.bool( True ),
    CAHardPtCut = cms.double( 0.0 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 100.0 ),
      value1 = cms.double( 500.0 ),
      pt1 = cms.double( 0.8 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.0 ),
    useBendingCorrection = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True )
)
process.hltFullIter4PixelSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet( 
      FilterStripHits = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      FilterAtHelixStage = cms.bool( False ),
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter4PixelHitQuadrupletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter4CkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter4PixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPDetachedQuadStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter4MaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedQuadStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltFullIter4CtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter4CkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter4MaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "detachedQuadStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltFullIter4TrackMVAClassifierPPOnAA = cms.EDProducer( "TrackMVAClassifierDetached",
    src = cms.InputTag( "hltFullIter4CtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.5, 0.0, 0.5 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorDetachedQuadStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter4HighPurityTracksPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter4CtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltFullIter4TrackMVAClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter4TrackMVAClassifierPPOnAA','MVAValues' )
)
process.hltFullIter5ClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter4HighPurityTracksPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter4ClustersRefRemovalPPOnAA" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacilityFull" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter5MaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter5ClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter5PixelTripletsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter5ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter5ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter5PixelTrackingRegionsPPOnAA = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 3.0 ),
      maxNVertices = cms.int32( -1 ),
      sigmaZVertex = cms.double( 4.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.9 ),
      originRadius = cms.double( 1.5 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
)
process.hltFullIter5PixelClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripRawToClustersFacilityFull" )
)
process.hltFullIter5PixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter5PixelTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "hltFullIter5PixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter5PixelTripletsPPOnAA" )
)
process.hltFullIter5PixelHitTripletsPPOnAA = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.2 ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter5PixelHitDoubletsPPOnAA" ),
    CAThetaCut = cms.double( 0.001 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 10.0 ),
      value1 = cms.double( 300.0 ),
      pt1 = cms.double( 0.8 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.0 ),
    useBendingCorrection = cms.bool( True )
)
process.hltFullIter5PixelSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet( 
      FilterStripHits = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      FilterAtHelixStage = cms.bool( False ),
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter5PixelHitTripletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter5CkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter5PixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPDetachedTripletStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter5MaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedTripletStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltFullIter5CtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter5CkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter5MaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "detachedTripletStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltFullIter5TrackMVAClassifierPPOnAA = cms.EDProducer( "TrackMVAClassifierDetached",
    src = cms.InputTag( "hltFullIter5CtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.2, 0.3, 0.8 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorDetachedTripletStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter5HighPurityTracksPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter5CtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltFullIter5TrackMVAClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter5TrackMVAClassifierPPOnAA','MVAValues' )
)
process.hltFullIter6ClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter5HighPurityTracksPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter5ClustersRefRemovalPPOnAA" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacilityFull" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter6MaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter6ClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter6PixelPairsAPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter6ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter6ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter6PixelTrackingRegionsAPPOnAA = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 0.03 ),
      maxNVertices = cms.int32( 5 ),
      sigmaZVertex = cms.double( 3.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.6 ),
      originRadius = cms.double( 0.015 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
)
process.hltFullIter6PixelClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripRawToClustersFacilityFull" )
)
process.hltFullIter6PixelHitDoubletsAPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter6PixelTrackingRegionsAPPOnAA" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltFullIter6PixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter6PixelPairsAPPOnAA" )
)
process.hltFullIter6PixelSeedsAPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet( 
      FilterStripHits = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      FilterAtHelixStage = cms.bool( True ),
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter6PixelHitDoubletsAPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter6PixelPairsBPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix4' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter6ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter6ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter6ClustersRefRemovalPPOnAA" ),
      matchedRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','matchedRecHit' ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) )
    )
)
process.hltFullIter6PixelTrackingRegionsBPPOnAA = cms.EDProducer( "PointSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet( 
      vertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
      zErrorVetex = cms.double( 0.03 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 24.2 ),
      maxNVertices = cms.int32( 5 ),
      maxNRegions = cms.int32( 5 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      ptMin = cms.double( 0.6 ),
      points = cms.PSet( 
        phi = cms.vdouble( 3.0 ),
        eta = cms.vdouble( 0.0 )
      ),
      mode = cms.string( "VerticesFixed" ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "Never" ),
      originRadius = cms.double( 0.015 ),
      measurementTrackerName = cms.InputTag( "" ),
      precise = cms.bool( True ),
      deltaEta = cms.double( 1.2 ),
      deltaPhi = cms.double( 0.5 )
    )
)
process.hltFullIter6PixelHitDoubletsBPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter6PixelTrackingRegionsBPPOnAA" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltFullIter6PixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter6PixelPairsBPPOnAA" )
)
process.hltFullIter6PixelSeedsBPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet( 
      FilterStripHits = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      FilterAtHelixStage = cms.bool( True ),
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter6PixelHitDoubletsBPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter6PixelSeedsPPOnAA = cms.EDProducer( "SeedCombiner",
    seedCollections = cms.VInputTag( 'hltFullIter6PixelSeedsAPPOnAA','hltFullIter6PixelSeedsBPPOnAA' )
)
process.hltFullIter6CkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter6PixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter6MaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltFullIter6CtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter6CkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter6MaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "pixelPairStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltFullIter6TrackMVAClassifierPPOnAA = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltFullIter6CtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.2, 0.0, 0.3 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorIter2_13TeV" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter6HighPurityTracksPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter6CtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltFullIter6TrackMVAClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter6TrackMVAClassifierPPOnAA','MVAValues' )
)
process.hltFullIter7ClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter6HighPurityTracksPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter6ClustersRefRemovalPPOnAA" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacilityFull" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter7MaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter7ClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter7MixedLayersAPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 1 ),
      skipClusters = cms.InputTag( "hltFullIter7ClustersRefRemovalPPOnAA" ),
      matchedRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','matchedRecHit' ),
      useRingSlector = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      maxRing = cms.int32( 1 )
    ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter7ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter7ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter7MixedTrackingRegionsAPPOnAA = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 3.75 ),
      maxNVertices = cms.int32( -1 ),
      sigmaZVertex = cms.double( 4.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.4 ),
      originRadius = cms.double( 1.5 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False ),
      originRScaling4BigEvts = cms.bool( True ),
      ptMinScaling4BigEvts = cms.bool( True ),
      minOriginR = cms.double( 0.0 ),
      maxPtMin = cms.double( 0.7 ),
      scalingStartNPix = cms.double( 20000.0 ),
      scalingEndNPix = cms.double( 35000.0 ),
      pixelClustersForScaling = cms.InputTag( "hltSiPixelClustersPPOnAA" )
    )
)
process.hltFullIter7MixedClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripRawToClustersFacilityFull" )
)
process.hltFullIter7MixedHitDoubletsAPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter7MixedTrackingRegionsAPPOnAA" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltFullIter7MixedClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter7MixedLayersAPPOnAA" )
)
process.hltFullIter7MixedHitTripletsAPPOnAA = cms.EDProducer( "PixelTripletLargeTipEDProducer",
    useBending = cms.bool( True ),
    useFixedPreFiltering = cms.bool( False ),
    produceIntermediateHitTriplets = cms.bool( False ),
    maxElement = cms.uint32( 1000000 ),
    phiPreFiltering = cms.double( 0.3 ),
    extraHitRPhitolerance = cms.double( 0.0 ),
    produceSeedingHitSets = cms.bool( True ),
    doublets = cms.InputTag( "hltFullIter7MixedHitDoubletsAPPOnAA" ),
    useMultScattering = cms.bool( True ),
    extraHitRZtolerance = cms.double( 0.0 )
)
process.hltFullIter7MixedSeedsAPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet( 
      FilterStripHits = cms.bool( True ),
      FilterPixelHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "hltESPMixedStepClusterShapeHitFilter" ),
      FilterAtHelixStage = cms.bool( False ),
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter7MixedHitTripletsAPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter7MixedLayersBPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix3+BPix4+TIB1' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter7ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter7ClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter7ClustersRefRemovalPPOnAA" ),
      matchedRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','matchedRecHit' ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) )
    )
)
process.hltFullIter7MixedTrackingRegionsBPPOnAA = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 2.5 ),
      maxNVertices = cms.int32( -1 ),
      sigmaZVertex = cms.double( 4.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.6 ),
      originRadius = cms.double( 1.5 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False ),
      originRScaling4BigEvts = cms.bool( True ),
      ptMinScaling4BigEvts = cms.bool( True ),
      minOriginR = cms.double( 0.0 ),
      maxPtMin = cms.double( 0.7 ),
      scalingStartNPix = cms.double( 20000.0 ),
      scalingEndNPix = cms.double( 35000.0 ),
      pixelClustersForScaling = cms.InputTag( "hltSiPixelClustersPPOnAA" )
    )
)
process.hltFullIter7MixedHitDoubletsBPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter7MixedTrackingRegionsBPPOnAA" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltFullIter7MixedClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter7MixedLayersBPPOnAA" )
)
process.hltFullIter7MixedHitTripletsBPPOnAA = cms.EDProducer( "PixelTripletLargeTipEDProducer",
    useBending = cms.bool( True ),
    useFixedPreFiltering = cms.bool( False ),
    produceIntermediateHitTriplets = cms.bool( False ),
    maxElement = cms.uint32( 1000000 ),
    phiPreFiltering = cms.double( 0.3 ),
    extraHitRPhitolerance = cms.double( 0.0 ),
    produceSeedingHitSets = cms.bool( True ),
    doublets = cms.InputTag( "hltFullIter7MixedHitDoubletsBPPOnAA" ),
    useMultScattering = cms.bool( True ),
    extraHitRZtolerance = cms.double( 0.0 )
)
process.hltFullIter7MixedSeedsBPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet( 
      FilterStripHits = cms.bool( True ),
      FilterPixelHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "hltESPMixedStepClusterShapeHitFilter" ),
      FilterAtHelixStage = cms.bool( False ),
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter7MixedHitTripletsBPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter7MixedSeedsPPOnAA = cms.EDProducer( "SeedCombiner",
    seedCollections = cms.VInputTag( 'hltFullIter7MixedSeedsAPPOnAA','hltFullIter7MixedSeedsBPPOnAA' )
)
process.hltFullIter7CkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter7MixedSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPMixedTripletStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter7MaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMixedTripletStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltFullIter7CtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter7CkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter7MaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "mixedTripletStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltFullIter7TrackMVAClassifierPPOnAA = cms.EDProducer( "TrackMVAClassifierDetached",
    src = cms.InputTag( "hltFullIter7CtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.5, 0.0, 0.5 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorMixedTripletStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter7HighPurityTracksPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter7CtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltFullIter7TrackMVAClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter7TrackMVAClassifierPPOnAA','MVAValues' )
)
process.hltFullIter8ClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter7HighPurityTracksPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter7ClustersRefRemovalPPOnAA" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacilityFull" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter8MaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter8ClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter8PixelLessLayersPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'TIB1+TIB2+MTIB3',
      'TIB1+TIB2+MTIB4',
      'TIB1+TIB2+MTID1_pos',
      'TIB1+TIB2+MTID1_neg',
      'TID1_pos+TID2_pos+TID3_pos',
      'TID1_neg+TID2_neg+TID3_neg',
      'TID1_pos+TID2_pos+MTID3_pos',
      'TID1_neg+TID2_neg+MTID3_neg',
      'TID1_pos+TID2_pos+MTEC1_pos',
      'TID1_neg+TID2_neg+MTEC1_neg',
      'TID2_pos+TID3_pos+TEC1_pos',
      'TID2_neg+TID3_neg+TEC1_neg',
      'TID2_pos+TID3_pos+MTEC1_pos',
      'TID2_neg+TID3_neg+MTEC1_neg',
      'TEC1_pos+TEC2_pos+TEC3_pos',
      'TEC1_neg+TEC2_neg+TEC3_neg',
      'TEC1_pos+TEC2_pos+MTEC3_pos',
      'TEC1_neg+TEC2_neg+MTEC3_neg',
      'TEC1_pos+TEC2_pos+TEC4_pos',
      'TEC1_neg+TEC2_neg+TEC4_neg',
      'TEC1_pos+TEC2_pos+MTEC4_pos',
      'TEC1_neg+TEC2_neg+MTEC4_neg',
      'TEC2_pos+TEC3_pos+TEC4_pos',
      'TEC2_neg+TEC3_neg+TEC4_neg',
      'TEC2_pos+TEC3_pos+MTEC4_pos',
      'TEC2_neg+TEC3_neg+MTEC4_neg',
      'TEC2_pos+TEC3_pos+TEC5_pos',
      'TEC2_neg+TEC3_neg+TEC5_neg',
      'TEC2_pos+TEC3_pos+TEC6_pos',
      'TEC2_neg+TEC3_neg+TEC6_neg',
      'TEC3_pos+TEC4_pos+TEC5_pos',
      'TEC3_neg+TEC4_neg+TEC5_neg',
      'TEC3_pos+TEC4_pos+MTEC5_pos',
      'TEC3_neg+TEC4_neg+MTEC5_neg',
      'TEC3_pos+TEC5_pos+TEC6_pos',
      'TEC3_neg+TEC5_neg+TEC6_neg',
      'TEC4_pos+TEC5_pos+TEC6_pos',
      'TEC4_neg+TEC5_neg+TEC6_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 1 ),
      skipClusters = cms.InputTag( "hltFullIter8ClustersRefRemovalPPOnAA" ),
      matchedRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','matchedRecHit' ),
      useRingSlector = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      maxRing = cms.int32( 2 )
    ),
    MTID = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 3 ),
      skipClusters = cms.InputTag( "hltFullIter8ClustersRefRemovalPPOnAA" ),
      useRingSlector = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      maxRing = cms.int32( 3 ),
      rphiRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','rphiRecHit' )
    ),
    FPix = cms.PSet(  ),
    MTEC = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 3 ),
      skipClusters = cms.InputTag( "hltFullIter8ClustersRefRemovalPPOnAA" ),
      useRingSlector = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      maxRing = cms.int32( 3 ),
      rphiRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','rphiRecHit' )
    ),
    MTIB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter8ClustersRefRemovalPPOnAA" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      rphiRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','rphiRecHit' )
    ),
    TID = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 1 ),
      skipClusters = cms.InputTag( "hltFullIter8ClustersRefRemovalPPOnAA" ),
      matchedRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','matchedRecHit' ),
      useRingSlector = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      maxRing = cms.int32( 2 )
    ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(  ),
    TIB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter8ClustersRefRemovalPPOnAA" ),
      matchedRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','matchedRecHit' ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) )
    )
)
process.hltFullIter8PixelLessTrackingRegionsPPOnAA = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 3.0 ),
      maxNVertices = cms.int32( -1 ),
      sigmaZVertex = cms.double( 4.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 2.0 ),
      originRadius = cms.double( 1.0 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False ),
      originRScaling4BigEvts = cms.bool( True ),
      ptMinScaling4BigEvts = cms.bool( False ),
      minOriginR = cms.double( 0.0 ),
      maxPtMin = cms.double( 0.7 ),
      scalingStartNPix = cms.double( 20000.0 ),
      scalingEndNPix = cms.double( 35000.0 ),
      pixelClustersForScaling = cms.InputTag( "hltSiPixelClustersPPOnAA" )
    )
)
process.hltFullIter8PixelLessClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripRawToClustersFacilityFull" )
)
process.hltFullIter8PixelLessHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter8PixelLessTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltFullIter8PixelLessClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter8PixelLessLayersPPOnAA" )
)
process.hltFullIter8PixelLessHitTripletsPPOnAA = cms.EDProducer( "MultiHitFromChi2EDProducer",
    detIdsToDebug = cms.vint32( 0, 0, 0 ),
    extraPhiKDBox = cms.double( 0.005 ),
    pt_interv = cms.vdouble( 0.4, 0.7, 1.0, 2.0 ),
    useFixedPreFiltering = cms.bool( False ),
    refitHits = cms.bool( True ),
    chi2VsPtCut = cms.bool( True ),
    maxChi2 = cms.double( 5.0 ),
    extraHitRPhitolerance = cms.double( 0.0 ),
    extraRKDBox = cms.double( 0.2 ),
    chi2_cuts = cms.vdouble( 3.0, 4.0, 5.0, 5.0 ),
    extraZKDBox = cms.double( 0.2 ),
    doublets = cms.InputTag( "hltFullIter8PixelLessHitDoubletsPPOnAA" ),
    maxElement = cms.uint32( 1000000 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    phiPreFiltering = cms.double( 0.3 ),
    extraHitRZtolerance = cms.double( 0.0 ),
    ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
    fnSigmaRZ = cms.double( 2.0 )
)
process.hltFullIter8PixelLessSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet( 
      mode = cms.string( "and" ),
      comparitors = cms.VPSet( 
        cms.PSet(  FilterStripHits = cms.bool( True ),
          FilterPixelHits = cms.bool( False ),
          ClusterShapeHitFilterName = cms.string( "hltESPPixelLessStepClusterShapeHitFilter" ),
          FilterAtHelixStage = cms.bool( True ),
          ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
          ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
        ),
        cms.PSet(  subclusterCutSN = cms.double( 12.0 ),
          trimMaxADC = cms.double( 30.0 ),
          seedCutMIPs = cms.double( 0.35 ),
          subclusterCutMIPs = cms.double( 0.45 ),
          subclusterWindow = cms.double( 0.7 ),
          maxNSat = cms.uint32( 3 ),
          trimMaxFracNeigh = cms.double( 0.25 ),
          FilterAtHelixStage = cms.bool( False ),
          maxTrimmedSizeDiffNeg = cms.double( 1.0 ),
          seedCutSN = cms.double( 7.0 ),
          ComponentName = cms.string( "StripSubClusterShapeSeedFilter" ),
          maxTrimmedSizeDiffPos = cms.double( 0.7 ),
          trimMaxFracTotal = cms.double( 0.15 )
        )
      ),
      ComponentName = cms.string( "CombinedSeedComparitor" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter8PixelLessHitTripletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter8CkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter8PixelLessSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPPixelLessStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter8MaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelLessStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltFullIter8CtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter8CkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter8MaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "pixelLessStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltFullIter8TrackMVAClassifierPPOnAA = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltFullIter8CtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.4, 0.0, 0.4 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorPixelLessStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter8HighPurityTracksPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter8CtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltFullIter8TrackMVAClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter8TrackMVAClassifierPPOnAA','MVAValues' )
)
process.hltFullIter9ClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter8HighPurityTracksPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter8ClustersRefRemovalPPOnAA" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacilityFull" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter9MaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter9ClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter9TobTecLayersTriplPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'TOB1+TOB2+MTOB3',
      'TOB1+TOB2+MTOB4',
      'TOB1+TOB2+MTEC1_pos',
      'TOB1+TOB2+MTEC1_neg' ),
    MTOB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter9ClustersRefRemovalPPOnAA" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      rphiRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','rphiRecHit' )
    ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(  ),
    MTEC = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 6 ),
      skipClusters = cms.InputTag( "hltFullIter9ClustersRefRemovalPPOnAA" ),
      useRingSlector = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      maxRing = cms.int32( 7 ),
      rphiRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','rphiRecHit' )
    ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter9ClustersRefRemovalPPOnAA" ),
      matchedRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','matchedRecHit' ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) )
    ),
    BPix = cms.PSet(  ),
    TIB = cms.PSet(  )
)
process.hltFullIter9TobTecTrackingRegionsTriplPPOnAA = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 5.0 ),
      maxNVertices = cms.int32( -1 ),
      sigmaZVertex = cms.double( 4.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 2.0 ),
      originRadius = cms.double( 3.5 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False ),
      originRScaling4BigEvts = cms.bool( True ),
      ptMinScaling4BigEvts = cms.bool( False ),
      minOriginR = cms.double( 0.0 ),
      maxPtMin = cms.double( 0.7 ),
      scalingStartNPix = cms.double( 20000.0 ),
      scalingEndNPix = cms.double( 35000.0 ),
      pixelClustersForScaling = cms.InputTag( "hltSiPixelClustersPPOnAA" )
    )
)
process.hltFullIter9TobTecClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripRawToClustersFacilityFull" )
)
process.hltFullIter9TobTecHitDoubletsTriplPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter9TobTecTrackingRegionsTriplPPOnAA" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltFullIter9TobTecClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter9TobTecLayersTriplPPOnAA" )
)
process.hltFullIter9TobTecHitTripletsTriplPPOnAA = cms.EDProducer( "MultiHitFromChi2EDProducer",
    detIdsToDebug = cms.vint32( 0, 0, 0 ),
    extraPhiKDBox = cms.double( 0.01 ),
    pt_interv = cms.vdouble( 0.4, 0.7, 1.0, 2.0 ),
    useFixedPreFiltering = cms.bool( False ),
    refitHits = cms.bool( True ),
    chi2VsPtCut = cms.bool( True ),
    maxChi2 = cms.double( 5.0 ),
    extraHitRPhitolerance = cms.double( 0.0 ),
    extraRKDBox = cms.double( 0.2 ),
    chi2_cuts = cms.vdouble( 3.0, 4.0, 5.0, 5.0 ),
    extraZKDBox = cms.double( 0.2 ),
    doublets = cms.InputTag( "hltFullIter9TobTecHitDoubletsTriplPPOnAA" ),
    maxElement = cms.uint32( 1000000 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    phiPreFiltering = cms.double( 0.3 ),
    extraHitRZtolerance = cms.double( 0.0 ),
    ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
    fnSigmaRZ = cms.double( 2.0 )
)
process.hltFullIter9TobTecSeedsTriplPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet( 
      mode = cms.string( "and" ),
      comparitors = cms.VPSet( 
        cms.PSet(  FilterStripHits = cms.bool( True ),
          FilterPixelHits = cms.bool( False ),
          ClusterShapeHitFilterName = cms.string( "hltESPTobTecStepClusterShapeHitFilter" ),
          FilterAtHelixStage = cms.bool( True ),
          ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
          ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
        ),
        cms.PSet(  subclusterCutSN = cms.double( 12.0 ),
          trimMaxADC = cms.double( 30.0 ),
          seedCutMIPs = cms.double( 0.35 ),
          subclusterCutMIPs = cms.double( 0.45 ),
          subclusterWindow = cms.double( 0.7 ),
          maxNSat = cms.uint32( 3 ),
          trimMaxFracNeigh = cms.double( 0.25 ),
          FilterAtHelixStage = cms.bool( False ),
          maxTrimmedSizeDiffNeg = cms.double( 1.0 ),
          seedCutSN = cms.double( 7.0 ),
          ComponentName = cms.string( "StripSubClusterShapeSeedFilter" ),
          maxTrimmedSizeDiffPos = cms.double( 0.7 ),
          trimMaxFracTotal = cms.double( 0.15 )
        )
      ),
      ComponentName = cms.string( "CombinedSeedComparitor" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter9TobTecHitTripletsTriplPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter9TobTecLayersPairPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'TOB1+TEC1_pos',
      'TOB1+TEC1_neg',
      'TEC1_pos+TEC2_pos',
      'TEC1_neg+TEC2_neg',
      'TEC2_pos+TEC3_pos',
      'TEC2_neg+TEC3_neg',
      'TEC3_pos+TEC4_pos',
      'TEC3_neg+TEC4_neg',
      'TEC4_pos+TEC5_pos',
      'TEC4_neg+TEC5_neg',
      'TEC5_pos+TEC6_pos',
      'TEC5_neg+TEC6_neg',
      'TEC6_pos+TEC7_pos',
      'TEC6_neg+TEC7_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 5 ),
      skipClusters = cms.InputTag( "hltFullIter9ClustersRefRemovalPPOnAA" ),
      matchedRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','matchedRecHit' ),
      useRingSlector = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      maxRing = cms.int32( 5 )
    ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(  ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltFullIter9ClustersRefRemovalPPOnAA" ),
      matchedRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','matchedRecHit' ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) )
    ),
    BPix = cms.PSet(  ),
    TIB = cms.PSet(  )
)
process.hltFullIter9TobTecTrackingRegionsPairPPOnAA = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 7.5 ),
      maxNVertices = cms.int32( -1 ),
      sigmaZVertex = cms.double( 4.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 2.0 ),
      originRadius = cms.double( 6.0 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False ),
      originRScaling4BigEvts = cms.bool( True ),
      ptMinScaling4BigEvts = cms.bool( False ),
      minOriginR = cms.double( 0.0 ),
      maxPtMin = cms.double( 0.7 ),
      scalingStartNPix = cms.double( 20000.0 ),
      scalingEndNPix = cms.double( 35000.0 ),
      pixelClustersForScaling = cms.InputTag( "hltSiPixelClustersPPOnAA" )
    )
)
process.hltFullIter9TobTecHitDoubletsPairPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter9TobTecTrackingRegionsPairPPOnAA" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltFullIter9TobTecClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter9TobTecLayersPairPPOnAA" )
)
process.hltFullIter9TobTecSeedsPairPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet( 
      mode = cms.string( "and" ),
      comparitors = cms.VPSet( 
        cms.PSet(  FilterStripHits = cms.bool( True ),
          FilterPixelHits = cms.bool( False ),
          ClusterShapeHitFilterName = cms.string( "hltESPTobTecStepClusterShapeHitFilter" ),
          FilterAtHelixStage = cms.bool( True ),
          ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
          ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
        ),
        cms.PSet(  subclusterCutSN = cms.double( 12.0 ),
          trimMaxADC = cms.double( 30.0 ),
          seedCutMIPs = cms.double( 0.35 ),
          subclusterCutMIPs = cms.double( 0.45 ),
          subclusterWindow = cms.double( 0.7 ),
          maxNSat = cms.uint32( 3 ),
          trimMaxFracNeigh = cms.double( 0.25 ),
          FilterAtHelixStage = cms.bool( False ),
          maxTrimmedSizeDiffNeg = cms.double( 1.0 ),
          seedCutSN = cms.double( 7.0 ),
          ComponentName = cms.string( "StripSubClusterShapeSeedFilter" ),
          maxTrimmedSizeDiffPos = cms.double( 0.7 ),
          trimMaxFracTotal = cms.double( 0.15 )
        )
      ),
      ComponentName = cms.string( "CombinedSeedComparitor" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter9TobTecHitDoubletsPairPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter9TobTecSeedsPPOnAA = cms.EDProducer( "SeedCombiner",
    seedCollections = cms.VInputTag( 'hltFullIter9TobTecSeedsTriplPPOnAA','hltFullIter9TobTecSeedsPairPPOnAA' )
)
process.hltFullIter9CkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter9TobTecSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTobTecStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter9MaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTobTecStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltFullIter9CtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter9CkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter9MaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPTobTecStepFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "tobTecStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltFullIter9TrackMVAClassifierPPOnAA = cms.EDProducer( "TrackMVAClassifierDetached",
    src = cms.InputTag( "hltFullIter9CtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.6, -0.45, -0.3 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorTobTecStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFirstStepGoodPrimaryVerticesPPOnAA = cms.EDFilter( "PrimaryVertexObjectFilter",
    src = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
    filterParams = cms.PSet( 
      maxZ = cms.double( 15.0 ),
      minNdof = cms.double( 25.0 ),
      maxRho = cms.double( 2.0 )
    )
)
process.hltFullIter10JetCoreLayersPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix1+BPix4',
      'BPix2+BPix3',
      'BPix2+BPix4',
      'BPix3+BPix4',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix3_pos',
      'FPix1_neg+FPix3_neg',
      'FPix2_pos+FPix3_pos',
      'FPix2_neg+FPix3_neg',
      'BPix4+TIB1',
      'BPix4+TIB2' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
    ),
    TIB = cms.PSet( 
      matchedRecHits = cms.InputTag( 'hltSiStripMatchedRecHitsFull','matchedRecHit' ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    )
)
process.hltFullIter10JetCoreTrackingRegionsPPOnAA = cms.EDProducer( "TauRegionalPixelSeedTrackingRegionEDProducer",
    RegionPSet = cms.PSet( 
      deltaPhiRegion = cms.double( 0.2 ),
      originHalfLength = cms.double( 0.2 ),
      howToUseMeasurementTracker = cms.string( "never" ),
      measurementTrackerName = cms.InputTag( "" ),
      deltaEtaRegion = cms.double( 0.2 ),
      vertexSrc = cms.InputTag( "hltFirstStepGoodPrimaryVerticesPPOnAA" ),
      searchOpt = cms.bool( False ),
      JetSrc = cms.InputTag( "hltJetsForCoreTracking" ),
      originRadius = cms.double( 0.2 ),
      ptMin = cms.double( 10.0 )
    )
)
process.hltFullIter10JetCoreClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripRawToClustersFacilityFull" )
)
process.hltFullIter10JetCoreHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter10JetCoreTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltFullIter10JetCoreClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter10JetCoreLayersPPOnAA" )
)
process.hltFullIter10JetCoreSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( True ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter10JetCoreHitDoubletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter10CkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter10JetCoreSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 10000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersFullPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetJetCoreStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltFullIter10CtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter10CkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "jetCoreRegionalStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltFullIter10TrackMVAClassifierPPOnAA = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltFullIter10CtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.2, 0.0, 0.4 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorJetCoreRegionalStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIterativeTrackingMergedPPOnAA = cms.EDProducer( "TrackCollectionMerger",
    shareFrac = cms.double( 0.19 ),
    inputClassifiers = cms.vstring( 'hltFullIter0TrackMVAClassifierPPOnAA',
      'hltFullIter1TrackMVAClassifierPPOnAA',
      'hltFullIter2TrackMVAClassifierPPOnAA',
      'hltFullIter3TrackMVAClassifierPPOnAA',
      'hltFullIter4TrackMVAClassifierPPOnAA',
      'hltFullIter5TrackMVAClassifierPPOnAA',
      'hltFullIter6TrackMVAClassifierPPOnAA',
      'hltFullIter7TrackMVAClassifierPPOnAA',
      'hltFullIter8TrackMVAClassifierPPOnAA',
      'hltFullIter9TrackMVAClassifierPPOnAA',
      'hltFullIter10TrackMVAClassifierPPOnAA' ),
    minQuality = cms.string( "loose" ),
    enableMerging = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    minShareHits = cms.uint32( 2 ),
    copyTrajectories = cms.untracked.bool( False ),
    allowFirstHitShare = cms.bool( True ),
    foundHitBonus = cms.double( 10.0 ),
    trackProducers = cms.VInputTag( 'hltFullIter0CtfWithMaterialTracksPPOnAA','hltFullIter1CtfWithMaterialTracksPPOnAA','hltFullIter2CtfWithMaterialTracksPPOnAA','hltFullIter3CtfWithMaterialTracksPPOnAA','hltFullIter4CtfWithMaterialTracksPPOnAA','hltFullIter5CtfWithMaterialTracksPPOnAA','hltFullIter6CtfWithMaterialTracksPPOnAA','hltFullIter7CtfWithMaterialTracksPPOnAA','hltFullIter8CtfWithMaterialTracksPPOnAA','hltFullIter9CtfWithMaterialTracksPPOnAA','hltFullIter10CtfWithMaterialTracksPPOnAA' ),
    lostHitPenalty = cms.double( 5.0 ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" )
)
process.hltFullOnlinePrimaryVerticesPPOnAA = cms.EDProducer( "PrimaryVertexProducer",
    vertexCollections = cms.VPSet( 
      cms.PSet(  chi2cutoff = cms.double( 3.0 ),
        label = cms.string( "" ),
        useBeamConstraint = cms.bool( False ),
        minNdof = cms.double( 0.0 ),
        maxDistanceToBeam = cms.double( 1.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" )
      ),
      cms.PSet(  chi2cutoff = cms.double( 3.0 ),
        label = cms.string( "WithBS" ),
        useBeamConstraint = cms.bool( True ),
        minNdof = cms.double( 2.0 ),
        maxDistanceToBeam = cms.double( 1.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" )
      )
    ),
    verbose = cms.untracked.bool( False ),
    TkFilterParameters = cms.PSet( 
      maxEta = cms.double( 2.4 ),
      minPt = cms.double( 0.7 ),
      minSiliconLayersWithHits = cms.int32( 5 ),
      minPixelLayersWithHits = cms.int32( 3 ),
      maxNormalizedChi2 = cms.double( 20.0 ),
      trackQuality = cms.string( "highPurity" ),
      algorithm = cms.string( "filter" ),
      maxD0Significance = cms.double( 2.0 )
    ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltFullIterativeTrackingMergedPPOnAA" ),
    TkClusParameters = cms.PSet( 
      TkDAClusParameters = cms.PSet( 
        zmerge = cms.double( 0.01 ),
        Tstop = cms.double( 0.5 ),
        d0CutOff = cms.double( 3.0 ),
        dzCutOff = cms.double( 4.0 ),
        vertexSize = cms.double( 0.01 ),
        coolingFactor = cms.double( 0.6 ),
        Tpurge = cms.double( 2.0 ),
        Tmin = cms.double( 2.4 ),
        uniquetrkweight = cms.double( 0.9 )
      ),
      algorithm = cms.string( "DA_vect" )
    )
)
process.hltGoodHighPurityFullTrackCutClassifierForHighPt = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltFullIterativeTrackingMergedPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullOnlinePrimaryVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      dr_par = cms.PSet( 
        drWPVerr_par = cms.vdouble( 9999.0, 9999.0, 9999.0 ),
        dr_exp = cms.vint32( 0, 0, 0 )
      ),
      minLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet( 
        dz_exp = cms.vint32( 0, 0, 0 ),
        dzWPVerr_par = cms.vdouble( 9999.0, 9999.0, 9999.0 )
      ),
      maxChi2 = cms.vdouble( 9999.0, 9999.0, 9999.0 ),
      maxChi2n = cms.vdouble( 9999.0, 9999.0, 9999.0 ),
      maxLostLayers = cms.vint32( 999, 999, 999 ),
      maxDz = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 999.0, 999.0 ),
      maxDr = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
      minNdof = cms.vdouble( -1.0, -1.0, -1.0 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      minPixelHits = cms.vint32( 0, 0, 0 ),
      minNVtxTrk = cms.int32( 2 ),
      minHits = cms.vint32( 0, 0, 0 ),
      maxRelPtErr = cms.vdouble( 0.3, 0.3, 0.3 )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltGoodHighPurityFullTracksForHighPt = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIterativeTrackingMergedPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltGoodHighPurityFullTrackCutClassifierForHighPt','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltGoodHighPurityFullTrackCutClassifierForHighPt','MVAValues' )
)
process.hltFullCandsForHighPtTrigger = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( "hltGoodHighPurityFullTracksForHighPt" ),
    particleType = cms.string( "pi+" )
)
process.hltFullTrackHighPt8 = cms.EDFilter( "HLTSingleVertexPixelTrackFilter",
    saveTags = cms.bool( True ),
    MinTrks = cms.int32( 1 ),
    MinPt = cms.double( 8.0 ),
    MaxVz = cms.double( 15.0 ),
    MaxEta = cms.double( 2.4 ),
    trackCollection = cms.InputTag( "hltFullCandsForHighPtTrigger" ),
    vertexCollection = cms.InputTag( "hltFullOnlinePrimaryVerticesPPOnAA" ),
    MaxPt = cms.double( 9999.0 ),
    MinSep = cms.double( 9999.0 )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtStage2Digis + process.hltGtStage2ObjectMap )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence( process.hltEcalDigis + process.hltEcalUncalibRecHit + process.hltEcalDetIdToBeRecovered + process.hltEcalRecHit )
process.HLTDoLocalHcalSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhePhase1Reco + process.hltHbhereco + process.hltHfprereco + process.hltHfreco + process.hltHoreco )
process.HLTDoCaloSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence + process.HLTDoLocalHcalSequence + process.hltTowerMakerForAll )
process.HLTPuAK4CaloJetsReconstructionSequence = cms.Sequence( process.HLTDoCaloSequence + process.hltPuAK4CaloJets + process.hltPuAK4CaloJetsIDPassed )
process.HLTPuAK4CaloCorrectorProducersSequence = cms.Sequence( process.hltAK4CaloFastJetCorrector + process.hltAK4CaloRelativeCorrector + process.hltAK4CaloAbsoluteCorrector + process.hltPuAK4CaloCorrector )
process.HLTPuAK4CaloJetsCorrectionSequence = cms.Sequence( process.hltFixedGridRhoFastjetAllCalo + process.HLTPuAK4CaloCorrectorProducersSequence + process.hltPuAK4CaloJetsCorrected + process.hltPuAK4CaloJetsCorrectedIDPassed )
process.HLTPuAK4CaloJetsSequence = cms.Sequence( process.HLTPuAK4CaloJetsReconstructionSequence + process.HLTPuAK4CaloJetsCorrectionSequence )
process.HLTDoLocalPixelSequencePPOnAA = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClustersPPOnAA + process.hltSiPixelClustersCachePPOnAA + process.hltSiPixelRecHitsPPOnAA )
process.HLTDoLocalStripSequencePPOnAA = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.hltSiStripRawToClustersFacility + process.hltSiStripClustersPPOnAA )
process.HLTFullIterativeTrackingIteration0PreSplittingPPOnAA = cms.Sequence( process.hltFullIter0PixelQuadrupletsPreSplittingPPOnAA + process.hltFullIter0PixelTrackingRegionsPreSplitting + process.hltFullIter0PixelClusterCheckPreSplittingPPOnAA + process.hltFullIter0PixelHitDoubletsPreSplittingPPOnAA + process.hltFullIter0PixelHitQuadrupletsPreSplittingPPOnAA + process.hltFullIter0PixelSeedsPreSplittingPPOnAA + process.hltFullIter0CkfTrackCandidatesPreSplittingPPOnAA + process.hltFullIter0CtfWithMaterialTracksPreSplittingPPOnAA + process.hltFullIter0PrimaryVerticesPreSplittingPPOnAA )
process.HLTDoLocalPixelSequenceAfterSplittingPPOnAA = cms.Sequence( process.hltSiPixelClustersAfterSplittingPPOnAA + process.hltSiPixelClustersCacheAfterSplittingPPOnAA + process.hltSiPixelRecHitsAfterSplittingPPOnAA )
process.HLTDoLocalStripSequenceFullPPOnAA = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.hltSiStripRawToClustersFacilityFull + process.hltSiStripClustersFullPPOnAA + process.hltSiStripMatchedRecHitsFull )
process.HLTPixelClusterSplittingPPOnAA = cms.Sequence( process.HLTPuAK4CaloJetsSequence + process.hltJetsForCoreTracking + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripSequencePPOnAA + process.HLTFullIterativeTrackingIteration0PreSplittingPPOnAA + process.HLTDoLocalPixelSequenceAfterSplittingPPOnAA + process.HLTDoLocalStripSequenceFullPPOnAA )
process.HLTFullIterativeTrackingIteration0PPOnAA = cms.Sequence( process.hltFullIter0PixelQuadrupletsPPOnAA + process.hltFullIter0PixelTrackingRegions + process.hltFullIter0PixelClusterCheckPPOnAA + process.hltFullIter0PixelHitDoubletsPPOnAA + process.hltFullIter0PixelHitQuadrupletsPPOnAA + process.hltFullIter0PixelSeedsPPOnAA + process.hltFullIter0CkfTrackCandidatesPPOnAA + process.hltFullIter0CtfWithMaterialTracksPPOnAA + process.hltFullIter0PrimaryVerticesPPOnAA + process.hltFullIter0TrackMVAClassifierPPOnAA + process.hltFullIter0HighPurityTracksPPOnAA )
process.HLTFullIterativeTrackingIteration1PPOnAA = cms.Sequence( process.hltFullIter1ClustersRefRemovalPPOnAA + process.hltFullIter1MaskedMeasurementTrackerEventPPOnAA + process.hltFullIter1PixelQuadrupletsPPOnAA + process.hltFullIter1PixelTrackingRegionsPPOnAA + process.hltFullIter1PixelClusterCheckPPOnAA + process.hltFullIter1PixelHitDoubletsPPOnAA + process.hltFullIter1PixelHitQuadrupletsPPOnAA + process.hltFullIter1PixelSeedsPPOnAA + process.hltFullIter1CkfTrackCandidatesPPOnAA + process.hltFullIter1CtfWithMaterialTracksPPOnAA + process.hltFullIter1TrackMVAClassifierPPOnAA + process.hltFullIter1HighPurityTracksPPOnAA )
process.HLTFullIterativeTrackingIteration2PPOnAA = cms.Sequence( process.hltFullIter2ClustersRefRemovalPPOnAA + process.hltFullIter2MaskedMeasurementTrackerEventPPOnAA + process.hltFullIter2PixelTripletsPPOnAA + process.hltFullIter2PixelTrackingRegionsPPOnAA + process.hltFullIter2PixelClusterCheckPPOnAA + process.hltFullIter2PixelHitDoubletsPPOnAA + process.hltFullIter2PixelHitTripletsPPOnAA + process.hltFullIter2PixelSeedsPPOnAA + process.hltFullIter2CkfTrackCandidatesPPOnAA + process.hltFullIter2CtfWithMaterialTracksPPOnAA + process.hltFullIter2TrackMVAClassifierPPOnAA + process.hltFullIter2HighPurityTracksPPOnAA )
process.HLTFullIterativeTrackingIteration3PPOnAA = cms.Sequence( process.hltFullIter3ClustersRefRemovalPPOnAA + process.hltFullIter3MaskedMeasurementTrackerEventPPOnAA + process.hltFullIter3PixelTripletsPPOnAA + process.hltFullIter3PixelTrackingRegionsPPOnAA + process.hltFullIter3PixelClusterCheckPPOnAA + process.hltFullIter3PixelHitDoubletsPPOnAA + process.hltFullIter3PixelHitTripletsPPOnAA + process.hltFullIter3PixelSeedsPPOnAA + process.hltFullIter3CkfTrackCandidatesPPOnAA + process.hltFullIter3CtfWithMaterialTracksPPOnAA + process.hltFullIter3TrackMVAClassifierPPOnAA + process.hltFullIter3HighPurityTracksPPOnAA )
process.HLTFullIterativeTrackingIteration4PPOnAA = cms.Sequence( process.hltFullIter4ClustersRefRemovalPPOnAA + process.hltFullIter4MaskedMeasurementTrackerEventPPOnAA + process.hltFullIter4PixelQuadrupletsPPOnAA + process.hltFullIter4PixelTrackingRegionsPPOnAA + process.hltFullIter4PixelClusterCheckPPOnAA + process.hltFullIter4PixelHitDoubletsPPOnAA + process.hltFullIter4PixelHitQuadrupletsPPOnAA + process.hltFullIter4PixelSeedsPPOnAA + process.hltFullIter4CkfTrackCandidatesPPOnAA + process.hltFullIter4CtfWithMaterialTracksPPOnAA + process.hltFullIter4TrackMVAClassifierPPOnAA + process.hltFullIter4HighPurityTracksPPOnAA )
process.HLTFullIterativeTrackingIteration5PPOnAA = cms.Sequence( process.hltFullIter5ClustersRefRemovalPPOnAA + process.hltFullIter5MaskedMeasurementTrackerEventPPOnAA + process.hltFullIter5PixelTripletsPPOnAA + process.hltFullIter5PixelTrackingRegionsPPOnAA + process.hltFullIter5PixelClusterCheckPPOnAA + process.hltFullIter5PixelHitDoubletsPPOnAA + process.hltFullIter5PixelHitTripletsPPOnAA + process.hltFullIter5PixelSeedsPPOnAA + process.hltFullIter5CkfTrackCandidatesPPOnAA + process.hltFullIter5CtfWithMaterialTracksPPOnAA + process.hltFullIter5TrackMVAClassifierPPOnAA + process.hltFullIter5HighPurityTracksPPOnAA )
process.HLTFullIterativeTrackingIteration6PPOnAA = cms.Sequence( process.hltFullIter6ClustersRefRemovalPPOnAA + process.hltFullIter6MaskedMeasurementTrackerEventPPOnAA + process.hltFullIter6PixelPairsAPPOnAA + process.hltFullIter6PixelTrackingRegionsAPPOnAA + process.hltFullIter6PixelClusterCheckPPOnAA + process.hltFullIter6PixelHitDoubletsAPPOnAA + process.hltFullIter6PixelSeedsAPPOnAA + process.hltFullIter6PixelPairsBPPOnAA + process.hltFullIter6PixelTrackingRegionsBPPOnAA + process.hltFullIter6PixelHitDoubletsBPPOnAA + process.hltFullIter6PixelSeedsBPPOnAA + process.hltFullIter6PixelSeedsPPOnAA + process.hltFullIter6CkfTrackCandidatesPPOnAA + process.hltFullIter6CtfWithMaterialTracksPPOnAA + process.hltFullIter6TrackMVAClassifierPPOnAA + process.hltFullIter6HighPurityTracksPPOnAA )
process.HLTFullIterativeTrackingIteration7PPOnAA = cms.Sequence( process.hltFullIter7ClustersRefRemovalPPOnAA + process.hltFullIter7MaskedMeasurementTrackerEventPPOnAA + process.hltFullIter7MixedLayersAPPOnAA + process.hltFullIter7MixedTrackingRegionsAPPOnAA + process.hltFullIter7MixedClusterCheckPPOnAA + process.hltFullIter7MixedHitDoubletsAPPOnAA + process.hltFullIter7MixedHitTripletsAPPOnAA + process.hltFullIter7MixedSeedsAPPOnAA + process.hltFullIter7MixedLayersBPPOnAA + process.hltFullIter7MixedTrackingRegionsBPPOnAA + process.hltFullIter7MixedHitDoubletsBPPOnAA + process.hltFullIter7MixedHitTripletsBPPOnAA + process.hltFullIter7MixedSeedsBPPOnAA + process.hltFullIter7MixedSeedsPPOnAA + process.hltFullIter7CkfTrackCandidatesPPOnAA + process.hltFullIter7CtfWithMaterialTracksPPOnAA + process.hltFullIter7TrackMVAClassifierPPOnAA + process.hltFullIter7HighPurityTracksPPOnAA )
process.HLTFullIterativeTrackingIteration8PPOnAA = cms.Sequence( process.hltFullIter8ClustersRefRemovalPPOnAA + process.hltFullIter8MaskedMeasurementTrackerEventPPOnAA + process.hltFullIter8PixelLessLayersPPOnAA + process.hltFullIter8PixelLessTrackingRegionsPPOnAA + process.hltFullIter8PixelLessClusterCheckPPOnAA + process.hltFullIter8PixelLessHitDoubletsPPOnAA + process.hltFullIter8PixelLessHitTripletsPPOnAA + process.hltFullIter8PixelLessSeedsPPOnAA + process.hltFullIter8CkfTrackCandidatesPPOnAA + process.hltFullIter8CtfWithMaterialTracksPPOnAA + process.hltFullIter8TrackMVAClassifierPPOnAA + process.hltFullIter8HighPurityTracksPPOnAA )
process.HLTFullIterativeTrackingIteration9PPOnAA = cms.Sequence( process.hltFullIter9ClustersRefRemovalPPOnAA + process.hltFullIter9MaskedMeasurementTrackerEventPPOnAA + process.hltFullIter9TobTecLayersTriplPPOnAA + process.hltFullIter9TobTecTrackingRegionsTriplPPOnAA + process.hltFullIter9TobTecClusterCheckPPOnAA + process.hltFullIter9TobTecHitDoubletsTriplPPOnAA + process.hltFullIter9TobTecHitTripletsTriplPPOnAA + process.hltFullIter9TobTecSeedsTriplPPOnAA + process.hltFullIter9TobTecLayersPairPPOnAA + process.hltFullIter9TobTecTrackingRegionsPairPPOnAA + process.hltFullIter9TobTecHitDoubletsPairPPOnAA + process.hltFullIter9TobTecSeedsPairPPOnAA + process.hltFullIter9TobTecSeedsPPOnAA + process.hltFullIter9CkfTrackCandidatesPPOnAA + process.hltFullIter9CtfWithMaterialTracksPPOnAA + process.hltFullIter9TrackMVAClassifierPPOnAA )
process.HLTFullIterativeTrackingIteration10PPOnAA = cms.Sequence( process.hltFirstStepGoodPrimaryVerticesPPOnAA + process.hltFullIter10JetCoreLayersPPOnAA + process.hltFullIter10JetCoreTrackingRegionsPPOnAA + process.hltFullIter10JetCoreClusterCheckPPOnAA + process.hltFullIter10JetCoreHitDoubletsPPOnAA + process.hltFullIter10JetCoreSeedsPPOnAA + process.hltFullIter10CkfTrackCandidatesPPOnAA + process.hltFullIter10CtfWithMaterialTracksPPOnAA + process.hltFullIter10TrackMVAClassifierPPOnAA )
process.HLTFullIterativeTrackingPPOnAA = cms.Sequence( process.HLTFullIterativeTrackingIteration0PPOnAA + process.HLTFullIterativeTrackingIteration1PPOnAA + process.HLTFullIterativeTrackingIteration2PPOnAA + process.HLTFullIterativeTrackingIteration3PPOnAA + process.HLTFullIterativeTrackingIteration4PPOnAA + process.HLTFullIterativeTrackingIteration5PPOnAA + process.HLTFullIterativeTrackingIteration6PPOnAA + process.HLTFullIterativeTrackingIteration7PPOnAA + process.HLTFullIterativeTrackingIteration8PPOnAA + process.HLTFullIterativeTrackingIteration9PPOnAA + process.HLTFullIterativeTrackingIteration10PPOnAA + process.hltFullIterativeTrackingMergedPPOnAA )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )

process.HLT_HIFullTracks2018_HighPt8_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIFullTracks2018HighPt8 + process.HLTPixelClusterSplittingPPOnAA + process.HLTFullIterativeTrackingPPOnAA + process.hltFullOnlinePrimaryVerticesPPOnAA + process.hltGoodHighPurityFullTrackCutClassifierForHighPt + process.hltGoodHighPurityFullTracksForHighPt + process.hltFullCandsForHighPtTrigger + process.hltFullTrackHighPt8 + process.HLTEndSequence )


process.HLTSchedule = cms.Schedule( (process.HLT_HIFullTracks2018_HighPt8_v1 ))


process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        'root://xrootd.cmsaf.mit.edu//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/898/00000/A0E925FB-89AF-E711-8C82-02163E0144E9.root',
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

# run the Full L1T emulator, then repack the data into a new RAW collection, to be used by the HLT
from HLTrigger.Configuration.CustomConfigs import L1REPACK
process = L1REPACK(process,"Full")

# avoid PrescaleService error due to missing HLT paths
if 'PrescaleService' in process.__dict__:
    for pset in reversed(process.PrescaleService.prescaleTable):
        if not hasattr(process,pset.pathName.value()):
            process.PrescaleService.prescaleTable.remove(pset)

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 100 )
)

# enable TrigReport, TimeReport and MultiThreading
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    numberOfThreads = cms.untracked.uint32( 4 ),
    numberOfStreams = cms.untracked.uint32( 0 ),
    sizeOfStackForThreadsInKB = cms.untracked.uint32( 10*1024 )
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = '100X_dataRun2_v1')

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('L1TGlobalSummary')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')

# load the DQMStore and DQMRootOutputModule
process.load( "DQMServices.Core.DQMStore_cfi" )
process.DQMStore.enableMultiThread = True

process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("DQMIO.root")
)

process.DQMOutput = cms.EndPath( process.dqmOutput )

# add specific customizations
_customInfo = {}
_customInfo['menuType'  ]= "GRun"
_customInfo['globalTags']= {}
_customInfo['globalTags'][True ] = "auto:run2_hlt_GRun"
_customInfo['globalTags'][False] = "auto:run2_mc_GRun"
_customInfo['inputFiles']={}
_customInfo['inputFiles'][True]  = "file:RelVal_Raw_GRun_DATA.root"
_customInfo['inputFiles'][False] = "file:RelVal_Raw_GRun_MC.root"
_customInfo['maxEvents' ]=  100
_customInfo['globalTag' ]= "100X_dataRun2_v1"
_customInfo['inputFile' ]=  ['root://xrootd.cmsaf.mit.edu//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/898/00000/A0E925FB-89AF-E711-8C82-02163E0144E9.root']
_customInfo['realData'  ]=  True
from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
process = customizeHLTforAll(process,"GRun",_customInfo)

from HLTrigger.Configuration.customizeHLTforCMSSW import customizeHLTforCMSSW
process = customizeHLTforCMSSW(process,"GRun")

# Eras-based customisations
from HLTrigger.Configuration.Eras import modifyHLTforEras
modifyHLTforEras(process)

#User-defined customization functions
from FWCore.ParameterSet.MassReplace import massReplaceInputTag
process = massReplaceInputTag(process)

