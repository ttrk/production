# hltGetConfiguration /users/katatar/HI2018PbPb/hltTestHighPt/V4 --globaltag 103X_upgrade2018_realistic_HI_v6 --input /store/user/mnguyen/AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8_5020GeV_DIGI2RAW_103X_upgrade2018_realistic_HI_v4/Pythia8_AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8/crab_AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8_5020GeV_DIGI2RAW_103X_upgrade2018_realistic_HI_v4/181013_203555/0000/step1_private_DIGI_L1_DIGI2RAW_HLT_PU_99.root --setup /dev/CMSSW_10_3_0/GRun --process MyHLT --full --offline --mc --unprescale --l1-emulator FullMC --l1Xml L1Menu_CollisionsHeavyIons2018_v4.xml --customise L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_4 --max-events 100

# /users/katatar/HI2018PbPb/hltTestHighPt/V4 (CMSSW_10_3_0_pre6)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "MyHLT" )
process.load("setup_dev_CMSSW_10_3_0_GRun_cff")

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/katatar/HI2018PbPb/hltTestHighPt/V4')
)

process.ThroughputService = cms.Service( "ThroughputService",
    dqmPath = cms.untracked.string( "HLT/Throughput" ),
    timeRange = cms.untracked.double( 60000.0 ),
    dqmPathByProcesses = cms.untracked.bool( False ),
    timeResolution = cms.untracked.double( 5.828 )
)
process.MessageLogger = cms.Service( "MessageLogger",
    suppressInfo = cms.untracked.vstring(  ),
    debugs = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    suppressDebug = cms.untracked.vstring(  ),
    cout = cms.untracked.PSet(  placeholder = cms.untracked.bool( True ) ),
    cerr_stats = cms.untracked.PSet( 
      threshold = cms.untracked.string( "WARNING" ),
      output = cms.untracked.string( "cerr" ),
      optionalPSet = cms.untracked.bool( True )
    ),
    warnings = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    statistics = cms.untracked.vstring( 'cerr' ),
    cerr = cms.untracked.PSet( 
      INFO = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      noTimeStamps = cms.untracked.bool( False ),
      FwkReport = cms.untracked.PSet( 
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 0 )
      ),
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkSummary = cms.untracked.PSet( 
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 10000000 )
      ),
      threshold = cms.untracked.string( "INFO" ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    FrameworkJobReport = cms.untracked.PSet( 
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) )
    ),
    suppressWarning = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltCtf3HitL1SeededWithMaterialTracks',
      'hltL3MuonsOIState',
      'hltPixelTracksForHighMult',
      'hltHITPixelTracksHE',
      'hltHITPixelTracksHB',
      'hltCtfL1SeededWithMaterialTracks',
      'hltRegionalTracksForL3MuonIsolation',
      'hltSiPixelClusters',
      'hltActivityStartUpElectronPixelSeeds',
      'hltLightPFTracks',
      'hltPixelVertices3DbbPhi',
      'hltL3MuonsIOHit',
      'hltPixelTracks',
      'hltSiPixelDigis',
      'hltL3MuonsOIHit',
      'hltL1SeededElectronGsfTracks',
      'hltL1SeededStartUpElectronPixelSeeds',
      'hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV',
      'hltCtfActivityWithMaterialTracks' ),
    errors = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    fwkJobReports = cms.untracked.vstring( 'FrameworkJobReport' ),
    debugModules = cms.untracked.vstring(  ),
    infos = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    categories = cms.untracked.vstring( 'FwkJob',
      'FwkReport',
      'FwkSummary',
      'Root_NoDictionary' ),
    destinations = cms.untracked.vstring( 'warnings',
      'errors',
      'infos',
      'debugs',
      'cout',
      'cerr' ),
    threshold = cms.untracked.string( "INFO" ),
    suppressError = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltL3MuonCandidates',
      'hltL3TkTracksFromL2OIState',
      'hltPFJetCtfWithMaterialTracks',
      'hltL3TkTracksFromL2IOHit',
      'hltL3TkTracksFromL2OIHit' )
)
process.FastTimerService = cms.Service( "FastTimerService",
    dqmPath = cms.untracked.string( "HLT/TimerService" ),
    dqmModuleTimeRange = cms.untracked.double( 40.0 ),
    enableDQMbyPath = cms.untracked.bool( False ),
    dqmModuleTimeResolution = cms.untracked.double( 0.2 ),
    dqmPathMemoryResolution = cms.untracked.double( 5000.0 ),
    enableDQM = cms.untracked.bool( True ),
    enableDQMbyModule = cms.untracked.bool( False ),
    dqmModuleMemoryRange = cms.untracked.double( 100000.0 ),
    dqmMemoryResolution = cms.untracked.double( 5000.0 ),
    enableDQMbyLumiSection = cms.untracked.bool( True ),
    dqmPathTimeResolution = cms.untracked.double( 0.5 ),
    printEventSummary = cms.untracked.bool( False ),
    dqmPathTimeRange = cms.untracked.double( 100.0 ),
    dqmTimeRange = cms.untracked.double( 2000.0 ),
    enableDQMTransitions = cms.untracked.bool( False ),
    dqmLumiSectionsRange = cms.untracked.uint32( 2500 ),
    dqmPathMemoryRange = cms.untracked.double( 1000000.0 ),
    dqmMemoryRange = cms.untracked.double( 1000000.0 ),
    dqmTimeResolution = cms.untracked.double( 5.0 ),
    printRunSummary = cms.untracked.bool( True ),
    dqmModuleMemoryResolution = cms.untracked.double( 500.0 ),
    printJobSummary = cms.untracked.bool( True ),
    enableDQMbyProcesses = cms.untracked.bool( True )
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
    lenAMCTrailer = cms.untracked.int32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1404 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    DmxFWId = cms.uint32( 0 ),
    FWOverride = cms.bool( False )
)
process.hltPreHLTAnalyzerEndpath = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1TGlobalSummary = cms.EDAnalyzer( "L1TGlobalSummary",
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    MaxBx = cms.int32( 0 ),
    DumpRecord = cms.bool( False ),
    psFileName = cms.string( "prescale_L1TGlobal.csv" ),
    ReadPrescalesFromFile = cms.bool( False ),
    AlgInputTag = cms.InputTag( "hltGtStage2Digis" ),
    MinBx = cms.int32( 0 ),
    psColumn = cms.int32( 0 ),
    DumpTrigResults = cms.bool( False ),
    DumpTrigSummary = cms.bool( True )
)
process.hltTrigReport = cms.EDAnalyzer( "HLTrigReport",
    ReferencePath = cms.untracked.string( "HLTriggerFinalPath" ),
    ReferenceRate = cms.untracked.double( 100.0 ),
    serviceBy = cms.untracked.string( "never" ),
    resetBy = cms.untracked.string( "never" ),
    reportBy = cms.untracked.string( "job" ),
    HLTriggerResults = cms.InputTag( 'TriggerResults','','@currentProcess' )
)
process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtStage2ObjectMap = cms.EDProducer( "L1TGlobalProducer",
    L1DataBxInEvent = cms.int32( 5 ),
    JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    AlgorithmTriggersUnmasked = cms.bool( True ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    PrintL1Menu = cms.untracked.bool( False ),
    PrescaleCSVFile = cms.string( "prescale_L1TGlobal.csv" ),
    Verbosity = cms.untracked.int32( 0 ),
    AlgoBlkInputTag = cms.InputTag( "hltGtStage2Digis" ),
    EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    ProduceL1GtDaqRecord = cms.bool( True ),
    PrescaleSet = cms.uint32( 1 ),
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    TriggerMenuLuminosity = cms.string( "startup" ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    GetPrescaleColumnFromData = cms.bool( False ),
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
process.hltL1sMinimumBiasHF1ANDBptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_MinimumBiasHF1_AND_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIGEDPhoton10 = cms.EDFilter( "HLTPrescaler",
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
process.hltEcalPreshowerDigis = cms.EDProducer( "ESRawToDigi",
    sourceTag = cms.InputTag( "rawDataCollector" ),
    debugMode = cms.untracked.bool( False ),
    InstanceES = cms.string( "" ),
    ESdigiCollection = cms.string( "" ),
    LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" )
)
process.hltEcalUncalibRecHit = cms.EDProducer( "EcalUncalibRecHitProducer",
    EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    EBhitCollection = cms.string( "EcalUncalibRecHitsEB" ),
    algo = cms.string( "EcalUncalibRecHitWorkerMultiFit" ),
    algoPSet = cms.PSet( 
      ebSpikeThreshold = cms.double( 1.042 ),
      EBtimeFitLimits_Upper = cms.double( 1.4 ),
      EEtimeFitLimits_Lower = cms.double( 0.2 ),
      timealgo = cms.string( "None" ),
      EBtimeNconst = cms.double( 28.5 ),
      prefitMaxChiSqEE = cms.double( 10.0 ),
      outOfTimeThresholdGain12mEB = cms.double( 5.0 ),
      outOfTimeThresholdGain12mEE = cms.double( 1000.0 ),
      EEtimeFitParameters = cms.vdouble( -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 140.7432, -75.41106, 16.20277 ),
      prefitMaxChiSqEB = cms.double( 25.0 ),
      simplifiedNoiseModelForGainSwitch = cms.bool( True ),
      EBtimeFitParameters = cms.vdouble( -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 91.01147, -50.35761, 11.05621 ),
      selectiveBadSampleCriteriaEB = cms.bool( False ),
      dynamicPedestalsEB = cms.bool( False ),
      useLumiInfoRunHeader = cms.bool( False ),
      EBamplitudeFitParameters = cms.vdouble( 1.138, 1.652 ),
      doPrefitEE = cms.bool( False ),
      dynamicPedestalsEE = cms.bool( False ),
      selectiveBadSampleCriteriaEE = cms.bool( False ),
      outOfTimeThresholdGain61pEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain61pEB = cms.double( 5.0 ),
      activeBXs = cms.vint32( -5, -4, -3, -2, -1, 0, 1, 2, 3, 4 ),
      EcalPulseShapeParameters = cms.PSet( 
        EEPulseShapeTemplate = cms.vdouble( 0.116442, 0.756246, 1.0, 0.897182, 0.686831, 0.491506, 0.344111, 0.245731, 0.174115, 0.123361, 0.0874288, 0.061957 ),
        EEdigiCollection = cms.string( "" ),
        EcalPreMixStage2 = cms.bool( False ),
        EcalPreMixStage1 = cms.bool( False ),
        EBPulseShapeCovariance = cms.vdouble( 3.001E-6, 1.233E-5, 0.0, -4.416E-6, -4.571E-6, -3.614E-6, -2.636E-6, -1.286E-6, -8.41E-7, -5.296E-7, 0.0, 0.0, 1.233E-5, 6.154E-5, 0.0, -2.2E-5, -2.309E-5, -1.838E-5, -1.373E-5, -7.334E-6, -5.088E-6, -3.745E-6, -2.428E-6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -4.416E-6, -2.2E-5, 0.0, 8.319E-6, 8.545E-6, 6.792E-6, 5.059E-6, 2.678E-6, 1.816E-6, 1.223E-6, 8.245E-7, 5.589E-7, -4.571E-6, -2.309E-5, 0.0, 8.545E-6, 9.182E-6, 7.219E-6, 5.388E-6, 2.853E-6, 1.944E-6, 1.324E-6, 9.083E-7, 6.335E-7, -3.614E-6, -1.838E-5, 0.0, 6.792E-6, 7.219E-6, 6.016E-6, 4.437E-6, 2.385E-6, 1.636E-6, 1.118E-6, 7.754E-7, 5.556E-7, -2.636E-6, -1.373E-5, 0.0, 5.059E-6, 5.388E-6, 4.437E-6, 3.602E-6, 1.917E-6, 1.322E-6, 9.079E-7, 6.529E-7, 4.752E-7, -1.286E-6, -7.334E-6, 0.0, 2.678E-6, 2.853E-6, 2.385E-6, 1.917E-6, 1.375E-6, 9.1E-7, 6.455E-7, 4.693E-7, 3.657E-7, -8.41E-7, -5.088E-6, 0.0, 1.816E-6, 1.944E-6, 1.636E-6, 1.322E-6, 9.1E-7, 9.115E-7, 6.062E-7, 4.436E-7, 3.422E-7, -5.296E-7, -3.745E-6, 0.0, 1.223E-6, 1.324E-6, 1.118E-6, 9.079E-7, 6.455E-7, 6.062E-7, 7.217E-7, 4.862E-7, 3.768E-7, 0.0, -2.428E-6, 0.0, 8.245E-7, 9.083E-7, 7.754E-7, 6.529E-7, 4.693E-7, 4.436E-7, 4.862E-7, 6.509E-7, 4.418E-7, 0.0, 0.0, 0.0, 5.589E-7, 6.335E-7, 5.556E-7, 4.752E-7, 3.657E-7, 3.422E-7, 3.768E-7, 4.418E-7, 6.142E-7 ),
        ESdigiCollection = cms.string( "" ),
        EBdigiCollection = cms.string( "" ),
        EBCorrNoiseMatrixG01 = cms.vdouble( 1.0, 0.73354, 0.64442, 0.58851, 0.55425, 0.53082, 0.51916, 0.51097, 0.50732, 0.50409 ),
        EBCorrNoiseMatrixG12 = cms.vdouble( 1.0, 0.71073, 0.55721, 0.46089, 0.40449, 0.35931, 0.33924, 0.32439, 0.31581, 0.30481 ),
        EBCorrNoiseMatrixG06 = cms.vdouble( 1.0, 0.70946, 0.58021, 0.49846, 0.45006, 0.41366, 0.39699, 0.38478, 0.37847, 0.37055 ),
        EEPulseShapeCovariance = cms.vdouble( 3.941E-5, 3.333E-5, 0.0, -1.449E-5, -1.661E-5, -1.424E-5, -1.183E-5, -6.842E-6, -4.915E-6, -3.411E-6, 0.0, 0.0, 3.333E-5, 2.862E-5, 0.0, -1.244E-5, -1.431E-5, -1.233E-5, -1.032E-5, -5.883E-6, -4.154E-6, -2.902E-6, -2.128E-6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.449E-5, -1.244E-5, 0.0, 5.84E-6, 6.649E-6, 5.72E-6, 4.812E-6, 2.708E-6, 1.869E-6, 1.33E-6, 9.186E-7, 6.446E-7, -1.661E-5, -1.431E-5, 0.0, 6.649E-6, 7.966E-6, 6.898E-6, 5.794E-6, 3.157E-6, 2.184E-6, 1.567E-6, 1.084E-6, 7.575E-7, -1.424E-5, -1.233E-5, 0.0, 5.72E-6, 6.898E-6, 6.341E-6, 5.347E-6, 2.859E-6, 1.991E-6, 1.431E-6, 9.839E-7, 6.886E-7, -1.183E-5, -1.032E-5, 0.0, 4.812E-6, 5.794E-6, 5.347E-6, 4.854E-6, 2.628E-6, 1.809E-6, 1.289E-6, 9.02E-7, 6.146E-7, -6.842E-6, -5.883E-6, 0.0, 2.708E-6, 3.157E-6, 2.859E-6, 2.628E-6, 1.863E-6, 1.296E-6, 8.882E-7, 6.108E-7, 4.283E-7, -4.915E-6, -4.154E-6, 0.0, 1.869E-6, 2.184E-6, 1.991E-6, 1.809E-6, 1.296E-6, 1.217E-6, 8.669E-7, 5.751E-7, 3.882E-7, -3.411E-6, -2.902E-6, 0.0, 1.33E-6, 1.567E-6, 1.431E-6, 1.289E-6, 8.882E-7, 8.669E-7, 9.522E-7, 6.717E-7, 4.293E-7, 0.0, -2.128E-6, 0.0, 9.186E-7, 1.084E-6, 9.839E-7, 9.02E-7, 6.108E-7, 5.751E-7, 6.717E-7, 7.911E-7, 5.493E-7, 0.0, 0.0, 0.0, 6.446E-7, 7.575E-7, 6.886E-7, 6.146E-7, 4.283E-7, 3.882E-7, 4.293E-7, 5.493E-7, 7.027E-7 ),
        EBPulseShapeTemplate = cms.vdouble( 0.0113979, 0.758151, 1.0, 0.887744, 0.673548, 0.474332, 0.319561, 0.215144, 0.147464, 0.101087, 0.0693181, 0.0475044 ),
        EECorrNoiseMatrixG01 = cms.vdouble( 1.0, 0.72698, 0.62048, 0.55691, 0.51848, 0.49147, 0.47813, 0.47007, 0.46621, 0.46265 ),
        EECorrNoiseMatrixG12 = cms.vdouble( 1.0, 0.71373, 0.44825, 0.30152, 0.21609, 0.14786, 0.11772, 0.10165, 0.09465, 0.08098 ),
        UseLCcorrection = cms.untracked.bool( True ),
        EECorrNoiseMatrixG06 = cms.vdouble( 1.0, 0.71217, 0.47464, 0.34056, 0.26282, 0.20287, 0.17734, 0.16256, 0.15618, 0.14443 )
      ),
      doPrefitEB = cms.bool( False ),
      addPedestalUncertaintyEE = cms.double( 0.0 ),
      addPedestalUncertaintyEB = cms.double( 0.0 ),
      gainSwitchUseMaxSampleEB = cms.bool( True ),
      EEtimeNconst = cms.double( 31.8 ),
      EEamplitudeFitParameters = cms.vdouble( 1.89, 1.4 ),
      chi2ThreshEE_ = cms.double( 50.0 ),
      eePulseShape = cms.vdouble( 5.2E-5, -5.26E-5, 6.66E-5, 0.1168, 0.7575, 1.0, 0.8876, 0.6732, 0.4741, 0.3194 ),
      outOfTimeThresholdGain12pEB = cms.double( 5.0 ),
      gainSwitchUseMaxSampleEE = cms.bool( False ),
      mitigateBadSamplesEB = cms.bool( False ),
      outOfTimeThresholdGain12pEE = cms.double( 1000.0 ),
      ebPulseShape = cms.vdouble( 5.2E-5, -5.26E-5, 6.66E-5, 0.1168, 0.7575, 1.0, 0.8876, 0.6732, 0.4741, 0.3194 ),
      ampErrorCalculation = cms.bool( False ),
      mitigateBadSamplesEE = cms.bool( False ),
      amplitudeThresholdEB = cms.double( 10.0 ),
      kPoorRecoFlagEB = cms.bool( True ),
      amplitudeThresholdEE = cms.double( 10.0 ),
      EBtimeFitLimits_Lower = cms.double( 0.2 ),
      kPoorRecoFlagEE = cms.bool( False ),
      EEtimeFitLimits_Upper = cms.double( 1.4 ),
      outOfTimeThresholdGain61mEE = cms.double( 1000.0 ),
      EEtimeConstantTerm = cms.double( 1.0 ),
      EBtimeConstantTerm = cms.double( 0.6 ),
      chi2ThreshEB_ = cms.double( 65.0 ),
      outOfTimeThresholdGain61mEB = cms.double( 5.0 )
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
      kDead = cms.vstring( 'kNoDataNoTP' ),
      kGood = cms.vstring( 'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy' ),
      kTowerRecovered = cms.vstring( 'kDeadFE' ),
      kNoisy = cms.vstring( 'kNNoisy',
        'kFixedG6',
        'kFixedG1' ),
      kNeighboursRecovered = cms.vstring( 'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE' )
    ),
    EBuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    skipTimeCalib = cms.bool( True ),
    algoRecover = cms.string( "EcalRecHitWorkerRecover" ),
    eeFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeFE' ),
    cleaningConfig = cms.PSet( 
      cThreshold_endcap = cms.double( 15.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e6e2thresh = cms.double( 0.04 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      cThreshold_double = cms.double( 10.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 )
    ),
    logWarningEtThreshold_EB_FE = cms.double( 50.0 ),
    logWarningEtThreshold_EE_FE = cms.double( 50.0 )
)
process.hltEcalPreshowerRecHit = cms.EDProducer( "ESRecHitProducer",
    ESRecoAlgo = cms.int32( 0 ),
    ESrechitCollection = cms.string( "EcalRecHitsES" ),
    algo = cms.string( "ESRecHitWorker" ),
    ESdigiCollection = cms.InputTag( "hltEcalPreshowerDigis" )
)
process.hltParticleFlowRecHitECALPPOnAA = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        srFlags = cms.InputTag( "" ),
        name = cms.string( "PFEBRecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  name = cms.string( "PFRecHitQTestDBThreshold" ),
            applySelectionsToAllCrystals = cms.bool( True )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        )
      ),
      cms.PSet(  src = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        srFlags = cms.InputTag( "" ),
        name = cms.string( "PFEERecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  name = cms.string( "PFRecHitQTestDBThreshold" ),
            applySelectionsToAllCrystals = cms.bool( True )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        )
      )
    ),
    navigator = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitECALNavigator" )
    )
)
process.hltParticleFlowRecHitPSPPOnAA = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltEcalPreshowerRecHit','EcalRecHitsES' ),
        name = cms.string( "PFPSRecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 7.0E-6 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          )
        )
      )
    ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitPreshowerNavigator" ) )
)
process.hltParticleFlowClusterPSPPOnAA = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 6.0E-5 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 50 ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS2" )
        )
      ),
      showerSigma = cms.double( 0.3 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( False )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 4 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitPSPPOnAA" )
)
process.hltParticleFlowClusterECALUncorrectedPPOnAA = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 9 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet( 
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet( 
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      maxIterations = cms.uint32( 50 ),
      positionCalcForConvergence = cms.PSet( 
        minAllowedNormalization = cms.double( 0.0 ),
        T0_ES = cms.double( 1.2 ),
        algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
        T0_EE = cms.double( 3.1 ),
        T0_EB = cms.double( 7.4 ),
        X0 = cms.double( 0.89 ),
        minFractionInCalc = cms.double( 0.0 ),
        W0 = cms.double( 4.2 )
      ),
      allCellsPositionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet( 
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet( 
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  recHitEnergyNorm = cms.double( 0.08 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 0.3 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      showerSigma = cms.double( 1.5 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet( 
      minAllowedNormalization = cms.double( 0.0 ),
      T0_ES = cms.double( 1.2 ),
      algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
      T0_EE = cms.double( 3.1 ),
      T0_EB = cms.double( 7.4 ),
      X0 = cms.double( 0.89 ),
      minFractionInCalc = cms.double( 0.0 ),
      W0 = cms.double( 4.2 )
    ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.08 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.3 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( True )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThresholdPt = cms.double( 0.15 ),
          seedingThreshold = cms.double( 0.6 ),
          detector = cms.string( "ECAL_ENDCAP" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 0.23 ),
          detector = cms.string( "ECAL_BARREL" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 8 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitECALPPOnAA" )
)
process.hltParticleFlowClusterECALPPOnAA = cms.EDProducer( "CorrectedECALPFClusterProducer",
    inputPS = cms.InputTag( "hltParticleFlowClusterPSPPOnAA" ),
    minimumPSEnergy = cms.double( 0.0 ),
    energyCorrector = cms.PSet( 
      algoName = cms.string( "PFClusterEMEnergyCorrector" ),
      applyCrackCorrections = cms.bool( False )
    ),
    inputECAL = cms.InputTag( "hltParticleFlowClusterECALUncorrectedPPOnAA" )
)
process.hltParticleFlowSuperClusterECALPPOnAA = cms.EDProducer( "PFECALSuperClusterProducer",
    PFSuperClusterCollectionEndcap = cms.string( "hltParticleFlowSuperClusterECALEndcap" ),
    doSatelliteClusterMerge = cms.bool( False ),
    BeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PFBasicClusterCollectionBarrel = cms.string( "hltParticleFlowBasicClusterECALBarrel" ),
    useRegression = cms.bool( True ),
    satelliteMajorityFraction = cms.double( 0.5 ),
    isOOTCollection = cms.bool( False ),
    thresh_PFClusterEndcap = cms.double( 0.5 ),
    ESAssociation = cms.InputTag( "hltParticleFlowClusterECALPPOnAA" ),
    PFBasicClusterCollectionPreshower = cms.string( "hltParticleFlowBasicClusterECALPreshower" ),
    use_preshower = cms.bool( True ),
    thresh_PFClusterBarrel = cms.double( 0.5 ),
    thresh_SCEt = cms.double( 4.0 ),
    etawidth_SuperClusterEndcap = cms.double( 0.04 ),
    phiwidth_SuperClusterEndcap = cms.double( 0.6 ),
    verbose = cms.untracked.bool( False ),
    useDynamicDPhiWindow = cms.bool( True ),
    PFSuperClusterCollectionBarrel = cms.string( "hltParticleFlowSuperClusterECALBarrel" ),
    regressionConfig = cms.PSet( 
      uncertaintyKeyEB = cms.string( "pfscecal_EBUncertainty_online" ),
      ecalRecHitsEE = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
      ecalRecHitsEB = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      regressionKeyEE = cms.string( "pfscecal_EECorrection_online" ),
      regressionKeyEB = cms.string( "pfscecal_EBCorrection_online" ),
      uncertaintyKeyEE = cms.string( "pfscecal_EEUncertainty_online" ),
      isHLT = cms.bool( True )
    ),
    applyCrackCorrections = cms.bool( False ),
    satelliteClusterSeedThreshold = cms.double( 50.0 ),
    endcapRecHits = cms.InputTag( 'ecalRecHit','EcalRecHitsEB' ),
    etawidth_SuperClusterBarrel = cms.double( 0.04 ),
    PFBasicClusterCollectionEndcap = cms.string( "hltParticleFlowBasicClusterECALEndcap" ),
    barrelRecHits = cms.InputTag( 'ecalRecHit','EcalRecHitsEE' ),
    thresh_PFClusterSeedBarrel = cms.double( 1.0 ),
    ClusteringType = cms.string( "Mustache" ),
    dropUnseedable = cms.bool( False ),
    EnergyWeight = cms.string( "Raw" ),
    PFClusters = cms.InputTag( "hltParticleFlowClusterECALPPOnAA" ),
    thresh_PFClusterSeedEndcap = cms.double( 1.0 ),
    phiwidth_SuperClusterBarrel = cms.double( 0.6 ),
    thresh_PFClusterES = cms.double( 0.5 ),
    seedThresholdIsET = cms.bool( True ),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string( "hltParticleFlowSuperClusterECALEndcapWithPreshower" )
)
process.hltEgammaCandidatesPPOnAA = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALPPOnAA','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
    scHybridBarrelProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALPPOnAA','hltParticleFlowSuperClusterECALBarrel' ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltEgammaCandidatesWrapperPPOnAA = cms.EDFilter( "HLTEgammaTriggerFilterObjectWrapper",
    doIsolated = cms.bool( True ),
    saveTags = cms.bool( True ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    candNonIsolatedTag = cms.InputTag( "" )
)
process.hltEG10EtPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 10.0 ),
    etcutEB = cms.double( 10.0 ),
    ncandcut = cms.int32( 1 )
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
    missingHcalRescaleFactorForEcal = cms.double( 0.0 ),
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
    HBThreshold1 = cms.double( 0.7 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    HBThreshold2 = cms.double( 0.7 ),
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
    HF2Grid = cms.vdouble(  ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
process.hltEgammaHoverEPPOnAA = cms.EDProducer( "EgammaHLTBcHcalIsolationProducersRegional",
    effectiveAreas = cms.vdouble( 0.105, 0.17 ),
    doRhoCorrection = cms.bool( False ),
    outerCone = cms.double( 0.14 ),
    caloTowerProducer = cms.InputTag( "hltTowerMakerForAll" ),
    innerCone = cms.double( 0.0 ),
    useSingleTower = cms.bool( False ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    depth = cms.int32( -1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    rhoMax = cms.double( 9.9999999E7 ),
    etMin = cms.double( 0.0 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( False )
)
process.hltEG10HoverELoosePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG10EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltSiStripRawToDigi = cms.EDProducer( "SiStripRawToDigiModule",
    UseDaqRegister = cms.bool( False ),
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    MarkModulesOnMissingFeds = cms.bool( True ),
    UnpackCommonModeValues = cms.bool( False ),
    AppendedBytes = cms.int32( 0 ),
    UseFedKey = cms.bool( False ),
    LegacyUnpacker = cms.bool( False ),
    ErrorThreshold = cms.uint32( 7174 ),
    TriggerFedId = cms.int32( 0 ),
    DoAPVEmulatorCheck = cms.bool( False ),
    UnpackBadChannels = cms.bool( False ),
    DoAllCorruptBufferChecks = cms.bool( False )
)
process.hltSiStripZeroSuppression = cms.EDProducer( "SiStripZeroSuppression",
    fixCM = cms.bool( False ),
    produceHybridFormat = cms.bool( False ),
    produceBaselinePoints = cms.bool( False ),
    produceCalculatedBaseline = cms.bool( False ),
    storeInZScollBadAPV = cms.bool( True ),
    Algorithms = cms.PSet( 
      CutToAvoidSignal = cms.double( 2.0 ),
      lastGradient = cms.int32( 10 ),
      slopeY = cms.int32( 4 ),
      slopeX = cms.int32( 3 ),
      PedestalSubtractionFedMode = cms.bool( False ),
      Use10bitsTruncation = cms.bool( False ),
      Fraction = cms.double( 0.2 ),
      minStripsToFit = cms.uint32( 4 ),
      consecThreshold = cms.uint32( 5 ),
      hitStripThreshold = cms.uint32( 40 ),
      Deviation = cms.uint32( 25 ),
      CommonModeNoiseSubtractionMode = cms.string( "IteratedMedian" ),
      filteredBaselineDerivativeSumSquare = cms.double( 30.0 ),
      ApplyBaselineCleaner = cms.bool( True ),
      doAPVRestore = cms.bool( True ),
      TruncateInSuppressor = cms.bool( True ),
      restoreThreshold = cms.double( 0.5 ),
      sizeWindow = cms.int32( 1 ),
      APVInspectMode = cms.string( "BaselineFollower" ),
      ForceNoRestore = cms.bool( False ),
      useRealMeanCM = cms.bool( False ),
      ApplyBaselineRejection = cms.bool( True ),
      DeltaCMThreshold = cms.uint32( 20 ),
      nSigmaNoiseDerTh = cms.uint32( 4 ),
      nSaturatedStrip = cms.uint32( 2 ),
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      useCMMeanMap = cms.bool( False ),
      discontinuityThreshold = cms.int32( 12 ),
      distortionThreshold = cms.uint32( 20 ),
      filteredBaselineMax = cms.double( 6.0 ),
      Iterations = cms.int32( 3 ),
      CleaningSequence = cms.uint32( 1 ),
      nSmooth = cms.uint32( 9 ),
      APVRestoreMode = cms.string( "BaselineFollower" ),
      MeanCM = cms.int32( 0 ),
      widthCluster = cms.int32( 64 )
    ),
    RawDigiProducersList = cms.VInputTag( 'hltSiStripRawToDigi:VirginRaw','hltSiStripRawToDigi:ProcessedRaw','hltSiStripRawToDigi:ScopeMode','hltSiStripRawToDigi:ZeroSuppressed' ),
    storeCM = cms.bool( True ),
    produceRawDigis = cms.bool( True )
)
process.hltSiStripDigiToZSRaw = cms.EDProducer( "SiStripDigiToRawModule",
    CopyBufferHeader = cms.bool( True ),
    UseFedKey = cms.bool( False ),
    PacketCode = cms.string( "ZERO_SUPPRESSED" ),
    RawDataTag = cms.InputTag( "rawDataCollector" ),
    FedReadoutMode = cms.string( "ZERO_SUPPRESSED" ),
    UseWrongDigiType = cms.bool( False ),
    InputDigis = cms.InputTag( 'hltSiStripZeroSuppression','ZeroSuppressed' )
)
process.hltSiStripRawDigiToVirginRaw = cms.EDProducer( "SiStripDigiToRawModule",
    CopyBufferHeader = cms.bool( True ),
    UseFedKey = cms.bool( False ),
    PacketCode = cms.string( "VIRGIN_RAW" ),
    RawDataTag = cms.InputTag( "rawDataCollector" ),
    FedReadoutMode = cms.string( "VIRGIN_RAW" ),
    UseWrongDigiType = cms.bool( False ),
    InputDigis = cms.InputTag( 'hltSiStripRawToDigi','VirginRaw' )
)
process.virginRawDataRepacker = cms.EDProducer( "RawDataCollectorByLabel",
    verbose = cms.untracked.int32( 0 ),
    RawCollectionList = cms.VInputTag( 'hltSiStripRawDigiToVirginRaw' )
)
process.rawDataRepacker = cms.EDProducer( "RawDataCollectorByLabel",
    verbose = cms.untracked.int32( 0 ),
    RawCollectionList = cms.VInputTag( 'hltSiStripDigiToZSRaw','source','rawDataCollector' )
)
process.rawDataReducedFormat = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataRepacker" ),
    fedList = ( cms.vuint32( 100, 101, 102, 1024, 103, 104, 105, 106, 107, 108, 109, 110, 111, 1118, 1119, 112, 1120, 1121, 1122, 1123, 113, 1134, 1135, 114, 115, 116, 117, 118, 119, 120, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 121, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 122, 1220, 1221, 1224, 1225, 1226, 1227, 1228, 1229, 123, 1230, 1231, 1232, 1233, 1236, 1237, 1238, 1239, 124, 1240, 1241, 1242, 1243, 1244, 1245, 1248, 1249, 125, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 126, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 127, 1272, 1273, 1274, 1275, 1276, 1277, 1278, 1279, 128, 1280, 1281, 1284, 1285, 1286, 1287, 1288, 1289, 129, 1290, 1291, 1292, 1293, 1296, 1297, 1298, 1299, 130, 1300, 1301, 1302, 1308, 1309, 131, 1310, 1311, 1312, 1313, 1314, 132, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 133, 1332, 1333, 1334, 1335, 1336, 1337, 1338, 134, 135, 1354, 1356, 1358, 136, 1360, 1368, 1369, 137, 1370, 1371, 1376, 1377, 138, 1380, 1381, 1384, 1385, 1386, 139, 1390, 1391, 1392, 1393, 1394, 1395, 140, 1402, 1404, 1405, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213)+cms.vuint32( 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468)+cms.vuint32( 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 690, 691, 692, 693, 70, 71, 72, 73, 735, 74, 75, 76, 77, 78, 79, 790, 791, 792, 793, 80, 81, 82, 83, 831, 832, 833, 834, 835, 836, 837, 838, 839, 84, 841, 842, 843, 844, 845, 846, 847, 848, 849, 85, 851, 852, 853, 854, 855, 856, 857, 858, 859, 86, 861, 862, 863, 864, 865, 866, 867, 868, 869, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99) )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltPreHIGEDPhoton15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG15EtPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 15.0 ),
    etcutEB = cms.double( 15.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG15HoverELoosePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG15EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG20EtPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 20.0 ),
    etcutEB = cms.double( 20.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG20HoverELoosePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG20EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltL1sSingleEG7BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG7_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIGEDPhoton30 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG30EtPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 30.0 ),
    etcutEB = cms.double( 30.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG30HoverELoosePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG30EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltL1sSingleEG21BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG21_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIGEDPhoton40 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG40EtPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 40.0 ),
    etcutEB = cms.double( 40.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG40HoverELoosePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG40EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton50 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG50EtPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 50.0 ),
    etcutEB = cms.double( 50.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG50HoverELoosePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG50EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltL1sSingleEG30BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG30_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIGEDPhoton60 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG60EtPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 60.0 ),
    etcutEB = cms.double( 60.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG60HoverELoosePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG60EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltL1sSingleEG3BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG3_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltL1sSingleEG5BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG5_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltL1sSingleEG12BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG12_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltL1sSingleEG15BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG15_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIGEDPhoton10EB = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG10EtEBPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 10.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG10HoverELooseEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG10EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton15EB = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG15EtEBPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 15.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG15HoverELooseEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG15EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton20EB = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG20EtEBPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 20.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG20HoverELooseEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG20EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton30EB = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG30EtEBPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 30.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG30HoverELooseEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG30EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton40EB = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG40EtEBPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 40.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG40HoverELooseEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG40EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton50EB = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG50EtEBPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 50.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG50HoverELooseEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG50EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton60EB = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG60EtEBPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 60.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG60HoverELooseEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 2.0 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 2.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG60EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton10HECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG10HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG10EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton15HECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG15HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG15EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton20HECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG20HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG20EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton30HECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG30HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG30EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton40HECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG40HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG40EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton50HECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG50HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG50EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton60HECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG60HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG60EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton10EBHECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG10HoverEEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG10EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton15EBHECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG15HoverEEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG15EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton20EBHECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG20HoverEEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG20EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton30EBHECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG30HoverEEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG30EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton40EBHECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG40HoverEEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG40EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton50EBHECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG50HoverEEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG50EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton60EBHECut = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG60HoverEEBPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG60EtEBPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
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
process.hltPreHIGEDPhoton10L1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltRechitInRegionsECAL = cms.EDProducer( "HLTEcalRecHitInAllL1RegionsProducer",
    l1InputRegions = cms.VPSet( 
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "EGamma" ),
        minEt = cms.double( 5.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Jet' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Jet" ),
        minEt = cms.double( 170.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Tau' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Tau" ),
        minEt = cms.double( 100.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      )
    ),
    recHitLabels = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    productLabels = cms.vstring( 'EcalRecHitsEB',
      'EcalRecHitsEE' )
)
process.hltRechitInRegionsES = cms.EDProducer( "HLTEcalRecHitInAllL1RegionsProducer",
    l1InputRegions = cms.VPSet( 
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "EGamma" ),
        minEt = cms.double( 5.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Jet' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Jet" ),
        minEt = cms.double( 170.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Tau' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Tau" ),
        minEt = cms.double( 100.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      )
    ),
    recHitLabels = cms.VInputTag( 'hltEcalPreshowerRecHit:EcalRecHitsES' ),
    productLabels = cms.vstring( 'EcalRecHitsES' )
)
process.hltParticleFlowRecHitECALL1Seeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEB' ),
        srFlags = cms.InputTag( "" ),
        name = cms.string( "PFEBRecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  name = cms.string( "PFRecHitQTestECALMultiThreshold" ),
            thresholds = cms.vdouble( 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 1.25023, 1.25033, 1.25047, 1.25068, 1.25097, 1.25139, 1.25199, 1.25286, 1.2541, 1.25587, 1.25842, 1.26207, 1.26729, 1.27479, 1.28553, 1.30092, 1.32299, 1.35462, 1.39995, 1.46493, 1.55807, 1.69156, 1.88291, 2.15716, 2.55027, 3.11371, 3.92131, 5.07887, 6.73803, 9.11615, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 1.25023, 1.25033, 1.25047, 1.25068, 1.25097, 1.25139, 1.25199, 1.25286, 1.2541, 1.25587, 1.25842, 1.26207, 1.26729, 1.27479, 1.28553, 1.30092, 1.32299, 1.35462, 1.39995, 1.46493, 1.55807, 1.69156, 1.88291, 2.15716, 2.55027, 3.11371, 3.92131, 5.07887, 6.73803, 9.11615, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ),
            applySelectionsToAllCrystals = cms.bool( True )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        )
      ),
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEE' ),
        srFlags = cms.InputTag( "" ),
        name = cms.string( "PFEERecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  name = cms.string( "PFRecHitQTestECALMultiThreshold" ),
            thresholds = cms.vdouble( 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 1.25023, 1.25033, 1.25047, 1.25068, 1.25097, 1.25139, 1.25199, 1.25286, 1.2541, 1.25587, 1.25842, 1.26207, 1.26729, 1.27479, 1.28553, 1.30092, 1.32299, 1.35462, 1.39995, 1.46493, 1.55807, 1.69156, 1.88291, 2.15716, 2.55027, 3.11371, 3.92131, 5.07887, 6.73803, 9.11615, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 1.25023, 1.25033, 1.25047, 1.25068, 1.25097, 1.25139, 1.25199, 1.25286, 1.2541, 1.25587, 1.25842, 1.26207, 1.26729, 1.27479, 1.28553, 1.30092, 1.32299, 1.35462, 1.39995, 1.46493, 1.55807, 1.69156, 1.88291, 2.15716, 2.55027, 3.11371, 3.92131, 5.07887, 6.73803, 9.11615, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 ),
            applySelectionsToAllCrystals = cms.bool( True )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        )
      )
    ),
    navigator = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitECALNavigator" )
    )
)
process.hltParticleFlowRecHitPSL1Seeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsES','EcalRecHitsES' ),
        name = cms.string( "PFPSRecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 7.0E-6 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          )
        )
      )
    ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitPreshowerNavigator" ) )
)
process.hltParticleFlowClusterPSL1Seeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 6.0E-5 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 50 ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS2" )
        )
      ),
      showerSigma = cms.double( 0.3 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( False )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 4 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitPSL1Seeded" )
)
process.hltParticleFlowClusterECALUncorrectedL1Seeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 9 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet( 
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet( 
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      maxIterations = cms.uint32( 50 ),
      positionCalcForConvergence = cms.PSet( 
        minAllowedNormalization = cms.double( 0.0 ),
        T0_ES = cms.double( 1.2 ),
        algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
        T0_EE = cms.double( 3.1 ),
        T0_EB = cms.double( 7.4 ),
        X0 = cms.double( 0.89 ),
        minFractionInCalc = cms.double( 0.0 ),
        W0 = cms.double( 4.2 )
      ),
      allCellsPositionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet( 
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet( 
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  recHitEnergyNorm = cms.double( 0.08 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 0.3 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      showerSigma = cms.double( 1.5 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet( 
      minAllowedNormalization = cms.double( 0.0 ),
      T0_ES = cms.double( 1.2 ),
      algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
      T0_EE = cms.double( 3.1 ),
      T0_EB = cms.double( 7.4 ),
      X0 = cms.double( 0.89 ),
      minFractionInCalc = cms.double( 0.0 ),
      W0 = cms.double( 4.2 )
    ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.08 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.3 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( True )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThresholdPt = cms.double( 0.15 ),
          seedingThreshold = cms.double( 0.6 ),
          detector = cms.string( "ECAL_ENDCAP" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 0.23 ),
          detector = cms.string( "ECAL_BARREL" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 8 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitECALL1Seeded" )
)
process.hltParticleFlowClusterECALL1Seeded = cms.EDProducer( "CorrectedECALPFClusterProducer",
    inputPS = cms.InputTag( "hltParticleFlowClusterPSL1Seeded" ),
    minimumPSEnergy = cms.double( 0.0 ),
    energyCorrector = cms.PSet( 
      algoName = cms.string( "PFClusterEMEnergyCorrector" ),
      applyCrackCorrections = cms.bool( False )
    ),
    inputECAL = cms.InputTag( "hltParticleFlowClusterECALUncorrectedL1Seeded" )
)
process.hltParticleFlowSuperClusterECALL1Seeded = cms.EDProducer( "PFECALSuperClusterProducer",
    PFSuperClusterCollectionEndcap = cms.string( "hltParticleFlowSuperClusterECALEndcap" ),
    doSatelliteClusterMerge = cms.bool( False ),
    BeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PFBasicClusterCollectionBarrel = cms.string( "hltParticleFlowBasicClusterECALBarrel" ),
    useRegression = cms.bool( True ),
    satelliteMajorityFraction = cms.double( 0.5 ),
    isOOTCollection = cms.bool( False ),
    thresh_PFClusterEndcap = cms.double( 0.5 ),
    ESAssociation = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    PFBasicClusterCollectionPreshower = cms.string( "hltParticleFlowBasicClusterECALPreshower" ),
    use_preshower = cms.bool( True ),
    thresh_PFClusterBarrel = cms.double( 0.5 ),
    thresh_SCEt = cms.double( 4.0 ),
    etawidth_SuperClusterEndcap = cms.double( 0.04 ),
    phiwidth_SuperClusterEndcap = cms.double( 0.6 ),
    verbose = cms.untracked.bool( False ),
    useDynamicDPhiWindow = cms.bool( True ),
    PFSuperClusterCollectionBarrel = cms.string( "hltParticleFlowSuperClusterECALBarrel" ),
    regressionConfig = cms.PSet( 
      uncertaintyKeyEB = cms.string( "pfscecal_EBUncertainty_online" ),
      ecalRecHitsEE = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
      ecalRecHitsEB = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      regressionKeyEE = cms.string( "pfscecal_EECorrection_online" ),
      regressionKeyEB = cms.string( "pfscecal_EBCorrection_online" ),
      uncertaintyKeyEE = cms.string( "pfscecal_EEUncertainty_online" ),
      isHLT = cms.bool( True )
    ),
    applyCrackCorrections = cms.bool( False ),
    satelliteClusterSeedThreshold = cms.double( 50.0 ),
    endcapRecHits = cms.InputTag( 'ecalRecHit','EcalRecHitsEB' ),
    etawidth_SuperClusterBarrel = cms.double( 0.04 ),
    PFBasicClusterCollectionEndcap = cms.string( "hltParticleFlowBasicClusterECALEndcap" ),
    barrelRecHits = cms.InputTag( 'ecalRecHit','EcalRecHitsEE' ),
    thresh_PFClusterSeedBarrel = cms.double( 1.0 ),
    ClusteringType = cms.string( "Mustache" ),
    dropUnseedable = cms.bool( False ),
    EnergyWeight = cms.string( "Raw" ),
    PFClusters = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    thresh_PFClusterSeedEndcap = cms.double( 1.0 ),
    phiwidth_SuperClusterBarrel = cms.double( 0.6 ),
    thresh_PFClusterES = cms.double( 0.5 ),
    seedThresholdIsET = cms.bool( True ),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string( "hltParticleFlowSuperClusterECALEndcapWithPreshower" )
)
process.hltEgammaCandidates = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
    scHybridBarrelProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALBarrel' ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltEGL1SingleEG3BptxANDFilter = cms.EDFilter( "HLTEgammaL1TMatchFilterRegional",
    doIsolated = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    region_phi_size = cms.double( 1.044 ),
    saveTags = cms.bool( True ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    l1CenJetsTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sSingleEG3BptxAND" ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    ncandcut = cms.int32( 1 ),
    l1TausTag = cms.InputTag( 'hltGtStage2Digis','Tau' )
)
process.hltEG10EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG3BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 10.0 ),
    etcutEB = cms.double( 10.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltFixedGridRhoFastjetAllCaloForMuons = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 2.5 ),
    pfCandidatesTag = cms.InputTag( "hltTowerMakerForAll" )
)
process.hltEgammaHoverE = cms.EDProducer( "EgammaHLTBcHcalIsolationProducersRegional",
    effectiveAreas = cms.vdouble( 0.105, 0.17 ),
    doRhoCorrection = cms.bool( False ),
    outerCone = cms.double( 0.14 ),
    caloTowerProducer = cms.InputTag( "hltTowerMakerForAll" ),
    innerCone = cms.double( 0.0 ),
    useSingleTower = cms.bool( False ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    depth = cms.int32( -1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    rhoMax = cms.double( 9.9999999E7 ),
    etMin = cms.double( 0.0 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( False )
)
process.hltEG10HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG10EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton15L1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG15EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG3BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 15.0 ),
    etcutEB = cms.double( 15.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG15HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG15EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton20L1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG20EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG3BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 20.0 ),
    etcutEB = cms.double( 20.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG20HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG20EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton30L1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEGL1SingleEG7BptxANDFilter = cms.EDFilter( "HLTEgammaL1TMatchFilterRegional",
    doIsolated = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    region_phi_size = cms.double( 1.044 ),
    saveTags = cms.bool( True ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    l1CenJetsTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sSingleEG7BptxAND" ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    ncandcut = cms.int32( 1 ),
    l1TausTag = cms.InputTag( 'hltGtStage2Digis','Tau' )
)
process.hltEG30EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG7BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 30.0 ),
    etcutEB = cms.double( 30.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG30HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG30EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton40L1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEGL1SingleEG21BptxANDFilter = cms.EDFilter( "HLTEgammaL1TMatchFilterRegional",
    doIsolated = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    region_phi_size = cms.double( 1.044 ),
    saveTags = cms.bool( True ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    l1CenJetsTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sSingleEG21BptxAND" ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    ncandcut = cms.int32( 1 ),
    l1TausTag = cms.InputTag( 'hltGtStage2Digis','Tau' )
)
process.hltEG40EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG21BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 40.0 ),
    etcutEB = cms.double( 40.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG40HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG40EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton50L1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG50EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG21BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 50.0 ),
    etcutEB = cms.double( 50.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG50HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG50EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton60L1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEGL1SingleEG30BptxANDFilter = cms.EDFilter( "HLTEgammaL1TMatchFilterRegional",
    doIsolated = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    region_phi_size = cms.double( 1.044 ),
    saveTags = cms.bool( True ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    l1CenJetsTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sSingleEG30BptxAND" ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    ncandcut = cms.int32( 1 ),
    l1TausTag = cms.InputTag( 'hltGtStage2Digis','Tau' )
)
process.hltEG60EtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG30BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 60.0 ),
    etcutEB = cms.double( 60.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG60HEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG60EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton10EBL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG10EBEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG3BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 10.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG10EBHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG10EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton15EBL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG15EBEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG3BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 15.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG15EBHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG15EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton20EBL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG20EBEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG3BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 20.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG20EBHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG20EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton30EBL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG30EBEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG7BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 30.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG30EBHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG30EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton40EBL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG40EBEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG21BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 40.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG40EBHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG40EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton50EBL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG50EBEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG21BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 50.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG50EBHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG50EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton60EBL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG60EBEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEG30BptxANDFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 999999.0 ),
    etcutEB = cms.double( 60.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG60EBHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.9999 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 1.9999 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG60EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton10HECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG10HEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG10EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton15HECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG15HEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG15EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton20HECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG20HEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG20EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton30HECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG30HEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG30EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton40HECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG40HEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG40EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton50HECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG50HEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG50EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton60HECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG60HEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG60EtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton10EBHECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG10EBHEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG10EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton15EBHECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG15EBHEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG15EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton20EBHECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG20EBHEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG20EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton30EBHECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG30EBHEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG30EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton40EBHECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG40EBHEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG40EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton50EBHECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG50EBHEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG50EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIGEDPhoton60EBHECutL1Seeded = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEG60EBHEFilterHECut = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.2 ),
    varTag = cms.InputTag( "hltEgammaHoverE" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG60EBEtFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIIslandPhoton10Eta3p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltIslandBasicClustersHI = cms.EDProducer( "IslandClusterProducer",
    SeedRecHitFlagToBeExcludedEE = cms.vstring( 'kFaultyHardware',
      'kNeighboursRecovered',
      'kTowerRecovered',
      'kDead',
      'kWeird' ),
    RecHitFlagToBeExcludedEB = cms.vstring( 'kWeird',
      'kDiWeird',
      'kOutOfTime',
      'kTowerRecovered' ),
    endcapHits = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    IslandEndcapSeedThr = cms.double( 0.18 ),
    SeedRecHitFlagToBeExcludedEB = cms.vstring( 'kFaultyHardware',
      'kTowerRecovered',
      'kDead' ),
    posCalcParameters = cms.PSet( 
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    barrelShapeAssociation = cms.string( "islandBarrelShapeAssoc" ),
    endcapShapeAssociation = cms.string( "islandEndcapShapeAssoc" ),
    barrelHits = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    clustershapecollectionEE = cms.string( "islandEndcapShape" ),
    clustershapecollectionEB = cms.string( "islandBarrelShape" ),
    VerbosityLevel = cms.string( "ERROR" ),
    RecHitFlagToBeExcludedEE = cms.vstring( 'kWeird',
      'kDiWeird',
      'kOutOfTime',
      'kTowerRecovered' ),
    barrelClusterCollection = cms.string( "islandBarrelBasicClustersHI" ),
    endcapClusterCollection = cms.string( "islandEndcapBasicClustersHI" ),
    IslandBarrelSeedThr = cms.double( 0.5 )
)
process.hltHiIslandSuperClustersHI = cms.EDProducer( "HiSuperClusterProducer",
    barrelSuperclusterCollection = cms.string( "islandBarrelSuperClustersHI" ),
    endcapEtaSearchRoad = cms.double( 0.14 ),
    barrelClusterCollection = cms.string( "islandBarrelBasicClustersHI" ),
    endcapClusterProducer = cms.string( "hltIslandBasicClustersHI" ),
    barrelPhiSearchRoad = cms.double( 0.8 ),
    endcapPhiSearchRoad = cms.double( 0.6 ),
    endcapBCEnergyThreshold = cms.double( 0.0 ),
    VerbosityLevel = cms.string( "ERROR" ),
    seedTransverseEnergyThreshold = cms.double( 1.0 ),
    barrelEtaSearchRoad = cms.double( 0.07 ),
    endcapSuperclusterCollection = cms.string( "islandEndcapSuperClustersHI" ),
    barrelBCEnergyThreshold = cms.double( 0.0 ),
    doBarrel = cms.bool( True ),
    doEndcaps = cms.bool( True ),
    endcapClusterCollection = cms.string( "islandEndcapBasicClustersHI" ),
    barrelClusterProducer = cms.string( "hltIslandBasicClustersHI" )
)
process.hltHiCorrectedIslandBarrelSuperClustersHI = cms.EDProducer( "HiEgammaSCCorrectionMaker",
    corectedSuperClusterCollection = cms.string( "" ),
    sigmaElectronicNoise = cms.double( 0.03 ),
    superClusterAlgo = cms.string( "Island" ),
    etThresh = cms.double( 0.0 ),
    rawSuperClusterProducer = cms.InputTag( 'hltHiIslandSuperClustersHI','islandBarrelSuperClustersHI' ),
    applyEnergyCorrection = cms.bool( True ),
    isl_fCorrPset = cms.PSet( 
      fEtaVect = cms.vdouble( 0.993, 0.0, 0.00546, 1.165, -0.180844, 0.040312 ),
      fBremVect = cms.vdouble( -0.773799, 2.73438, -1.07235, 0.986821, -0.0101822, 3.06744E-4, 1.00595, -0.0495958, 0.00451986, 1.00595, -0.0495958, 0.00451986 ),
      fBremThVect = cms.vdouble( 1.2, 1.2 ),
      fEtEtaVect = cms.vdouble( 0.9497, 0.006985, 1.03754, -0.0142667, -0.0233993, 0.0, 0.0, 0.908915, 0.0137322, 16.9602, -29.3093, 19.8976, -5.92666, 0.654571 ),
      brLinearLowThr = cms.double( 0.0 ),
      brLinearHighThr = cms.double( 0.0 ),
      minR9Barrel = cms.double( 0.94 ),
      minR9Endcap = cms.double( 0.95 ),
      maxR9 = cms.double( 1.5 )
    ),
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' )
)
process.hltHiCorrectedIslandEndcapSuperClustersHI = cms.EDProducer( "HiEgammaSCCorrectionMaker",
    corectedSuperClusterCollection = cms.string( "" ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    superClusterAlgo = cms.string( "Island" ),
    etThresh = cms.double( 0.0 ),
    rawSuperClusterProducer = cms.InputTag( 'hltHiIslandSuperClustersHI','islandEndcapSuperClustersHI' ),
    applyEnergyCorrection = cms.bool( True ),
    isl_fCorrPset = cms.PSet( 
      fEtaVect = cms.vdouble( 0.993, 0.0, 0.00546, 1.165, -0.180844, 0.040312 ),
      fBremVect = cms.vdouble( -0.773799, 2.73438, -1.07235, 0.986821, -0.0101822, 3.06744E-4, 1.00595, -0.0495958, 0.00451986, 1.00595, -0.0495958, 0.00451986 ),
      fBremThVect = cms.vdouble( 1.2, 1.2 ),
      fEtEtaVect = cms.vdouble( 0.9497, 0.006985, 1.03754, -0.0142667, -0.0233993, 0.0, 0.0, 0.908915, 0.0137322, 16.9602, -29.3093, 19.8976, -5.92666, 0.654571 ),
      brLinearLowThr = cms.double( 0.0 ),
      brLinearHighThr = cms.double( 0.0 ),
      minR9Barrel = cms.double( 0.94 ),
      minR9Endcap = cms.double( 0.95 ),
      maxR9 = cms.double( 1.5 )
    ),
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' )
)
process.hltCleanedHiCorrectedIslandBarrelSuperClustersHI = cms.EDProducer( "HiSpikeCleaner",
    originalSuperClusterProducer = cms.InputTag( "hltHiCorrectedIslandBarrelSuperClustersHI" ),
    recHitProducerEndcap = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    TimingCut = cms.untracked.double( 9999999.0 ),
    swissCutThr = cms.untracked.double( 0.95 ),
    recHitProducerBarrel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    etCut = cms.double( 8.0 ),
    outputColl = cms.string( "" )
)
process.hltRecoHIEcalWithCleaningCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( "hltHiCorrectedIslandEndcapSuperClustersHI" ),
    scHybridBarrelProducer = cms.InputTag( "hltCleanedHiCorrectedIslandBarrelSuperClustersHI" ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltHIIslandPhoton10Eta3p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 3.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 10.0 )
)
process.hltPreHIIslandPhoton10Eta1p5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton10Eta1p5 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 10.0 )
)
process.hltPreHIIslandPhoton15Eta3p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton15Eta3p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 3.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 15.0 )
)
process.hltPreHIIslandPhoton15Eta1p5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton15Eta1p5 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 15.0 )
)
process.hltPreHIIslandPhoton20Eta3p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton20Eta3p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 3.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 20.0 )
)
process.hltPreHIIslandPhoton20Eta1p5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton20Eta1p5 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 20.0 )
)
process.hltPreHIIslandPhoton30Eta3p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton30Eta3p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 3.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 30.0 )
)
process.hltPreHIIslandPhoton30Eta1p5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton30Eta1p5 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 30.0 )
)
process.hltPreHIIslandPhoton40Eta3p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton40Eta3p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 3.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 40.0 )
)
process.hltPreHIIslandPhoton40Eta1p5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton40Eta1p5 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 40.0 )
)
process.hltPreHIIslandPhoton50Eta3p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton50Eta3p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 3.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 50.0 )
)
process.hltPreHIIslandPhoton50Eta1p5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton50Eta1p5 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 50.0 )
)
process.hltPreHIIslandPhoton60Eta3p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton60Eta3p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 3.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 60.0 )
)
process.hltPreHIIslandPhoton60Eta1p5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHIIslandPhoton60Eta1p5 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 ),
    MinPt = cms.double( 60.0 )
)
process.hltPreZeroBias = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023, 1024 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    moduleLabelPatternsToSkip = cms.vstring(  ),
    processName = cms.string( "@" ),
    moduleLabelPatternsToMatch = cms.vstring( 'hlt*' ),
    throw = cms.bool( False )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
process.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet( 
    ),
    verbose = cms.untracked.bool( False )
)
process.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
process.hltL1sSingleEG3Cent30100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG3_Centrality_30_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIIslandPhoton10Eta3p1Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton10Eta1p5Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton15Eta3p1Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton15Eta1p5Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton20Eta3p1Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton20Eta1p5Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleEG7Cent30100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG7_Centrality_30_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIIslandPhoton30Eta3p1Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton30Eta1p5Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleEG21Cent30100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG21_Centrality_30_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIIslandPhoton40Eta3p1Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton40Eta1p5Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleEG3Cent50100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG3_Centrality_50_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIIslandPhoton10Eta3p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton10Eta1p5Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton15Eta3p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton15Eta1p5Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton20Eta3p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton20Eta1p5Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleEG7Cent50100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG7_Centrality_50_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIIslandPhoton30Eta3p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton30Eta1p5Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleEG21Cent50100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG21_Centrality_50_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIIslandPhoton40Eta3p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIIslandPhoton40Eta1p5Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton10Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton15Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton20Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton30Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton40Cent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton10Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton15Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton20Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton30Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton40Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton10EBCent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton15EBCent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton20EBCent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton30EBCent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton40EBCent30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton10EBCent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton15EBCent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton20EBCent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton30EBCent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIGEDPhoton40EBCent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleJet28BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet28_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet40Eta5p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
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
process.hltSinglePuAK4CaloJet40Eta5p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( False ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 5.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 40.0 )
)
process.hltL1sSingleJet44BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet44_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet60Eta5p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet60Eta5p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 5.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 60.0 )
)
process.hltL1sSingleJet56BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet56_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet80Eta5p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet80Eta5p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 5.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 80.0 )
)
process.hltL1sSingleJet60BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet60_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet100Eta5p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet100Eta5p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 5.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 100.0 )
)
process.hltPreHIPuAK4CaloJet120Eta5p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet120Eta5p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 5.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 120.0 )
)
process.hltPreHIPuAK4CaloJet8035Eta1p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet80Eta1p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 80.0 )
)
process.hltDoublePuAK4CaloJet35Eta1p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 1.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 35.0 )
)
process.hltPreHIPuAK4CaloJet10035Eta1p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet100Eta1p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 100.0 )
)
process.hltPreHIPuAK4CaloJet8035Eta0p7 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet80Eta0p7 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 0.7 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 80.0 )
)
process.hltDoublePuAK4CaloJet35Eta0p7 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 0.7 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 35.0 )
)
process.hltPreHIPuAK4CaloJet10035Eta0p7 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet100Eta0p7 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 0.7 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 100.0 )
)
process.hltPreHIPuAK4CaloJet804545Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet80Eta2p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 80.0 )
)
process.hltTriplePuAK4CaloJet45Eta2p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 3 ),
    MaxEta = cms.double( 2.1 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 45.0 )
)
process.hltL1sSingleJet28FwdBptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet28_FWD_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet40Fwd = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet40Fwd = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 5.1 ),
    MinEta = cms.double( 2.7 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 40.0 )
)
process.hltL1sSingleJet44FwdBptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet44_FWD_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet60Fwd = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet60Fwd = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 5.1 ),
    MinEta = cms.double( 2.7 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 60.0 )
)
process.hltL1sSingleJet56FwdBptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet56_FWD_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet80Fwd = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet80Fwd = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 5.1 ),
    MinEta = cms.double( 2.7 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 80.0 )
)
process.hltPreHIPuAK4CaloJet100Fwd = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet100Fwd = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 5.1 ),
    MinEta = cms.double( 2.7 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 100.0 )
)
process.hltPreHIPuAK4CaloJet120Fwd = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet120Fwd = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 5.1 ),
    MinEta = cms.double( 2.7 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 120.0 )
)
process.hltPreHIPuAK4CaloJet60Eta2p4DeepCSV0p71 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet60Eta2p4 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.4 ),
    MinEta = cms.double( -2.4 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 60.0 )
)
process.hltSelectorJets60 = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    etMin = cms.double( 60.0 )
)
process.hltSelectorCentralJets60 = cms.EDFilter( "EtaRangeCaloJetSelector",
    src = cms.InputTag( "hltSelectorJets60" ),
    etaMin = cms.double( -2.4 ),
    etaMax = cms.double( 2.4 )
)
process.hltSelector4CentralJetsPtCut = cms.EDFilter( "LargestEtCaloJetSelector",
    maxNumber = cms.uint32( 4 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelectorCentralJets60" )
)
process.hltSelectorCentralJets = cms.EDFilter( "EtaRangeCaloJetSelector",
    src = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    etaMin = cms.double( -2.4 ),
    etaMax = cms.double( 2.4 )
)
process.hltSelector4CentralJets = cms.EDFilter( "LargestEtCaloJetSelector",
    maxNumber = cms.uint32( 4 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelectorCentralJets" )
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
    Phase2DigiBaseline = cms.double( 1200.0 ),
    ElectronPerADCGain = cms.double( 135.0 ),
    Phase2ReadoutMode = cms.int32( -1 ),
    maxNumberOfClusters = cms.int32( -1 ),
    ClusterThreshold_L1 = cms.int32( 2000 ),
    MissCalibrate = cms.untracked.bool( True ),
    VCaltoElectronGain = cms.int32( 47 ),
    VCaltoElectronGain_L1 = cms.int32( 50 ),
    VCaltoElectronOffset = cms.int32( -60 ),
    SplitClusters = cms.bool( False ),
    payloadType = cms.string( "Offline" ),
    Phase2Calibration = cms.bool( False ),
    Phase2KinkADC = cms.int32( 8 ),
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
process.hltHITrackingSiStripRawToClustersFacilityZeroSuppression = cms.EDProducer( "SiStripClusterizer",
    DigiProducersList = cms.VInputTag( 'hltSiStripZeroSuppression:VirginRaw','hltSiStripZeroSuppression:ProcessedRaw','hltSiStripZeroSuppression:ScopeMode','hltSiStripZeroSuppression:ZeroSuppressed' ),
    Clusterizer = cms.PSet( 
      ChannelThreshold = cms.double( 2.0 ),
      MaxSequentialBad = cms.uint32( 1 ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
      MaxSequentialHoles = cms.uint32( 0 ),
      MaxAdjacentBad = cms.uint32( 0 ),
      QualityLabel = cms.string( "" ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      SeedThreshold = cms.double( 3.0 ),
      RemoveApvShots = cms.bool( True ),
      ClusterThreshold = cms.double( 5.0 )
    )
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
    stripClusterProducer = cms.string( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" )
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
    ClusterCollectionLabel = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" )
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
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryBuilderPreSplittingPPOnAA" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
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
    useSimpleMF = cms.bool( False ),
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
      maxNormalizedChi2 = cms.double( 10.0 ),
      trackQuality = cms.string( "any" ),
      algorithm = cms.string( "filter" ),
      maxD0Significance = cms.double( 3.0 )
    ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltFullIter0CtfWithMaterialTracksPreSplittingPPOnAA" ),
    TkClusParameters = cms.PSet( 
      algorithm = cms.string( "gap" ),
      TkGapClusParameters = cms.PSet(  zSeparation = cms.double( 1.0 ) )
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
process.hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression = cms.EDProducer( "SiStripClusterizer",
    DigiProducersList = cms.VInputTag( 'hltSiStripZeroSuppression:VirginRaw','hltSiStripZeroSuppression:ProcessedRaw','hltSiStripZeroSuppression:ScopeMode','hltSiStripZeroSuppression:ZeroSuppressed' ),
    Clusterizer = cms.PSet( 
      ChannelThreshold = cms.double( 2.0 ),
      MaxSequentialBad = cms.uint32( 1 ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
      MaxSequentialHoles = cms.uint32( 0 ),
      MaxAdjacentBad = cms.uint32( 0 ),
      QualityLabel = cms.string( "" ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      SeedThreshold = cms.double( 3.0 ),
      RemoveApvShots = cms.bool( True ),
      ClusterThreshold = cms.double( 5.0 )
    )
)
process.hltSiStripClustersFullPPOnAA = cms.EDProducer( "MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(  ),
    Phase2TrackerCluster1DProducer = cms.string( "" ),
    measurementTracker = cms.string( "hltESPMeasurementTracker" ),
    pixelClusterProducer = cms.string( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag(  ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    skipClusters = cms.InputTag( "" ),
    pixelCablingMapLabel = cms.string( "" ),
    stripClusterProducer = cms.string( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" )
)
process.hltSiStripMatchedRecHitsFull = cms.EDProducer( "SiStripRecHitConverter",
    StripCPE = cms.ESInputTag( 'hltESPStripCPEfromTrackAngle','hltESPStripCPEfromTrackAngle' ),
    stereoRecHits = cms.string( "stereoRecHit" ),
    useSiStripQuality = cms.bool( False ),
    matchedRecHits = cms.string( "matchedRecHit" ),
    ClusterProducer = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" ),
    VerbosityLevel = cms.untracked.int32( 1 ),
    rphiRecHits = cms.string( "rphiRecHit" ),
    Matcher = cms.ESInputTag( 'SiStripRecHitMatcherESProducer','StandardMatcher' ),
    siStripQualityLabel = cms.ESInputTag( "" ),
    MaskBadAPVFibers = cms.bool( False )
)
process.hltFullIter0PixelQuadrupletsPPOnAAForBTag = cms.EDProducer( "SeedingLayersEDProducer",
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
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter0PixelTrackingCandRegionsForBTag = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet( 
      precise = cms.bool( True ),
      originRadius = cms.double( 0.02 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorVetex = cms.double( 0.2 ),
      zErrorBeamSpot = cms.double( 24.2 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      deltaEta = cms.double( 0.5 ),
      measurementTrackerName = cms.InputTag( "" ),
      vertexCollection = cms.InputTag( "" ),
      maxNRegions = cms.int32( 10 ),
      ptMin = cms.double( 0.9 ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "Never" ),
      input = cms.InputTag( "hltSelector4CentralJets" ),
      deltaPhi = cms.double( 0.5 ),
      maxNVertices = cms.int32( 1 ),
      mode = cms.string( "BeamSpotSigma" )
    )
)
process.hltFullIter0PixelClusterCheckPPOnAAForBTag = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" )
)
process.hltFullIter0PixelHitDoubletsPPOnAAForBTag = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter0PixelTrackingCandRegionsForBTag" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "hltFullIter0PixelClusterCheckPPOnAAForBTag" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter0PixelQuadrupletsPPOnAAForBTag" )
)
process.hltFullIter0PixelHitQuadrupletsPPOnAAForBTag = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.0012 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplittingPPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter0PixelHitDoubletsPPOnAAForBTag" ),
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
process.hltFullIter0PixelSeedsPPOnAAForBTag = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet( 
      FilterStripHits = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      FilterAtHelixStage = cms.bool( False ),
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplittingPPOnAA" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter0PixelHitQuadrupletsPPOnAAForBTag" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter0CkfTrackCandidatesPPOnAAForBTag = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter0PixelSeedsPPOnAAForBTag" ),
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
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryBuilderPPOnAA" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
)
process.hltFullIter0CtfWithMaterialTracksPPOnAAForBTag = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter0CkfTrackCandidatesPPOnAAForBTag" ),
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
process.hltFullIter0PrimaryVerticesPPOnAAForBTag = cms.EDProducer( "PrimaryVertexProducer",
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
    TrackLabel = cms.InputTag( "hltFullIter0CtfWithMaterialTracksPPOnAAForBTag" ),
    TkClusParameters = cms.PSet( 
      algorithm = cms.string( "gap" ),
      TkGapClusParameters = cms.PSet(  zSeparation = cms.double( 1.0 ) )
    )
)
process.hltFullIter0TrackMVAClassifierPPOnAAForBTag = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltFullIter0CtfWithMaterialTracksPPOnAAForBTag" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAAForBTag" ),
    qualityCuts = cms.vdouble( -0.95, -0.85, -0.75 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorInitialStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter0HighPurityTracksPPOnAAForBTag = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter0CtfWithMaterialTracksPPOnAAForBTag" ),
    originalQualVals = cms.InputTag( 'hltFullIter0TrackMVAClassifierPPOnAAForBTag','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter0TrackMVAClassifierPPOnAAForBTag','MVAValues' )
)
process.hltFullIter1ClustersRefRemovalPPOnAAForBTag = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter0HighPurityTracksPPOnAAForBTag" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter1MaskedMeasurementTrackerEventPPOnAAForBTag = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter1ClustersRefRemovalPPOnAAForBTag" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter1PixelQuadrupletsPPOnAAForBTag = cms.EDProducer( "SeedingLayersEDProducer",
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
      skipClusters = cms.InputTag( "hltFullIter1ClustersRefRemovalPPOnAAForBTag" ),
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
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter1ClustersRefRemovalPPOnAAForBTag" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter1PixelTrackingCandRegionsForBTag = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet( 
      precise = cms.bool( True ),
      originRadius = cms.double( 0.02 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorVetex = cms.double( 0.2 ),
      zErrorBeamSpot = cms.double( 24.2 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      deltaEta = cms.double( 0.5 ),
      measurementTrackerName = cms.InputTag( "hltFullIter1MaskedMeasurementTrackerEventPPOnAAForBTag" ),
      vertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAAForBTag" ),
      maxNRegions = cms.int32( 10 ),
      ptMin = cms.double( 0.7 ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
      input = cms.InputTag( "hltSelector4CentralJetsPtCut" ),
      deltaPhi = cms.double( 0.5 ),
      maxNVertices = cms.int32( 1 ),
      mode = cms.string( "BeamSpotSigma" )
    )
)
process.hltFullIter1PixelClusterCheckPPOnAAForBTag = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 100000 ),
    ClusterCollectionLabel = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" )
)
process.hltFullIter1PixelHitDoubletsPPOnAAForBTag = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter1PixelTrackingCandRegionsForBTag" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "hltFullIter1PixelClusterCheckPPOnAAForBTag" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter1PixelQuadrupletsPPOnAAForBTag" )
)
process.hltFullIter1PixelHitQuadrupletsPPOnAAForBTag = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.0017 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplittingPPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter1PixelHitDoubletsPPOnAAForBTag" ),
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
process.hltFullIter1PixelSeedsPPOnAAForBTag = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter1PixelHitQuadrupletsPPOnAAForBTag" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter1CkfTrackCandidatesPPOnAAForBTag = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter1PixelSeedsPPOnAAForBTag" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPLowPtQuadStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter1MaskedMeasurementTrackerEventPPOnAAForBTag" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtQuadStepTrajectoryBuilderPPOnAA" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
)
process.hltFullIter1CtfWithMaterialTracksPPOnAAForBTag = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter1CkfTrackCandidatesPPOnAAForBTag" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter1MaskedMeasurementTrackerEventPPOnAAForBTag" ),
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
process.hltFullIter1TrackMVAClassifierPPOnAAForBTag = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltFullIter1CtfWithMaterialTracksPPOnAAForBTag" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAAForBTag" ),
    qualityCuts = cms.vdouble( -0.65, -0.35, -0.15 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorLowPtQuadStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter1HighPurityTracksPPOnAAForBTag = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter1CtfWithMaterialTracksPPOnAAForBTag" ),
    originalQualVals = cms.InputTag( 'hltFullIter1TrackMVAClassifierPPOnAAForBTag','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter1TrackMVAClassifierPPOnAAForBTag','MVAValues' )
)
process.hltFullIter2ClustersRefRemovalPPOnAAForBTag = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter1HighPurityTracksPPOnAAForBTag" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter1ClustersRefRemovalPPOnAAForBTag" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter2MaskedMeasurementTrackerEventPPOnAAForBTag = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter2ClustersRefRemovalPPOnAAForBTag" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter2PixelTripletsPPOnAAForBTag = cms.EDProducer( "SeedingLayersEDProducer",
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
      skipClusters = cms.InputTag( "hltFullIter2ClustersRefRemovalPPOnAAForBTag" ),
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
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter2ClustersRefRemovalPPOnAAForBTag" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter2PixelTrackingCandRegionsForBTag = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet( 
      precise = cms.bool( True ),
      originRadius = cms.double( 0.02 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorVetex = cms.double( 0.2 ),
      zErrorBeamSpot = cms.double( 24.2 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      deltaEta = cms.double( 0.5 ),
      measurementTrackerName = cms.InputTag( "hltFullIter2MaskedMeasurementTrackerEventPPOnAAForBTag" ),
      vertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAAForBTag" ),
      maxNRegions = cms.int32( 10 ),
      ptMin = cms.double( 0.9 ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
      input = cms.InputTag( "hltSelector4CentralJetsPtCut" ),
      deltaPhi = cms.double( 0.5 ),
      maxNVertices = cms.int32( 1 ),
      mode = cms.string( "BeamSpotSigma" )
    )
)
process.hltFullIter2PixelClusterCheckPPOnAAForBTag = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" )
)
process.hltFullIter2PixelHitDoubletsPPOnAAForBTag = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter2PixelTrackingCandRegionsForBTag" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "hltFullIter2PixelClusterCheckPPOnAAForBTag" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter2PixelTripletsPPOnAAForBTag" )
)
process.hltFullIter2PixelHitTripletsPPOnAAForBTag = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.3 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplittingPPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter2PixelHitDoubletsPPOnAAForBTag" ),
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
process.hltFullIter2PixelSeedsPPOnAAForBTag = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter2PixelHitTripletsPPOnAAForBTag" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter2CkfTrackCandidatesPPOnAAForBTag = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter2PixelSeedsPPOnAAForBTag" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter2MaskedMeasurementTrackerEventPPOnAAForBTag" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetHighPtTripletStepTrajectoryBuilderPPOnAA" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
)
process.hltFullIter2CtfWithMaterialTracksPPOnAAForBTag = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter2CkfTrackCandidatesPPOnAAForBTag" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter2MaskedMeasurementTrackerEventPPOnAAForBTag" ),
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
process.hltFullIter2TrackMVAClassifierPPOnAAForBTag = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltFullIter2CtfWithMaterialTracksPPOnAAForBTag" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAAForBTag" ),
    qualityCuts = cms.vdouble( 0.2, 0.3, 0.4 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorHighPtTripletStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter2HighPurityTracksPPOnAAForBTag = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter2CtfWithMaterialTracksPPOnAAForBTag" ),
    originalQualVals = cms.InputTag( 'hltFullIter2TrackMVAClassifierPPOnAAForBTag','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter2TrackMVAClassifierPPOnAAForBTag','MVAValues' )
)
process.hltFullIter3ClustersRefRemovalPPOnAAForBTag = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter2HighPurityTracksPPOnAAForBTag" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter2ClustersRefRemovalPPOnAAForBTag" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter3MaskedMeasurementTrackerEventPPOnAAForBTag = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter3ClustersRefRemovalPPOnAAForBTag" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter3PixelTripletsPPOnAAForBTag = cms.EDProducer( "SeedingLayersEDProducer",
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
      skipClusters = cms.InputTag( "hltFullIter3ClustersRefRemovalPPOnAAForBTag" ),
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
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter3ClustersRefRemovalPPOnAAForBTag" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter3PixelTrackingCandRegionsForBTag = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet( 
      precise = cms.bool( True ),
      originRadius = cms.double( 0.02 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorVetex = cms.double( 0.2 ),
      zErrorBeamSpot = cms.double( 24.2 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      deltaEta = cms.double( 0.5 ),
      measurementTrackerName = cms.InputTag( "hltFullIter3MaskedMeasurementTrackerEventPPOnAAForBTag" ),
      vertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAAForBTag" ),
      maxNRegions = cms.int32( 10 ),
      ptMin = cms.double( 0.7 ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
      input = cms.InputTag( "hltSelector4CentralJetsPtCut" ),
      deltaPhi = cms.double( 0.5 ),
      maxNVertices = cms.int32( 1 ),
      mode = cms.string( "BeamSpotSigma" )
    )
)
process.hltFullIter3PixelClusterCheckPPOnAAForBTag = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 100000 ),
    ClusterCollectionLabel = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" )
)
process.hltFullIter3PixelHitDoubletsPPOnAAForBTag = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter3PixelTrackingCandRegionsForBTag" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "hltFullIter3PixelClusterCheckPPOnAAForBTag" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter3PixelTripletsPPOnAAForBTag" )
)
process.hltFullIter3PixelHitTripletsPPOnAAForBTag = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.3 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplittingPPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter3PixelHitDoubletsPPOnAAForBTag" ),
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
process.hltFullIter3PixelSeedsPPOnAAForBTag = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter3PixelHitTripletsPPOnAAForBTag" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter3CkfTrackCandidatesPPOnAAForBTag = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter3PixelSeedsPPOnAAForBTag" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPLowPtTripletStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter3MaskedMeasurementTrackerEventPPOnAAForBTag" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtTripletStepTrajectoryBuilderPPOnAA" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
)
process.hltFullIter3CtfWithMaterialTracksPPOnAAForBTag = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter3CkfTrackCandidatesPPOnAAForBTag" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter3MaskedMeasurementTrackerEventPPOnAAForBTag" ),
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
process.hltFullIter3TrackMVAClassifierPPOnAAForBTag = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltFullIter3CtfWithMaterialTracksPPOnAAForBTag" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAAForBTag" ),
    qualityCuts = cms.vdouble( 0.0, 0.2, 0.4 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorLowPtTripletStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter3HighPurityTracksPPOnAAForBTag = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter3CtfWithMaterialTracksPPOnAAForBTag" ),
    originalQualVals = cms.InputTag( 'hltFullIter3TrackMVAClassifierPPOnAAForBTag','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter3TrackMVAClassifierPPOnAAForBTag','MVAValues' )
)
process.hltFullIter4ClustersRefRemovalPPOnAAForBTag = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter3HighPurityTracksPPOnAAForBTag" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter3ClustersRefRemovalPPOnAAForBTag" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter4MaskedMeasurementTrackerEventPPOnAAForBTag = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter4ClustersRefRemovalPPOnAAForBTag" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter4PixelQuadrupletsPPOnAAForBTag = cms.EDProducer( "SeedingLayersEDProducer",
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
      skipClusters = cms.InputTag( "hltFullIter4ClustersRefRemovalPPOnAAForBTag" ),
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
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter4ClustersRefRemovalPPOnAAForBTag" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter4PixelTrackingCandRegionsForBTag = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet( 
      precise = cms.bool( True ),
      originRadius = cms.double( 1.5 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorVetex = cms.double( 0.2 ),
      zErrorBeamSpot = cms.double( 24.2 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      deltaEta = cms.double( 0.5 ),
      measurementTrackerName = cms.InputTag( "hltFullIter4MaskedMeasurementTrackerEventPPOnAAForBTag" ),
      vertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAAForBTag" ),
      maxNRegions = cms.int32( 10 ),
      ptMin = cms.double( 0.7 ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
      input = cms.InputTag( "hltSelector4CentralJetsPtCut" ),
      deltaPhi = cms.double( 0.5 ),
      maxNVertices = cms.int32( 1 ),
      mode = cms.string( "BeamSpotSigma" )
    )
)
process.hltFullIter4PixelClusterCheckPPOnAAForBTag = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 100000 ),
    ClusterCollectionLabel = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" )
)
process.hltFullIter4PixelHitDoubletsPPOnAAForBTag = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter4PixelTrackingCandRegionsForBTag" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "hltFullIter4PixelClusterCheckPPOnAAForBTag" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter4PixelQuadrupletsPPOnAAForBTag" )
)
process.hltFullIter4PixelHitQuadrupletsPPOnAAForBTag = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.0011 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplittingPPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter4PixelHitDoubletsPPOnAAForBTag" ),
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
process.hltFullIter4PixelSeedsPPOnAAForBTag = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet( 
      FilterStripHits = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      FilterAtHelixStage = cms.bool( False ),
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplittingPPOnAA" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter4PixelHitQuadrupletsPPOnAAForBTag" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter4CkfTrackCandidatesPPOnAAForBTag = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter4PixelSeedsPPOnAAForBTag" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPDetachedQuadStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter4MaskedMeasurementTrackerEventPPOnAAForBTag" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedQuadStepTrajectoryBuilderPPOnAA" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
)
process.hltFullIter4CtfWithMaterialTracksPPOnAAForBTag = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter4CkfTrackCandidatesPPOnAAForBTag" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter4MaskedMeasurementTrackerEventPPOnAAForBTag" ),
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
process.hltFullIter4TrackMVAClassifierPPOnAAForBTag = cms.EDProducer( "TrackMVAClassifierDetached",
    src = cms.InputTag( "hltFullIter4CtfWithMaterialTracksPPOnAAForBTag" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAAForBTag" ),
    qualityCuts = cms.vdouble( -0.5, 0.0, 0.5 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorDetachedQuadStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter4HighPurityTracksPPOnAAForBTag = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter4CtfWithMaterialTracksPPOnAAForBTag" ),
    originalQualVals = cms.InputTag( 'hltFullIter4TrackMVAClassifierPPOnAAForBTag','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter4TrackMVAClassifierPPOnAAForBTag','MVAValues' )
)
process.hltFullIter5ClustersRefRemovalPPOnAAForBTag = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter4HighPurityTracksPPOnAAForBTag" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter4ClustersRefRemovalPPOnAAForBTag" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltFullIter5MaskedMeasurementTrackerEventPPOnAAForBTag = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltFullIter5ClustersRefRemovalPPOnAAForBTag" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltFullIter5PixelTripletsPPOnAAForBTag = cms.EDProducer( "SeedingLayersEDProducer",
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
      skipClusters = cms.InputTag( "hltFullIter5ClustersRefRemovalPPOnAAForBTag" ),
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
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltFullIter5ClustersRefRemovalPPOnAAForBTag" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltFullIter5PixelTrackingCandRegionsForBTag = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet( 
      precise = cms.bool( True ),
      originRadius = cms.double( 1.5 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorVetex = cms.double( 0.2 ),
      zErrorBeamSpot = cms.double( 24.2 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      deltaEta = cms.double( 0.5 ),
      measurementTrackerName = cms.InputTag( "hltFullIter5MaskedMeasurementTrackerEventPPOnAAForBTag" ),
      vertexCollection = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAAForBTag" ),
      maxNRegions = cms.int32( 10 ),
      ptMin = cms.double( 0.7 ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
      input = cms.InputTag( "hltSelector4CentralJetsPtCut" ),
      deltaPhi = cms.double( 0.5 ),
      maxNVertices = cms.int32( 1 ),
      mode = cms.string( "BeamSpotSigma" )
    )
)
process.hltFullIter5PixelClusterCheckPPOnAAForBTag = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 100000 ),
    ClusterCollectionLabel = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" )
)
process.hltFullIter5PixelHitDoubletsPPOnAAForBTag = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter5PixelTrackingCandRegionsForBTag" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "hltFullIter5PixelClusterCheckPPOnAAForBTag" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltFullIter5PixelTripletsPPOnAAForBTag" )
)
process.hltFullIter5PixelHitTripletsPPOnAAForBTag = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.2 ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltFullIter5PixelHitDoubletsPPOnAAForBTag" ),
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
process.hltFullIter5PixelSeedsPPOnAAForBTag = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet( 
      FilterStripHits = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      FilterAtHelixStage = cms.bool( False ),
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplittingPPOnAA" )
    ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltFullIter5PixelHitTripletsPPOnAAForBTag" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltFullIter5CkfTrackCandidatesPPOnAAForBTag = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltFullIter5PixelSeedsPPOnAAForBTag" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPDetachedTripletStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter5MaskedMeasurementTrackerEventPPOnAAForBTag" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedTripletStepTrajectoryBuilderPPOnAA" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
)
process.hltFullIter5CtfWithMaterialTracksPPOnAAForBTag = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltFullIter5CkfTrackCandidatesPPOnAAForBTag" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltFullIter5MaskedMeasurementTrackerEventPPOnAAForBTag" ),
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
process.hltFullIter5TrackMVAClassifierPPOnAAForBTag = cms.EDProducer( "TrackMVAClassifierDetached",
    src = cms.InputTag( "hltFullIter5CtfWithMaterialTracksPPOnAAForBTag" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltFullIter0PrimaryVerticesPPOnAAForBTag" ),
    qualityCuts = cms.vdouble( -0.2, 0.3, 0.8 ),
    mva = cms.PSet( 
      GBRForestFileName = cms.string( "" ),
      GBRForestLabel = cms.string( "MVASelectorDetachedTripletStep_Phase1" )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltFullIter5HighPurityTracksPPOnAAForBTag = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltFullIter5CtfWithMaterialTracksPPOnAAForBTag" ),
    originalQualVals = cms.InputTag( 'hltFullIter5TrackMVAClassifierPPOnAAForBTag','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltFullIter5TrackMVAClassifierPPOnAAForBTag','MVAValues' )
)
process.hltFullIterativeTrackingMergedPPOnAAForBTag = cms.EDProducer( "TrackCollectionMerger",
    shareFrac = cms.double( 0.19 ),
    inputClassifiers = cms.vstring( 'hltFullIter0TrackMVAClassifierPPOnAAForBTag',
      'hltFullIter1TrackMVAClassifierPPOnAAForBTag',
      'hltFullIter2TrackMVAClassifierPPOnAAForBTag',
      'hltFullIter3TrackMVAClassifierPPOnAAForBTag',
      'hltFullIter4TrackMVAClassifierPPOnAAForBTag',
      'hltFullIter5TrackMVAClassifierPPOnAAForBTag' ),
    minQuality = cms.string( "highPurity" ),
    enableMerging = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    minShareHits = cms.uint32( 2 ),
    copyTrajectories = cms.untracked.bool( False ),
    allowFirstHitShare = cms.bool( True ),
    foundHitBonus = cms.double( 10.0 ),
    trackProducers = cms.VInputTag( 'hltFullIter0CtfWithMaterialTracksPPOnAAForBTag','hltFullIter1CtfWithMaterialTracksPPOnAAForBTag','hltFullIter2CtfWithMaterialTracksPPOnAAForBTag','hltFullIter3CtfWithMaterialTracksPPOnAAForBTag','hltFullIter4CtfWithMaterialTracksPPOnAAForBTag','hltFullIter5CtfWithMaterialTracksPPOnAAForBTag' ),
    lostHitPenalty = cms.double( 5.0 ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" )
)
process.hltFullOnlinePrimaryVerticesPPOnAAForBTag = cms.EDProducer( "PrimaryVertexProducer",
    vertexCollections = cms.VPSet( 
      cms.PSet(  chi2cutoff = cms.double( 2.5 ),
        label = cms.string( "" ),
        useBeamConstraint = cms.bool( False ),
        minNdof = cms.double( 0.0 ),
        maxDistanceToBeam = cms.double( 1.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" )
      ),
      cms.PSet(  chi2cutoff = cms.double( 2.5 ),
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
      minPt = cms.double( 0.0 ),
      minSiliconLayersWithHits = cms.int32( 5 ),
      minPixelLayersWithHits = cms.int32( 2 ),
      maxNormalizedChi2 = cms.double( 10.0 ),
      trackQuality = cms.string( "any" ),
      algorithm = cms.string( "filter" ),
      maxD0Significance = cms.double( 3.0 )
    ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltFullIterativeTrackingMergedPPOnAAForBTag" ),
    TkClusParameters = cms.PSet( 
      algorithm = cms.string( "gap" ),
      TkGapClusParameters = cms.PSet(  zSeparation = cms.double( 1.0 ) )
    )
)
process.hltFastPixelBLifetimeL3AssociatorHI = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltSelector4CentralJetsPtCut" ),
    tracks = cms.InputTag( "hltFullIterativeTrackingMergedPPOnAAForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
process.hltImpactParameterTagInfosHI = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.2 ),
    minimumNumberOfHits = cms.int32( 3 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    primaryVertex = cms.InputTag( "hltFullOnlinePrimaryVerticesPPOnAAForBTag" ),
    maximumLongitudinalImpactParameter = cms.double( 17.0 ),
    computeGhostTrack = cms.bool( True ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltFastPixelBLifetimeL3AssociatorHI" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( True ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 5.0 )
)
process.hltInclusiveVertexFinderPPOnAA = cms.EDProducer( "InclusiveVertexFinder",
    fitterSigmacut = cms.double( 3.0 ),
    vertexReco = cms.PSet( 
      primcut = cms.double( 1.0 ),
      seccut = cms.double( 3.0 ),
      finder = cms.string( "avr" ),
      smoothing = cms.bool( True )
    ),
    fitterTini = cms.double( 256.0 ),
    fitterRatio = cms.double( 0.25 ),
    vertexMinDLen2DSig = cms.double( 2.5 ),
    maximumLongitudinalImpactParameter = cms.double( 0.3 ),
    vertexMinAngleCosine = cms.double( 0.95 ),
    primaryVertices = cms.InputTag( "hltFullOnlinePrimaryVerticesPPOnAAForBTag" ),
    tracks = cms.InputTag( "hltFullIterativeTrackingMergedPPOnAAForBTag" ),
    minPt = cms.double( 0.8 ),
    maxNTracks = cms.uint32( 30 ),
    clusterizer = cms.PSet( 
      distanceRatio = cms.double( 20.0 ),
      clusterMaxDistance = cms.double( 0.05 ),
      seedMax3DIPSignificance = cms.double( 9999.0 ),
      clusterMaxSignificance = cms.double( 4.5 ),
      seedMin3DIPSignificance = cms.double( 1.2 ),
      clusterMinAngleCosine = cms.double( 0.5 ),
      seedMin3DIPValue = cms.double( 0.005 ),
      seedMax3DIPValue = cms.double( 9999.0 )
    ),
    useVertexReco = cms.bool( True ),
    vertexMinDLenSig = cms.double( 0.5 ),
    useDirectVertexFitter = cms.bool( True ),
    minHits = cms.uint32( 8 ),
    maximumTimeSignificance = cms.double( 3.0 ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
)
process.hltInclusiveSecondaryVerticesPPOnAA = cms.EDProducer( "VertexMerger",
    minSignificance = cms.double( 2.0 ),
    secondaryVertices = cms.InputTag( "hltInclusiveVertexFinderPPOnAA" ),
    maxFraction = cms.double( 0.7 )
)
process.hltTrackVertexArbitratorPPOnAA = cms.EDProducer( "TrackVertexArbitrator",
    fitterSigmacut = cms.double( 3.0 ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    fitterTini = cms.double( 256.0 ),
    trackMinLayers = cms.int32( 4 ),
    fitterRatio = cms.double( 0.25 ),
    secondaryVertices = cms.InputTag( "hltInclusiveSecondaryVerticesPPOnAA" ),
    sigCut = cms.double( 5.0 ),
    distCut = cms.double( 0.04 ),
    trackMinPt = cms.double( 0.4 ),
    primaryVertices = cms.InputTag( "hltFullOnlinePrimaryVerticesPPOnAAForBTag" ),
    tracks = cms.InputTag( "hltFullIterativeTrackingMergedPPOnAAForBTag" ),
    dLenFraction = cms.double( 0.333 ),
    trackMinPixels = cms.int32( 1 ),
    maxTimeSignificance = cms.double( 3.5 ),
    dRCut = cms.double( 0.4 )
)
process.hltInclusiveMergedVerticesPPOnAA = cms.EDProducer( "VertexMerger",
    minSignificance = cms.double( 10.0 ),
    secondaryVertices = cms.InputTag( "hltTrackVertexArbitratorPPOnAA" ),
    maxFraction = cms.double( 0.2 )
)
process.hltInclusiveSecondaryVertexFinderTagInfosHI = cms.EDProducer( "SecondaryVertexProducer",
    extSVDeltaRToJet = cms.double( 0.3 ),
    beamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    vertexReco = cms.PSet( 
      primcut = cms.double( 1.8 ),
      seccut = cms.double( 6.0 ),
      finder = cms.string( "avr" ),
      weightthreshold = cms.double( 0.001 ),
      minweight = cms.double( 0.5 ),
      smoothing = cms.bool( False )
    ),
    vertexSelection = cms.PSet(  sortCriterium = cms.string( "dist3dError" ) ),
    constraint = cms.string( "BeamSpot" ),
    trackIPTagInfos = cms.InputTag( "hltImpactParameterTagInfosHI" ),
    vertexCuts = cms.PSet( 
      distSig2dMin = cms.double( 2.0 ),
      useTrackWeights = cms.bool( True ),
      distVal3dMax = cms.double( 99999.9 ),
      massMax = cms.double( 6.5 ),
      distSig3dMax = cms.double( 99999.9 ),
      distVal2dMin = cms.double( 0.01 ),
      minimumTrackWeight = cms.double( 0.5 ),
      v0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
      distSig2dMax = cms.double( 99999.9 ),
      distSig3dMin = cms.double( -99999.9 ),
      fracPV = cms.double( 0.79 ),
      maxDeltaRToJetAxis = cms.double( 0.5 ),
      distVal2dMax = cms.double( 2.5 ),
      distVal3dMin = cms.double( -99999.9 ),
      multiplicityMin = cms.uint32( 2 )
    ),
    useExternalSV = cms.bool( True ),
    minimumTrackWeight = cms.double( 0.5 ),
    usePVError = cms.bool( True ),
    trackSelection = cms.PSet( 
      max_pT_dRcut = cms.double( 0.1 ),
      b_dR = cms.double( 0.6263 ),
      min_pT = cms.double( 120.0 ),
      b_pT = cms.double( 0.3684 ),
      ptMin = cms.double( 1.0 ),
      max_pT_trackPTcut = cms.double( 3.0 ),
      max_pT = cms.double( 500.0 ),
      useVariableJTA = cms.bool( False ),
      maxDecayLen = cms.double( 99999.9 ),
      qualityClass = cms.string( "any" ),
      normChi2Max = cms.double( 99999.9 ),
      sip2dValMin = cms.double( -99999.9 ),
      sip3dValMin = cms.double( -99999.9 ),
      a_dR = cms.double( -0.001053 ),
      maxDistToAxis = cms.double( 0.2 ),
      totalHitsMin = cms.uint32( 2 ),
      a_pT = cms.double( 0.005263 ),
      sip2dSigMax = cms.double( 99999.9 ),
      sip2dValMax = cms.double( 99999.9 ),
      sip3dSigMax = cms.double( 99999.9 ),
      sip3dValMax = cms.double( 99999.9 ),
      min_pT_dRcut = cms.double( 0.5 ),
      jetDeltaRMax = cms.double( 0.3 ),
      pixelHitsMin = cms.uint32( 2 ),
      sip3dSigMin = cms.double( -99999.9 ),
      sip2dSigMin = cms.double( -99999.9 )
    ),
    trackSort = cms.string( "sip3dSig" ),
    extSVCollection = cms.InputTag( "hltInclusiveMergedVerticesPPOnAA" )
)
process.hltDeepCombinedSecondaryVertexBJetTagsInfosCaloHIBJet60 = cms.EDProducer( "TrackDeepNNTagInfoProducer",
    computer = cms.PSet( 
      trackFlip = cms.bool( False ),
      useTrackWeights = cms.bool( True ),
      trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
      SoftLeptonFlip = cms.bool( False ),
      pseudoMultiplicityMin = cms.uint32( 2 ),
      correctVertexMass = cms.bool( True ),
      minimumTrackWeight = cms.double( 0.5 ),
      charmCut = cms.double( 1.5 ),
      trackPseudoSelection = cms.PSet( 
        max_pT_dRcut = cms.double( 0.1 ),
        b_dR = cms.double( 0.6263 ),
        min_pT = cms.double( 120.0 ),
        b_pT = cms.double( 0.3684 ),
        ptMin = cms.double( 0.0 ),
        max_pT_trackPTcut = cms.double( 3.0 ),
        max_pT = cms.double( 500.0 ),
        useVariableJTA = cms.bool( False ),
        maxDecayLen = cms.double( 5.0 ),
        qualityClass = cms.string( "any" ),
        normChi2Max = cms.double( 99999.9 ),
        sip2dValMin = cms.double( -99999.9 ),
        sip3dValMin = cms.double( -99999.9 ),
        a_dR = cms.double( -0.001053 ),
        maxDistToAxis = cms.double( 0.07 ),
        totalHitsMin = cms.uint32( 0 ),
        a_pT = cms.double( 0.005263 ),
        sip2dSigMax = cms.double( 99999.9 ),
        sip2dValMax = cms.double( 99999.9 ),
        sip3dSigMax = cms.double( 99999.9 ),
        sip3dValMax = cms.double( 99999.9 ),
        min_pT_dRcut = cms.double( 0.5 ),
        jetDeltaRMax = cms.double( 0.3 ),
        pixelHitsMin = cms.uint32( 0 ),
        sip3dSigMin = cms.double( -99999.9 ),
        sip2dSigMin = cms.double( 2.0 )
      ),
      trackSelection = cms.PSet( 
        max_pT_dRcut = cms.double( 0.1 ),
        b_dR = cms.double( 0.6263 ),
        min_pT = cms.double( 120.0 ),
        b_pT = cms.double( 0.3684 ),
        ptMin = cms.double( 0.0 ),
        max_pT_trackPTcut = cms.double( 3.0 ),
        max_pT = cms.double( 500.0 ),
        useVariableJTA = cms.bool( False ),
        maxDecayLen = cms.double( 5.0 ),
        qualityClass = cms.string( "any" ),
        normChi2Max = cms.double( 99999.9 ),
        sip2dValMin = cms.double( -99999.9 ),
        sip3dValMin = cms.double( -99999.9 ),
        a_dR = cms.double( -0.001053 ),
        maxDistToAxis = cms.double( 0.07 ),
        totalHitsMin = cms.uint32( 0 ),
        a_pT = cms.double( 0.005263 ),
        sip2dSigMax = cms.double( 99999.9 ),
        sip2dValMax = cms.double( 99999.9 ),
        sip3dSigMax = cms.double( 99999.9 ),
        sip3dValMax = cms.double( 99999.9 ),
        min_pT_dRcut = cms.double( 0.5 ),
        jetDeltaRMax = cms.double( 0.3 ),
        pixelHitsMin = cms.uint32( 0 ),
        sip3dSigMin = cms.double( -99999.9 ),
        sip2dSigMin = cms.double( -99999.9 )
      ),
      pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
      trackSort = cms.string( "sip2dSig" ),
      trackMultiplicityMin = cms.uint32( 2 ),
      vertexFlip = cms.bool( False )
    ),
    svTagInfos = cms.InputTag( "hltInclusiveSecondaryVertexFinderTagInfosHI" )
)
process.hltDeepCombinedSecondaryVertexBJetTagsCaloBJet60 = cms.EDProducer( "DeepFlavourJetTagsProducer",
    src = cms.InputTag( "hltDeepCombinedSecondaryVertexBJetTagsInfosCaloHIBJet60" ),
    checkSVForDefaults = cms.bool( True ),
    toAdd = cms.PSet(  probbb = cms.string( "probb" ) ),
    NNConfig = cms.FileInPath( "RecoBTag/Combined/data/DeepCSV_PhaseI.json" ),
    meanPadding = cms.bool( True )
)
process.hltBTagCaloDeepCSV0p71SingleJet60 = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsCaloBJet60','probb' ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltSelector4CentralJetsPtCut" ),
    MinTag = cms.double( 0.52 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltPreHIPuAK4CaloJet80Eta2p4DeepCSV0p71 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet80Eta2p4 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.4 ),
    MinEta = cms.double( -2.4 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 80.0 )
)
process.hltSelectorJets80 = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    etMin = cms.double( 80.0 )
)
process.hltSelectorCentralJets80 = cms.EDFilter( "EtaRangeCaloJetSelector",
    src = cms.InputTag( "hltSelectorJets80" ),
    etaMin = cms.double( -2.4 ),
    etaMax = cms.double( 2.4 )
)
process.hltSelector4CentralJetsPtCut80 = cms.EDFilter( "LargestEtCaloJetSelector",
    maxNumber = cms.uint32( 4 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelectorCentralJets80" )
)
process.hltFastPixelBLifetimeL3AssociatorHIBJet80 = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltSelector4CentralJetsPtCut80" ),
    tracks = cms.InputTag( "hltFullIterativeTrackingMergedPPOnAAForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
process.hltImpactParameterTagInfosHIBJet80 = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.2 ),
    minimumNumberOfHits = cms.int32( 3 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    primaryVertex = cms.InputTag( "hltFullOnlinePrimaryVerticesPPOnAAForBTag" ),
    maximumLongitudinalImpactParameter = cms.double( 17.0 ),
    computeGhostTrack = cms.bool( True ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltFastPixelBLifetimeL3AssociatorHIBJet80" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( True ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 5.0 )
)
process.hltInclusiveSecondaryVertexFinderTagInfosHIBJet80 = cms.EDProducer( "SecondaryVertexProducer",
    extSVDeltaRToJet = cms.double( 0.3 ),
    beamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    vertexReco = cms.PSet( 
      primcut = cms.double( 1.8 ),
      seccut = cms.double( 6.0 ),
      finder = cms.string( "avr" ),
      weightthreshold = cms.double( 0.001 ),
      minweight = cms.double( 0.5 ),
      smoothing = cms.bool( False )
    ),
    vertexSelection = cms.PSet(  sortCriterium = cms.string( "dist3dError" ) ),
    constraint = cms.string( "BeamSpot" ),
    trackIPTagInfos = cms.InputTag( "hltImpactParameterTagInfosHIBJet80" ),
    vertexCuts = cms.PSet( 
      distSig2dMin = cms.double( 2.0 ),
      useTrackWeights = cms.bool( True ),
      distVal3dMax = cms.double( 99999.9 ),
      massMax = cms.double( 6.5 ),
      distSig3dMax = cms.double( 99999.9 ),
      distVal2dMin = cms.double( 0.01 ),
      minimumTrackWeight = cms.double( 0.5 ),
      v0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
      distSig2dMax = cms.double( 99999.9 ),
      distSig3dMin = cms.double( -99999.9 ),
      fracPV = cms.double( 0.79 ),
      maxDeltaRToJetAxis = cms.double( 0.5 ),
      distVal2dMax = cms.double( 2.5 ),
      distVal3dMin = cms.double( -99999.9 ),
      multiplicityMin = cms.uint32( 2 )
    ),
    useExternalSV = cms.bool( True ),
    minimumTrackWeight = cms.double( 0.5 ),
    usePVError = cms.bool( True ),
    trackSelection = cms.PSet( 
      max_pT_dRcut = cms.double( 0.1 ),
      b_dR = cms.double( 0.6263 ),
      min_pT = cms.double( 120.0 ),
      b_pT = cms.double( 0.3684 ),
      ptMin = cms.double( 1.0 ),
      max_pT_trackPTcut = cms.double( 3.0 ),
      max_pT = cms.double( 500.0 ),
      useVariableJTA = cms.bool( False ),
      maxDecayLen = cms.double( 99999.9 ),
      qualityClass = cms.string( "any" ),
      normChi2Max = cms.double( 99999.9 ),
      sip2dValMin = cms.double( -99999.9 ),
      sip3dValMin = cms.double( -99999.9 ),
      a_dR = cms.double( -0.001053 ),
      maxDistToAxis = cms.double( 0.2 ),
      totalHitsMin = cms.uint32( 2 ),
      a_pT = cms.double( 0.005263 ),
      sip2dSigMax = cms.double( 99999.9 ),
      sip2dValMax = cms.double( 99999.9 ),
      sip3dSigMax = cms.double( 99999.9 ),
      sip3dValMax = cms.double( 99999.9 ),
      min_pT_dRcut = cms.double( 0.5 ),
      jetDeltaRMax = cms.double( 0.3 ),
      pixelHitsMin = cms.uint32( 2 ),
      sip3dSigMin = cms.double( -99999.9 ),
      sip2dSigMin = cms.double( -99999.9 )
    ),
    trackSort = cms.string( "sip3dSig" ),
    extSVCollection = cms.InputTag( "hltInclusiveMergedVerticesPPOnAA" )
)
process.hltDeepCombinedSecondaryVertexBJetTagsInfosCaloHIBJet80 = cms.EDProducer( "TrackDeepNNTagInfoProducer",
    computer = cms.PSet( 
      trackFlip = cms.bool( False ),
      useTrackWeights = cms.bool( True ),
      trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
      SoftLeptonFlip = cms.bool( False ),
      pseudoMultiplicityMin = cms.uint32( 2 ),
      correctVertexMass = cms.bool( True ),
      minimumTrackWeight = cms.double( 0.5 ),
      charmCut = cms.double( 1.5 ),
      trackPseudoSelection = cms.PSet( 
        max_pT_dRcut = cms.double( 0.1 ),
        b_dR = cms.double( 0.6263 ),
        min_pT = cms.double( 120.0 ),
        b_pT = cms.double( 0.3684 ),
        ptMin = cms.double( 0.0 ),
        max_pT_trackPTcut = cms.double( 3.0 ),
        max_pT = cms.double( 500.0 ),
        useVariableJTA = cms.bool( False ),
        maxDecayLen = cms.double( 5.0 ),
        qualityClass = cms.string( "any" ),
        normChi2Max = cms.double( 99999.9 ),
        sip2dValMin = cms.double( -99999.9 ),
        sip3dValMin = cms.double( -99999.9 ),
        a_dR = cms.double( -0.001053 ),
        maxDistToAxis = cms.double( 0.07 ),
        totalHitsMin = cms.uint32( 0 ),
        a_pT = cms.double( 0.005263 ),
        sip2dSigMax = cms.double( 99999.9 ),
        sip2dValMax = cms.double( 99999.9 ),
        sip3dSigMax = cms.double( 99999.9 ),
        sip3dValMax = cms.double( 99999.9 ),
        min_pT_dRcut = cms.double( 0.5 ),
        jetDeltaRMax = cms.double( 0.3 ),
        pixelHitsMin = cms.uint32( 0 ),
        sip3dSigMin = cms.double( -99999.9 ),
        sip2dSigMin = cms.double( 2.0 )
      ),
      trackSelection = cms.PSet( 
        max_pT_dRcut = cms.double( 0.1 ),
        b_dR = cms.double( 0.6263 ),
        min_pT = cms.double( 120.0 ),
        b_pT = cms.double( 0.3684 ),
        ptMin = cms.double( 0.0 ),
        max_pT_trackPTcut = cms.double( 3.0 ),
        max_pT = cms.double( 500.0 ),
        useVariableJTA = cms.bool( False ),
        maxDecayLen = cms.double( 5.0 ),
        qualityClass = cms.string( "any" ),
        normChi2Max = cms.double( 99999.9 ),
        sip2dValMin = cms.double( -99999.9 ),
        sip3dValMin = cms.double( -99999.9 ),
        a_dR = cms.double( -0.001053 ),
        maxDistToAxis = cms.double( 0.07 ),
        totalHitsMin = cms.uint32( 0 ),
        a_pT = cms.double( 0.005263 ),
        sip2dSigMax = cms.double( 99999.9 ),
        sip2dValMax = cms.double( 99999.9 ),
        sip3dSigMax = cms.double( 99999.9 ),
        sip3dValMax = cms.double( 99999.9 ),
        min_pT_dRcut = cms.double( 0.5 ),
        jetDeltaRMax = cms.double( 0.3 ),
        pixelHitsMin = cms.uint32( 0 ),
        sip3dSigMin = cms.double( -99999.9 ),
        sip2dSigMin = cms.double( -99999.9 )
      ),
      pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
      trackSort = cms.string( "sip2dSig" ),
      trackMultiplicityMin = cms.uint32( 2 ),
      vertexFlip = cms.bool( False )
    ),
    svTagInfos = cms.InputTag( "hltInclusiveSecondaryVertexFinderTagInfosHIBJet80" )
)
process.hltDeepCombinedSecondaryVertexBJetTagsCaloBJet80 = cms.EDProducer( "DeepFlavourJetTagsProducer",
    src = cms.InputTag( "hltDeepCombinedSecondaryVertexBJetTagsInfosCaloHIBJet80" ),
    checkSVForDefaults = cms.bool( True ),
    toAdd = cms.PSet(  probbb = cms.string( "probb" ) ),
    NNConfig = cms.FileInPath( "RecoBTag/Combined/data/DeepCSV_PhaseI.json" ),
    meanPadding = cms.bool( True )
)
process.hltBTagCaloDeepCSV0p71SingleJet80 = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsCaloBJet80','probb' ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltSelector4CentralJetsPtCut80" ),
    MinTag = cms.double( 0.52 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltPreHIPuAK4CaloJet100Eta2p4DeepCSV0p71 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet100Eta2p4 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.4 ),
    MinEta = cms.double( -2.4 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 100.0 )
)
process.hltSelectorJets100 = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    etMin = cms.double( 100.0 )
)
process.hltSelectorCentralJets100 = cms.EDFilter( "EtaRangeCaloJetSelector",
    src = cms.InputTag( "hltSelectorJets100" ),
    etaMin = cms.double( -2.4 ),
    etaMax = cms.double( 2.4 )
)
process.hltSelector4CentralJetsPtCut100 = cms.EDFilter( "LargestEtCaloJetSelector",
    maxNumber = cms.uint32( 4 ),
    filter = cms.bool( False ),
    src = cms.InputTag( "hltSelectorCentralJets100" )
)
process.hltFastPixelBLifetimeL3AssociatorHIBJet100 = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( "hltSelector4CentralJetsPtCut100" ),
    tracks = cms.InputTag( "hltFullIterativeTrackingMergedPPOnAAForBTag" ),
    useAssigned = cms.bool( False ),
    coneSize = cms.double( 0.4 ),
    pvSrc = cms.InputTag( "" )
)
process.hltImpactParameterTagInfosHIBJet100 = cms.EDProducer( "TrackIPProducer",
    maximumTransverseImpactParameter = cms.double( 0.2 ),
    minimumNumberOfHits = cms.int32( 3 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    primaryVertex = cms.InputTag( "hltFullOnlinePrimaryVerticesPPOnAAForBTag" ),
    maximumLongitudinalImpactParameter = cms.double( 17.0 ),
    computeGhostTrack = cms.bool( True ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    jetTracks = cms.InputTag( "hltFastPixelBLifetimeL3AssociatorHIBJet100" ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    jetDirectionUsingTracks = cms.bool( False ),
    computeProbabilities = cms.bool( True ),
    useTrackQuality = cms.bool( False ),
    maximumChiSquared = cms.double( 5.0 )
)
process.hltInclusiveSecondaryVertexFinderTagInfosHIBJet100 = cms.EDProducer( "SecondaryVertexProducer",
    extSVDeltaRToJet = cms.double( 0.3 ),
    beamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    vertexReco = cms.PSet( 
      primcut = cms.double( 1.8 ),
      seccut = cms.double( 6.0 ),
      finder = cms.string( "avr" ),
      weightthreshold = cms.double( 0.001 ),
      minweight = cms.double( 0.5 ),
      smoothing = cms.bool( False )
    ),
    vertexSelection = cms.PSet(  sortCriterium = cms.string( "dist3dError" ) ),
    constraint = cms.string( "BeamSpot" ),
    trackIPTagInfos = cms.InputTag( "hltImpactParameterTagInfosHIBJet100" ),
    vertexCuts = cms.PSet( 
      distSig2dMin = cms.double( 2.0 ),
      useTrackWeights = cms.bool( True ),
      distVal3dMax = cms.double( 99999.9 ),
      massMax = cms.double( 6.5 ),
      distSig3dMax = cms.double( 99999.9 ),
      distVal2dMin = cms.double( 0.01 ),
      minimumTrackWeight = cms.double( 0.5 ),
      v0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
      distSig2dMax = cms.double( 99999.9 ),
      distSig3dMin = cms.double( -99999.9 ),
      fracPV = cms.double( 0.79 ),
      maxDeltaRToJetAxis = cms.double( 0.5 ),
      distVal2dMax = cms.double( 2.5 ),
      distVal3dMin = cms.double( -99999.9 ),
      multiplicityMin = cms.uint32( 2 )
    ),
    useExternalSV = cms.bool( True ),
    minimumTrackWeight = cms.double( 0.5 ),
    usePVError = cms.bool( True ),
    trackSelection = cms.PSet( 
      max_pT_dRcut = cms.double( 0.1 ),
      b_dR = cms.double( 0.6263 ),
      min_pT = cms.double( 120.0 ),
      b_pT = cms.double( 0.3684 ),
      ptMin = cms.double( 1.0 ),
      max_pT_trackPTcut = cms.double( 3.0 ),
      max_pT = cms.double( 500.0 ),
      useVariableJTA = cms.bool( False ),
      maxDecayLen = cms.double( 99999.9 ),
      qualityClass = cms.string( "any" ),
      normChi2Max = cms.double( 99999.9 ),
      sip2dValMin = cms.double( -99999.9 ),
      sip3dValMin = cms.double( -99999.9 ),
      a_dR = cms.double( -0.001053 ),
      maxDistToAxis = cms.double( 0.2 ),
      totalHitsMin = cms.uint32( 2 ),
      a_pT = cms.double( 0.005263 ),
      sip2dSigMax = cms.double( 99999.9 ),
      sip2dValMax = cms.double( 99999.9 ),
      sip3dSigMax = cms.double( 99999.9 ),
      sip3dValMax = cms.double( 99999.9 ),
      min_pT_dRcut = cms.double( 0.5 ),
      jetDeltaRMax = cms.double( 0.3 ),
      pixelHitsMin = cms.uint32( 2 ),
      sip3dSigMin = cms.double( -99999.9 ),
      sip2dSigMin = cms.double( -99999.9 )
    ),
    trackSort = cms.string( "sip3dSig" ),
    extSVCollection = cms.InputTag( "hltInclusiveMergedVerticesPPOnAA" )
)
process.hltDeepCombinedSecondaryVertexBJetTagsInfosCaloHIBJet100 = cms.EDProducer( "TrackDeepNNTagInfoProducer",
    computer = cms.PSet( 
      trackFlip = cms.bool( False ),
      useTrackWeights = cms.bool( True ),
      trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
      SoftLeptonFlip = cms.bool( False ),
      pseudoMultiplicityMin = cms.uint32( 2 ),
      correctVertexMass = cms.bool( True ),
      minimumTrackWeight = cms.double( 0.5 ),
      charmCut = cms.double( 1.5 ),
      trackPseudoSelection = cms.PSet( 
        max_pT_dRcut = cms.double( 0.1 ),
        b_dR = cms.double( 0.6263 ),
        min_pT = cms.double( 120.0 ),
        b_pT = cms.double( 0.3684 ),
        ptMin = cms.double( 0.0 ),
        max_pT_trackPTcut = cms.double( 3.0 ),
        max_pT = cms.double( 500.0 ),
        useVariableJTA = cms.bool( False ),
        maxDecayLen = cms.double( 5.0 ),
        qualityClass = cms.string( "any" ),
        normChi2Max = cms.double( 99999.9 ),
        sip2dValMin = cms.double( -99999.9 ),
        sip3dValMin = cms.double( -99999.9 ),
        a_dR = cms.double( -0.001053 ),
        maxDistToAxis = cms.double( 0.07 ),
        totalHitsMin = cms.uint32( 0 ),
        a_pT = cms.double( 0.005263 ),
        sip2dSigMax = cms.double( 99999.9 ),
        sip2dValMax = cms.double( 99999.9 ),
        sip3dSigMax = cms.double( 99999.9 ),
        sip3dValMax = cms.double( 99999.9 ),
        min_pT_dRcut = cms.double( 0.5 ),
        jetDeltaRMax = cms.double( 0.3 ),
        pixelHitsMin = cms.uint32( 0 ),
        sip3dSigMin = cms.double( -99999.9 ),
        sip2dSigMin = cms.double( 2.0 )
      ),
      trackSelection = cms.PSet( 
        max_pT_dRcut = cms.double( 0.1 ),
        b_dR = cms.double( 0.6263 ),
        min_pT = cms.double( 120.0 ),
        b_pT = cms.double( 0.3684 ),
        ptMin = cms.double( 0.0 ),
        max_pT_trackPTcut = cms.double( 3.0 ),
        max_pT = cms.double( 500.0 ),
        useVariableJTA = cms.bool( False ),
        maxDecayLen = cms.double( 5.0 ),
        qualityClass = cms.string( "any" ),
        normChi2Max = cms.double( 99999.9 ),
        sip2dValMin = cms.double( -99999.9 ),
        sip3dValMin = cms.double( -99999.9 ),
        a_dR = cms.double( -0.001053 ),
        maxDistToAxis = cms.double( 0.07 ),
        totalHitsMin = cms.uint32( 0 ),
        a_pT = cms.double( 0.005263 ),
        sip2dSigMax = cms.double( 99999.9 ),
        sip2dValMax = cms.double( 99999.9 ),
        sip3dSigMax = cms.double( 99999.9 ),
        sip3dValMax = cms.double( 99999.9 ),
        min_pT_dRcut = cms.double( 0.5 ),
        jetDeltaRMax = cms.double( 0.3 ),
        pixelHitsMin = cms.uint32( 0 ),
        sip3dSigMin = cms.double( -99999.9 ),
        sip2dSigMin = cms.double( -99999.9 )
      ),
      pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
      trackSort = cms.string( "sip2dSig" ),
      trackMultiplicityMin = cms.uint32( 2 ),
      vertexFlip = cms.bool( False )
    ),
    svTagInfos = cms.InputTag( "hltInclusiveSecondaryVertexFinderTagInfosHIBJet100" )
)
process.hltDeepCombinedSecondaryVertexBJetTagsCaloBJet100 = cms.EDProducer( "DeepFlavourJetTagsProducer",
    src = cms.InputTag( "hltDeepCombinedSecondaryVertexBJetTagsInfosCaloHIBJet100" ),
    checkSVForDefaults = cms.bool( True ),
    toAdd = cms.PSet(  probbb = cms.string( "probb" ) ),
    NNConfig = cms.FileInPath( "RecoBTag/Combined/data/DeepCSV_PhaseI.json" ),
    meanPadding = cms.bool( True )
)
process.hltBTagCaloDeepCSV0p71SingleJet100 = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( 'hltDeepCombinedSecondaryVertexBJetTagsCaloBJet100','probb' ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltSelector4CentralJetsPtCut100" ),
    MinTag = cms.double( 0.52 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltPreHIPuAK4CaloJet60Eta2p4CSVv2WP0p8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltCombinedSecondaryVertexV2BJetTagsCalo = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltCombinedSecondaryVertexV2" ),
    tagInfos = cms.VInputTag( 'hltImpactParameterTagInfosHI','hltInclusiveSecondaryVertexFinderTagInfosHI' )
)
process.hltBTagCaloCSVv2WP0p8SingleJet60HI = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltCombinedSecondaryVertexV2BJetTagsCalo" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltSelector4CentralJetsPtCut" ),
    MinTag = cms.double( 0.8 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltPreHIPuAK4CaloJet80Eta2p4CSVv2WP0p8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltCombinedSecondaryVertexV2BJetTagsCaloBJet80 = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltCombinedSecondaryVertexV2" ),
    tagInfos = cms.VInputTag( 'hltImpactParameterTagInfosHIBJet80','hltInclusiveSecondaryVertexFinderTagInfosHIBJet80' )
)
process.hltBTagCaloCSVv2WP0p8SingleJet80HI = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltCombinedSecondaryVertexV2BJetTagsCaloBJet80" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltSelector4CentralJetsPtCut80" ),
    MinTag = cms.double( 0.8 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltPreHIPuAK4CaloJet100Eta2p4CSVv2WP0p8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltCombinedSecondaryVertexV2BJetTagsCaloBJet100 = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltCombinedSecondaryVertexV2" ),
    tagInfos = cms.VInputTag( 'hltImpactParameterTagInfosHIBJet100','hltInclusiveSecondaryVertexFinderTagInfosHIBJet100' )
)
process.hltBTagCaloCSVv2WP0p8SingleJet100HI = cms.EDFilter( "HLTCaloJetTag",
    saveTags = cms.bool( True ),
    MinJets = cms.int32( 1 ),
    JetTags = cms.InputTag( "hltCombinedSecondaryVertexV2BJetTagsCaloBJet100" ),
    TriggerType = cms.int32( 86 ),
    Jets = cms.InputTag( "hltSelector4CentralJetsPtCut100" ),
    MinTag = cms.double( 0.8 ),
    MaxTag = cms.double( 99999.0 )
)
process.hltL1sSingleJet28Centrality30100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet28_Centrality_30_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet40Eta5p1Centrality30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleJet44Centrality30100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet44_Centrality_30_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet60Eta5p1Centrality30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleJet56Centrality30100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet56_Centrality_30_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet80Eta5p1Centrality30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleJet60Centrality30100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet60_Centrality_30_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet100Eta5p1Centrality30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleJet28Centrality50100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet28_Centrality_50_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet40Eta5p1Centrality50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleJet44Centrality50100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet44_Centrality_50_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet60Eta5p1Centrality50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleJet56Centrality50100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet56_Centrality_50_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHIPuAK4CaloJet80Eta5p1Centrality50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleJet60Centrality50100BptxAND = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet60_Centrality_50_100_BptxAND" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHLTHIPuAK4CaloJet100Eta5p1Centrality50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHICsAK4PFJet60Eta1p5Centrality30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet60Eta1p5 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( False ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 60.0 )
)
process.hltAK4CaloJetsPF = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    useMassDropTagger = cms.bool( False ),
    doAreaFastjet = cms.bool( False ),
    muMin = cms.double( -1.0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    subtractorName = cms.string( "" ),
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
    minSeed = cms.uint32( 0 ),
    voronoiRfact = cms.double( -9.0 ),
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
    jetPtMin = cms.double( 1.0 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "NotUsed" ),
    verbosity = cms.int32( 0 ),
    inputEtMin = cms.double( 0.3 ),
    useConstituentSubtraction = cms.bool( False ),
    beta = cms.double( -1.0 ),
    trimPtFracMin = cms.double( -1.0 ),
    radiusPU = cms.double( 0.4 ),
    nFilt = cms.int32( -1 ),
    useKtPruning = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    useCMSBoostedTauSeedingAlgorithm = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    writeJetsWithConst = cms.bool( False ),
    inputEMin = cms.double( 0.0 )
)
process.hltAK4CaloJetsPFEt5 = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltAK4CaloJetsPF" ),
    etMin = cms.double( 5.0 )
)
process.hltMuonDTDigis = cms.EDProducer( "DTuROSRawToDigi",
    debug = cms.untracked.bool( False ),
    inputLabel = cms.InputTag( "rawDataCollector" )
)
process.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    debug = cms.untracked.bool( False ),
    recAlgoConfig = cms.PSet( 
      maxTime = cms.double( 420.0 ),
      debug = cms.untracked.bool( False ),
      stepTwoFromDigi = cms.bool( False ),
      tTrigModeConfig = cms.PSet( 
        debug = cms.untracked.bool( False ),
        tofCorrType = cms.int32( 0 ),
        tTrigLabel = cms.string( "" ),
        wirePropCorrType = cms.int32( 0 ),
        doTOFCorrection = cms.bool( True ),
        vPropWire = cms.double( 24.4 ),
        doT0Correction = cms.bool( True ),
        doWirePropCorrection = cms.bool( True )
      ),
      useUncertDB = cms.bool( True ),
      doVdriftCorr = cms.bool( True ),
      minTime = cms.double( -3.0 ),
      tTrigMode = cms.string( "DTTTrigSyncFromDB" )
    ),
    dtDigiLabel = cms.InputTag( "hltMuonDTDigis" ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" )
)
process.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    debug = cms.untracked.bool( False ),
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    recHits2DLabel = cms.InputTag( "dt2DSegments" ),
    recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
    Reco4DAlgoConfig = cms.PSet( 
      Reco2DAlgoConfig = cms.PSet( 
        AlphaMaxPhi = cms.double( 1.0 ),
        debug = cms.untracked.bool( False ),
        segmCleanerMode = cms.int32( 2 ),
        AlphaMaxTheta = cms.double( 0.9 ),
        hit_afterT0_resolution = cms.double( 0.03 ),
        performT0_vdriftSegCorrection = cms.bool( False ),
        recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
        recAlgoConfig = cms.PSet( 
          maxTime = cms.double( 420.0 ),
          debug = cms.untracked.bool( False ),
          stepTwoFromDigi = cms.bool( False ),
          tTrigModeConfig = cms.PSet( 
            debug = cms.untracked.bool( False ),
            tofCorrType = cms.int32( 0 ),
            tTrigLabel = cms.string( "" ),
            wirePropCorrType = cms.int32( 0 ),
            doTOFCorrection = cms.bool( True ),
            vPropWire = cms.double( 24.4 ),
            doT0Correction = cms.bool( True ),
            doWirePropCorrection = cms.bool( True )
          ),
          useUncertDB = cms.bool( True ),
          doVdriftCorr = cms.bool( True ),
          minTime = cms.double( -3.0 ),
          tTrigMode = cms.string( "DTTTrigSyncFromDB" )
        ),
        MaxAllowedHits = cms.uint32( 50 ),
        nUnSharedHitsMin = cms.int32( 2 ),
        nSharedHitsMax = cms.int32( 2 ),
        performT0SegCorrection = cms.bool( False ),
        perform_delta_rejecting = cms.bool( False )
      ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      debug = cms.untracked.bool( False ),
      segmCleanerMode = cms.int32( 2 ),
      AllDTRecHits = cms.bool( True ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      recAlgoConfig = cms.PSet( 
        maxTime = cms.double( 420.0 ),
        debug = cms.untracked.bool( False ),
        stepTwoFromDigi = cms.bool( False ),
        tTrigModeConfig = cms.PSet( 
          debug = cms.untracked.bool( False ),
          tofCorrType = cms.int32( 0 ),
          tTrigLabel = cms.string( "" ),
          wirePropCorrType = cms.int32( 0 ),
          doTOFCorrection = cms.bool( True ),
          vPropWire = cms.double( 24.4 ),
          doT0Correction = cms.bool( True ),
          doWirePropCorrection = cms.bool( True )
        ),
        useUncertDB = cms.bool( True ),
        doVdriftCorr = cms.bool( True ),
        minTime = cms.double( -3.0 ),
        tTrigMode = cms.string( "DTTTrigSyncFromDB" )
      ),
      nUnSharedHitsMin = cms.int32( 2 ),
      nSharedHitsMax = cms.int32( 2 ),
      performT0SegCorrection = cms.bool( False ),
      perform_delta_rejecting = cms.bool( False )
    )
)
process.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
    PrintEventNumber = cms.untracked.bool( False ),
    SuppressZeroLCT = cms.untracked.bool( True ),
    UseExaminer = cms.bool( True ),
    Debug = cms.untracked.bool( False ),
    ErrorMask = cms.uint32( 0 ),
    InputObjects = cms.InputTag( "rawDataCollector" ),
    ExaminerMask = cms.uint32( 535558134 ),
    runDQM = cms.untracked.bool( False ),
    UnpackStatusDigis = cms.bool( False ),
    VisualFEDInspect = cms.untracked.bool( False ),
    FormatedEventDump = cms.untracked.bool( False ),
    UseFormatStatus = cms.bool( True ),
    UseSelectiveUnpacking = cms.bool( True ),
    VisualFEDShort = cms.untracked.bool( False )
)
process.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    XTasymmetry_ME1b = cms.double( 0.0 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    CSCWireTimeWindowHigh = cms.int32( 15 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    CSCUseCalibrations = cms.bool( True ),
    CSCUseTimingCorrections = cms.bool( True ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    UseFivePoleFit = cms.bool( True ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    readBadChambers = cms.bool( True ),
    CSCWireTimeWindowLow = cms.int32( 0 ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    ConstSyst_ME1b = cms.double( 0.007 ),
    CSCStripClusterSize = cms.untracked.int32( 3 ),
    CSCStripPeakThreshold = cms.double( 10.0 ),
    readBadChannels = cms.bool( False ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    UseParabolaFit = cms.bool( False ),
    CSCUseReducedWireTimeWindow = cms.bool( False ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    wireDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCWireDigi' ),
    CSCDebug = cms.untracked.bool( False ),
    CSCUseGasGainCorrections = cms.bool( False ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    UseAverageTime = cms.bool( False ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCUseStaticPedestals = cms.bool( False ),
    stripDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCStripDigi' ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 )
)
process.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
    algo_psets = cms.VPSet( 
      cms.PSet(  parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 ),
        algo_psets = cms.VPSet( 
          cms.PSet(  dYclusBoxMax = cms.double( 8.0 ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            maxRatioResidualPrune = cms.double( 3.0 ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            maxRecHitsInCluster = cms.int32( 20 ),
            useShowering = cms.bool( False ),
            BPMinImprovement = cms.double( 10000.0 ),
            curvePenalty = cms.double( 2.0 ),
            ForceCovariance = cms.bool( False ),
            yweightPenalty = cms.double( 1.5 ),
            dPhiFineMax = cms.double( 0.025 ),
            SeedBig = cms.double( 0.0015 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            Covariance = cms.double( 0.0 ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            Pruning = cms.bool( True ),
            tanPhiMax = cms.double( 0.5 ),
            onlyBestSegment = cms.bool( False ),
            dXclusBoxMax = cms.double( 4.0 ),
            maxDTheta = cms.double( 999.0 ),
            preClustering = cms.bool( True ),
            preClusteringUseChaining = cms.bool( True ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            prePrun = cms.bool( True ),
            CorrectTheErrors = cms.bool( True ),
            ForceCovarianceAll = cms.bool( False ),
            NormChi2Cut2D = cms.double( 20.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            minHitsPerSegment = cms.int32( 3 ),
            dRPhiFineMax = cms.double( 8.0 ),
            maxDPhi = cms.double( 999.0 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            BrutePruning = cms.bool( True ),
            prePrunLimit = cms.double( 3.17 )
          ),
          cms.PSet(  dYclusBoxMax = cms.double( 8.0 ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            maxRatioResidualPrune = cms.double( 3.0 ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            maxRecHitsInCluster = cms.int32( 24 ),
            useShowering = cms.bool( False ),
            BPMinImprovement = cms.double( 10000.0 ),
            curvePenalty = cms.double( 2.0 ),
            ForceCovariance = cms.bool( False ),
            yweightPenalty = cms.double( 1.5 ),
            dPhiFineMax = cms.double( 0.025 ),
            SeedBig = cms.double( 0.0015 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            Covariance = cms.double( 0.0 ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            Pruning = cms.bool( True ),
            tanPhiMax = cms.double( 0.5 ),
            onlyBestSegment = cms.bool( False ),
            dXclusBoxMax = cms.double( 4.0 ),
            maxDTheta = cms.double( 999.0 ),
            preClustering = cms.bool( True ),
            preClusteringUseChaining = cms.bool( True ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            prePrun = cms.bool( True ),
            CorrectTheErrors = cms.bool( True ),
            ForceCovarianceAll = cms.bool( False ),
            NormChi2Cut2D = cms.double( 20.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            minHitsPerSegment = cms.int32( 3 ),
            dRPhiFineMax = cms.double( 8.0 ),
            maxDPhi = cms.double( 999.0 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            BrutePruning = cms.bool( True ),
            prePrunLimit = cms.double( 3.17 )
          )
        ),
        algo_name = cms.string( "CSCSegAlgoST" ),
        chamber_types = cms.vstring( 'ME1/a',
          'ME1/b',
          'ME1/2',
          'ME1/3',
          'ME2/1',
          'ME2/2',
          'ME3/1',
          'ME3/2',
          'ME4/1',
          'ME4/2' )
      )
    ),
    algo_type = cms.int32( 1 )
)
process.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
    InputLabel = cms.InputTag( "rawDataCollector" ),
    doSynchro = cms.bool( False )
)
process.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    recAlgoConfig = cms.PSet(  ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
    rpcDigiLabel = cms.InputTag( "hltMuonRPCDigis" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    deadSource = cms.string( "File" ),
    maskSource = cms.string( "File" )
)
process.hltL2OfflineMuonSeeds = cms.EDProducer( "MuonSeedGenerator",
    EnableDTMeasurement = cms.bool( True ),
    EnableCSCMeasurement = cms.bool( True ),
    EnableME0Measurement = cms.bool( False ),
    SMB_21 = cms.vdouble( 1.043, -0.124, 0.0, 0.183, 0.0, 0.0 ),
    SMB_20 = cms.vdouble( 1.011, -0.052, 0.0, 0.188, 0.0, 0.0 ),
    SMB_22 = cms.vdouble( 1.474, -0.758, 0.0, 0.185, 0.0, 0.0 ),
    OL_2213 = cms.vdouble( 0.117, 0.0, 0.0, 0.044, 0.0, 0.0 ),
    SME_11 = cms.vdouble( 3.295, -1.527, 0.112, 0.378, 0.02, 0.0 ),
    SME_13 = cms.vdouble( -1.286, 1.711, 0.0, 0.356, 0.0, 0.0 ),
    SME_12 = cms.vdouble( 0.102, 0.599, 0.0, 0.38, 0.0, 0.0 ),
    DT_34_2_scale = cms.vdouble( -11.901897, 0.0 ),
    OL_1213_0_scale = cms.vdouble( -4.488158, 0.0 ),
    OL_1222_0_scale = cms.vdouble( -5.810449, 0.0 ),
    DT_13 = cms.vdouble( 0.315, 0.068, -0.127, 0.051, -0.002, 0.0 ),
    DT_12 = cms.vdouble( 0.183, 0.054, -0.087, 0.028, 0.002, 0.0 ),
    DT_14 = cms.vdouble( 0.359, 0.052, -0.107, 0.072, -0.004, 0.0 ),
    CSC_13_3_scale = cms.vdouble( -1.701268, 0.0 ),
    DT_24_2_scale = cms.vdouble( -6.63094, 0.0 ),
    CSC_23 = cms.vdouble( -0.081, 0.113, -0.029, 0.015, 0.008, 0.0 ),
    CSC_24 = cms.vdouble( 0.004, 0.021, -0.002, 0.053, 0.0, 0.0 ),
    OL_2222 = cms.vdouble( 0.107, 0.0, 0.0, 0.04, 0.0, 0.0 ),
    DT_14_2_scale = cms.vdouble( -4.808546, 0.0 ),
    SMB_10 = cms.vdouble( 1.387, -0.038, 0.0, 0.19, 0.0, 0.0 ),
    SMB_11 = cms.vdouble( 1.247, 0.72, -0.802, 0.229, -0.075, 0.0 ),
    SMB_12 = cms.vdouble( 2.128, -0.956, 0.0, 0.199, 0.0, 0.0 ),
    SME_21 = cms.vdouble( -0.529, 1.194, -0.358, 0.472, 0.086, 0.0 ),
    SME_22 = cms.vdouble( -1.207, 1.491, -0.251, 0.189, 0.243, 0.0 ),
    DT_13_2_scale = cms.vdouble( -4.257687, 0.0 ),
    CSC_34 = cms.vdouble( 0.062, -0.067, 0.019, 0.021, 0.003, 0.0 ),
    SME_22_0_scale = cms.vdouble( -3.457901, 0.0 ),
    DT_24_1_scale = cms.vdouble( -7.490909, 0.0 ),
    OL_1232_0_scale = cms.vdouble( -5.964634, 0.0 ),
    SMB_32 = cms.vdouble( 0.67, -0.327, 0.0, 0.22, 0.0, 0.0 ),
    SME_13_0_scale = cms.vdouble( 0.104905, 0.0 ),
    SMB_22_0_scale = cms.vdouble( 1.346681, 0.0 ),
    CSC_12_1_scale = cms.vdouble( -6.434242, 0.0 ),
    DT_34 = cms.vdouble( 0.044, 0.004, -0.013, 0.029, 0.003, 0.0 ),
    ME0RecSegmentLabel = cms.InputTag( "me0Segments" ),
    SME_32 = cms.vdouble( -0.901, 1.333, -0.47, 0.41, 0.073, 0.0 ),
    SME_31 = cms.vdouble( -1.594, 1.482, -0.317, 0.487, 0.097, 0.0 ),
    SMB_32_0_scale = cms.vdouble( -3.054156, 0.0 ),
    crackEtas = cms.vdouble( 0.2, 1.6, 1.7 ),
    SME_11_0_scale = cms.vdouble( 1.325085, 0.0 ),
    SMB_20_0_scale = cms.vdouble( 1.486168, 0.0 ),
    DT_13_1_scale = cms.vdouble( -4.520923, 0.0 ),
    CSC_24_1_scale = cms.vdouble( -6.055701, 0.0 ),
    CSC_01_1_scale = cms.vdouble( -1.915329, 0.0 ),
    DT_23 = cms.vdouble( 0.13, 0.023, -0.057, 0.028, 0.004, 0.0 ),
    DT_24 = cms.vdouble( 0.176, 0.014, -0.051, 0.051, 0.003, 0.0 ),
    SMB_12_0_scale = cms.vdouble( 2.283221, 0.0 ),
    deltaPhiSearchWindow = cms.double( 0.25 ),
    SMB_30_0_scale = cms.vdouble( -3.629838, 0.0 ),
    SME_42 = cms.vdouble( -0.003, 0.005, 0.005, 0.608, 0.076, 0.0 ),
    SME_41 = cms.vdouble( -0.003, 0.005, 0.005, 0.608, 0.076, 0.0 ),
    deltaEtaSearchWindow = cms.double( 0.2 ),
    CSC_12_2_scale = cms.vdouble( -1.63622, 0.0 ),
    DT_34_1_scale = cms.vdouble( -13.783765, 0.0 ),
    CSC_34_1_scale = cms.vdouble( -11.520507, 0.0 ),
    OL_2213_0_scale = cms.vdouble( -7.239789, 0.0 ),
    CSC_13_2_scale = cms.vdouble( -6.077936, 0.0 ),
    CSC_12_3_scale = cms.vdouble( -1.63622, 0.0 ),
    deltaEtaCrackSearchWindow = cms.double( 0.25 ),
    SME_21_0_scale = cms.vdouble( -0.040862, 0.0 ),
    OL_1232 = cms.vdouble( 0.184, 0.0, 0.0, 0.066, 0.0, 0.0 ),
    DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
    SMB_10_0_scale = cms.vdouble( 2.448566, 0.0 ),
    CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
    CSC_23_2_scale = cms.vdouble( -6.079917, 0.0 ),
    scaleDT = cms.bool( True ),
    DT_12_2_scale = cms.vdouble( -3.518165, 0.0 ),
    OL_1222 = cms.vdouble( 0.848, -0.591, 0.0, 0.062, 0.0, 0.0 ),
    CSC_23_1_scale = cms.vdouble( -19.084285, 0.0 ),
    OL_1213 = cms.vdouble( 0.96, -0.737, 0.0, 0.052, 0.0, 0.0 ),
    CSC_02 = cms.vdouble( 0.612, -0.207, 0.0, 0.067, -0.001, 0.0 ),
    CSC_03 = cms.vdouble( 0.787, -0.338, 0.029, 0.101, -0.008, 0.0 ),
    CSC_01 = cms.vdouble( 0.166, 0.0, 0.0, 0.031, 0.0, 0.0 ),
    DT_23_1_scale = cms.vdouble( -5.320346, 0.0 ),
    SMB_30 = cms.vdouble( 0.505, -0.022, 0.0, 0.215, 0.0, 0.0 ),
    SMB_31 = cms.vdouble( 0.549, -0.145, 0.0, 0.207, 0.0, 0.0 ),
    crackWindow = cms.double( 0.04 ),
    CSC_14_3_scale = cms.vdouble( -1.969563, 0.0 ),
    SMB_31_0_scale = cms.vdouble( -3.323768, 0.0 ),
    DT_12_1_scale = cms.vdouble( -3.692398, 0.0 ),
    SMB_21_0_scale = cms.vdouble( 1.58384, 0.0 ),
    DT_23_2_scale = cms.vdouble( -5.117625, 0.0 ),
    SME_12_0_scale = cms.vdouble( 2.279181, 0.0 ),
    DT_14_1_scale = cms.vdouble( -5.644816, 0.0 ),
    beamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    SMB_11_0_scale = cms.vdouble( 2.56363, 0.0 ),
    CSC_13 = cms.vdouble( 0.901, -1.302, 0.533, 0.045, 0.005, 0.0 ),
    CSC_14 = cms.vdouble( 0.606, -0.181, -0.002, 0.111, -0.003, 0.0 ),
    OL_2222_0_scale = cms.vdouble( -7.667231, 0.0 ),
    CSC_12 = cms.vdouble( -0.161, 0.254, -0.047, 0.042, -0.007, 0.0 )
)
process.hltL2MuonSeedsPPOnAA = cms.EDProducer( "L2MuonSeedGeneratorFromL1T",
    OfflineSeedLabel = cms.untracked.InputTag( "hltL2OfflineMuonSeeds" ),
    SetMinPtEndcapTo = cms.double( 0.5 ),
    SortType = cms.uint32( 0 ),
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'SteppingHelixPropagatorAny' )
    ),
    CentralBxOnly = cms.bool( True ),
    InputObjects = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    MatchDR = cms.vdouble( 1.0 ),
    L1MaxEta = cms.double( 2.5 ),
    EtaMatchingBins = cms.vdouble( 0.0, 2.5 ),
    L1MinPt = cms.double( 0.0 ),
    L1MinQuality = cms.uint32( 0 ),
    GMTReadoutCollection = cms.InputTag( "" ),
    UseUnassociatedL1 = cms.bool( False ),
    UseOfflineSeed = cms.untracked.bool( True ),
    MatchType = cms.uint32( 0 ),
    Propagator = cms.string( "SteppingHelixPropagatorAny" ),
    SetMinPtBarrelTo = cms.double( 3.0 )
)
process.hltL2MuonsPPOnAA = cms.EDProducer( "L2MuonProducer",
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny',
        'hltESPFastSteppingHelixPropagatorOpposite' )
    ),
    InputObjects = cms.InputTag( "hltL2MuonSeedsPPOnAA" ),
    SeedTransformerParameters = cms.PSet( 
      Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
      NMinRecHits = cms.uint32( 2 ),
      RescaleError = cms.double( 100.0 ),
      Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      UseSubRecHits = cms.bool( False ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
    ),
    L2TrajBuilderParameters = cms.PSet( 
      BWFilterParameters = cms.PSet( 
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        BWSeedType = cms.string( "fromGenerator" ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        EnableRPCMeasurement = cms.bool( True ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          ExcludeRPCFromFit = cms.bool( False ),
          Granularity = cms.int32( 0 ),
          MaxChi2 = cms.double( 25.0 ),
          RescaleError = cms.bool( False ),
          RescaleErrorFactor = cms.double( 100.0 ),
          UseInvalidHits = cms.bool( True )
        ),
        EnableCSCMeasurement = cms.bool( True ),
        MaxChi2 = cms.double( 100.0 ),
        FitDirection = cms.string( "outsideIn" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        NumberOfSigma = cms.double( 3.0 ),
        EnableDTMeasurement = cms.bool( True )
      ),
      DoSeedRefit = cms.bool( False ),
      FilterParameters = cms.PSet( 
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        EnableRPCMeasurement = cms.bool( True ),
        MuonTrajectoryUpdatorParameters = cms.PSet( 
          ExcludeRPCFromFit = cms.bool( False ),
          Granularity = cms.int32( 0 ),
          MaxChi2 = cms.double( 25.0 ),
          RescaleError = cms.bool( False ),
          RescaleErrorFactor = cms.double( 100.0 ),
          UseInvalidHits = cms.bool( True )
        ),
        EnableCSCMeasurement = cms.bool( True ),
        MaxChi2 = cms.double( 1000.0 ),
        FitDirection = cms.string( "insideOut" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        NumberOfSigma = cms.double( 3.0 ),
        EnableDTMeasurement = cms.bool( True )
      ),
      SeedPosition = cms.string( "in" ),
      DoBackwardFilter = cms.bool( True ),
      DoRefit = cms.bool( False ),
      NavigationType = cms.string( "Standard" ),
      SeedTransformerParameters = cms.PSet( 
        Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
        NMinRecHits = cms.uint32( 2 ),
        RescaleError = cms.double( 100.0 ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        UseSubRecHits = cms.bool( False ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
      ),
      SeedPropagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" )
    ),
    DoSeedRefit = cms.bool( False ),
    TrackLoaderParameters = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      DoSmoothing = cms.bool( False ),
      VertexConstraint = cms.bool( True ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 ),
        BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" )
      ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
    ),
    MuonTrajectoryBuilder = cms.string( "Exhaustive" )
)
process.hltL2MuonCandidatesPPOnAA = cms.EDProducer( "L2MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL2MuonsPPOnAA','UpdatedAtVtx' )
)
process.hltIterL3OISeedsFromL2MuonsPPOnAA = cms.EDProducer( "TSGForOIFromL2",
    hitsToTry = cms.int32( 1 ),
    tsosDiff2 = cms.double( 0.02 ),
    adjustErrorsDynamicallyForHitless = cms.bool( True ),
    SF6 = cms.double( 2.0 ),
    SF4 = cms.double( 7.0 ),
    SF5 = cms.double( 10.0 ),
    propagatorName = cms.string( "PropagatorWithMaterialParabolicMf" ),
    SF3 = cms.double( 5.0 ),
    SF1 = cms.double( 3.0 ),
    minEtaForTEC = cms.double( 0.7 ),
    fixedErrorRescaleFactorForHits = cms.double( 1.0 ),
    maxSeeds = cms.uint32( 20 ),
    maxEtaForTOB = cms.double( 1.8 ),
    pT3 = cms.double( 70.0 ),
    pT2 = cms.double( 30.0 ),
    pT1 = cms.double( 13.0 ),
    layersToTry = cms.int32( 2 ),
    fixedErrorRescaleFactorForHitless = cms.double( 2.0 ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersPPOnAA" ),
    SF2 = cms.double( 4.0 ),
    numL2ValidHitsCutAllEta = cms.uint32( 20 ),
    adjustErrorsDynamicallyForHits = cms.bool( False ),
    eta4 = cms.double( 1.2 ),
    src = cms.InputTag( 'hltL2MuonsPPOnAA','UpdatedAtVtx' ),
    eta6 = cms.double( 1.4 ),
    eta7 = cms.double( 2.1 ),
    eta1 = cms.double( 0.2 ),
    eta2 = cms.double( 0.3 ),
    eta3 = cms.double( 1.0 ),
    UseHitLessSeeds = cms.bool( True ),
    estimator = cms.string( "hltESPChi2MeasurementEstimator100" ),
    numL2ValidHitsCutAllEndcap = cms.uint32( 30 ),
    debug = cms.untracked.bool( False ),
    maxHitSeeds = cms.uint32( 1 ),
    eta5 = cms.double( 1.6 ),
    tsosDiff1 = cms.double( 0.2 ),
    maxHitlessSeeds = cms.uint32( 5 )
)
process.hltIterL3OITrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIterL3OISeedsFromL2MuonsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "muonSeededTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( True ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "CkfTrajectoryBuilder" )
)
process.hltIterL3OIMuCtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIterL3OITrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersPPOnAA" ),
    Fitter = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "hltESPMeasurementTracker" ),
    AlgorithmName = cms.string( "iter10" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltIterL3OIMuonTrackCutClassifierPPOnAA = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIterL3OIMuCtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "Notused" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 0, 1 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 0.3, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 4, 3, 2 ),
      min3DLayers = cms.vint32( 1, 2, 1 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 0.35, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 10.0, 1.0, 0.4 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 5, 5 )
    ),
    ignoreVertices = cms.bool( True )
)
process.hltIterL3OIMuonTrackSelectionHighPurityPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIterL3OIMuCtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltIterL3OIMuonTrackCutClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIterL3OIMuonTrackCutClassifierPPOnAA','MVAValues' )
)
process.hltL3MuonsIterL3OIPPOnAA = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      PtCut = cms.double( 0.5 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_2 = cms.double( 15.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        Quality_3 = cms.double( 7.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        Quality_1 = cms.double( 20.0 ),
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        LocChi2Cut = cms.double( 0.001 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        MinPt = cms.double( 0.5 ),
        MinP = cms.double( 2.5 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      tkTrajUseVertex = cms.bool( False ),
      MuonTrackingRegionBuilder = cms.PSet( 
        Rescale_Dz = cms.double( 4.0 ),
        Pt_fixed = cms.bool( False ),
        Eta_fixed = cms.bool( True ),
        Eta_min = cms.double( 0.1 ),
        DeltaZ = cms.double( 24.2 ),
        maxRegions = cms.int32( 2 ),
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        UseVertex = cms.bool( False ),
        Z_fixed = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Rescale_phi = cms.double( 3.0 ),
        DeltaEta = cms.double( 0.2 ),
        precise = cms.bool( True ),
        OnDemand = cms.int32( -1 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        MeasurementTrackerName = cms.InputTag( "hltESPMeasurementTracker" ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Pt_min = cms.double( 0.1 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        Phi_fixed = cms.bool( True ),
        DeltaR = cms.double( 0.025 ),
        input = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
        DeltaPhi = cms.double( 0.15 ),
        Phi_min = cms.double( 0.1 ),
        Rescale_eta = cms.double( 3.0 )
      ),
      TrackTransformer = cms.PSet( 
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
      ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      RefitRPCHits = cms.bool( True ),
      tkTrajVertex = cms.InputTag( "Notused" ),
      GlbRefitterParameters = cms.PSet( 
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        RefitFlag = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        PropDirForCosmics = cms.bool( False ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        HitThreshold = cms.int32( 1 ),
        DYTthrs = cms.vint32( 30, 15 ),
        TrackerSkipSystem = cms.int32( -1 ),
        RefitDirection = cms.string( "insideOut" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        TrackerSkipSection = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonHitsOption = cms.int32( 1 ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
      ),
      PCut = cms.double( 2.5 ),
      tkTrajMaxDXYBeamSpot = cms.double( 9999.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      ScaleTECyFactor = cms.double( -1.0 ),
      tkTrajLabel = cms.InputTag( "hltIterL3OIMuonTrackSelectionHighPurityPPOnAA" )
    ),
    TrackLoaderParameters = cms.PSet( 
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      DoSmoothing = cms.bool( True ),
      SmoothTkTrack = cms.untracked.bool( False ),
      VertexConstraint = cms.bool( False ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
      ),
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2MuonsPPOnAA','UpdatedAtVtx' )
)
process.hltIterL3OIL3MuonsLinksCombinationPPOnAA = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltL3MuonsIterL3OIPPOnAA' )
)
process.hltIterL3OIL3MuonsPPOnAA = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsIterL3OIPPOnAA' )
)
process.hltIterL3OIL3MuonCandidatesPPOnAA = cms.EDProducer( "L3MuonCandidateProducer",
    InputLinksObjects = cms.InputTag( "hltIterL3OIL3MuonsLinksCombinationPPOnAA" ),
    InputObjects = cms.InputTag( "hltIterL3OIL3MuonsPPOnAA" ),
    MuonPtOption = cms.string( "Tracker" )
)
process.hltL2SelectorForL3IOPPOnAA = cms.EDProducer( "HLTMuonL2SelectorForL3IO",
    MaxNormalizedChi2 = cms.double( 200.0 ),
    MinNmuonHits = cms.int32( 1 ),
    MinNhits = cms.int32( 1 ),
    applyL3Filters = cms.bool( False ),
    MaxPtDifference = cms.double( 0.3 ),
    l3OISrc = cms.InputTag( "hltIterL3OIL3MuonCandidatesPPOnAA" ),
    InputLinks = cms.InputTag( "hltIterL3OIL3MuonsLinksCombinationPPOnAA" ),
    l2Src = cms.InputTag( 'hltL2MuonsPPOnAA','UpdatedAtVtx' )
)
process.hltIterL3MuonPixelTracksFilter = cms.EDProducer( "PixelTrackFilterByKinematicsProducer",
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.1 ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    tipMax = cms.double( 1.0 )
)
process.hltIterL3MuonPixelTracksFitter = cms.EDProducer( "PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool( False ),
    scaleFactor = cms.double( 0.65 )
)
process.hltIterL3MuonPixelTracksTrackingRegionsPPOnAA = cms.EDProducer( "MuonTrackingRegionEDProducer",
    precise = cms.bool( True ),
    Eta_fixed = cms.bool( True ),
    Eta_min = cms.double( 0.0 ),
    Z_fixed = cms.bool( True ),
    MeasurementTrackerName = cms.InputTag( "" ),
    maxRegions = cms.int32( 5 ),
    Pt_min = cms.double( 1.4 ),
    Rescale_Dz = cms.double( 4.0 ),
    PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
    PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
    vertexCollection = cms.InputTag( "notUsed" ),
    Phi_fixed = cms.bool( True ),
    input = cms.InputTag( "hltL2SelectorForL3IOPPOnAA" ),
    DeltaR = cms.double( 0.025 ),
    OnDemand = cms.int32( -1 ),
    DeltaZ = cms.double( 24.2 ),
    Rescale_phi = cms.double( 3.0 ),
    Rescale_eta = cms.double( 3.0 ),
    DeltaEta = cms.double( 0.2 ),
    Phi_min = cms.double( 0.0 ),
    DeltaPhi = cms.double( 0.15 ),
    UseVertex = cms.bool( False ),
    EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
    EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Pt_fixed = cms.bool( True )
)
process.hltIterL3MuonPixelLayerQuadrupletsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
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
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltIterL3MuonPixelTracksHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIterL3MuonPixelTracksTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIterL3MuonPixelLayerQuadrupletsPPOnAA" )
)
process.hltIterL3MuonPixelTracksHitQuadrupletsPPOnAA = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.005 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltIterL3MuonPixelTracksHitDoubletsPPOnAA" ),
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
process.hltIterL3MuonPixelTracksPPOnAA = cms.EDProducer( "PixelTrackProducer",
    Filter = cms.InputTag( "hltIterL3MuonPixelTracksFilter" ),
    Cleaner = cms.string( "hltPixelTracksCleanerBySharedHits" ),
    passLabel = cms.string( "" ),
    Fitter = cms.InputTag( "hltIterL3MuonPixelTracksFitter" ),
    SeedingHitSets = cms.InputTag( "hltIterL3MuonPixelTracksHitQuadrupletsPPOnAA" )
)
process.hltIterL3MuonPixelVerticesPPOnAA = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltIterL3MuonPixelTracksPPOnAA" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
process.hltIterL3MuonTrimmedPixelVerticesPPOnAA = cms.EDProducer( "PixelVertexCollectionTrimmer",
    minSumPt2 = cms.double( 0.0 ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    maxVtx = cms.uint32( 100 ),
    fractionSumPt2 = cms.double( 0.3 ),
    src = cms.InputTag( "hltIterL3MuonPixelVerticesPPOnAA" )
)
process.hltIter0IterL3MuonPixelSeedsFromPixelTracksPPOnAA = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 0.3 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) ),
    InputVertexCollection = cms.InputTag( "hltIterL3MuonTrimmedPixelVerticesPPOnAA" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    InputCollection = cms.InputTag( "hltIterL3MuonPixelTracksPPOnAA" ),
    originRadius = cms.double( 0.1 )
)
process.hltIter0IterL3MuonCkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter0IterL3MuonPixelSeedsFromPixelTracksPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "none" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0IterL3MuonPSetGroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
)
process.hltIter0IterL3MuonCtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter0IterL3MuonCkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter0" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltIter0IterL3MuonTrackCutClassifierPPOnAA = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter0IterL3MuonCtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltIterL3MuonTrimmedPixelVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 3, 4 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 0.3, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 3, 4 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 0.35, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 4 )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltIter0IterL3MuonTrackSelectionHighPurityPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter0IterL3MuonCtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltIter0IterL3MuonTrackCutClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter0IterL3MuonTrackCutClassifierPPOnAA','MVAValues' )
)
process.hltIter2IterL3MuonClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter0IterL3MuonTrackSelectionHighPurityPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltIter2IterL3MuonMaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter2IterL3MuonClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersPPOnAA" )
)
process.hltIter2IterL3MuonPixelLayerTripletsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix1+BPix3+BPix4',
      'BPix1+BPix2+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg',
      'BPix1+BPix3+FPix1_pos',
      'BPix1+BPix2+FPix2_pos',
      'BPix1+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix2_neg',
      'BPix1+FPix2_neg+FPix3_neg',
      'BPix1+FPix1_neg+FPix3_neg',
      'BPix1+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_pos+FPix3_pos' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2IterL3MuonClustersRefRemovalPPOnAA" ),
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
      skipClusters = cms.InputTag( "hltIter2IterL3MuonClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltIter2IterL3MuonPixelClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersPPOnAA" )
)
process.hltIter2IterL3MuonPixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIterL3MuonPixelTracksTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "hltIter2IterL3MuonPixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIter2IterL3MuonPixelLayerTripletsPPOnAA" )
)
process.hltIter2IterL3MuonPixelHitTripletsPPOnAA = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.3 ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltIter2IterL3MuonPixelHitDoubletsPPOnAA" ),
    CAThetaCut = cms.double( 0.015 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 6.0 ),
      value1 = cms.double( 100.0 ),
      pt1 = cms.double( 0.8 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 8.0 )
    ),
    CAPhiCut = cms.double( 0.1 ),
    useBendingCorrection = cms.bool( True )
)
process.hltIter2IterL3MuonPixelSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltIter2IterL3MuonPixelHitTripletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltIter2IterL3MuonCkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter2IterL3MuonPixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2IterL3MuonMaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2IterL3MuonPSetGroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltIter2IterL3MuonCtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter2IterL3MuonCkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2IterL3MuonMaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter2" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltIter2IterL3MuonTrackCutClassifierPPOnAA = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter2IterL3MuonCtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltIterL3MuonTrimmedPixelVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltIter2IterL3MuonTrackSelectionHighPurityPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter2IterL3MuonCtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltIter2IterL3MuonTrackCutClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter2IterL3MuonTrackCutClassifierPPOnAA','MVAValues' )
)
process.hltIter2IterL3MuonMergedPPOnAA = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter0IterL3MuonTrackSelectionHighPurityPPOnAA','hltIter2IterL3MuonTrackSelectionHighPurityPPOnAA' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter0IterL3MuonTrackSelectionHighPurityPPOnAA','hltIter2IterL3MuonTrackSelectionHighPurityPPOnAA' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltIter3IterL3MuonClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter2IterL3MuonTrackSelectionHighPurityPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter2IterL3MuonClustersRefRemovalPPOnAA" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltIter3IterL3MuonMaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter3IterL3MuonClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersPPOnAA" )
)
process.hltIter3IterL3MuonPixelLayerPairsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix1+BPix4',
      'BPix2+BPix3',
      'BPix2+BPix4',
      'BPix3+BPix4',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix1+FPix3_pos',
      'BPix1+FPix3_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'BPix3+FPix1_pos',
      'BPix3+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix3_pos',
      'FPix1_neg+FPix3_neg',
      'FPix2_pos+FPix3_pos',
      'FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter3IterL3MuonClustersRefRemovalPPOnAA" ),
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
      skipClusters = cms.InputTag( "hltIter3IterL3MuonClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltIter3IterL3MuonL2CandidatesPPOnAA = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( "hltL2SelectorForL3IOPPOnAA" ),
    particleType = cms.string( "mu+" )
)
process.hltIter3IterL3MuonTrackingRegionsPPOnAA = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet( 
      vertexCollection = cms.InputTag( "notUsed" ),
      zErrorVetex = cms.double( 0.2 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 24.2 ),
      maxNVertices = cms.int32( 1 ),
      maxNRegions = cms.int32( 2 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      ptMin = cms.double( 2.0 ),
      mode = cms.string( "BeamSpotSigma" ),
      input = cms.InputTag( "hltIter3IterL3MuonL2CandidatesPPOnAA" ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "Never" ),
      originRadius = cms.double( 0.015 ),
      measurementTrackerName = cms.InputTag( "" ),
      precise = cms.bool( True ),
      deltaEta = cms.double( 0.1 ),
      deltaPhi = cms.double( 0.1 )
    )
)
process.hltIter3IterL3MuonPixelClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersPPOnAA" )
)
process.hltIter3IterL3MuonPixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIter3IterL3MuonTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltIter3IterL3MuonPixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( False ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIter3IterL3MuonPixelLayerPairsPPOnAA" )
)
process.hltIter3IterL3MuonPixelSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltIter3IterL3MuonPixelHitDoubletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltIter3IterL3MuonCkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter3IterL3MuonPixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter3IterL3MuonMaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2IterL3MuonPSetGroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltIter3IterL3MuonCtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter3IterL3MuonCkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter3IterL3MuonMaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter3" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltIter3IterL3MuonTrackCutClassifierPPOnAA = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter3IterL3MuonCtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltIterL3MuonTrimmedPixelVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltIter3IterL3MuonTrackSelectionHighPurityPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter3IterL3MuonCtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltIter3IterL3MuonTrackCutClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter3IterL3MuonTrackCutClassifierPPOnAA','MVAValues' )
)
process.hltIter3IterL3MuonMergedPPOnAA = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter2IterL3MuonMergedPPOnAA','hltIter3IterL3MuonTrackSelectionHighPurityPPOnAA' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter2IterL3MuonMergedPPOnAA','hltIter3IterL3MuonTrackSelectionHighPurityPPOnAA' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltL3MuonsIterL3IOPPOnAA = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      PtCut = cms.double( 0.5 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_2 = cms.double( 15.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        Quality_3 = cms.double( 7.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        Quality_1 = cms.double( 20.0 ),
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        LocChi2Cut = cms.double( 0.001 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        MinPt = cms.double( 0.5 ),
        MinP = cms.double( 2.5 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      tkTrajUseVertex = cms.bool( False ),
      MuonTrackingRegionBuilder = cms.PSet( 
        Rescale_Dz = cms.double( 4.0 ),
        Pt_fixed = cms.bool( True ),
        Eta_fixed = cms.bool( True ),
        Eta_min = cms.double( 0.1 ),
        DeltaZ = cms.double( 24.2 ),
        maxRegions = cms.int32( 2 ),
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        UseVertex = cms.bool( False ),
        Z_fixed = cms.bool( True ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Rescale_phi = cms.double( 3.0 ),
        DeltaEta = cms.double( 0.04 ),
        precise = cms.bool( True ),
        OnDemand = cms.int32( -1 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        MeasurementTrackerName = cms.InputTag( "hltESPMeasurementTracker" ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Pt_min = cms.double( 0.1 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        Phi_fixed = cms.bool( True ),
        DeltaR = cms.double( 0.025 ),
        input = cms.InputTag( "hltL2SelectorForL3IOPPOnAA" ),
        DeltaPhi = cms.double( 0.15 ),
        Phi_min = cms.double( 0.1 ),
        Rescale_eta = cms.double( 3.0 )
      ),
      TrackTransformer = cms.PSet( 
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
      ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      RefitRPCHits = cms.bool( True ),
      tkTrajVertex = cms.InputTag( "hltIterL3MuonPixelVerticesPPOnAA" ),
      GlbRefitterParameters = cms.PSet( 
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        RefitFlag = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        PropDirForCosmics = cms.bool( False ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        HitThreshold = cms.int32( 1 ),
        DYTthrs = cms.vint32( 30, 15 ),
        TrackerSkipSystem = cms.int32( -1 ),
        RefitDirection = cms.string( "insideOut" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        TrackerSkipSection = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonHitsOption = cms.int32( 1 ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
      ),
      PCut = cms.double( 2.5 ),
      tkTrajMaxDXYBeamSpot = cms.double( 9999.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      matchToSeeds = cms.bool( True ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      ScaleTECyFactor = cms.double( -1.0 ),
      tkTrajLabel = cms.InputTag( "hltIter3IterL3MuonMergedPPOnAA" )
    ),
    TrackLoaderParameters = cms.PSet( 
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      DoSmoothing = cms.bool( False ),
      SmoothTkTrack = cms.untracked.bool( False ),
      VertexConstraint = cms.bool( False ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
      ),
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2MuonsPPOnAA','UpdatedAtVtx' )
)
process.hltIterL3MuonsFromL2LinksCombinationPPOnAA = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltL3MuonsIterL3OIPPOnAA','hltL3MuonsIterL3IOPPOnAA' )
)
process.hltL1MuonsPt0PPOnAA = cms.EDProducer( "HLTL1TMuonSelector",
    L1MinPt = cms.double( -1.0 ),
    CentralBxOnly = cms.bool( True ),
    InputObjects = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1MinQuality = cms.uint32( 0 ),
    L1MaxEta = cms.double( 5.0 )
)
process.hltIterL3FromL1MuonPixelTracksTrackingRegionsPPOnAA = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet( 
      vertexCollection = cms.InputTag( "notUsed" ),
      zErrorVetex = cms.double( 0.2 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 24.2 ),
      maxNVertices = cms.int32( 1 ),
      maxNRegions = cms.int32( 5 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      ptMin = cms.double( 1.5 ),
      mode = cms.string( "BeamSpotSigma" ),
      input = cms.InputTag( "hltL1MuonsPt0PPOnAA" ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "Never" ),
      originRadius = cms.double( 0.2 ),
      measurementTrackerName = cms.InputTag( "" ),
      precise = cms.bool( True ),
      deltaEta = cms.double( 0.35 ),
      deltaPhi = cms.double( 0.2 )
    )
)
process.hltIterL3FromL1MuonPixelLayerQuadrupletsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
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
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltIterL3FromL1MuonPixelTracksHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIterL3FromL1MuonPixelTracksTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIterL3FromL1MuonPixelLayerQuadrupletsPPOnAA" )
)
process.hltIterL3FromL1MuonPixelTracksHitQuadrupletsPPOnAA = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.005 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltIterL3FromL1MuonPixelTracksHitDoubletsPPOnAA" ),
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
process.hltIterL3FromL1MuonPixelTracksPPOnAA = cms.EDProducer( "PixelTrackProducer",
    Filter = cms.InputTag( "hltIterL3MuonPixelTracksFilter" ),
    Cleaner = cms.string( "hltPixelTracksCleanerBySharedHits" ),
    passLabel = cms.string( "" ),
    Fitter = cms.InputTag( "hltIterL3MuonPixelTracksFitter" ),
    SeedingHitSets = cms.InputTag( "hltIterL3FromL1MuonPixelTracksHitQuadrupletsPPOnAA" )
)
process.hltIterL3FromL1MuonPixelVerticesPPOnAA = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltIterL3MuonPixelTracksPPOnAA" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
process.hltIterL3FromL1MuonTrimmedPixelVerticesPPOnAA = cms.EDProducer( "PixelVertexCollectionTrimmer",
    minSumPt2 = cms.double( 0.0 ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    maxVtx = cms.uint32( 100 ),
    fractionSumPt2 = cms.double( 0.3 ),
    src = cms.InputTag( "hltIterL3FromL1MuonPixelVerticesPPOnAA" )
)
process.hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracksPPOnAA = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 0.3 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) ),
    InputVertexCollection = cms.InputTag( "hltIterL3FromL1MuonTrimmedPixelVerticesPPOnAA" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    InputCollection = cms.InputTag( "hltIterL3FromL1MuonPixelTracksPPOnAA" ),
    originRadius = cms.double( 0.1 )
)
process.hltIter0IterL3FromL1MuonCkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracksPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "none" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
)
process.hltIter0IterL3FromL1MuonCtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter0IterL3FromL1MuonCkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersPPOnAA" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter0" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltIter0IterL3FromL1MuonTrackCutClassifierPPOnAA = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter0IterL3FromL1MuonCtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltIterL3FromL1MuonTrimmedPixelVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 3, 4 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 0.3, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 3, 4 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 0.35, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 4 )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltIter0IterL3FromL1MuonTrackSelectionHighPurityPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter0IterL3FromL1MuonCtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltIter0IterL3FromL1MuonTrackCutClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter0IterL3FromL1MuonTrackCutClassifierPPOnAA','MVAValues' )
)
process.hltIter2IterL3FromL1MuonClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter0IterL3FromL1MuonTrackSelectionHighPurityPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltIter2IterL3FromL1MuonMaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter2IterL3FromL1MuonClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersPPOnAA" )
)
process.hltIter2IterL3FromL1MuonPixelLayerTripletsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix1+BPix3+BPix4',
      'BPix1+BPix2+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg',
      'BPix1+BPix3+FPix1_pos',
      'BPix1+BPix2+FPix2_pos',
      'BPix1+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix2_neg',
      'BPix1+FPix2_neg+FPix3_neg',
      'BPix1+FPix1_neg+FPix3_neg',
      'BPix1+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_pos+FPix3_pos' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2IterL3FromL1MuonClustersRefRemovalPPOnAA" ),
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
      skipClusters = cms.InputTag( "hltIter2IterL3FromL1MuonClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltIter2IterL3FromL1MuonPixelClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersPPOnAA" )
)
process.hltIter2IterL3FromL1MuonPixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIterL3FromL1MuonPixelTracksTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "hltIter2IterL3FromL1MuonPixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIter2IterL3FromL1MuonPixelLayerTripletsPPOnAA" )
)
process.hltIter2IterL3FromL1MuonPixelHitTripletsPPOnAA = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.3 ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltIter2IterL3FromL1MuonPixelHitDoubletsPPOnAA" ),
    CAThetaCut = cms.double( 0.015 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 6.0 ),
      value1 = cms.double( 100.0 ),
      pt1 = cms.double( 0.8 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 8.0 )
    ),
    CAPhiCut = cms.double( 0.1 ),
    useBendingCorrection = cms.bool( True )
)
process.hltIter2IterL3FromL1MuonPixelSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltIter2IterL3FromL1MuonPixelHitTripletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltIter2IterL3FromL1MuonCkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter2IterL3FromL1MuonPixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2IterL3FromL1MuonMaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltIter2IterL3FromL1MuonCtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter2IterL3FromL1MuonCkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2IterL3FromL1MuonMaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter2" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltIter2IterL3FromL1MuonTrackCutClassifierPPOnAA = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter2IterL3FromL1MuonCtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltIterL3FromL1MuonTrimmedPixelVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltIter2IterL3FromL1MuonTrackSelectionHighPurityPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter2IterL3FromL1MuonCtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltIter2IterL3FromL1MuonTrackCutClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter2IterL3FromL1MuonTrackCutClassifierPPOnAA','MVAValues' )
)
process.hltIter2IterL3FromL1MuonMergedPPOnAA = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter0IterL3FromL1MuonTrackSelectionHighPurityPPOnAA','hltIter2IterL3FromL1MuonTrackSelectionHighPurityPPOnAA' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter0IterL3FromL1MuonTrackSelectionHighPurityPPOnAA','hltIter2IterL3FromL1MuonTrackSelectionHighPurityPPOnAA' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltIter3IterL3FromL1MuonClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter2IterL3FromL1MuonTrackSelectionHighPurityPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter2IterL3FromL1MuonClustersRefRemovalPPOnAA" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltIter3IterL3FromL1MuonMaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter3IterL3FromL1MuonClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersPPOnAA" )
)
process.hltIter3IterL3FromL1MuonPixelLayerPairsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix1+BPix4',
      'BPix2+BPix3',
      'BPix2+BPix4',
      'BPix3+BPix4',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix1+FPix3_pos',
      'BPix1+FPix3_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'BPix3+FPix1_pos',
      'BPix3+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix3_pos',
      'FPix1_neg+FPix3_neg',
      'FPix2_pos+FPix3_pos',
      'FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter3IterL3FromL1MuonClustersRefRemovalPPOnAA" ),
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
      skipClusters = cms.InputTag( "hltIter3IterL3FromL1MuonClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltIter3IterL3FromL1MuonTrackingRegionsPPOnAA = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet( 
      vertexCollection = cms.InputTag( "notUsed" ),
      zErrorVetex = cms.double( 0.2 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 24.2 ),
      maxNVertices = cms.int32( 1 ),
      maxNRegions = cms.int32( 5 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      ptMin = cms.double( 1.0 ),
      mode = cms.string( "BeamSpotSigma" ),
      input = cms.InputTag( "hltL1MuonsPt0PPOnAA" ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "Never" ),
      originRadius = cms.double( 0.015 ),
      measurementTrackerName = cms.InputTag( "" ),
      precise = cms.bool( True ),
      deltaEta = cms.double( 0.2 ),
      deltaPhi = cms.double( 0.1 )
    )
)
process.hltIter3IterL3FromL1MuonPixelClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersPPOnAA" )
)
process.hltIter3IterL3FromL1MuonPixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIter3IterL3FromL1MuonTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltIter3IterL3FromL1MuonPixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( False ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIter3IterL3FromL1MuonPixelLayerPairsPPOnAA" )
)
process.hltIter3IterL3FromL1MuonPixelSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltIter3IterL3FromL1MuonPixelHitDoubletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltIter3IterL3FromL1MuonCkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter3IterL3FromL1MuonPixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter3IterL3FromL1MuonMaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2IterL3MuonPSetGroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltIter3IterL3FromL1MuonCtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter3IterL3FromL1MuonCkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter3IterL3FromL1MuonMaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter3" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltIter3IterL3FromL1MuonTrackCutClassifierPPOnAA = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter3IterL3FromL1MuonCtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltIterL3FromL1MuonTrimmedPixelVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltIter3IterL3FromL1MuonTrackSelectionHighPurityPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter3IterL3FromL1MuonCtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltIter3IterL3FromL1MuonTrackCutClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter3IterL3FromL1MuonTrackCutClassifierPPOnAA','MVAValues' )
)
process.hltIter3IterL3FromL1MuonMergedPPOnAA = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter2IterL3FromL1MuonMergedPPOnAA','hltIter3IterL3FromL1MuonTrackSelectionHighPurityPPOnAA' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter2IterL3FromL1MuonMergedPPOnAA','hltIter3IterL3FromL1MuonTrackSelectionHighPurityPPOnAA' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltIterL3MuonMergedPPOnAA = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIterL3OIMuonTrackSelectionHighPurityPPOnAA','hltIter3IterL3MuonMergedPPOnAA' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIterL3OIMuonTrackSelectionHighPurityPPOnAA','hltIter3IterL3MuonMergedPPOnAA' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltIterL3MuonAndMuonFromL1MergedPPOnAA = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIterL3MuonMergedPPOnAA','hltIter3IterL3FromL1MuonMergedPPOnAA' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIterL3MuonMergedPPOnAA','hltIter3IterL3FromL1MuonMergedPPOnAA' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltIterL3GlbMuonPPOnAA = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet( 
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' )
    ),
    L3TrajBuilderParameters = cms.PSet( 
      PtCut = cms.double( 1.5 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      GlobalMuonTrackMatcher = cms.PSet( 
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_2 = cms.double( 15.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        Quality_3 = cms.double( 7.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        Quality_1 = cms.double( 20.0 ),
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        LocChi2Cut = cms.double( 0.001 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        MinPt = cms.double( 1.5 ),
        MinP = cms.double( 2.5 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      tkTrajUseVertex = cms.bool( False ),
      MuonTrackingRegionBuilder = cms.PSet( 
        Rescale_Dz = cms.double( 4.0 ),
        Pt_fixed = cms.bool( False ),
        Eta_fixed = cms.bool( True ),
        Eta_min = cms.double( 0.1 ),
        DeltaZ = cms.double( 24.2 ),
        maxRegions = cms.int32( 20 ),
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        UseVertex = cms.bool( False ),
        Z_fixed = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Rescale_phi = cms.double( 3.0 ),
        DeltaEta = cms.double( 0.2 ),
        precise = cms.bool( True ),
        OnDemand = cms.int32( -1 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        MeasurementTrackerName = cms.InputTag( "hltESPMeasurementTracker" ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Pt_min = cms.double( 1.4 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        Phi_fixed = cms.bool( True ),
        DeltaR = cms.double( 0.025 ),
        input = cms.InputTag( 'hltL2MuonsPPOnAA','UpdatedAtVtx' ),
        DeltaPhi = cms.double( 0.15 ),
        Phi_min = cms.double( 0.1 ),
        Rescale_eta = cms.double( 3.0 )
      ),
      TrackTransformer = cms.PSet( 
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
      ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      RefitRPCHits = cms.bool( True ),
      tkTrajVertex = cms.InputTag( "Notused" ),
      GlbRefitterParameters = cms.PSet( 
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        RefitFlag = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        PropDirForCosmics = cms.bool( False ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        HitThreshold = cms.int32( 1 ),
        DYTthrs = cms.vint32( 30, 15 ),
        TrackerSkipSystem = cms.int32( -1 ),
        RefitDirection = cms.string( "insideOut" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        TrackerSkipSection = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonHitsOption = cms.int32( 1 ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
      ),
      PCut = cms.double( 2.5 ),
      tkTrajMaxDXYBeamSpot = cms.double( 9999.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      ScaleTECyFactor = cms.double( -1.0 ),
      tkTrajLabel = cms.InputTag( "hltIterL3MuonAndMuonFromL1MergedPPOnAA" )
    ),
    TrackLoaderParameters = cms.PSet( 
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      DoSmoothing = cms.bool( True ),
      SmoothTkTrack = cms.untracked.bool( False ),
      VertexConstraint = cms.bool( False ),
      MuonUpdatorAtVertexParameters = cms.PSet( 
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
      ),
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2MuonsPPOnAA','UpdatedAtVtx' )
)
process.hltIterL3MuonsNoIDPPOnAA = cms.EDProducer( "MuonIdProducer",
    TrackExtractorPSet = cms.PSet( 
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltIter3IterL3FromL1MuonMergedPPOnAA" ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      BeamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
      DR_Veto = cms.double( 0.01 ),
      Pt_Min = cms.double( -1.0 ),
      DR_Max = cms.double( 1.0 ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Prob_Min = cms.double( -1.0 ),
      Diff_r = cms.double( 0.1 ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" ),
      ComponentName = cms.string( "TrackExtractor" )
    ),
    maxAbsEta = cms.double( 3.0 ),
    fillGlobalTrackRefits = cms.bool( False ),
    arbitrationCleanerOptions = cms.PSet( 
      OverlapDTheta = cms.double( 0.02 ),
      Overlap = cms.bool( True ),
      Clustering = cms.bool( True ),
      ME1a = cms.bool( True ),
      ClusterDTheta = cms.double( 0.02 ),
      ClusterDPhi = cms.double( 0.6 ),
      OverlapDPhi = cms.double( 0.0786 )
    ),
    globalTrackQualityInputTag = cms.InputTag( "glbTrackQual" ),
    addExtraSoftMuons = cms.bool( False ),
    debugWithTruthMatching = cms.bool( False ),
    CaloExtractorPSet = cms.PSet( 
      DR_Veto_H = cms.double( 0.1 ),
      CenterConeOnCalIntersection = cms.bool( False ),
      NoiseTow_EE = cms.double( 0.15 ),
      Noise_EB = cms.double( 0.025 ),
      Noise_HE = cms.double( 0.2 ),
      DR_Veto_E = cms.double( 0.07 ),
      NoiseTow_EB = cms.double( 0.04 ),
      Noise_EE = cms.double( 0.1 ),
      UseRecHitsFlag = cms.bool( False ),
      DR_Max = cms.double( 1.0 ),
      DepositLabel = cms.untracked.string( "Cal" ),
      Noise_HO = cms.double( 0.2 ),
      DR_Veto_HO = cms.double( 0.1 ),
      Threshold_H = cms.double( 0.5 ),
      PrintTimeReport = cms.untracked.bool( False ),
      Threshold_E = cms.double( 0.2 ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      ComponentName = cms.string( "CaloExtractorByAssociator" ),
      Threshold_HO = cms.double( 0.5 ),
      DepositInstanceLabels = cms.vstring( 'ecal',
        'hcal',
        'ho' ),
      ServiceParameters = cms.PSet( 
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False ),
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
      ),
      TrackAssociatorParameters = cms.PSet( 
        useMuon = cms.bool( False ),
        truthMatch = cms.bool( False ),
        usePreshower = cms.bool( False ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        useEcal = cms.bool( False ),
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        dRMuon = cms.double( 9999.0 ),
        dREcal = cms.double( 1.0 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EBRecHitCollectionLabel = cms.InputTag( "Notused" ),
        CaloTowerCollectionLabel = cms.InputTag( "Notused" ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        muonMaxDistanceX = cms.double( 5.0 ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        useHcal = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "Notused" ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        dREcalPreselection = cms.double( 1.0 ),
        useCalo = cms.bool( True ),
        dRMuonPreselection = cms.double( 0.2 ),
        EERecHitCollectionLabel = cms.InputTag( "Notused" ),
        dRHcal = cms.double( 1.0 ),
        dRHcalPreselection = cms.double( 1.0 ),
        HORecHitCollectionLabel = cms.InputTag( "Notused" )
      ),
      Noise_HB = cms.double( 0.2 )
    ),
    runArbitrationCleaner = cms.bool( False ),
    fillEnergy = cms.bool( False ),
    TrackerKinkFinderParameters = cms.PSet( 
      usePosition = cms.bool( False ),
      diagonalOnly = cms.bool( False )
    ),
    TimingFillerParameters = cms.PSet( 
      DTTimingParameters = cms.PSet( 
        HitError = cms.double( 6.0 ),
        MatchParameters = cms.PSet( 
          TightMatchDT = cms.bool( False ),
          DTradius = cms.double( 0.01 ),
          TightMatchCSC = cms.bool( True ),
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" )
        ),
        debug = cms.bool( False ),
        DoWireCorr = cms.bool( False ),
        RequireBothProjections = cms.bool( False ),
        DTTimeOffset = cms.double( 2.7 ),
        PruneCut = cms.double( 10000.0 ),
        DTsegments = cms.InputTag( "hltDt4DSegments" ),
        UseSegmentT0 = cms.bool( False ),
        HitsMin = cms.int32( 5 ),
        DropTheta = cms.bool( True ),
        ServiceParameters = cms.PSet( 
          RPCLayers = cms.bool( True ),
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
        )
      ),
      UseCSC = cms.bool( True ),
      CSCTimingParameters = cms.PSet( 
        MatchParameters = cms.PSet( 
          TightMatchDT = cms.bool( False ),
          DTradius = cms.double( 0.01 ),
          TightMatchCSC = cms.bool( True ),
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" )
        ),
        debug = cms.bool( False ),
        CSCWireTimeOffset = cms.double( 0.0 ),
        CSCStripError = cms.double( 7.0 ),
        CSCTimeOffset = cms.double( 0.0 ),
        CSCWireError = cms.double( 8.6 ),
        PruneCut = cms.double( 100.0 ),
        CSCsegments = cms.InputTag( "hltCscSegments" ),
        UseStripTime = cms.bool( True ),
        CSCStripTimeOffset = cms.double( 0.0 ),
        UseWireTime = cms.bool( True ),
        ServiceParameters = cms.PSet( 
          RPCLayers = cms.bool( True ),
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
        )
      ),
      ErrorDT = cms.double( 6.0 ),
      EcalEnergyCut = cms.double( 0.4 ),
      UseECAL = cms.bool( True ),
      ErrorEB = cms.double( 2.085 ),
      UseDT = cms.bool( True ),
      ErrorEE = cms.double( 6.95 ),
      ErrorCSC = cms.double( 7.4 )
    ),
    inputCollectionTypes = cms.vstring( 'inner tracks',
      'links',
      'outer tracks' ),
    arbitrateTrackerMuons = cms.bool( True ),
    minCaloCompatibility = cms.double( 0.6 ),
    ecalDepositName = cms.string( "ecal" ),
    minP = cms.double( 2.5 ),
    fillIsolation = cms.bool( False ),
    jetDepositName = cms.string( "jets" ),
    hoDepositName = cms.string( "ho" ),
    writeIsoDeposits = cms.bool( False ),
    maxAbsPullX = cms.double( 9999.0 ),
    maxAbsPullY = cms.double( 9999.0 ),
    minPt = cms.double( 1.5 ),
    TrackAssociatorParameters = cms.PSet( 
      useMuon = cms.bool( True ),
      truthMatch = cms.bool( False ),
      usePreshower = cms.bool( False ),
      dRPreshowerPreselection = cms.double( 0.2 ),
      muonMaxDistanceSigmaY = cms.double( 0.0 ),
      useEcal = cms.bool( False ),
      muonMaxDistanceSigmaX = cms.double( 0.0 ),
      dRMuon = cms.double( 9999.0 ),
      dREcal = cms.double( 9999.0 ),
      CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
      DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
      EBRecHitCollectionLabel = cms.InputTag( "Notused" ),
      CaloTowerCollectionLabel = cms.InputTag( "Notused" ),
      propagateAllDirections = cms.bool( True ),
      muonMaxDistanceY = cms.double( 5.0 ),
      useHO = cms.bool( False ),
      muonMaxDistanceX = cms.double( 5.0 ),
      trajectoryUncertaintyTolerance = cms.double( -1.0 ),
      useHcal = cms.bool( False ),
      HBHERecHitCollectionLabel = cms.InputTag( "Notused" ),
      accountForTrajectoryChangeCalo = cms.bool( False ),
      dREcalPreselection = cms.double( 0.05 ),
      useCalo = cms.bool( False ),
      dRMuonPreselection = cms.double( 0.2 ),
      EERecHitCollectionLabel = cms.InputTag( "Notused" ),
      dRHcal = cms.double( 9999.0 ),
      dRHcalPreselection = cms.double( 0.2 ),
      HORecHitCollectionLabel = cms.InputTag( "Notused" )
    ),
    JetExtractorPSet = cms.PSet( 
      JetCollectionLabel = cms.InputTag( "Notused" ),
      DR_Veto = cms.double( 0.1 ),
      DR_Max = cms.double( 1.0 ),
      ExcludeMuonVeto = cms.bool( True ),
      PrintTimeReport = cms.untracked.bool( False ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      ComponentName = cms.string( "JetExtractor" ),
      ServiceParameters = cms.PSet( 
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False ),
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
      ),
      TrackAssociatorParameters = cms.PSet( 
        useMuon = cms.bool( False ),
        truthMatch = cms.bool( False ),
        usePreshower = cms.bool( False ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        useEcal = cms.bool( False ),
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        dRMuon = cms.double( 9999.0 ),
        dREcal = cms.double( 0.5 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EBRecHitCollectionLabel = cms.InputTag( "Notused" ),
        CaloTowerCollectionLabel = cms.InputTag( "Notused" ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        muonMaxDistanceX = cms.double( 5.0 ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        useHcal = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "Notused" ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        dREcalPreselection = cms.double( 0.5 ),
        useCalo = cms.bool( True ),
        dRMuonPreselection = cms.double( 0.2 ),
        EERecHitCollectionLabel = cms.InputTag( "Notused" ),
        dRHcal = cms.double( 0.5 ),
        dRHcalPreselection = cms.double( 0.5 ),
        HORecHitCollectionLabel = cms.InputTag( "Notused" )
      ),
      Threshold = cms.double( 5.0 )
    ),
    fillGlobalTrackQuality = cms.bool( False ),
    minPCaloMuon = cms.double( 1.0E9 ),
    maxAbsDy = cms.double( 9999.0 ),
    fillCaloCompatibility = cms.bool( False ),
    fillMatching = cms.bool( True ),
    MuonCaloCompatibility = cms.PSet( 
      delta_eta = cms.double( 0.02 ),
      delta_phi = cms.double( 0.02 ),
      allSiPMHO = cms.bool( False ),
      MuonTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root" ),
      PionTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root" )
    ),
    fillTrackerKink = cms.bool( False ),
    hcalDepositName = cms.string( "hcal" ),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double( 2.0 ),
    inputCollectionLabels = cms.VInputTag( 'hltIterL3MuonAndMuonFromL1MergedPPOnAA','hltIterL3GlbMuonPPOnAA','hltL2MuonsPPOnAA:UpdatedAtVtx' ),
    trackDepositName = cms.string( "tracker" ),
    maxAbsDx = cms.double( 9999.0 ),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double( 200.0 ),
    minNumberOfMatches = cms.int32( 1 )
)
process.hltIterL3MuonsPPOnAA = cms.EDProducer( "MuonIDFilterProducerForHLT",
    maxNormalizedChi2 = cms.double( 9999.0 ),
    minPt = cms.double( 0.0 ),
    applyTriggerIdLoose = cms.bool( True ),
    minNMuonHits = cms.int32( 0 ),
    minPixHits = cms.int32( 0 ),
    requiredTypeMask = cms.uint32( 0 ),
    minNMuonStations = cms.int32( 0 ),
    minPixLayer = cms.int32( 0 ),
    minNTrkLayers = cms.int32( 0 ),
    minTrkHits = cms.int32( 0 ),
    inputMuonCollection = cms.InputTag( "hltIterL3MuonsNoIDPPOnAA" ),
    allowedTypeMask = cms.uint32( 0 ),
    typeMuon = cms.uint32( 0 )
)
process.hltL3MuonsIterL3LinksPPOnAA = cms.EDProducer( "MuonLinksProducer",
    inputCollection = cms.InputTag( "hltIterL3MuonsPPOnAA" )
)
process.hltIterL3MuonTracksPPOnAA = cms.EDProducer( "HLTMuonTrackSelector",
    muon = cms.InputTag( "hltIterL3MuonsPPOnAA" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    track = cms.InputTag( "hltIterL3MuonAndMuonFromL1MergedPPOnAA" ),
    copyMVA = cms.bool( False ),
    originalMVAVals = cms.InputTag( "none" )
)
process.hltIterL3MuonCandidatesPPOnAA = cms.EDProducer( "L3MuonCandidateProducerFromMuons",
    InputObjects = cms.InputTag( "hltIterL3MuonsPPOnAA" )
)
process.hltPixelTracksFilter = cms.EDProducer( "PixelTrackFilterByKinematicsProducer",
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.1 ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    tipMax = cms.double( 1.0 )
)
process.hltPixelTracksFitter = cms.EDProducer( "PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool( False ),
    scaleFactor = cms.double( 0.65 )
)
process.hltPixelTracksTrackingRegionsPPOnAA = cms.EDProducer( "GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet( 
      nSigmaZ = cms.double( 4.0 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      ptMin = cms.double( 0.8 ),
      originRadius = cms.double( 0.02 ),
      precise = cms.bool( True )
    )
)
process.hltPixelLayerQuadrupletsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
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
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltPixelTracksHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltPixelTracksTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltPixelLayerQuadrupletsPPOnAA" )
)
process.hltPixelTracksHitQuadrupletsPPOnAA = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.002 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltPixelTracksHitDoubletsPPOnAA" ),
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
process.hltPixelTracksPPOnAA = cms.EDProducer( "PixelTrackProducer",
    Filter = cms.InputTag( "hltPixelTracksFilter" ),
    Cleaner = cms.string( "hltPixelTracksCleanerBySharedHits" ),
    passLabel = cms.string( "" ),
    Fitter = cms.InputTag( "hltPixelTracksFitter" ),
    SeedingHitSets = cms.InputTag( "hltPixelTracksHitQuadrupletsPPOnAA" )
)
process.hltPixelVerticesPPOnAA = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPixelTracksPPOnAA" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
process.hltTrimmedPixelVerticesPPOnAA = cms.EDProducer( "PixelVertexCollectionTrimmer",
    minSumPt2 = cms.double( 0.0 ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    maxVtx = cms.uint32( 100 ),
    fractionSumPt2 = cms.double( 0.3 ),
    src = cms.InputTag( "hltPixelVerticesPPOnAA" )
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
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
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
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 100000 ),
    ClusterCollectionLabel = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" )
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
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplittingPPOnAA" )
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
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplittingPPOnAA" )
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
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryBuilderPPOnAA" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
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
      maxNormalizedChi2 = cms.double( 10.0 ),
      trackQuality = cms.string( "any" ),
      algorithm = cms.string( "filter" ),
      maxD0Significance = cms.double( 3.0 )
    ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltFullIter0CtfWithMaterialTracksPPOnAA" ),
    TkClusParameters = cms.PSet( 
      algorithm = cms.string( "gap" ),
      TkGapClusParameters = cms.PSet(  zSeparation = cms.double( 1.0 ) )
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
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
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
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
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
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
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
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 100000 ),
    ClusterCollectionLabel = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" )
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
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplittingPPOnAA" )
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
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtQuadStepTrajectoryBuilderPPOnAA" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
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
process.hltIter1MergedPPOnAA = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltFullIter0HighPurityTracksPPOnAA','hltFullIter1HighPurityTracksPPOnAA' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltFullIter0HighPurityTracksPPOnAA','hltFullIter1HighPurityTracksPPOnAA' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltIter1TrackRefsForJets4Iter2PPOnAA = cms.EDProducer( "ChargedRefCandidateProducer",
    src = cms.InputTag( "hltIter1MergedPPOnAA" ),
    particleType = cms.string( "pi+" )
)
process.hltAK4Iter1TrackJets4Iter2PPOnAA = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    useMassDropTagger = cms.bool( False ),
    doAreaFastjet = cms.bool( False ),
    muMin = cms.double( -1.0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    subtractorName = cms.string( "" ),
    dRMax = cms.double( -1.0 ),
    useExplicitGhosts = cms.bool( False ),
    puWidth = cms.double( 0.0 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    R0 = cms.double( -1.0 ),
    jetType = cms.string( "TrackJet" ),
    muCut = cms.double( -1.0 ),
    subjetPtMin = cms.double( -1.0 ),
    csRParam = cms.double( -1.0 ),
    MinVtxNdof = cms.int32( 0 ),
    minSeed = cms.uint32( 14327 ),
    voronoiRfact = cms.double( 0.9 ),
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
    MaxVtxZ = cms.double( 30.0 ),
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
    DzTrVtxMax = cms.double( 0.5 ),
    UseOnlyOnePV = cms.bool( True ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    correctShape = cms.bool( False ),
    rcut_factor = cms.double( -1.0 ),
    src = cms.InputTag( "hltIter1TrackRefsForJets4Iter2PPOnAA" ),
    gridMaxRapidity = cms.double( -1.0 ),
    sumRecHits = cms.bool( False ),
    jetPtMin = cms.double( 7.5 ),
    puPtMin = cms.double( 0.0 ),
    srcPVs = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
    verbosity = cms.int32( 0 ),
    inputEtMin = cms.double( 0.1 ),
    useConstituentSubtraction = cms.bool( False ),
    beta = cms.double( -1.0 ),
    trimPtFracMin = cms.double( -1.0 ),
    radiusPU = cms.double( 0.4 ),
    nFilt = cms.int32( -1 ),
    useKtPruning = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.2 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    useCMSBoostedTauSeedingAlgorithm = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    writeJetsWithConst = cms.bool( False ),
    inputEMin = cms.double( 0.0 )
)
process.hltIter1TrackAndTauJets4Iter2PPOnAA = cms.EDProducer( "TauJetSelectorForHLTTrackSeeding",
    fractionMinCaloInTauCone = cms.double( 0.7 ),
    fractionMaxChargedPUInCaloCone = cms.double( 0.3 ),
    tauConeSize = cms.double( 0.2 ),
    ptTrkMaxInCaloCone = cms.double( 1.4 ),
    isolationConeSize = cms.double( 0.5 ),
    inputTrackJetTag = cms.InputTag( "hltAK4Iter1TrackJets4Iter2PPOnAA" ),
    nTrkMaxInCaloCone = cms.int32( 0 ),
    inputCaloJetTag = cms.InputTag( "hltAK4CaloJetsPFEt5" ),
    etaMinCaloJet = cms.double( -2.7 ),
    etaMaxCaloJet = cms.double( 2.7 ),
    ptMinCaloJet = cms.double( 10.0 ),
    inputTrackTag = cms.InputTag( "hltIter1MergedPPOnAA" )
)
process.hltFullIter2ClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltFullIter1HighPurityTracksPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter1ClustersRefRemovalPPOnAA" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
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
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
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
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
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
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 100000 ),
    ClusterCollectionLabel = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" )
)
process.hltFullIter2PixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltFullIter2PixelTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "hltFullIter2PixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( False ),
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
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplittingPPOnAA" )
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
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetHighPtTripletStepTrajectoryBuilderPPOnAA" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
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
process.hltIter2MergedPPOnAA = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter1MergedPPOnAA','hltFullIter2HighPurityTracksPPOnAA' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter1MergedPPOnAA','hltFullIter2HighPurityTracksPPOnAA' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltDoubletRecoveryClustersRefRemovalPPOnAA = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltFullIter2HighPurityTracksPPOnAA" ),
    oldClusterRemovalInfo = cms.InputTag( "hltFullIter2ClustersRefRemovalPPOnAA" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltDoubletRecoveryMaskedMeasurementTrackerEventPPOnAA = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltDoubletRecoveryClustersRefRemovalPPOnAA" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltDoubletRecoveryPixelLayersAndRegionsPPOnAA = cms.EDProducer( "PixelInactiveAreaTrackingRegionsSeedingLayersProducer",
    inactivePixelDetectorLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix1+BPix4',
      'BPix2+BPix3',
      'BPix2+BPix4',
      'BPix3+BPix4',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix1+FPix3_pos',
      'BPix1+FPix3_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'BPix3+FPix1_pos',
      'BPix3+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix3_pos',
      'FPix1_neg+FPix3_neg',
      'FPix2_pos+FPix3_pos',
      'FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    RegionPSet = cms.PSet( 
      precise = cms.bool( True ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 15.0 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      measurementTrackerName = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEventPPOnAA" ),
      extraEta = cms.double( 0.0 ),
      vertexCollection = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
      ptMin = cms.double( 1.2 ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
      maxNVertices = cms.int32( 3 ),
      extraPhi = cms.double( 0.0 ),
      originRadius = cms.double( 0.015 ),
      zErrorVertex = cms.double( 0.03 ),
      operationMode = cms.string( "VerticesFixed" )
    ),
    TEC = cms.PSet(  ),
    ignoreSingleFPixPanelModules = cms.bool( True ),
    TID = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltDoubletRecoveryClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
    ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltDoubletRecoveryClustersRefRemovalPPOnAA" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplittingPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    debug = cms.untracked.bool( False ),
    TOB = cms.PSet(  ),
    createPlottingFiles = cms.untracked.bool( False ),
    TIB = cms.PSet(  )
)
process.hltDoubletRecoveryPFlowPixelClusterCheckPPOnAA = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplittingPPOnAA" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 40000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersFullPPOnAA" )
)
process.hltDoubletRecoveryPFlowPixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltDoubletRecoveryPFlowPixelClusterCheckPPOnAA" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( False ),
    trackingRegionsSeedingLayers = cms.InputTag( "hltDoubletRecoveryPixelLayersAndRegionsPPOnAA" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "" )
)
process.hltDoubletRecoveryPFlowPixelSeedsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltDoubletRecoveryPFlowPixelHitDoubletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltDoubletRecoveryPFlowCkfTrackCandidatesPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltDoubletRecoveryPFlowPixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEventPPOnAA" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2GroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltDoubletRecoveryPFlowCtfWithMaterialTracksPPOnAA = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltDoubletRecoveryPFlowCkfTrackCandidatesPPOnAA" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEventPPOnAA" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltDoubletRecovery" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltDoubletRecoveryPFlowTrackCutClassifierPPOnAA = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltDoubletRecoveryPFlowCtfWithMaterialTracksPPOnAA" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      dr_par = cms.PSet( 
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 0.3 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 0.4 ),
        dr_exp = cms.vint32( 4, 4, 4 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet( 
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 0.4 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 0.35 ),
        dz_exp = cms.vint32( 4, 4, 4 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    ),
    ignoreVertices = cms.bool( False )
)
process.hltDoubletRecoveryPFlowTrackSelectionHighPurityPPOnAA = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltDoubletRecoveryPFlowCtfWithMaterialTracksPPOnAA" ),
    originalQualVals = cms.InputTag( 'hltDoubletRecoveryPFlowTrackCutClassifierPPOnAA','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltDoubletRecoveryPFlowTrackCutClassifierPPOnAA','MVAValues' )
)
process.hltMergedTracksPPOnAA = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter2MergedPPOnAA','hltDoubletRecoveryPFlowTrackSelectionHighPurityPPOnAA' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter2MergedPPOnAA','hltDoubletRecoveryPFlowTrackSelectionHighPurityPPOnAA' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltPFMuonMergingPPOnAA = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIterL3MuonTracksPPOnAA','hltMergedTracksPPOnAA' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIterL3MuonTracksPPOnAA','hltMergedTracksPPOnAA' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltMuonLinksPPOnAA = cms.EDProducer( "MuonLinksProducerForHLT",
    pMin = cms.double( 2.5 ),
    InclusiveTrackerTrackCollection = cms.InputTag( "hltPFMuonMergingPPOnAA" ),
    shareHitFraction = cms.double( 0.8 ),
    LinkCollection = cms.InputTag( "hltL3MuonsIterL3LinksPPOnAA" ),
    ptMin = cms.double( 2.5 )
)
process.hltMuonsPPOnAA = cms.EDProducer( "MuonIdProducer",
    TrackExtractorPSet = cms.PSet( 
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltPFMuonMergingPPOnAA" ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      BeamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
      DR_Veto = cms.double( 0.01 ),
      Pt_Min = cms.double( -1.0 ),
      DR_Max = cms.double( 1.0 ),
      DepositLabel = cms.untracked.string( "" ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Prob_Min = cms.double( -1.0 ),
      Diff_r = cms.double( 0.1 ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" ),
      ComponentName = cms.string( "TrackExtractor" )
    ),
    maxAbsEta = cms.double( 3.0 ),
    fillGlobalTrackRefits = cms.bool( False ),
    arbitrationCleanerOptions = cms.PSet( 
      OverlapDTheta = cms.double( 0.02 ),
      Overlap = cms.bool( True ),
      Clustering = cms.bool( True ),
      ME1a = cms.bool( True ),
      ClusterDTheta = cms.double( 0.02 ),
      ClusterDPhi = cms.double( 0.6 ),
      OverlapDPhi = cms.double( 0.0786 )
    ),
    globalTrackQualityInputTag = cms.InputTag( "glbTrackQual" ),
    addExtraSoftMuons = cms.bool( False ),
    debugWithTruthMatching = cms.bool( False ),
    CaloExtractorPSet = cms.PSet( 
      DR_Veto_H = cms.double( 0.1 ),
      CenterConeOnCalIntersection = cms.bool( False ),
      NoiseTow_EE = cms.double( 0.15 ),
      Noise_EB = cms.double( 0.025 ),
      Noise_HE = cms.double( 0.2 ),
      DR_Veto_E = cms.double( 0.07 ),
      NoiseTow_EB = cms.double( 0.04 ),
      Noise_EE = cms.double( 0.1 ),
      UseRecHitsFlag = cms.bool( False ),
      DR_Max = cms.double( 1.0 ),
      DepositLabel = cms.untracked.string( "Cal" ),
      Noise_HO = cms.double( 0.2 ),
      DR_Veto_HO = cms.double( 0.1 ),
      Threshold_H = cms.double( 0.5 ),
      PrintTimeReport = cms.untracked.bool( False ),
      Threshold_E = cms.double( 0.2 ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      ComponentName = cms.string( "CaloExtractorByAssociator" ),
      Threshold_HO = cms.double( 0.5 ),
      DepositInstanceLabels = cms.vstring( 'ecal',
        'hcal',
        'ho' ),
      ServiceParameters = cms.PSet( 
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False ),
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
      ),
      TrackAssociatorParameters = cms.PSet( 
        useMuon = cms.bool( False ),
        truthMatch = cms.bool( False ),
        usePreshower = cms.bool( False ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        useEcal = cms.bool( False ),
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        dRMuon = cms.double( 9999.0 ),
        dREcal = cms.double( 1.0 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForAll" ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        muonMaxDistanceX = cms.double( 5.0 ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        useHcal = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        dREcalPreselection = cms.double( 1.0 ),
        useCalo = cms.bool( True ),
        dRMuonPreselection = cms.double( 0.2 ),
        EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        dRHcal = cms.double( 1.0 ),
        dRHcalPreselection = cms.double( 1.0 ),
        HORecHitCollectionLabel = cms.InputTag( "hltHoreco" )
      ),
      Noise_HB = cms.double( 0.2 )
    ),
    runArbitrationCleaner = cms.bool( False ),
    fillEnergy = cms.bool( True ),
    TrackerKinkFinderParameters = cms.PSet( 
      usePosition = cms.bool( False ),
      diagonalOnly = cms.bool( False )
    ),
    TimingFillerParameters = cms.PSet( 
      DTTimingParameters = cms.PSet( 
        HitError = cms.double( 6.0 ),
        MatchParameters = cms.PSet( 
          TightMatchDT = cms.bool( False ),
          DTradius = cms.double( 0.01 ),
          TightMatchCSC = cms.bool( True ),
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" )
        ),
        debug = cms.bool( False ),
        DoWireCorr = cms.bool( False ),
        RequireBothProjections = cms.bool( False ),
        DTTimeOffset = cms.double( 2.7 ),
        PruneCut = cms.double( 10000.0 ),
        DTsegments = cms.InputTag( "hltDt4DSegments" ),
        UseSegmentT0 = cms.bool( False ),
        HitsMin = cms.int32( 5 ),
        DropTheta = cms.bool( True ),
        ServiceParameters = cms.PSet( 
          RPCLayers = cms.bool( True ),
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
        )
      ),
      UseCSC = cms.bool( True ),
      CSCTimingParameters = cms.PSet( 
        MatchParameters = cms.PSet( 
          TightMatchDT = cms.bool( False ),
          DTradius = cms.double( 0.01 ),
          TightMatchCSC = cms.bool( True ),
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" )
        ),
        debug = cms.bool( False ),
        CSCWireTimeOffset = cms.double( 0.0 ),
        CSCStripError = cms.double( 7.0 ),
        CSCTimeOffset = cms.double( 0.0 ),
        CSCWireError = cms.double( 8.6 ),
        PruneCut = cms.double( 100.0 ),
        CSCsegments = cms.InputTag( "hltCscSegments" ),
        UseStripTime = cms.bool( True ),
        CSCStripTimeOffset = cms.double( 0.0 ),
        UseWireTime = cms.bool( True ),
        ServiceParameters = cms.PSet( 
          RPCLayers = cms.bool( True ),
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
        )
      ),
      ErrorDT = cms.double( 6.0 ),
      EcalEnergyCut = cms.double( 0.4 ),
      UseECAL = cms.bool( True ),
      ErrorEB = cms.double( 2.085 ),
      UseDT = cms.bool( True ),
      ErrorEE = cms.double( 6.95 ),
      ErrorCSC = cms.double( 7.4 )
    ),
    inputCollectionTypes = cms.vstring( 'inner tracks',
      'links',
      'outer tracks' ),
    arbitrateTrackerMuons = cms.bool( False ),
    minCaloCompatibility = cms.double( 0.6 ),
    ecalDepositName = cms.string( "ecal" ),
    minP = cms.double( 10.0 ),
    fillIsolation = cms.bool( True ),
    jetDepositName = cms.string( "jets" ),
    hoDepositName = cms.string( "ho" ),
    writeIsoDeposits = cms.bool( False ),
    maxAbsPullX = cms.double( 4.0 ),
    maxAbsPullY = cms.double( 9999.0 ),
    minPt = cms.double( 10.0 ),
    TrackAssociatorParameters = cms.PSet( 
      useMuon = cms.bool( True ),
      truthMatch = cms.bool( False ),
      usePreshower = cms.bool( False ),
      dRPreshowerPreselection = cms.double( 0.2 ),
      muonMaxDistanceSigmaY = cms.double( 0.0 ),
      useEcal = cms.bool( True ),
      muonMaxDistanceSigmaX = cms.double( 0.0 ),
      dRMuon = cms.double( 9999.0 ),
      dREcal = cms.double( 9999.0 ),
      CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
      DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
      EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForAll" ),
      propagateAllDirections = cms.bool( True ),
      muonMaxDistanceY = cms.double( 5.0 ),
      useHO = cms.bool( True ),
      muonMaxDistanceX = cms.double( 5.0 ),
      trajectoryUncertaintyTolerance = cms.double( -1.0 ),
      useHcal = cms.bool( True ),
      HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
      accountForTrajectoryChangeCalo = cms.bool( False ),
      dREcalPreselection = cms.double( 0.05 ),
      useCalo = cms.bool( False ),
      dRMuonPreselection = cms.double( 0.2 ),
      EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
      dRHcal = cms.double( 9999.0 ),
      dRHcalPreselection = cms.double( 0.2 ),
      HORecHitCollectionLabel = cms.InputTag( "hltHoreco" )
    ),
    JetExtractorPSet = cms.PSet( 
      JetCollectionLabel = cms.InputTag( "hltAK4CaloJetsPFEt5" ),
      DR_Veto = cms.double( 0.1 ),
      DR_Max = cms.double( 1.0 ),
      ExcludeMuonVeto = cms.bool( True ),
      PrintTimeReport = cms.untracked.bool( False ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      ComponentName = cms.string( "JetExtractor" ),
      ServiceParameters = cms.PSet( 
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False ),
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
      ),
      TrackAssociatorParameters = cms.PSet( 
        useMuon = cms.bool( False ),
        truthMatch = cms.bool( False ),
        usePreshower = cms.bool( False ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        useEcal = cms.bool( False ),
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        dRMuon = cms.double( 9999.0 ),
        dREcal = cms.double( 0.5 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForAll" ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        muonMaxDistanceX = cms.double( 5.0 ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        useHcal = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        dREcalPreselection = cms.double( 0.5 ),
        useCalo = cms.bool( True ),
        dRMuonPreselection = cms.double( 0.2 ),
        EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        dRHcal = cms.double( 0.5 ),
        dRHcalPreselection = cms.double( 0.5 ),
        HORecHitCollectionLabel = cms.InputTag( "hltHoreco" )
      ),
      Threshold = cms.double( 5.0 )
    ),
    fillGlobalTrackQuality = cms.bool( False ),
    minPCaloMuon = cms.double( 1.0E9 ),
    maxAbsDy = cms.double( 9999.0 ),
    fillCaloCompatibility = cms.bool( True ),
    fillMatching = cms.bool( True ),
    MuonCaloCompatibility = cms.PSet( 
      delta_eta = cms.double( 0.02 ),
      delta_phi = cms.double( 0.02 ),
      allSiPMHO = cms.bool( False ),
      MuonTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root" ),
      PionTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root" )
    ),
    fillTrackerKink = cms.bool( False ),
    hcalDepositName = cms.string( "hcal" ),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double( 2.0 ),
    inputCollectionLabels = cms.VInputTag( 'hltPFMuonMergingPPOnAA','hltMuonLinksPPOnAA','hltL2MuonsPPOnAA' ),
    trackDepositName = cms.string( "tracker" ),
    maxAbsDx = cms.double( 3.0 ),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double( 200.0 ),
    minNumberOfMatches = cms.int32( 1 )
)
process.hltParticleFlowRecHitECALUnseeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        srFlags = cms.InputTag( "" ),
        name = cms.string( "PFEBRecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  name = cms.string( "PFRecHitQTestDBThreshold" ),
            applySelectionsToAllCrystals = cms.bool( True )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        )
      ),
      cms.PSet(  src = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        srFlags = cms.InputTag( "" ),
        name = cms.string( "PFEERecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  name = cms.string( "PFRecHitQTestDBThreshold" ),
            applySelectionsToAllCrystals = cms.bool( True )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        )
      )
    ),
    navigator = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitECALNavigator" )
    )
)
process.hltParticleFlowRecHitHBHE = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( "hltHbhereco" ),
        name = cms.string( "PFHBHERecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.8 ),
            name = cms.string( "PFRecHitQTestThreshold" ),
            cuts = cms.VPSet( 
              cms.PSet(  depth = cms.vint32( 1, 2, 3, 4 ),
                threshold = cms.vdouble( 0.8, 0.8, 0.8, 0.8 ),
                detectorEnum = cms.int32( 1 )
              ),
              cms.PSet(  depth = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
                threshold = cms.vdouble( 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8 ),
                detectorEnum = cms.int32( 2 )
              )
            )
          ),
          cms.PSet(  flags = cms.vstring( 'Standard' ),
            cleaningThresholds = cms.vdouble( 0.0 ),
            name = cms.string( "PFRecHitQTestHCALChannel" ),
            maxSeverities = cms.vint32( 11 )
          )
        )
      )
    ),
    navigator = cms.PSet( 
      name = cms.string( "PFRecHitHCALNavigator" ),
      sigmaCut = cms.double( 4.0 ),
      timeResolutionCalc = cms.PSet( 
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 2.0 ),
        noiseTerm = cms.double( 8.64 ),
        constantTermLowE = cms.double( 6.0 ),
        noiseTermLowE = cms.double( 0.0 ),
        threshHighE = cms.double( 8.0 ),
        constantTerm = cms.double( 1.92 )
      )
    )
)
process.hltParticleFlowRecHitHF = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  thresh_HF = cms.double( 0.4 ),
        LongFibre_Fraction = cms.double( 0.1 ),
        src = cms.InputTag( "hltHfreco" ),
        EMDepthCorrection = cms.double( 22.0 ),
        ShortFibre_Fraction = cms.double( 0.01 ),
        HADDepthCorrection = cms.double( 25.0 ),
        HFCalib29 = cms.double( 1.07 ),
        LongFibre_Cut = cms.double( 120.0 ),
        name = cms.string( "PFHFRecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  flags = cms.vstring( 'Standard',
  'HFLong',
  'HFShort' ),
            cleaningThresholds = cms.vdouble( 0.0, 120.0, 60.0 ),
            name = cms.string( "PFRecHitQTestHCALChannel" ),
            maxSeverities = cms.vint32( 11, 9, 9 )
          ),
          cms.PSet(  name = cms.string( "PFRecHitQTestHCALThresholdVsDepth" ),
            cuts = cms.VPSet( 
              cms.PSet(  depth = cms.vint32( 1, 2 ),
                threshold = cms.vdouble( 1.2, 1.8 ),
                detectorEnum = cms.int32( 4 )
              )
            )
          )
        ),
        ShortFibre_Cut = cms.double( 60.0 )
      )
    ),
    navigator = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitHCALNavigator" )
    )
)
process.hltParticleFlowRecHitPSUnseeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltEcalPreshowerRecHit','EcalRecHitsES' ),
        name = cms.string( "PFPSRecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 7.0E-6 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          )
        )
      )
    ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitPreshowerNavigator" ) )
)
process.hltParticleFlowClusterECALUncorrectedUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 9 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet( 
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet( 
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      maxIterations = cms.uint32( 50 ),
      positionCalcForConvergence = cms.PSet( 
        minAllowedNormalization = cms.double( 0.0 ),
        T0_ES = cms.double( 1.2 ),
        algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
        T0_EE = cms.double( 3.1 ),
        T0_EB = cms.double( 7.4 ),
        X0 = cms.double( 0.89 ),
        minFractionInCalc = cms.double( 0.0 ),
        W0 = cms.double( 4.2 )
      ),
      allCellsPositionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet( 
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet( 
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  recHitEnergyNorm = cms.double( 0.08 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 0.3 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      showerSigma = cms.double( 1.5 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet( 
      minAllowedNormalization = cms.double( 0.0 ),
      T0_ES = cms.double( 1.2 ),
      algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
      T0_EE = cms.double( 3.1 ),
      T0_EB = cms.double( 7.4 ),
      X0 = cms.double( 0.89 ),
      minFractionInCalc = cms.double( 0.0 ),
      W0 = cms.double( 4.2 )
    ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.08 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.3 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( True )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThresholdPt = cms.double( 0.15 ),
          seedingThreshold = cms.double( 0.6 ),
          detector = cms.string( "ECAL_ENDCAP" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 0.23 ),
          detector = cms.string( "ECAL_BARREL" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 8 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitECALUnseeded" )
)
process.hltParticleFlowClusterPSUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 6.0E-5 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 50 ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS2" )
        )
      ),
      showerSigma = cms.double( 0.3 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( False )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 4 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitPSUnseeded" )
)
process.hltParticleFlowClusterECALUnseeded = cms.EDProducer( "CorrectedECALPFClusterProducer",
    inputPS = cms.InputTag( "hltParticleFlowClusterPSUnseeded" ),
    minimumPSEnergy = cms.double( 0.0 ),
    energyCorrector = cms.PSet( 
      algoName = cms.string( "PFClusterEMEnergyCorrector" ),
      applyCrackCorrections = cms.bool( False )
    ),
    inputECAL = cms.InputTag( "hltParticleFlowClusterECALUncorrectedUnseeded" )
)
process.hltParticleFlowClusterHBHE = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 50 ),
      minChi2Prob = cms.double( 0.0 ),
      allCellsPositionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          depths = cms.vint32( 1, 2, 3, 4 ),
          recHitEnergyNorm = cms.vdouble( 0.8, 0.8, 0.8, 0.8 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
          recHitEnergyNorm = cms.vdouble( 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8 )
        )
      ),
      maxNSigmaTime = cms.double( 10.0 ),
      showerSigma = cms.double( 10.0 ),
      timeSigmaEE = cms.double( 10.0 ),
      clusterTimeResFromSeed = cms.bool( False ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      timeResolutionCalcBarrel = cms.PSet( 
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 6.0 ),
        noiseTerm = cms.double( 21.86 ),
        constantTermLowE = cms.double( 4.24 ),
        noiseTermLowE = cms.double( 8.0 ),
        threshHighE = cms.double( 15.0 ),
        constantTerm = cms.double( 2.82 )
      ),
      timeResolutionCalcEndcap = cms.PSet( 
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 6.0 ),
        noiseTerm = cms.double( 21.86 ),
        constantTermLowE = cms.double( 4.24 ),
        noiseTermLowE = cms.double( 8.0 ),
        threshHighE = cms.double( 15.0 ),
        constantTerm = cms.double( 2.82 )
      ),
      timeSigmaEB = cms.double( 10.0 )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          depths = cms.vint32( 1, 2, 3, 4 ),
          gatheringThreshold = cms.vdouble( 0.8, 0.8, 0.8, 0.8 ),
          gatheringThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
          gatheringThreshold = cms.vdouble( 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8 ),
          gatheringThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( True )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          depths = cms.vint32( 1, 2, 3, 4 ),
          seedingThreshold = cms.vdouble( 1.0, 1.0, 1.0, 1.0 ),
          seedingThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
          seedingThreshold = cms.vdouble( 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1 ),
          seedingThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 4 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitHBHE" )
)
process.hltParticleFlowClusterHCAL = cms.EDProducer( "PFMultiDepthClusterProducer",
    pfClusterBuilder = cms.PSet( 
      allCellsPositionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      algoName = cms.string( "PFMultiDepthClusterizer" ),
      nSigmaPhi = cms.double( 2.0 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      nSigmaEta = cms.double( 2.0 )
    ),
    energyCorrector = cms.PSet(  ),
    positionReCalc = cms.PSet(  ),
    clustersSource = cms.InputTag( "hltParticleFlowClusterHBHE" )
)
process.hltParticleFlowClusterHF = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 50 ),
      allCellsPositionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  recHitEnergyNorm = cms.double( 0.8 ),
          detector = cms.string( "HF_EM" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 0.8 ),
          detector = cms.string( "HF_HAD" )
        )
      ),
      showerSigma = cms.double( 0.0 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HF_EM" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HF_HAD" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( False )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.4 ),
          detector = cms.string( "HF_EM" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.4 ),
          detector = cms.string( "HF_HAD" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 0 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitHF" )
)
process.hltLightPFTracksPPOnAA = cms.EDProducer( "LightPFTrackProducer",
    TrackQuality = cms.string( "none" ),
    UseQuality = cms.bool( False ),
    TkColList = cms.VInputTag( 'hltPFMuonMergingPPOnAA' )
)
process.hltParticleFlowBlockPPOnAA = cms.EDProducer( "PFBlockProducer",
    debug = cms.untracked.bool( False ),
    linkDefinitions = cms.VPSet( 
      cms.PSet(  linkType = cms.string( "PS1:ECAL" ),
        useKDTree = cms.bool( True ),
        linkerName = cms.string( "PreshowerAndECALLinker" )
      ),
      cms.PSet(  linkType = cms.string( "PS2:ECAL" ),
        useKDTree = cms.bool( True ),
        linkerName = cms.string( "PreshowerAndECALLinker" )
      ),
      cms.PSet(  linkType = cms.string( "TRACK:ECAL" ),
        useKDTree = cms.bool( True ),
        linkerName = cms.string( "TrackAndECALLinker" )
      ),
      cms.PSet(  linkType = cms.string( "TRACK:HCAL" ),
        useKDTree = cms.bool( True ),
        linkerName = cms.string( "TrackAndHCALLinker" )
      ),
      cms.PSet(  linkType = cms.string( "ECAL:HCAL" ),
        useKDTree = cms.bool( False ),
        linkerName = cms.string( "ECALAndHCALLinker" )
      ),
      cms.PSet(  linkType = cms.string( "HFEM:HFHAD" ),
        useKDTree = cms.bool( False ),
        linkerName = cms.string( "HFEMAndHFHADLinker" )
      )
    ),
    elementImporters = cms.VPSet( 
      cms.PSet(  muonSrc = cms.InputTag( "hltMuonsPPOnAA" ),
        source = cms.InputTag( "hltLightPFTracksPPOnAA" ),
        NHitCuts_byTrackAlgo = cms.vuint32( 3, 3, 3, 3, 3, 3 ),
        useIterativeTracking = cms.bool( False ),
        importerName = cms.string( "GeneralTracksImporter" ),
        DPtOverPtCuts_byTrackAlgo = cms.vdouble( 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 )
      ),
      cms.PSet(  source = cms.InputTag( "hltParticleFlowClusterECALUnseeded" ),
        importerName = cms.string( "ECALClusterImporter" ),
        BCtoPFCMap = cms.InputTag( "" )
      ),
      cms.PSet(  source = cms.InputTag( "hltParticleFlowClusterHCAL" ),
        importerName = cms.string( "GenericClusterImporter" )
      ),
      cms.PSet(  source = cms.InputTag( "hltParticleFlowClusterHF" ),
        importerName = cms.string( "GenericClusterImporter" )
      ),
      cms.PSet(  source = cms.InputTag( "hltParticleFlowClusterPSUnseeded" ),
        importerName = cms.string( "GenericClusterImporter" )
      )
    ),
    verbose = cms.untracked.bool( False )
)
process.hltParticleFlowPPOnAA = cms.EDProducer( "PFProducer",
    photon_SigmaiEtaiEta_endcap = cms.double( 0.034 ),
    minPtForPostCleaning = cms.double( 20.0 ),
    pf_nsigma_ECAL = cms.double( 0.0 ),
    GedPhotonValueMap = cms.InputTag( 'tmpGedPhotons','valMapPFEgammaCandToPhoton' ),
    sumPtTrackIsoForPhoton = cms.double( -1.0 ),
    goodPixelTrackDeadHcal_ptErrRel = cms.double( 1.0 ),
    calibrationsLabel = cms.string( "HLT" ),
    metFactorForFakes = cms.double( 4.0 ),
    muon_HO = cms.vdouble( 0.9, 0.9 ),
    electron_missinghits = cms.uint32( 1 ),
    metSignificanceForCleaning = cms.double( 3.0 ),
    usePFPhotons = cms.bool( False ),
    maxDeltaPhiPt = cms.double( 7.0 ),
    nTrackIsoForEgammaSC = cms.uint32( 2 ),
    pf_nsigma_HCAL = cms.double( 1.0 ),
    cosmicRejectionDistance = cms.double( 1.0 ),
    goodTrackDeadHcal_ptErrRel = cms.double( 0.2 ),
    useEGammaFilters = cms.bool( False ),
    useEGammaElectrons = cms.bool( False ),
    nsigma_TRACK = cms.double( 1.0 ),
    useEGammaSupercluster = cms.bool( False ),
    goodTrackDeadHcal_dxy = cms.double( 0.5 ),
    eventFractionForCleaning = cms.double( 0.5 ),
    usePFDecays = cms.bool( False ),
    rejectTracks_Step45 = cms.bool( False ),
    eventFractionForRejection = cms.double( 0.8 ),
    photon_MinEt = cms.double( 10.0 ),
    usePFNuclearInteractions = cms.bool( False ),
    maxSignificance = cms.double( 2.5 ),
    electron_iso_mva_endcap = cms.double( -0.1075 ),
    debug = cms.untracked.bool( False ),
    pf_convID_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_pfConversionAug0411.txt" ),
    calibHF_eta_step = cms.vdouble( 0.0, 2.9, 3.0, 3.2, 4.2, 4.4, 4.6, 4.8, 5.2, 5.4 ),
    ptErrorScale = cms.double( 8.0 ),
    goodPixelTrackDeadHcal_maxLost3Hit = cms.int32( 0 ),
    minSignificance = cms.double( 2.5 ),
    minMomentumForPunchThrough = cms.double( 100.0 ),
    pf_conv_mvaCut = cms.double( 0.0 ),
    useCalibrationsFromDB = cms.bool( True ),
    usePFElectrons = cms.bool( False ),
    electron_iso_combIso_endcap = cms.double( 10.0 ),
    photon_combIso = cms.double( 10.0 ),
    goodTrackDeadHcal_validFr = cms.double( 0.5 ),
    electron_iso_mva_barrel = cms.double( -0.1875 ),
    postHFCleaning = cms.bool( False ),
    factors_45 = cms.vdouble( 10.0, 100.0 ),
    cleanedHF = cms.VInputTag( 'hltParticleFlowRecHitHF:Cleaned','hltParticleFlowClusterHF:Cleaned' ),
    coneEcalIsoForEgammaSC = cms.double( 0.3 ),
    minSignificanceReduction = cms.double( 1.4 ),
    photon_SigmaiEtaiEta_barrel = cms.double( 0.0125 ),
    calibHF_b_HADonly = cms.vdouble( 1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 0.94348, 0.9437, 1.0034, 1.0444, 1.0444 ),
    minPixelHits = cms.int32( 1 ),
    maxDPtOPt = cms.double( 1.0 ),
    useHO = cms.bool( False ),
    pf_electron_output_col = cms.string( "electrons" ),
    electron_noniso_mvaCut = cms.double( -0.1 ),
    goodPixelTrackDeadHcal_minEta = cms.double( 2.3 ),
    useVerticesForNeutral = cms.bool( True ),
    trackQuality = cms.string( "highPurity" ),
    PFEGammaCandidates = cms.InputTag( "particleFlowEGamma" ),
    goodTrackDeadHcal_layers = cms.uint32( 4 ),
    sumPtTrackIsoSlopeForPhoton = cms.double( -1.0 ),
    goodPixelTrackDeadHcal_dxy = cms.double( 0.02 ),
    coneTrackIsoForEgammaSC = cms.double( 0.3 ),
    GedElectronValueMap = cms.InputTag( "gedGsfElectronsTmp" ),
    goodPixelTrackDeadHcal_chi2n = cms.double( 2.0 ),
    punchThroughMETFactor = cms.double( 4.0 ),
    useProtectionsForJetMET = cms.bool( True ),
    metFactorForRejection = cms.double( 4.0 ),
    sumPtTrackIsoForEgammaSC_endcap = cms.double( 4.0 ),
    calibHF_use = cms.bool( False ),
    verbose = cms.untracked.bool( False ),
    usePFConversions = cms.bool( False ),
    calibPFSCEle_endcap = cms.vdouble( 1.153, -16.5975, 5.668, -0.1772, 16.22, 7.326, 0.0483, -4.068, 9.406 ),
    metFactorForCleaning = cms.double( 4.0 ),
    eventFactorForCosmics = cms.double( 10.0 ),
    egammaElectrons = cms.InputTag( "" ),
    minEnergyForPunchThrough = cms.double( 100.0 ),
    minTrackerHits = cms.int32( 8 ),
    iCfgCandConnector = cms.PSet( 
      nuclCalibFactors = cms.vdouble( 0.8, 0.15, 0.5, 0.5, 0.05 ),
      bCalibSecondary = cms.bool( False ),
      bCorrect = cms.bool( False ),
      bCalibPrimary = cms.bool( False )
    ),
    rejectTracks_Bad = cms.bool( False ),
    pf_electronID_crackCorrection = cms.bool( False ),
    pf_Res_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFRes_14Dec2011.root" ),
    sumPtTrackIsoForEgammaSC_barrel = cms.double( 4.0 ),
    calibHF_a_EMonly = cms.vdouble( 0.96945, 0.96701, 0.76309, 0.82268, 0.87583, 0.89718, 0.98674, 1.4681, 1.458, 1.458 ),
    pf_locC_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFClusterLCorr_14Dec2011.root" ),
    metFactorForHighEta = cms.double( 25.0 ),
    minHFCleaningPt = cms.double( 5.0 ),
    photon_protectionsForBadHcal = cms.PSet( 
      solidConeTrkIsoSlope = cms.double( 0.3 ),
      enableProtections = cms.bool( False ),
      solidConeTrkIsoOffset = cms.double( 10.0 )
    ),
    pf_electron_mvaCut = cms.double( -0.1 ),
    ptFactorForHighEta = cms.double( 2.0 ),
    goodPixelTrackDeadHcal_maxPt = cms.double( 50.0 ),
    sumEtEcalIsoForEgammaSC_endcap = cms.double( 2.0 ),
    dptRel_DispVtx = cms.double( 10.0 ),
    pf_electronID_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_PfElectrons23Jan_IntToFloat.txt" ),
    goodTrackDeadHcal_chi2n = cms.double( 5.0 ),
    electron_protectionsForBadHcal = cms.PSet( 
      dEta = cms.vdouble( 0.0064, 0.01264 ),
      dPhi = cms.vdouble( 0.0547, 0.0394 ),
      enableProtections = cms.bool( False ),
      eInvPInv = cms.vdouble( 0.184, 0.0721 ),
      full5x5_sigmaIetaIeta = cms.vdouble( 0.0106, 0.0387 )
    ),
    goodPixelTrackDeadHcal_dz = cms.double( 0.05 ),
    calibHF_b_EMHAD = cms.vdouble( 1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 0.94348, 0.9437, 1.0034, 1.0444, 1.0444 ),
    pf_GlobC_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFGlobalCorr_14Dec2011.root" ),
    photon_HoE = cms.double( 0.05 ),
    sumEtEcalIsoForEgammaSC_barrel = cms.double( 1.0 ),
    calibPFSCEle_Fbrem_endcap = cms.vdouble( 0.9, 6.5, -0.0692932, 0.101776, 0.995338, -0.00236548, 0.874998, 1.653, -0.0750184, 0.147, 0.923165, 4.74665E-4, 1.10782 ),
    punchThroughFactor = cms.double( 3.0 ),
    algoType = cms.uint32( 0 ),
    electron_iso_combIso_barrel = cms.double( 10.0 ),
    muons = cms.InputTag( "hltMuonsPPOnAA" ),
    goodPixelTrackDeadHcal_maxLost4Hit = cms.int32( 1 ),
    postMuonCleaning = cms.bool( True ),
    minDeltaMet = cms.double( 0.4 ),
    calibPFSCEle_barrel = cms.vdouble( 1.004, -1.536, 22.88, -1.467, 0.3555, 0.6227, 14.65, 2051.0, 25.0, 0.9932, -0.5444, 0.0, 0.5438, 0.7109, 7.645, 0.2904, 0.0 ),
    electron_protectionsForJetMET = cms.PSet( 
      maxEeleOverPoutRes = cms.double( 0.5 ),
      maxEleHcalEOverEcalE = cms.double( 0.1 ),
      maxEcalEOverPRes = cms.double( 0.2 ),
      maxHcalEOverP = cms.double( 1.0 ),
      maxE = cms.double( 50.0 ),
      maxTrackPOverEele = cms.double( 1.0 ),
      maxDPhiIN = cms.double( 0.1 ),
      maxEcalEOverP_2 = cms.double( 0.2 ),
      maxEcalEOverP_1 = cms.double( 0.5 ),
      maxEeleOverPout = cms.double( 0.2 ),
      maxHcalEOverEcalE = cms.double( 0.1 ),
      maxHcalE = cms.double( 10.0 ),
      maxNtracks = cms.double( 3.0 )
    ),
    electron_iso_pt = cms.double( 10.0 ),
    isolatedElectronID_mvaWeightFile = cms.string( "RecoEgamma/ElectronIdentification/data/TMVA_BDTSimpleCat_17Feb2011.weights.xml" ),
    vertexCollection = cms.InputTag( "hltPixelVerticesPPOnAA" ),
    X0_Map = cms.string( "RecoParticleFlow/PFProducer/data/allX0histos.root" ),
    calibPFSCEle_Fbrem_barrel = cms.vdouble( 0.6, 6.0, -0.0255975, 0.0576727, 0.975442, -5.46394E-4, 1.26147, 25.0, -0.02025, 0.04537, 0.9728, -8.962E-4, 1.172 ),
    blocks = cms.InputTag( "hltParticleFlowBlockPPOnAA" ),
    pt_Error = cms.double( 1.0 ),
    metSignificanceForRejection = cms.double( 4.0 ),
    photon_protectionsForJetMET = cms.PSet( 
      sumPtTrackIsoSlope = cms.double( 0.001 ),
      sumPtTrackIso = cms.double( 2.0 )
    ),
    usePhotonReg = cms.bool( False ),
    dzPV = cms.double( 0.2 ),
    calibHF_a_EMHAD = cms.vdouble( 1.42215, 1.00496, 0.68961, 0.81656, 0.98504, 0.98504, 1.00802, 1.0593, 1.4576, 1.4576 ),
    muon_HCAL = cms.vdouble( 3.0, 3.0 ),
    useRegressionFromDB = cms.bool( False ),
    muon_ECAL = cms.vdouble( 0.5, 0.5 ),
    usePFSCEleCalib = cms.bool( True )
)
process.hltKT4PFJetsForRho = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    useMassDropTagger = cms.bool( False ),
    doAreaFastjet = cms.bool( True ),
    muMin = cms.double( -1.0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    subtractorName = cms.string( "" ),
    dRMax = cms.double( -1.0 ),
    useExplicitGhosts = cms.bool( False ),
    puWidth = cms.double( 0.0 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    R0 = cms.double( -1.0 ),
    jetType = cms.string( "PFJet" ),
    muCut = cms.double( -1.0 ),
    subjetPtMin = cms.double( -1.0 ),
    csRParam = cms.double( -1.0 ),
    MinVtxNdof = cms.int32( 0 ),
    minSeed = cms.uint32( 0 ),
    voronoiRfact = cms.double( -9.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "Kt" ),
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
    src = cms.InputTag( "hltParticleFlowPPOnAA" ),
    gridMaxRapidity = cms.double( -1.0 ),
    sumRecHits = cms.bool( False ),
    jetPtMin = cms.double( 0.0 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "hltPixelVerticesPPOnAA" ),
    verbosity = cms.int32( 0 ),
    inputEtMin = cms.double( 0.0 ),
    useConstituentSubtraction = cms.bool( False ),
    beta = cms.double( -1.0 ),
    trimPtFracMin = cms.double( -1.0 ),
    radiusPU = cms.double( 0.5 ),
    nFilt = cms.int32( -1 ),
    useKtPruning = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    useCMSBoostedTauSeedingAlgorithm = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    writeJetsWithConst = cms.bool( False ),
    inputEMin = cms.double( 0.0 )
)
process.hltHiFJRhoProducer = cms.EDProducer( "HiFJRhoProducer",
    etaMaxExcl2 = cms.double( 3.0 ),
    jetSource = cms.InputTag( "hltKT4PFJetsForRho" ),
    ptMinExcl = cms.double( 20.0 ),
    etaRanges = cms.vdouble( -5.0, -3.0, -2.1, -1.3, 1.3, 2.1, 3.0, 5.0 ),
    ptMinExcl2 = cms.double( 20.0 ),
    nExcl2 = cms.int32( 1 ),
    nExcl = cms.int32( 2 ),
    etaMaxExcl = cms.double( 2.0 )
)
process.hltCsAK4PFJetsPPOnAA = cms.EDProducer( "CSJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( True ),
    rhom = cms.InputTag( 'hltHiFJRhoProducer','mapToRhoM' ),
    voronoiRfact = cms.double( -0.9 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    subtractorName = cms.string( "" ),
    useExplicitGhosts = cms.bool( True ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "PFJet" ),
    csRParam = cms.double( -1.0 ),
    minSeed = cms.uint32( 14327 ),
    Ghost_EtaMax = cms.double( 6.5 ),
    doRhoFastjet = cms.bool( True ),
    maxInputs = cms.uint32( 1 ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.005 ),
    Rho_EtaMax = cms.double( 4.5 ),
    restrictInputs = cms.bool( False ),
    nExclude = cms.uint32( 2 ),
    csAlpha = cms.double( 2.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    jetCollInstanceName = cms.string( "pfParticlesCs" ),
    useDeterministicSeed = cms.bool( False ),
    doPVCorrection = cms.bool( False ),
    puCenters = cms.vdouble( -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.4 ),
    doFastJetNonUniform = cms.bool( True ),
    rho = cms.InputTag( 'hltHiFJRhoProducer','mapToRho' ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    writeCompound = cms.bool( False ),
    src = cms.InputTag( "hltParticleFlowPPOnAA" ),
    sumRecHits = cms.bool( False ),
    jetPtMin = cms.double( 5.0 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "" ),
    verbosity = cms.int32( 0 ),
    inputEtMin = cms.double( 0.0 ),
    puWidth = cms.double( 0.8 ),
    radiusPU = cms.double( 0.5 ),
    jetAlgorithm = cms.string( "AntiKt" ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    etaMap = cms.InputTag( 'hltHiFJRhoProducer','mapEtaEdges' ),
    doPUOffsetCorr = cms.bool( False ),
    writeJetsWithConst = cms.bool( True ),
    inputEMin = cms.double( 0.0 )
)
process.hltCsAK4PFJetsLooseIDPPOnAA = cms.EDProducer( "HLTPFJetIDProducer",
    CEF = cms.double( 0.99 ),
    NHF = cms.double( 0.99 ),
    minPt = cms.double( 20.0 ),
    CHF = cms.double( 0.0 ),
    jetsInput = cms.InputTag( "hltCsAK4PFJetsPPOnAA" ),
    NEF = cms.double( 0.99 ),
    NTOT = cms.int32( 1 ),
    NCH = cms.int32( 0 ),
    maxEta = cms.double( 1.0E99 ),
    maxCF = cms.double( 99.0 )
)
process.hltCsAK4PFJetsTightIDPPOnAA = cms.EDProducer( "HLTPFJetIDProducer",
    CEF = cms.double( 0.99 ),
    NHF = cms.double( 0.9 ),
    minPt = cms.double( 20.0 ),
    CHF = cms.double( 0.0 ),
    jetsInput = cms.InputTag( "hltCsAK4PFJetsPPOnAA" ),
    NEF = cms.double( 0.99 ),
    NTOT = cms.int32( 1 ),
    NCH = cms.int32( 0 ),
    maxEta = cms.double( 1.0E99 ),
    maxCF = cms.double( 99.0 )
)
process.hltFixedGridRhoFastjetAllPPOnAA = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 5.0 ),
    pfCandidatesTag = cms.InputTag( "hltParticleFlowPPOnAA" )
)
process.hltCsAK4PFFastJetCorrectorPPOnAA = cms.EDProducer( "L1FastjetCorrectorProducer",
    srcRho = cms.InputTag( "hltFixedGridRhoFastjetAllPPOnAA" ),
    algorithm = cms.string( "AK4PFHLT" ),
    level = cms.string( "L1FastJet" )
)
process.hltCsAK4PFRelativeCorrectorPPOnAA = cms.EDProducer( "LXXXCorrectorProducer",
    algorithm = cms.string( "AK4PFHLT" ),
    level = cms.string( "L2Relative" )
)
process.hltCsAK4PFAbsoluteCorrectorPPOnAA = cms.EDProducer( "LXXXCorrectorProducer",
    algorithm = cms.string( "AK4PFHLT" ),
    level = cms.string( "L3Absolute" )
)
process.hltCsAK4PFResidualCorrectorPPOnAA = cms.EDProducer( "LXXXCorrectorProducer",
    algorithm = cms.string( "AK4PFHLT" ),
    level = cms.string( "L2L3Residual" )
)
process.hltCsAK4PFCorrectorPPOnAA = cms.EDProducer( "ChainedJetCorrectorProducer",
    correctors = cms.VInputTag( 'hltCsAK4PFRelativeCorrectorPPOnAA','hltCsAK4PFAbsoluteCorrectorPPOnAA' )
)
process.hltCsAK4PFJetsCorrectedPPOnAA = cms.EDProducer( "CorrectedPFJetProducer",
    src = cms.InputTag( "hltCsAK4PFJetsPPOnAA" ),
    correctors = cms.VInputTag( 'hltCsAK4PFCorrectorPPOnAA' )
)
process.hltCsAK4PFJetsLooseIDCorrectedPPOnAA = cms.EDProducer( "CorrectedPFJetProducer",
    src = cms.InputTag( "hltCsAK4PFJetsLooseIDPPOnAA" ),
    correctors = cms.VInputTag( 'hltCsAK4PFCorrectorPPOnAA' )
)
process.hltCsAK4PFJetsTightIDCorrectedPPOnAA = cms.EDProducer( "CorrectedPFJetProducer",
    src = cms.InputTag( "hltCsAK4PFJetsTightIDPPOnAA" ),
    correctors = cms.VInputTag( 'hltCsAK4PFCorrectorPPOnAA' )
)
process.hltCsPFJetsCorrectedMatchedToPuCaloJets60 = cms.EDProducer( "PFJetsMatchedToFilteredCaloJetsProducer",
    DeltaR = cms.double( 0.2 ),
    CaloJetFilter = cms.InputTag( "hltSinglePuAK4CaloJet60Eta1p5" ),
    TriggerType = cms.int32( 85 ),
    PFJetSrc = cms.InputTag( "hltCsAK4PFJetsCorrectedPPOnAA" )
)
process.hltSingleCsPFJet60Eta1p5 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCsPFJetsCorrectedMatchedToPuCaloJets60" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 60.0 )
)
process.hltPreHICsAK4PFJet80Eta1p5Centrality30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet70Eta1p5 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( False ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 70.0 )
)
process.hltCsPFJetsCorrectedMatchedToPuCaloJets70 = cms.EDProducer( "PFJetsMatchedToFilteredCaloJetsProducer",
    DeltaR = cms.double( 0.2 ),
    CaloJetFilter = cms.InputTag( "hltSinglePuAK4CaloJet70Eta1p5" ),
    TriggerType = cms.int32( 85 ),
    PFJetSrc = cms.InputTag( "hltCsAK4PFJetsCorrectedPPOnAA" )
)
process.hltSingleCsPFJet80Eta1p5 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCsPFJetsCorrectedMatchedToPuCaloJets70" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 80.0 )
)
process.hltPreHICsAK4PFJet100Eta1p5Centrality30100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet80Eta1p5 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( False ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 80.0 )
)
process.hltCsPFJetsCorrectedMatchedToPuCaloJets80 = cms.EDProducer( "PFJetsMatchedToFilteredCaloJetsProducer",
    DeltaR = cms.double( 0.2 ),
    CaloJetFilter = cms.InputTag( "hltSinglePuAK4CaloJet80Eta1p5" ),
    TriggerType = cms.int32( 85 ),
    PFJetSrc = cms.InputTag( "hltCsAK4PFJetsCorrectedPPOnAA" )
)
process.hltSingleCsPFJet100Eta1p5 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCsPFJetsCorrectedMatchedToPuCaloJets80" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 100.0 )
)
process.hltPreHICsAK4PFJet60Eta1p5Centrality50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHICsAK4PFJet80Eta1p5Centrality50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHICsAK4PFJet100Eta1p5Centrality50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHICsAK4PFJet60Eta1p5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHICsAK4PFJet80Eta1p5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHICsAK4PFJet100Eta1p5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHICsAK4PFJet120Eta1p5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet90Eta1p5 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( False ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 90.0 )
)
process.hltCsPFJetsCorrectedMatchedToPuCaloJets90 = cms.EDProducer( "PFJetsMatchedToFilteredCaloJetsProducer",
    DeltaR = cms.double( 0.2 ),
    CaloJetFilter = cms.InputTag( "hltSinglePuAK4CaloJet90Eta1p5" ),
    TriggerType = cms.int32( 85 ),
    PFJetSrc = cms.InputTag( "hltCsAK4PFJetsCorrectedPPOnAA" )
)
process.hltSingleCsPFJet120Eta1p5 = cms.EDFilter( "HLT1PFJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltCsPFJetsCorrectedMatchedToPuCaloJets90" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 ),
    MinPt = cms.double( 120.0 )
)
process.hltPreHIEle10Gsf = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEgammaClusterShapePPOnAA = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
process.hltEle10ClusterShapePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.04 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaClusterShapePPOnAA','sigmaIEtaIEta5x5' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.015 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG10EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle10HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.15 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle10ClusterShapePPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEgammaEcalPFClusterIsoPPOnAA = cms.EDProducer( "EgammaHLTEcalPFClusterIsolationProducer",
    effectiveAreas = cms.vdouble( 0.29, 0.21 ),
    doRhoCorrection = cms.bool( False ),
    etaStripBarrel = cms.double( 0.0 ),
    energyEndcap = cms.double( 0.0 ),
    rhoProducer = cms.InputTag( "" ),
    pfClusterProducer = cms.InputTag( "hltParticleFlowClusterECALPPOnAA" ),
    etaStripEndcap = cms.double( 0.0 ),
    drVetoBarrel = cms.double( 0.0 ),
    drMax = cms.double( 0.3 ),
    energyBarrel = cms.double( 0.0 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    drVetoEndcap = cms.double( 0.0 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle10EcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle10HoverEPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltRegionalTowerForEgamma = cms.EDProducer( "EgammaHLTCaloTowerProducer",
    L1NonIsoCand = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    EMin = cms.double( 0.8 ),
    EtMin = cms.double( 0.5 ),
    L1IsoCand = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    useTowersInCone = cms.double( 0.8 ),
    towerCollection = cms.InputTag( "hltTowerMakerForAll" )
)
process.hltParticleFlowRecHitHBHEForEgamma = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( "hltHbhereco" ),
        name = cms.string( "PFHBHERecHitCreator" ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.8 ),
            name = cms.string( "PFRecHitQTestThreshold" ),
            cuts = cms.VPSet( 
              cms.PSet(  depth = cms.vint32( 1, 2, 3, 4 ),
                threshold = cms.vdouble( 0.8, 0.8, 0.8, 0.8 ),
                detectorEnum = cms.int32( 1 )
              ),
              cms.PSet(  depth = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
                threshold = cms.vdouble( 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8 ),
                detectorEnum = cms.int32( 2 )
              )
            )
          ),
          cms.PSet(  flags = cms.vstring( 'Standard' ),
            cleaningThresholds = cms.vdouble( 0.0 ),
            name = cms.string( "PFRecHitQTestHCALChannel" ),
            maxSeverities = cms.vint32( 11 )
          )
        )
      )
    ),
    navigator = cms.PSet( 
      name = cms.string( "PFRecHitHCALNavigator" ),
      sigmaCut = cms.double( 4.0 ),
      timeResolutionCalc = cms.PSet( 
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 2.0 ),
        noiseTerm = cms.double( 8.64 ),
        constantTermLowE = cms.double( 6.0 ),
        noiseTermLowE = cms.double( 0.0 ),
        threshHighE = cms.double( 8.0 ),
        constantTerm = cms.double( 1.92 )
      )
    )
)
process.hltParticleFlowClusterHBHEForEgamma = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 50 ),
      minChi2Prob = cms.double( 0.0 ),
      allCellsPositionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          depths = cms.vint32( 1, 2, 3, 4 ),
          recHitEnergyNorm = cms.vdouble( 0.8, 0.8, 0.8, 0.8 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
          recHitEnergyNorm = cms.vdouble( 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8 )
        )
      ),
      maxNSigmaTime = cms.double( 10.0 ),
      showerSigma = cms.double( 10.0 ),
      timeSigmaEE = cms.double( 10.0 ),
      clusterTimeResFromSeed = cms.bool( False ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      timeResolutionCalcBarrel = cms.PSet( 
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 6.0 ),
        noiseTerm = cms.double( 21.86 ),
        constantTermLowE = cms.double( 4.24 ),
        noiseTermLowE = cms.double( 8.0 ),
        threshHighE = cms.double( 15.0 ),
        constantTerm = cms.double( 2.82 )
      ),
      timeResolutionCalcEndcap = cms.PSet( 
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 6.0 ),
        noiseTerm = cms.double( 21.86 ),
        constantTermLowE = cms.double( 4.24 ),
        noiseTermLowE = cms.double( 8.0 ),
        threshHighE = cms.double( 15.0 ),
        constantTerm = cms.double( 2.82 )
      ),
      timeSigmaEB = cms.double( 10.0 )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          depths = cms.vint32( 1, 2, 3, 4 ),
          gatheringThreshold = cms.vdouble( 0.8, 0.8, 0.8, 0.8 ),
          gatheringThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
          gatheringThreshold = cms.vdouble( 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8 ),
          gatheringThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( True )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          depths = cms.vint32( 1, 2, 3, 4 ),
          seedingThreshold = cms.vdouble( 1.0, 1.0, 1.0, 1.0 ),
          seedingThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
          seedingThreshold = cms.vdouble( 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1 ),
          seedingThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 4 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitHBHEForEgamma" )
)
process.hltParticleFlowClusterHCALForEgamma = cms.EDProducer( "PFMultiDepthClusterProducer",
    pfClusterBuilder = cms.PSet( 
      allCellsPositionCalc = cms.PSet( 
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      algoName = cms.string( "PFMultiDepthClusterizer" ),
      nSigmaPhi = cms.double( 2.0 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      nSigmaEta = cms.double( 2.0 )
    ),
    energyCorrector = cms.PSet(  ),
    positionReCalc = cms.PSet(  ),
    clustersSource = cms.InputTag( "hltParticleFlowClusterHBHEForEgamma" )
)
process.hltEgammaHcalPFClusterIsoPPOnAA = cms.EDProducer( "EgammaHLTHcalPFClusterIsolationProducer",
    effectiveAreas = cms.vdouble( 0.2, 0.25 ),
    useHF = cms.bool( False ),
    useEt = cms.bool( True ),
    etaStripBarrel = cms.double( 0.0 ),
    pfClusterProducerHFHAD = cms.InputTag( "" ),
    energyEndcap = cms.double( 0.0 ),
    rhoProducer = cms.InputTag( "" ),
    etaStripEndcap = cms.double( 0.0 ),
    drVetoBarrel = cms.double( 0.0 ),
    pfClusterProducerHCAL = cms.InputTag( "hltParticleFlowClusterHCALForEgamma" ),
    drMax = cms.double( 0.3 ),
    doRhoCorrection = cms.bool( False ),
    energyBarrel = cms.double( 0.0 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    drVetoEndcap = cms.double( 0.0 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    rhoMax = cms.double( 9.9999999E7 ),
    pfClusterProducerHFEM = cms.InputTag( "" ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle10HcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaHcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle10EcalIsoPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltSiStripClustersPPOnAAZeroSuppression = cms.EDProducer( "MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    Phase2TrackerCluster1DProducer = cms.string( "" ),
    measurementTracker = cms.string( "hltESPMeasurementTracker" ),
    pixelClusterProducer = cms.string( "hltSiPixelClustersPPOnAA" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    skipClusters = cms.InputTag( "" ),
    pixelCablingMapLabel = cms.string( "" ),
    stripClusterProducer = cms.string( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" )
)
process.hltPixelLayerPairsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix1+BPix4',
      'BPix2+BPix3',
      'BPix2+BPix4',
      'BPix3+BPix4',
      'FPix1_pos+FPix2_pos',
      'FPix1_pos+FPix3_pos',
      'FPix2_pos+FPix3_pos',
      'BPix1+FPix1_pos',
      'BPix1+FPix2_pos',
      'BPix1+FPix3_pos',
      'BPix2+FPix1_pos',
      'BPix2+FPix2_pos',
      'BPix2+FPix3_pos',
      'BPix3+FPix1_pos',
      'BPix3+FPix2_pos',
      'BPix3+FPix3_pos',
      'BPix4+FPix1_pos',
      'BPix4+FPix2_pos',
      'BPix4+FPix3_pos',
      'FPix1_neg+FPix2_neg',
      'FPix1_neg+FPix3_neg',
      'FPix2_neg+FPix3_neg',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_neg',
      'BPix1+FPix3_neg',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_neg',
      'BPix2+FPix3_neg',
      'BPix3+FPix1_neg',
      'BPix3+FPix2_neg',
      'BPix3+FPix3_neg',
      'BPix4+FPix1_neg',
      'BPix4+FPix2_neg',
      'BPix4+FPix3_neg' ),
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
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltPixelLayerTripletsPPOnAA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix1+BPix3+BPix4',
      'BPix1+BPix2+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg',
      'BPix1+BPix3+FPix1_pos',
      'BPix1+BPix2+FPix2_pos',
      'BPix1+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix2_neg',
      'BPix1+FPix2_neg+FPix3_neg',
      'BPix1+FPix1_neg+FPix3_neg',
      'BPix1+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_pos+FPix3_pos' ),
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
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltEgammaSuperClustersToPixelMatchPPOnAA = cms.EDProducer( "EgammaHLTFilteredSuperClusterProducer",
    cands = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    cuts = cms.VPSet( 
      cms.PSet(  endcapCut = cms.PSet( 
  useEt = cms.bool( False ),
  cutOverE = cms.double( 0.2 )
),
        var = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
        barrelCut = cms.PSet( 
          useEt = cms.bool( False ),
          cutOverE = cms.double( 0.2 )
        )
      )
    )
)
process.hltEleSeedsTrackingRegionsPPOnAA = cms.EDProducer( "TrackingRegionsFromSuperClustersEDProducer",
    RegionPSet = cms.PSet( 
      minBSDeltaZ = cms.double( 0.0 ),
      useZInVertex = cms.bool( True ),
      vertices = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "" ),
      useZInBeamspot = cms.bool( False ),
      ptMin = cms.double( 4.0 ),
      deltaEtaRegion = cms.double( 0.1 ),
      nrSigmaForBSDeltaZ = cms.double( 3.0 ),
      originHalfLength = cms.double( 0.5 ),
      measurementTrackerEvent = cms.InputTag( "" ),
      originRadius = cms.double( 0.2 ),
      precise = cms.bool( True ),
      superClusters = cms.VInputTag( 'hltEgammaSuperClustersToPixelMatchPPOnAA' ),
      whereToUseMeasTracker = cms.string( "kNever" ),
      deltaPhiRegion = cms.double( 0.4 ),
      defaultZ = cms.double( 0.0 )
    )
)
process.hltElePixelHitDoubletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltEleSeedsTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltPixelLayerPairsPPOnAA" )
)
process.hltElePixelSeedsDoubletsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltElePixelHitDoubletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltElePixelHitDoubletsForTripletsPPOnAA = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltEleSeedsTrackingRegionsPPOnAA" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltPixelLayerTripletsPPOnAA" )
)
process.hltElePixelHitTripletsPPOnAA = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.3 ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltElePixelHitDoubletsForTripletsPPOnAA" ),
    CAThetaCut = cms.double( 0.004 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 6.0 ),
      value1 = cms.double( 100.0 ),
      pt1 = cms.double( 0.8 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 8.0 )
    ),
    CAPhiCut = cms.double( 0.1 ),
    useBendingCorrection = cms.bool( True )
)
process.hltElePixelSeedsTripletsPPOnAA = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltElePixelHitTripletsPPOnAA" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltElePixelSeedsCombinedPPOnAA = cms.EDProducer( "SeedCombiner",
    seedCollections = cms.VInputTag( 'hltElePixelSeedsDoubletsPPOnAA','hltElePixelSeedsTripletsPPOnAA' )
)
process.hltEgammaElectronPixelSeedsPPOnAA = cms.EDProducer( "ElectronNHitSeedProducer",
    matcherConfig = cms.PSet( 
      detLayerGeom = cms.string( "hltESPGlobalDetLayerGeometry" ),
      navSchool = cms.string( "SimpleNavigationSchool" ),
      useRecoVertex = cms.bool( False ),
      minNrHits = cms.vuint32( 2, 3 ),
      matchingCuts = cms.VPSet( 
        cms.PSet(  dPhiMaxHighEt = cms.vdouble( 0.05 ),
          version = cms.int32( 2 ),
          dRZMaxHighEt = cms.vdouble( 9999.0 ),
          dRZMaxLowEtGrad = cms.vdouble( 0.0 ),
          dPhiMaxLowEtGrad = cms.vdouble( -0.002 ),
          dPhiMaxHighEtThres = cms.vdouble( 20.0 ),
          dRZMaxHighEtThres = cms.vdouble( 0.0 )
        ),
        cms.PSet(  etaBins = cms.vdouble(  ),
          dPhiMaxHighEt = cms.vdouble( 0.003 ),
          version = cms.int32( 2 ),
          dRZMaxHighEt = cms.vdouble( 0.05 ),
          dRZMaxLowEtGrad = cms.vdouble( -0.002 ),
          dPhiMaxLowEtGrad = cms.vdouble( 0.0 ),
          dPhiMaxHighEtThres = cms.vdouble( 0.0 ),
          dRZMaxHighEtThres = cms.vdouble( 30.0 )
        ),
        cms.PSet(  etaBins = cms.vdouble(  ),
          dPhiMaxHighEt = cms.vdouble( 0.003 ),
          version = cms.int32( 2 ),
          dRZMaxHighEt = cms.vdouble( 0.05 ),
          dRZMaxLowEtGrad = cms.vdouble( -0.002 ),
          dPhiMaxLowEtGrad = cms.vdouble( 0.0 ),
          dPhiMaxHighEtThres = cms.vdouble( 0.0 ),
          dRZMaxHighEtThres = cms.vdouble( 30.0 )
        )
      ),
      minNrHitsValidLayerBins = cms.vint32( 4 )
    ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    measTkEvt = cms.InputTag( "hltSiStripClustersPPOnAAZeroSuppression" ),
    vertices = cms.InputTag( "" ),
    superClusters = cms.VInputTag( 'hltEgammaSuperClustersToPixelMatchPPOnAA' ),
    initialSeeds = cms.InputTag( "hltElePixelSeedsCombinedPPOnAA" )
)
process.hltEgammaPixelMatchVarsPPOnAA = cms.EDProducer( "EgammaHLTPixelMatchVarProducer",
    productsToWrite = cms.int32( 0 ),
    dRZ2SParams = cms.PSet(  bins = cms.VPSet( 
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.00299, 2.99E-4, -4.13E-6, 0.00191 ),
    xMin = cms.double( 0.0 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 1.5 ),
    funcType = cms.string( "TF1:=pol3" )
  ),
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.248, -0.329, 0.148, -0.0222 ),
    xMin = cms.double( 1.5 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 3.0 ),
    funcType = cms.string( "TF1:=pol3" )
  )
) ),
    pixelSeedsProducer = cms.InputTag( "hltEgammaElectronPixelSeedsPPOnAA" ),
    dPhi2SParams = cms.PSet(  bins = cms.VPSet( 
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 1.3E-4 ),
    xMin = cms.double( 0.0 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 1.6 ),
    funcType = cms.string( "TF1:=pol0" )
  ),
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 4.5E-4, -1.99E-4 ),
    xMin = cms.double( 1.5 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 1.9 ),
    funcType = cms.string( "TF1:=pol1" )
  ),
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 7.94E-5 ),
    xMin = cms.double( 1.9 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 3.0 ),
    funcType = cms.string( "TF1:=pol0" )
  )
) ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    dPhi1SParams = cms.PSet(  bins = cms.VPSet( 
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.00112, 7.52E-4, -0.00122, 0.00109 ),
    xMin = cms.double( 0.0 ),
    yMax = cms.int32( 1 ),
    xMax = cms.double( 1.5 ),
    funcType = cms.string( "TF1:=pol3" )
  ),
  cms.PSet(  yMin = cms.int32( 2 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.00222, 1.96E-4, -2.03E-4, 4.47E-4 ),
    xMin = cms.double( 0.0 ),
    yMax = cms.int32( 2 ),
    xMax = cms.double( 1.5 ),
    funcType = cms.string( "TF1:=pol3" )
  ),
  cms.PSet(  yMin = cms.int32( 3 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.00236, 6.91E-4, 1.99E-4, 4.16E-4 ),
    xMin = cms.double( 0.0 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 1.5 ),
    funcType = cms.string( "TF1:=pol3" )
  ),
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.00823, -0.0029 ),
    xMin = cms.double( 1.5 ),
    yMax = cms.int32( 1 ),
    xMax = cms.double( 2.0 ),
    funcType = cms.string( "TF1:=pol1" )
  ),
  cms.PSet(  yMin = cms.int32( 1 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.00282 ),
    xMin = cms.double( 2.0 ),
    yMax = cms.int32( 1 ),
    xMax = cms.double( 3.0 ),
    funcType = cms.string( "TF1:=pol0" )
  ),
  cms.PSet(  yMin = cms.int32( 2 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.010838, -0.00345 ),
    xMin = cms.double( 1.5 ),
    yMax = cms.int32( 2 ),
    xMax = cms.double( 2.0 ),
    funcType = cms.string( "TF1:=pol1" )
  ),
  cms.PSet(  yMin = cms.int32( 2 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.0043 ),
    xMin = cms.double( 2.0 ),
    yMax = cms.int32( 2 ),
    xMax = cms.double( 3.0 ),
    funcType = cms.string( "TF1:=pol0" )
  ),
  cms.PSet(  yMin = cms.int32( 3 ),
    binType = cms.string( "AbsEtaClus" ),
    funcParams = cms.vdouble( 0.0208, -0.0125, 0.00231 ),
    xMin = cms.double( 1.5 ),
    yMax = cms.int32( 99999 ),
    xMax = cms.double( 3.0 ),
    funcType = cms.string( "TF1:=pol2" )
  )
) )
)
process.hltEle10PixelMatchPPOnAAFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    s_a_rF = cms.double( 0.04 ),
    saveTags = cms.bool( True ),
    s_a_phi1B = cms.double( 0.0069 ),
    l1PixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeedsPPOnAA" ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    pixelVeto = cms.bool( False ),
    s2_threshold = cms.double( 0.4 ),
    s_a_rI = cms.double( 0.027 ),
    npixelmatchcut = cms.double( 1.0 ),
    tanhSO10InterThres = cms.double( 1.0 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    useS = cms.bool( False ),
    candTag = cms.InputTag( "hltEle10HcalIsoPPOnAAFilter" ),
    ncandcut = cms.int32( 1 ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    tanhSO10BarrelThres = cms.double( 0.35 ),
    s_a_zB = cms.double( 0.012 ),
    tanhSO10ForwardThres = cms.double( 1.0 ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_phi2I = cms.double( 7.0E-4 )
)
process.hltEgammaCkfTrackCandidatesForGSFPPOnAA = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltEgammaElectronPixelSeedsPPOnAA" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersPPOnAAZeroSuppression" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 1000000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryBuilderForGsfElectrons" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltEgammaGsfTracksPPOnAA = cms.EDProducer( "GsfTrackProducer",
    src = cms.InputTag( "hltEgammaCkfTrackCandidatesForGSFPPOnAA" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    producer = cms.string( "" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersPPOnAAZeroSuppression" ),
    Fitter = cms.string( "hltESPGsfElectronFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "hltESPMeasurementTracker" ),
    GeometricInnerState = cms.bool( True ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "gsf" ),
    Propagator = cms.string( "hltESPFwdElectronPropagator" )
)
process.hltEgammaGsfElectronsPPOnAA = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    UseGsfTracks = cms.bool( True ),
    TrackProducer = cms.InputTag( "" ),
    GsfTrackProducer = cms.InputTag( "hltEgammaGsfTracksPPOnAA" )
)
process.hltEgammaGsfTrackVarsPPOnAA = cms.EDProducer( "EgammaHLTGsfTrackVarProducer",
    upperTrackNrToRemoveCut = cms.int32( 9999 ),
    useDefaultValuesForEndcap = cms.bool( False ),
    lowerTrackNrToRemoveCut = cms.int32( -1 ),
    inputCollection = cms.InputTag( "hltEgammaGsfTracksPPOnAA" ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    beamSpotProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    useDefaultValuesForBarrel = cms.bool( False )
)
process.hltEle10GsfOneOEMinusOneOPPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.1 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','OneOESuperMinusOneOP' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.1 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle10PixelMatchPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle10GsfDetaPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.012 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','DetaSeed' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.008 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle10GsfOneOEMinusOneOPPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle10GsfDphiPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.1 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','Dphi' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.1 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle10GsfDetaPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltIter0ElectronsPixelSeedsFromPixelTracks = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 0.3 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( True ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) ),
    InputVertexCollection = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    InputCollection = cms.InputTag( "hltPixelTracksPPOnAA" ),
    originRadius = cms.double( 0.1 )
)
process.hltIter0ElectronsCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter0ElectronsPixelSeedsFromPixelTracks" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersPPOnAAZeroSuppression" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltIter0ElectronsCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter0ElectronsCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersPPOnAAZeroSuppression" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter0" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltIter0ElectronsTrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.4, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.35, 4.0 ),
    copyTrajectories = cms.untracked.bool( False ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter0ElectronsCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.4, 4.0 ),
    d0_par1 = cms.vdouble( 0.3, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltIter1ElectronsClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltIter0ElectronsTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltIter1ElectronsMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter1ElectronsClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersPPOnAAZeroSuppression" )
)
process.hltIter1ElectronsPixelLayerQuadruplets = cms.EDProducer( "SeedingLayersEDProducer",
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
      skipClusters = cms.InputTag( "hltIter1ElectronsClustersRefRemoval" ),
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
      skipClusters = cms.InputTag( "hltIter1ElectronsClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltIter1ElectronsPixelTrackingRegions = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 0.2 ),
      sigmaZVertex = cms.double( 3.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 4.0 ),
      originRadius = cms.double( 0.05 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
)
process.hltIter1ElectronsPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIter1ElectronsPixelTrackingRegions" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIter1ElectronsPixelLayerQuadruplets" )
)
process.hltIter1ElectronsPixelHitQuadruplets = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.004 ),
    SeedComparitorPSet = cms.PSet( 
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "none" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCachePPOnAA" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltIter1ElectronsPixelHitDoublets" ),
    fitFastCircle = cms.bool( True ),
    CAHardPtCut = cms.double( 0.0 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 100.0 ),
      value1 = cms.double( 1000.0 ),
      pt1 = cms.double( 0.4 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.3 ),
    useBendingCorrection = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True )
)
process.hltIter1ElectronsPixelTracks = cms.EDProducer( "PixelTrackProducer",
    Filter = cms.InputTag( "hltPixelTracksFilter" ),
    Cleaner = cms.string( "hltPixelTracksCleanerBySharedHits" ),
    passLabel = cms.string( "" ),
    Fitter = cms.InputTag( "hltPixelTracksFitter" ),
    SeedingHitSets = cms.InputTag( "hltIter1ElectronsPixelHitQuadruplets" )
)
process.hltIter1ElectronsPixelSeedsFromPixelTracks = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 0.3 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( True ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) ),
    InputVertexCollection = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    InputCollection = cms.InputTag( "hltIter1ElectronsPixelTracks" ),
    originRadius = cms.double( 0.1 )
)
process.hltIter1ElectronsCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter1ElectronsPixelSeedsFromPixelTracks" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1ElectronsMaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltIter1ElectronsCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter1ElectronsCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1ElectronsMaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter1" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltIter1ElectronsTrackSelectionHighPurityLoose = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.9, 3.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.8, 3.0 ),
    copyTrajectories = cms.untracked.bool( False ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter1ElectronsCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.9, 3.0 ),
    d0_par1 = cms.vdouble( 0.85, 3.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltIter1ElectronsTrackSelectionHighPurityTight = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 5 ),
    chi2n_par = cms.double( 0.4 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 1.0, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 1.0, 4.0 ),
    copyTrajectories = cms.untracked.bool( False ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter1ElectronsCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 1.0, 4.0 ),
    d0_par1 = cms.vdouble( 1.0, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltIter1ElectronsTrackSelectionHighPurity = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter1ElectronsTrackSelectionHighPurityLoose','hltIter1ElectronsTrackSelectionHighPurityTight' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter1ElectronsTrackSelectionHighPurityLoose','hltIter1ElectronsTrackSelectionHighPurityTight' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltIter1ForElectronsMerged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter0ElectronsTrackSelectionHighPurity','hltIter1ElectronsTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter0ElectronsTrackSelectionHighPurity','hltIter1ElectronsTrackSelectionHighPurity' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltIter2ElectronsClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter1ElectronsTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter1ElectronsClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltIter2ElectronsMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter2ElectronsClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersPPOnAAZeroSuppression" )
)
process.hltIter2ElectronsPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix1+BPix3+BPix4',
      'BPix1+BPix2+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg',
      'BPix1+BPix3+FPix1_pos',
      'BPix1+BPix2+FPix2_pos',
      'BPix1+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix2_neg',
      'BPix1+FPix2_neg+FPix3_neg',
      'BPix1+FPix1_neg+FPix3_neg',
      'BPix1+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_pos+FPix3_pos' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2ElectronsClustersRefRemoval" ),
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
      skipClusters = cms.InputTag( "hltIter2ElectronsClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    TIB = cms.PSet(  )
)
process.hltIter2ElectronsPixelTrackingRegions = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet( 
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 0.2 ),
      sigmaZVertex = cms.double( 3.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 4.0 ),
      originRadius = cms.double( 0.05 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
)
process.hltIter2ElectronsPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIter2ElectronsPixelTrackingRegions" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIter2ElectronsPixelLayerTriplets" )
)
process.hltIter2ElectronsPixelHitTriplets = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.3 ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltIter2ElectronsPixelHitDoublets" ),
    CAThetaCut = cms.double( 0.004 ),
    maxChi2 = cms.PSet( 
      value2 = cms.double( 6.0 ),
      value1 = cms.double( 100.0 ),
      pt1 = cms.double( 0.4 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 8.0 )
    ),
    CAPhiCut = cms.double( 0.1 ),
    useBendingCorrection = cms.bool( True )
)
process.hltIter2ElectronsPixelSeeds = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltIter2ElectronsPixelHitTriplets" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltIter2ElectronsCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter2ElectronsPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2ElectronsMaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltIter2ElectronsCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter2ElectronsCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2ElectronsMaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter2" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltIter2ElectronsTrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.4, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.35, 4.0 ),
    copyTrajectories = cms.untracked.bool( False ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter2ElectronsCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.4, 4.0 ),
    d0_par1 = cms.vdouble( 0.3, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltIter2ForElectronsMerged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter1ForElectronsMerged','hltIter2ElectronsTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter1ForElectronsMerged','hltIter2ElectronsTrackSelectionHighPurity' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltDoubletRecoveryForElectronsClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter2ElectronsTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter2ElectronsClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltHITrackingSiStripRawToClustersFacilityZeroSuppression" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersPPOnAA" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltDoubletRecoveryForElectronsMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltDoubletRecoveryForElectronsClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersPPOnAAZeroSuppression" )
)
process.hltDoubletRecoveryForElectronsPixelLayersAndRegions = cms.EDProducer( "PixelInactiveAreaTrackingRegionsSeedingLayersProducer",
    inactivePixelDetectorLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix1+BPix4',
      'BPix2+BPix3',
      'BPix2+BPix4',
      'BPix3+BPix4',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix1+FPix3_pos',
      'BPix1+FPix3_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'BPix3+FPix1_pos',
      'BPix3+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix3_pos',
      'FPix1_neg+FPix3_neg',
      'FPix2_pos+FPix3_pos',
      'FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    RegionPSet = cms.PSet( 
      precise = cms.bool( True ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 15.0 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      measurementTrackerName = cms.InputTag( "hltDoubletRecoveryForElectronsMaskedMeasurementTrackerEvent" ),
      extraEta = cms.double( 0.0 ),
      vertexCollection = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
      ptMin = cms.double( 4.0 ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
      maxNVertices = cms.int32( 3 ),
      extraPhi = cms.double( 0.0 ),
      originRadius = cms.double( 0.015 ),
      zErrorVertex = cms.double( 0.03 ),
      operationMode = cms.string( "VerticesFixed" )
    ),
    TEC = cms.PSet(  ),
    ignoreSingleFPixPanelModules = cms.bool( True ),
    TID = cms.PSet(  ),
    BPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltDoubletRecoveryForElectronsClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltDoubletRecoveryForElectronsClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHitsPPOnAA" )
    ),
    MTEC = cms.PSet(  ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    debug = cms.untracked.bool( False ),
    TOB = cms.PSet(  ),
    createPlottingFiles = cms.untracked.bool( False ),
    TIB = cms.PSet(  )
)
process.hltDoubletRecoveryForElectronsPFlowPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( False ),
    trackingRegionsSeedingLayers = cms.InputTag( "hltDoubletRecoveryForElectronsPixelLayersAndRegions" ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "" )
)
process.hltDoubletRecoveryForElectronsPFlowPixelSeeds = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltDoubletRecoveryForElectronsPFlowPixelHitDoublets" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
process.hltDoubletRecoveryForElectronsPFlowCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltDoubletRecoveryForElectronsPFlowPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryForElectronsMaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2GroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltDoubletRecoveryForElectronsPFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltDoubletRecoveryForElectronsPFlowCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryForElectronsMaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltDoubletRecovery" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltDoubletRecoveryForElectronsPFlowTrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.4, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.35, 4.0 ),
    copyTrajectories = cms.untracked.bool( False ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltDoubletRecoveryForElectronsPFlowCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltTrimmedPixelVerticesPPOnAA" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.4, 4.0 ),
    d0_par1 = cms.vdouble( 0.3, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltMergedForElectrons = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter2ForElectronsMerged','hltDoubletRecoveryForElectronsPFlowTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet( 
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter2ForElectronsMerged','hltDoubletRecoveryForElectronsPFlowTrackSelectionHighPurity' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
process.hltEgammaEleGsfTrackIsoPPOnAA = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    egTrkIsoStripEndcap = cms.double( 0.01 ),
    egTrkIsoVetoConeSizeBarrel = cms.double( 0.03 ),
    useGsfTrack = cms.bool( True ),
    useSCRefs = cms.bool( True ),
    trackProducer = cms.InputTag( "hltMergedForElectrons" ),
    egTrkIsoStripBarrel = cms.double( 0.01 ),
    electronProducer = cms.InputTag( "hltEgammaGsfElectronsPPOnAA" ),
    egTrkIsoConeSize = cms.double( 0.2 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSizeEndcap = cms.double( 0.03 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    beamSpotProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoZSpan = cms.double( 0.15 )
)
process.hltEle10GsfTrackIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEleGsfTrackIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle10GsfDphiPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIEle15Gsf = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEle15ClusterShapePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.04 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaClusterShapePPOnAA','sigmaIEtaIEta5x5' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.015 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG15EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle15HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.15 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle15ClusterShapePPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle15EcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle15HoverEPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle15HcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaHcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle15EcalIsoPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle15PixelMatchPPOnAAFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    s_a_rF = cms.double( 0.04 ),
    saveTags = cms.bool( True ),
    s_a_phi1B = cms.double( 0.0069 ),
    l1PixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeedsPPOnAA" ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    pixelVeto = cms.bool( False ),
    s2_threshold = cms.double( 0.4 ),
    s_a_rI = cms.double( 0.027 ),
    npixelmatchcut = cms.double( 1.0 ),
    tanhSO10InterThres = cms.double( 1.0 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    useS = cms.bool( False ),
    candTag = cms.InputTag( "hltEle15HcalIsoPPOnAAFilter" ),
    ncandcut = cms.int32( 1 ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    tanhSO10BarrelThres = cms.double( 0.35 ),
    s_a_zB = cms.double( 0.012 ),
    tanhSO10ForwardThres = cms.double( 1.0 ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_phi2I = cms.double( 7.0E-4 )
)
process.hltEle15GsfOneOEMinusOneOPPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.1 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','OneOESuperMinusOneOP' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.1 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle15PixelMatchPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle15GsfDetaPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.012 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','DetaSeed' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.008 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle15GsfOneOEMinusOneOPPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle15GsfDphiPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.1 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','Dphi' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.1 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle15GsfDetaPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle15GsfTrackIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEleGsfTrackIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle15GsfDphiPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIEle20Gsf = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEle20ClusterShapePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.04 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaClusterShapePPOnAA','sigmaIEtaIEta5x5' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.015 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG20EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle20HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.15 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle20ClusterShapePPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle20EcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle20HoverEPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle20HcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaHcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle20EcalIsoPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle20PixelMatchPPOnAAFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    s_a_rF = cms.double( 0.04 ),
    saveTags = cms.bool( True ),
    s_a_phi1B = cms.double( 0.0069 ),
    l1PixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeedsPPOnAA" ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    pixelVeto = cms.bool( False ),
    s2_threshold = cms.double( 0.4 ),
    s_a_rI = cms.double( 0.027 ),
    npixelmatchcut = cms.double( 1.0 ),
    tanhSO10InterThres = cms.double( 1.0 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    useS = cms.bool( False ),
    candTag = cms.InputTag( "hltEle20HcalIsoPPOnAAFilter" ),
    ncandcut = cms.int32( 1 ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    tanhSO10BarrelThres = cms.double( 0.35 ),
    s_a_zB = cms.double( 0.012 ),
    tanhSO10ForwardThres = cms.double( 1.0 ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_phi2I = cms.double( 7.0E-4 )
)
process.hltEle20GsfOneOEMinusOneOPPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.1 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','OneOESuperMinusOneOP' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.1 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle20PixelMatchPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle20GsfDetaPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.012 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','DetaSeed' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.008 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle20GsfOneOEMinusOneOPPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle20GsfDphiPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.1 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','Dphi' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.1 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle20GsfDetaPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle20GsfTrackIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEleGsfTrackIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle20GsfDphiPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIEle30Gsf = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEle30ClusterShapePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.04 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaClusterShapePPOnAA','sigmaIEtaIEta5x5' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.015 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG30EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle30HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.15 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle30ClusterShapePPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle30EcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle30HoverEPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle30HcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaHcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle30EcalIsoPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle30PixelMatchPPOnAAFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    s_a_rF = cms.double( 0.04 ),
    saveTags = cms.bool( True ),
    s_a_phi1B = cms.double( 0.0069 ),
    l1PixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeedsPPOnAA" ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    pixelVeto = cms.bool( False ),
    s2_threshold = cms.double( 0.4 ),
    s_a_rI = cms.double( 0.027 ),
    npixelmatchcut = cms.double( 1.0 ),
    tanhSO10InterThres = cms.double( 1.0 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    useS = cms.bool( False ),
    candTag = cms.InputTag( "hltEle30HcalIsoPPOnAAFilter" ),
    ncandcut = cms.int32( 1 ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    tanhSO10BarrelThres = cms.double( 0.35 ),
    s_a_zB = cms.double( 0.012 ),
    tanhSO10ForwardThres = cms.double( 1.0 ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_phi2I = cms.double( 7.0E-4 )
)
process.hltEle30GsfOneOEMinusOneOPPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.1 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','OneOESuperMinusOneOP' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.1 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle30PixelMatchPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle30GsfDetaPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.012 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','DetaSeed' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.008 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle30GsfOneOEMinusOneOPPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle30GsfDphiPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.1 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','Dphi' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.1 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle30GsfDetaPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle30GsfTrackIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEleGsfTrackIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle30GsfDphiPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIEle40Gsf = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEle40ClusterShapePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.04 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaClusterShapePPOnAA','sigmaIEtaIEta5x5' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.015 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG40EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle40HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.15 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle40ClusterShapePPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle40EcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle40HoverEPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle40HcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaHcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle40EcalIsoPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle40PixelMatchPPOnAAFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    s_a_rF = cms.double( 0.04 ),
    saveTags = cms.bool( True ),
    s_a_phi1B = cms.double( 0.0069 ),
    l1PixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeedsPPOnAA" ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    pixelVeto = cms.bool( False ),
    s2_threshold = cms.double( 0.4 ),
    s_a_rI = cms.double( 0.027 ),
    npixelmatchcut = cms.double( 1.0 ),
    tanhSO10InterThres = cms.double( 1.0 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    useS = cms.bool( False ),
    candTag = cms.InputTag( "hltEle40HcalIsoPPOnAAFilter" ),
    ncandcut = cms.int32( 1 ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    tanhSO10BarrelThres = cms.double( 0.35 ),
    s_a_zB = cms.double( 0.012 ),
    tanhSO10ForwardThres = cms.double( 1.0 ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_phi2I = cms.double( 7.0E-4 )
)
process.hltEle40GsfOneOEMinusOneOPPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.1 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','OneOESuperMinusOneOP' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.1 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle40PixelMatchPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle40GsfDetaPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.012 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','DetaSeed' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.008 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle40GsfOneOEMinusOneOPPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle40GsfDphiPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.1 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','Dphi' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.1 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle40GsfDetaPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle40GsfTrackIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEleGsfTrackIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle40GsfDphiPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIEle50Gsf = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEle50ClusterShapePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.04 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaClusterShapePPOnAA','sigmaIEtaIEta5x5' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.015 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEG50EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle50HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.15 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle50ClusterShapePPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle50EcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle50HoverEPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle50HcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaHcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle50EcalIsoPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle50PixelMatchPPOnAAFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    s_a_rF = cms.double( 0.04 ),
    saveTags = cms.bool( True ),
    s_a_phi1B = cms.double( 0.0069 ),
    l1PixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeedsPPOnAA" ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    pixelVeto = cms.bool( False ),
    s2_threshold = cms.double( 0.4 ),
    s_a_rI = cms.double( 0.027 ),
    npixelmatchcut = cms.double( 1.0 ),
    tanhSO10InterThres = cms.double( 1.0 ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    useS = cms.bool( False ),
    candTag = cms.InputTag( "hltEle50HcalIsoPPOnAAFilter" ),
    ncandcut = cms.int32( 1 ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    tanhSO10BarrelThres = cms.double( 0.35 ),
    s_a_zB = cms.double( 0.012 ),
    tanhSO10ForwardThres = cms.double( 1.0 ),
    s_a_phi2F = cms.double( 0.00906 ),
    s_a_phi2I = cms.double( 7.0E-4 )
)
process.hltEle50GsfOneOEMinusOneOPPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.1 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','OneOESuperMinusOneOP' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.1 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle50PixelMatchPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle50GsfDetaPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.012 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','DetaSeed' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.008 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle50GsfOneOEMinusOneOPPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle50GsfDphiPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.1 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaGsfTrackVarsPPOnAA','Dphi' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.1 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle50GsfDetaPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle50GsfTrackIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEleGsfTrackIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 1 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltEle50GsfDphiPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIEle15Ele10Gsf = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltDoubleEG10EtPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 10.0 ),
    etcutEB = cms.double( 10.0 ),
    ncandcut = cms.int32( 2 )
)
process.hltDoubleEle10ClusterShapePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.04 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaClusterShapePPOnAA','sigmaIEtaIEta5x5' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.015 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 2 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltDoubleEG10EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltDoubleEle10HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.15 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 2 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltDoubleEle10ClusterShapePPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltDoubleEle10EcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 2 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltDoubleEle10HoverEPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltDoubleEle10HcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaHcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 2 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltDoubleEle10EcalIsoPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltDoubleEle10GsfTrackIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEleGsfTrackIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 2 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltDoubleEle10HcalIsoPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIEle15Ele10GsfMass50 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltDoubleEle10Mass50PPOnAAFilter = cms.EDFilter( "HLTEgammaCombMassFilter",
    saveTags = cms.bool( True ),
    firstLegLastFilter = cms.InputTag( "hltDoubleEle10GsfTrackIsoPPOnAAFilter" ),
    minMass = cms.double( 50.0 ),
    secondLegLastFilter = cms.InputTag( "hltDoubleEle10GsfTrackIsoPPOnAAFilter" )
)
process.hltPreHIDoubleEle10Gsf = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIDoubleEle10GsfMass50 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIDoubleEle15Gsf = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltDoubleEG15EtPPOnAAFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperPPOnAA" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    etcutEE = cms.double( 15.0 ),
    etcutEB = cms.double( 15.0 ),
    ncandcut = cms.int32( 2 )
)
process.hltDoubleEle15ClusterShapePPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( 0.04 ),
    thrOverEEE = cms.vdouble( -1.0 ),
    varTag = cms.InputTag( 'hltEgammaClusterShapePPOnAA','sigmaIEtaIEta5x5' ),
    thrOverEEB = cms.vdouble( -1.0 ),
    thrRegularEB = cms.vdouble( 0.015 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 2 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltDoubleEG15EtPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltDoubleEle15HoverEPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 0.15 ),
    varTag = cms.InputTag( "hltEgammaHoverEPPOnAA" ),
    thrOverEEB = cms.vdouble( 0.2 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 2 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltDoubleEle15ClusterShapePPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltDoubleEle15EcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 2 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltDoubleEle15HoverEPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltDoubleEle15HcalIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaHcalPFClusterIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 2 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltDoubleEle15EcalIsoPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltDoubleEle15GsfTrackIsoPPOnAAFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    thrOverE2EE = cms.vdouble( -1.0 ),
    effectiveAreas = cms.vdouble( 0.0, 0.0 ),
    energyLowEdges = cms.vdouble( 0.0 ),
    doRhoCorrection = cms.bool( False ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.vdouble( -1.0 ),
    thrRegularEE = cms.vdouble( -1.0 ),
    thrOverEEE = cms.vdouble( 1.0 ),
    varTag = cms.InputTag( "hltEgammaEleGsfTrackIsoPPOnAA" ),
    thrOverEEB = cms.vdouble( 1.0 ),
    thrRegularEB = cms.vdouble( -1.0 ),
    lessThan = cms.bool( True ),
    l1EGCand = cms.InputTag( "hltEgammaCandidatesPPOnAA" ),
    ncandcut = cms.int32( 2 ),
    absEtaLowEdges = cms.vdouble( 0.0, 1.479 ),
    candTag = cms.InputTag( "hltDoubleEle15HcalIsoPPOnAAFilter" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( True ),
    rhoScale = cms.double( 1.0 )
)
process.hltPreHIDoubleEle15GsfMass50 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltDoubleEle15Mass50PPOnAAFilter = cms.EDFilter( "HLTEgammaCombMassFilter",
    saveTags = cms.bool( True ),
    firstLegLastFilter = cms.InputTag( "hltDoubleEle15GsfTrackIsoPPOnAAFilter" ),
    minMass = cms.double( 50.0 ),
    secondLegLastFilter = cms.InputTag( "hltDoubleEle15GsfTrackIsoPPOnAAFilter" )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtStage2Digis + process.hltGtStage2ObjectMap )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTDoFullUnpackingEgammaEcalSequence = cms.Sequence( process.hltEcalDigis + process.hltEcalPreshowerDigis + process.hltEcalUncalibRecHit + process.hltEcalDetIdToBeRecovered + process.hltEcalRecHit + process.hltEcalPreshowerRecHit )
process.HLTPFClusteringForEgammaPPOnAA = cms.Sequence( process.hltParticleFlowRecHitECALPPOnAA + process.hltParticleFlowRecHitPSPPOnAA + process.hltParticleFlowClusterPSPPOnAA + process.hltParticleFlowClusterECALUncorrectedPPOnAA + process.hltParticleFlowClusterECALPPOnAA + process.hltParticleFlowSuperClusterECALPPOnAA )
process.HLTDoLocalHcalWithTowerSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhePhase1Reco + process.hltHbhereco + process.hltHfprereco + process.hltHfreco + process.hltHoreco + process.hltTowerMakerForAll )
process.HLTHIGEDPhoton10PPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG10EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG10HoverELoosePPOnAAFilter )
process.HLTDoHIStripZeroSuppression = cms.Sequence( process.hltSiStripRawToDigi + process.hltSiStripZeroSuppression + process.hltSiStripDigiToZSRaw + process.hltSiStripRawDigiToVirginRaw + process.virginRawDataRepacker + process.rawDataRepacker + process.rawDataReducedFormat )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )
process.HLTEndSequenceWithZeroSuppression = cms.Sequence( process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLTHIGEDPhoton15PPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG15EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG15HoverELoosePPOnAAFilter )
process.HLTHIGEDPhoton20PPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG20EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG20HoverELoosePPOnAAFilter )
process.HLTHIGEDPhoton30PPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG30EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG30HoverELoosePPOnAAFilter )
process.HLTHIGEDPhoton40PPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG40EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG40HoverELoosePPOnAAFilter )
process.HLTHIGEDPhoton50PPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG50EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG50HoverELoosePPOnAAFilter )
process.HLTHIGEDPhoton60PPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG60EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG60HoverELoosePPOnAAFilter )
process.HLTHIGEDPhoton10EBPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG10EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG10HoverELooseEBPPOnAAFilter )
process.HLTHIGEDPhoton15EBPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG15EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG15HoverELooseEBPPOnAAFilter )
process.HLTHIGEDPhoton20EBPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG20EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG20HoverELooseEBPPOnAAFilter )
process.HLTHIGEDPhoton30EBPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG30EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG30HoverELooseEBPPOnAAFilter )
process.HLTHIGEDPhoton40EBPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG40EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG40HoverELooseEBPPOnAAFilter )
process.HLTHIGEDPhoton50EBPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG50EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG50HoverELooseEBPPOnAAFilter )
process.HLTHIGEDPhoton60EBPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG60EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG60HoverELooseEBPPOnAAFilter )
process.HLTHIGEDPhoton10HECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG10EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG10HoverEPPOnAAFilter )
process.HLTHIGEDPhoton15HECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG15EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG15HoverEPPOnAAFilter )
process.HLTHIGEDPhoton20HECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG20EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG20HoverEPPOnAAFilter )
process.HLTHIGEDPhoton30HECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG30EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG30HoverEPPOnAAFilter )
process.HLTHIGEDPhoton40HECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG40EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG40HoverEPPOnAAFilter )
process.HLTHIGEDPhoton50HECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG50EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG50HoverEPPOnAAFilter )
process.HLTHIGEDPhoton60HECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG60EtPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG60HoverEPPOnAAFilter )
process.HLTHIGEDPhoton10EBHECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG10EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG10HoverEEBPPOnAAFilter )
process.HLTHIGEDPhoton15EBHECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG15EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG15HoverEEBPPOnAAFilter )
process.HLTHIGEDPhoton20EBHECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG20EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG20HoverEEBPPOnAAFilter )
process.HLTHIGEDPhoton30EBHECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG30EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG30HoverEEBPPOnAAFilter )
process.HLTHIGEDPhoton40EBHECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG40EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG40HoverEEBPPOnAAFilter )
process.HLTHIGEDPhoton50EBHECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG50EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG50HoverEEBPPOnAAFilter )
process.HLTHIGEDPhoton60EBHECutPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG60EtEBPPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEG60HoverEEBPPOnAAFilter )
process.HLTPFClusteringForEgamma = cms.Sequence( process.hltRechitInRegionsECAL + process.hltRechitInRegionsES + process.hltParticleFlowRecHitECALL1Seeded + process.hltParticleFlowRecHitPSL1Seeded + process.hltParticleFlowClusterPSL1Seeded + process.hltParticleFlowClusterECALUncorrectedL1Seeded + process.hltParticleFlowClusterECALL1Seeded + process.hltParticleFlowSuperClusterECALL1Seeded )
process.HLTDoLocalHcalSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhePhase1Reco + process.hltHbhereco + process.hltHfprereco + process.hltHfreco + process.hltHoreco )
process.HLTFastJetForEgamma = cms.Sequence( process.hltTowerMakerForAll + process.hltFixedGridRhoFastjetAllCaloForMuons )
process.HLTHIGEDPhoton10L1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG3BptxANDFilter + process.hltEG10EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG10HEFilter )
process.HLTHIGEDPhoton15L1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG3BptxANDFilter + process.hltEG15EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG15HEFilter )
process.HLTHIGEDPhoton20L1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG3BptxANDFilter + process.hltEG20EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG20HEFilter )
process.HLTHIGEDPhoton30L1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG7BptxANDFilter + process.hltEG30EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG30HEFilter )
process.HLTHIGEDPhoton40L1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG21BptxANDFilter + process.hltEG40EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG40HEFilter )
process.HLTHIGEDPhoton50L1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG21BptxANDFilter + process.hltEG50EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG50HEFilter )
process.HLTHIGEDPhoton60L1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG30BptxANDFilter + process.hltEG60EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG60HEFilter )
process.HLTHIGEDPhoton10EBL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG3BptxANDFilter + process.hltEG10EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG10EBHEFilter )
process.HLTHIGEDPhoton15EBL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG3BptxANDFilter + process.hltEG15EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG15EBHEFilter )
process.HLTHIGEDPhoton20EBL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG3BptxANDFilter + process.hltEG20EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG20EBHEFilter )
process.HLTHIGEDPhoton30EBL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG7BptxANDFilter + process.hltEG30EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG30EBHEFilter )
process.HLTHIGEDPhoton40EBL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG21BptxANDFilter + process.hltEG40EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG40EBHEFilter )
process.HLTHIGEDPhoton50EBL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG21BptxANDFilter + process.hltEG50EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG50EBHEFilter )
process.HLTHIGEDPhoton60EBL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG30BptxANDFilter + process.hltEG60EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG60EBHEFilter )
process.HLTHIGEDPhoton10HECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG3BptxANDFilter + process.hltEG10EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG10HEFilterHECut )
process.HLTHIGEDPhoton15HECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG3BptxANDFilter + process.hltEG15EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG15HEFilterHECut )
process.HLTHIGEDPhoton20HECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG3BptxANDFilter + process.hltEG20EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG20HEFilterHECut )
process.HLTHIGEDPhoton30HECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG7BptxANDFilter + process.hltEG30EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG30HEFilterHECut )
process.HLTHIGEDPhoton40HECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG21BptxANDFilter + process.hltEG40EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG40HEFilterHECut )
process.HLTHIGEDPhoton50HECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG21BptxANDFilter + process.hltEG50EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG50HEFilterHECut )
process.HLTHIGEDPhoton60HECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG30BptxANDFilter + process.hltEG60EtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG60HEFilterHECut )
process.HLTHIGEDPhoton10EBHECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG3BptxANDFilter + process.hltEG10EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG10EBHEFilterHECut )
process.HLTHIGEDPhoton15EBHECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG3BptxANDFilter + process.hltEG15EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG15EBHEFilterHECut )
process.HLTHIGEDPhoton20EBHECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG3BptxANDFilter + process.hltEG20EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG20EBHEFilterHECut )
process.HLTHIGEDPhoton30EBHECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG7BptxANDFilter + process.hltEG30EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG30EBHEFilterHECut )
process.HLTHIGEDPhoton40EBHECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG21BptxANDFilter + process.hltEG40EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG40EBHEFilterHECut )
process.HLTHIGEDPhoton50EBHECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG21BptxANDFilter + process.hltEG50EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG50EBHEFilterHECut )
process.HLTHIGEDPhoton60EBHECutL1SeededSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEG30BptxANDFilter + process.hltEG60EBEtFilter + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG60EBHEFilterHECut )
process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence( process.hltEcalDigis + process.hltEcalUncalibRecHit + process.hltEcalDetIdToBeRecovered + process.hltEcalRecHit )
process.HLTDoCaloSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence + process.HLTDoLocalHcalSequence + process.hltTowerMakerForAll )
process.HLTDoHIEcalClusWithCleaningSequence = cms.Sequence( process.hltIslandBasicClustersHI + process.hltHiIslandSuperClustersHI + process.hltHiCorrectedIslandBarrelSuperClustersHI + process.hltHiCorrectedIslandEndcapSuperClustersHI + process.hltCleanedHiCorrectedIslandBarrelSuperClustersHI + process.hltRecoHIEcalWithCleaningCandidate )
process.HLTPuAK4CaloJetsReconstructionSequence = cms.Sequence( process.HLTDoCaloSequence + process.hltPuAK4CaloJets + process.hltPuAK4CaloJetsIDPassed )
process.HLTPuAK4CaloCorrectorProducersSequence = cms.Sequence( process.hltAK4CaloFastJetCorrector + process.hltAK4CaloRelativeCorrector + process.hltAK4CaloAbsoluteCorrector + process.hltPuAK4CaloCorrector )
process.HLTPuAK4CaloJetsCorrectionSequence = cms.Sequence( process.hltFixedGridRhoFastjetAllCalo + process.HLTPuAK4CaloCorrectorProducersSequence + process.hltPuAK4CaloJetsCorrected + process.hltPuAK4CaloJetsCorrectedIDPassed )
process.HLTPuAK4CaloJetsSequence = cms.Sequence( process.HLTPuAK4CaloJetsReconstructionSequence + process.HLTPuAK4CaloJetsCorrectionSequence )
process.HLTDoSiStripZeroSuppression = cms.Sequence( process.hltSiStripRawToDigi + process.hltSiStripZeroSuppression )
process.HLTDoLocalPixelSequencePPOnAA = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClustersPPOnAA + process.hltSiPixelClustersCachePPOnAA + process.hltSiPixelRecHitsPPOnAA )
process.HLTDoLocalStripSequencePPOnAA = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.hltHITrackingSiStripRawToClustersFacilityZeroSuppression + process.hltSiStripClustersPPOnAA )
process.HLTFullIterativeTrackingIteration0PreSplittingPPOnAA = cms.Sequence( process.hltFullIter0PixelQuadrupletsPreSplittingPPOnAA + process.hltFullIter0PixelTrackingRegionsPreSplitting + process.hltFullIter0PixelClusterCheckPreSplittingPPOnAA + process.hltFullIter0PixelHitDoubletsPreSplittingPPOnAA + process.hltFullIter0PixelHitQuadrupletsPreSplittingPPOnAA + process.hltFullIter0PixelSeedsPreSplittingPPOnAA + process.hltFullIter0CkfTrackCandidatesPreSplittingPPOnAA + process.hltFullIter0CtfWithMaterialTracksPreSplittingPPOnAA + process.hltFullIter0PrimaryVerticesPreSplittingPPOnAA )
process.HLTDoLocalPixelSequenceAfterSplittingPPOnAA = cms.Sequence( process.hltSiPixelClustersAfterSplittingPPOnAA + process.hltSiPixelClustersCacheAfterSplittingPPOnAA + process.hltSiPixelRecHitsAfterSplittingPPOnAA )
process.HLTDoLocalStripSequenceFullPPOnAA = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression + process.hltSiStripClustersFullPPOnAA + process.hltSiStripMatchedRecHitsFull )
process.HLTPixelClusterSplittingPPOnAA = cms.Sequence( process.HLTDoSiStripZeroSuppression + process.HLTPuAK4CaloJetsSequence + process.hltJetsForCoreTracking + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripSequencePPOnAA + process.HLTFullIterativeTrackingIteration0PreSplittingPPOnAA + process.HLTDoLocalPixelSequenceAfterSplittingPPOnAA + process.HLTDoLocalStripSequenceFullPPOnAA )
process.HLTFullIterativeTrackingIteration0PPOnAAForBTag = cms.Sequence( process.hltFullIter0PixelQuadrupletsPPOnAAForBTag + process.hltFullIter0PixelTrackingCandRegionsForBTag + process.hltFullIter0PixelClusterCheckPPOnAAForBTag + process.hltFullIter0PixelHitDoubletsPPOnAAForBTag + process.hltFullIter0PixelHitQuadrupletsPPOnAAForBTag + process.hltFullIter0PixelSeedsPPOnAAForBTag + process.hltFullIter0CkfTrackCandidatesPPOnAAForBTag + process.hltFullIter0CtfWithMaterialTracksPPOnAAForBTag + process.hltFullIter0PrimaryVerticesPPOnAAForBTag + process.hltFullIter0TrackMVAClassifierPPOnAAForBTag + process.hltFullIter0HighPurityTracksPPOnAAForBTag )
process.HLTFullIterativeTrackingIteration1PPOnAAForBTag = cms.Sequence( process.hltFullIter1ClustersRefRemovalPPOnAAForBTag + process.hltFullIter1MaskedMeasurementTrackerEventPPOnAAForBTag + process.hltFullIter1PixelQuadrupletsPPOnAAForBTag + process.hltFullIter1PixelTrackingCandRegionsForBTag + process.hltFullIter1PixelClusterCheckPPOnAAForBTag + process.hltFullIter1PixelHitDoubletsPPOnAAForBTag + process.hltFullIter1PixelHitQuadrupletsPPOnAAForBTag + process.hltFullIter1PixelSeedsPPOnAAForBTag + process.hltFullIter1CkfTrackCandidatesPPOnAAForBTag + process.hltFullIter1CtfWithMaterialTracksPPOnAAForBTag + process.hltFullIter1TrackMVAClassifierPPOnAAForBTag + process.hltFullIter1HighPurityTracksPPOnAAForBTag )
process.HLTFullIterativeTrackingIteration2PPOnAAForBTag = cms.Sequence( process.hltFullIter2ClustersRefRemovalPPOnAAForBTag + process.hltFullIter2MaskedMeasurementTrackerEventPPOnAAForBTag + process.hltFullIter2PixelTripletsPPOnAAForBTag + process.hltFullIter2PixelTrackingCandRegionsForBTag + process.hltFullIter2PixelClusterCheckPPOnAAForBTag + process.hltFullIter2PixelHitDoubletsPPOnAAForBTag + process.hltFullIter2PixelHitTripletsPPOnAAForBTag + process.hltFullIter2PixelSeedsPPOnAAForBTag + process.hltFullIter2CkfTrackCandidatesPPOnAAForBTag + process.hltFullIter2CtfWithMaterialTracksPPOnAAForBTag + process.hltFullIter2TrackMVAClassifierPPOnAAForBTag + process.hltFullIter2HighPurityTracksPPOnAAForBTag )
process.HLTFullIterativeTrackingIteration3PPOnAAForBTag = cms.Sequence( process.hltFullIter3ClustersRefRemovalPPOnAAForBTag + process.hltFullIter3MaskedMeasurementTrackerEventPPOnAAForBTag + process.hltFullIter3PixelTripletsPPOnAAForBTag + process.hltFullIter3PixelTrackingCandRegionsForBTag + process.hltFullIter3PixelClusterCheckPPOnAAForBTag + process.hltFullIter3PixelHitDoubletsPPOnAAForBTag + process.hltFullIter3PixelHitTripletsPPOnAAForBTag + process.hltFullIter3PixelSeedsPPOnAAForBTag + process.hltFullIter3CkfTrackCandidatesPPOnAAForBTag + process.hltFullIter3CtfWithMaterialTracksPPOnAAForBTag + process.hltFullIter3TrackMVAClassifierPPOnAAForBTag + process.hltFullIter3HighPurityTracksPPOnAAForBTag )
process.HLTFullIterativeTrackingIteration4PPOnAAForBTag = cms.Sequence( process.hltFullIter4ClustersRefRemovalPPOnAAForBTag + process.hltFullIter4MaskedMeasurementTrackerEventPPOnAAForBTag + process.hltFullIter4PixelQuadrupletsPPOnAAForBTag + process.hltFullIter4PixelTrackingCandRegionsForBTag + process.hltFullIter4PixelClusterCheckPPOnAAForBTag + process.hltFullIter4PixelHitDoubletsPPOnAAForBTag + process.hltFullIter4PixelHitQuadrupletsPPOnAAForBTag + process.hltFullIter4PixelSeedsPPOnAAForBTag + process.hltFullIter4CkfTrackCandidatesPPOnAAForBTag + process.hltFullIter4CtfWithMaterialTracksPPOnAAForBTag + process.hltFullIter4TrackMVAClassifierPPOnAAForBTag + process.hltFullIter4HighPurityTracksPPOnAAForBTag )
process.HLTFullIterativeTrackingIteration5PPOnAAForBTag = cms.Sequence( process.hltFullIter5ClustersRefRemovalPPOnAAForBTag + process.hltFullIter5MaskedMeasurementTrackerEventPPOnAAForBTag + process.hltFullIter5PixelTripletsPPOnAAForBTag + process.hltFullIter5PixelTrackingCandRegionsForBTag + process.hltFullIter5PixelClusterCheckPPOnAAForBTag + process.hltFullIter5PixelHitDoubletsPPOnAAForBTag + process.hltFullIter5PixelHitTripletsPPOnAAForBTag + process.hltFullIter5PixelSeedsPPOnAAForBTag + process.hltFullIter5CkfTrackCandidatesPPOnAAForBTag + process.hltFullIter5CtfWithMaterialTracksPPOnAAForBTag + process.hltFullIter5TrackMVAClassifierPPOnAAForBTag + process.hltFullIter5HighPurityTracksPPOnAAForBTag )
process.HLTFullIterativeTrackingPPOnAAForBTag = cms.Sequence( process.HLTFullIterativeTrackingIteration0PPOnAAForBTag + process.HLTFullIterativeTrackingIteration1PPOnAAForBTag + process.HLTFullIterativeTrackingIteration2PPOnAAForBTag + process.HLTFullIterativeTrackingIteration3PPOnAAForBTag + process.HLTFullIterativeTrackingIteration4PPOnAAForBTag + process.HLTFullIterativeTrackingIteration5PPOnAAForBTag + process.hltFullIterativeTrackingMergedPPOnAAForBTag )
process.HLTTrackReconstructionForBTagForHI = cms.Sequence( process.HLTPixelClusterSplittingPPOnAA + process.HLTFullIterativeTrackingPPOnAAForBTag )
process.HLTBtagDeepCSVSequenceL3ForHI = cms.Sequence( process.HLTTrackReconstructionForBTagForHI + process.hltFullOnlinePrimaryVerticesPPOnAAForBTag + process.hltFastPixelBLifetimeL3AssociatorHI + process.hltImpactParameterTagInfosHI + process.hltInclusiveVertexFinderPPOnAA + process.hltInclusiveSecondaryVerticesPPOnAA + process.hltTrackVertexArbitratorPPOnAA + process.hltInclusiveMergedVerticesPPOnAA + process.hltInclusiveSecondaryVertexFinderTagInfosHI + process.hltDeepCombinedSecondaryVertexBJetTagsInfosCaloHIBJet60 + process.hltDeepCombinedSecondaryVertexBJetTagsCaloBJet60 )
process.HLTDoHIStripZeroSuppressionRepacker = cms.Sequence( process.hltSiStripDigiToZSRaw + process.hltSiStripRawDigiToVirginRaw + process.virginRawDataRepacker + process.rawDataRepacker + process.rawDataReducedFormat )
process.HLTBtagDeepCSVSequenceL3ForHIBJet80 = cms.Sequence( process.HLTTrackReconstructionForBTagForHI + process.hltFullOnlinePrimaryVerticesPPOnAAForBTag + process.hltFastPixelBLifetimeL3AssociatorHIBJet80 + process.hltImpactParameterTagInfosHIBJet80 + process.hltInclusiveVertexFinderPPOnAA + process.hltInclusiveSecondaryVerticesPPOnAA + process.hltTrackVertexArbitratorPPOnAA + process.hltInclusiveMergedVerticesPPOnAA + process.hltInclusiveSecondaryVertexFinderTagInfosHIBJet80 + process.hltDeepCombinedSecondaryVertexBJetTagsInfosCaloHIBJet80 + process.hltDeepCombinedSecondaryVertexBJetTagsCaloBJet80 )
process.HLTBtagDeepCSVSequenceL3ForHIBJet100 = cms.Sequence( process.HLTTrackReconstructionForBTagForHI + process.hltFullOnlinePrimaryVerticesPPOnAAForBTag + process.hltFastPixelBLifetimeL3AssociatorHIBJet100 + process.hltImpactParameterTagInfosHIBJet100 + process.hltInclusiveVertexFinderPPOnAA + process.hltInclusiveSecondaryVerticesPPOnAA + process.hltTrackVertexArbitratorPPOnAA + process.hltInclusiveMergedVerticesPPOnAA + process.hltInclusiveSecondaryVertexFinderTagInfosHIBJet100 + process.hltDeepCombinedSecondaryVertexBJetTagsInfosCaloHIBJet100 + process.hltDeepCombinedSecondaryVertexBJetTagsCaloBJet100 )
process.HLTBtagCSVv2SequenceL3ForHI = cms.Sequence( process.HLTTrackReconstructionForBTagForHI + process.hltFullOnlinePrimaryVerticesPPOnAAForBTag + process.hltFastPixelBLifetimeL3AssociatorHI + process.hltImpactParameterTagInfosHI + process.hltInclusiveVertexFinderPPOnAA + process.hltInclusiveSecondaryVerticesPPOnAA + process.hltTrackVertexArbitratorPPOnAA + process.hltInclusiveMergedVerticesPPOnAA + process.hltInclusiveSecondaryVertexFinderTagInfosHI + process.hltCombinedSecondaryVertexV2BJetTagsCalo )
process.HLTBtagCSVv2SequenceL3ForHIBJet80 = cms.Sequence( process.HLTTrackReconstructionForBTagForHI + process.hltFullOnlinePrimaryVerticesPPOnAAForBTag + process.hltFastPixelBLifetimeL3AssociatorHIBJet80 + process.hltImpactParameterTagInfosHIBJet80 + process.hltInclusiveVertexFinderPPOnAA + process.hltInclusiveSecondaryVerticesPPOnAA + process.hltTrackVertexArbitratorPPOnAA + process.hltInclusiveMergedVerticesPPOnAA + process.hltInclusiveSecondaryVertexFinderTagInfosHIBJet80 + process.hltCombinedSecondaryVertexV2BJetTagsCaloBJet80 )
process.HLTBtagCSVv2SequenceL3ForHIBJet100 = cms.Sequence( process.HLTTrackReconstructionForBTagForHI + process.hltFullOnlinePrimaryVerticesPPOnAAForBTag + process.hltFastPixelBLifetimeL3AssociatorHIBJet100 + process.hltImpactParameterTagInfosHIBJet100 + process.hltInclusiveVertexFinderPPOnAA + process.hltInclusiveSecondaryVerticesPPOnAA + process.hltTrackVertexArbitratorPPOnAA + process.hltInclusiveMergedVerticesPPOnAA + process.hltInclusiveSecondaryVertexFinderTagInfosHIBJet100 + process.hltCombinedSecondaryVertexV2BJetTagsCaloBJet100 )
process.HLTDoCaloSequencePF = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence + process.HLTDoLocalHcalSequence + process.hltTowerMakerForAll )
process.HLTAK4CaloJetsPrePFRecoSequence = cms.Sequence( process.HLTDoCaloSequencePF + process.hltAK4CaloJetsPF )
process.HLTPreAK4PFJetsRecoSequence = cms.Sequence( process.HLTAK4CaloJetsPrePFRecoSequence + process.hltAK4CaloJetsPFEt5 )
process.HLTMuonLocalRecoSequence = cms.Sequence( process.hltMuonDTDigis + process.hltDt1DRecHits + process.hltDt4DSegments + process.hltMuonCSCDigis + process.hltCsc2DRecHits + process.hltCscSegments + process.hltMuonRPCDigis + process.hltRpcRecHits )
process.HLTL2muonrecoNocandSequencePPOnAA = cms.Sequence( process.HLTMuonLocalRecoSequence + process.hltL2OfflineMuonSeeds + process.hltL2MuonSeedsPPOnAA + process.hltL2MuonsPPOnAA )
process.HLTL2muonrecoSequencePPOnAA = cms.Sequence( process.HLTL2muonrecoNocandSequencePPOnAA + process.hltL2MuonCandidatesPPOnAA )
process.HLTIterL3OImuonTkCandidatePPOnAASequence = cms.Sequence( process.hltIterL3OISeedsFromL2MuonsPPOnAA + process.hltIterL3OITrackCandidatesPPOnAA + process.hltIterL3OIMuCtfWithMaterialTracksPPOnAA + process.hltIterL3OIMuonTrackCutClassifierPPOnAA + process.hltIterL3OIMuonTrackSelectionHighPurityPPOnAA + process.hltL3MuonsIterL3OIPPOnAA )
process.HLTIterL3MuonRecoPixelTracksPPOnAASequence = cms.Sequence( process.hltIterL3MuonPixelTracksFilter + process.hltIterL3MuonPixelTracksFitter + process.hltIterL3MuonPixelTracksTrackingRegionsPPOnAA + process.hltIterL3MuonPixelLayerQuadrupletsPPOnAA + process.hltIterL3MuonPixelTracksHitDoubletsPPOnAA + process.hltIterL3MuonPixelTracksHitQuadrupletsPPOnAA + process.hltIterL3MuonPixelTracksPPOnAA )
process.HLTIterL3MuonRecopixelvertexingPPOnAASequence = cms.Sequence( process.HLTIterL3MuonRecoPixelTracksPPOnAASequence + process.hltIterL3MuonPixelVerticesPPOnAA + process.hltIterL3MuonTrimmedPixelVerticesPPOnAA )
process.HLTIterativeTrackingIteration0ForIterL3MuonPPOnAA = cms.Sequence( process.hltIter0IterL3MuonPixelSeedsFromPixelTracksPPOnAA + process.hltIter0IterL3MuonCkfTrackCandidatesPPOnAA + process.hltIter0IterL3MuonCtfWithMaterialTracksPPOnAA + process.hltIter0IterL3MuonTrackCutClassifierPPOnAA + process.hltIter0IterL3MuonTrackSelectionHighPurityPPOnAA )
process.HLTIterativeTrackingIteration2ForIterL3MuonPPOnAA = cms.Sequence( process.hltIter2IterL3MuonClustersRefRemovalPPOnAA + process.hltIter2IterL3MuonMaskedMeasurementTrackerEventPPOnAA + process.hltIter2IterL3MuonPixelLayerTripletsPPOnAA + process.hltIter2IterL3MuonPixelClusterCheckPPOnAA + process.hltIter2IterL3MuonPixelHitDoubletsPPOnAA + process.hltIter2IterL3MuonPixelHitTripletsPPOnAA + process.hltIter2IterL3MuonPixelSeedsPPOnAA + process.hltIter2IterL3MuonCkfTrackCandidatesPPOnAA + process.hltIter2IterL3MuonCtfWithMaterialTracksPPOnAA + process.hltIter2IterL3MuonTrackCutClassifierPPOnAA + process.hltIter2IterL3MuonTrackSelectionHighPurityPPOnAA )
process.HLTIterativeTrackingIteration3ForIterL3MuonPPOnAA = cms.Sequence( process.hltIter3IterL3MuonClustersRefRemovalPPOnAA + process.hltIter3IterL3MuonMaskedMeasurementTrackerEventPPOnAA + process.hltIter3IterL3MuonPixelLayerPairsPPOnAA + process.hltIter3IterL3MuonL2CandidatesPPOnAA + process.hltIter3IterL3MuonTrackingRegionsPPOnAA + process.hltIter3IterL3MuonPixelClusterCheckPPOnAA + process.hltIter3IterL3MuonPixelHitDoubletsPPOnAA + process.hltIter3IterL3MuonPixelSeedsPPOnAA + process.hltIter3IterL3MuonCkfTrackCandidatesPPOnAA + process.hltIter3IterL3MuonCtfWithMaterialTracksPPOnAA + process.hltIter3IterL3MuonTrackCutClassifierPPOnAA + process.hltIter3IterL3MuonTrackSelectionHighPurityPPOnAA )
process.HLTIterativeTrackingIter023ForIterL3MuonPPOnAA = cms.Sequence( process.HLTIterativeTrackingIteration0ForIterL3MuonPPOnAA + process.HLTIterativeTrackingIteration2ForIterL3MuonPPOnAA + process.hltIter2IterL3MuonMergedPPOnAA + process.HLTIterativeTrackingIteration3ForIterL3MuonPPOnAA + process.hltIter3IterL3MuonMergedPPOnAA )
process.HLTIterL3IOmuonTkCandidatePPOnAASequence = cms.Sequence( process.HLTIterL3MuonRecopixelvertexingPPOnAASequence + process.HLTIterativeTrackingIter023ForIterL3MuonPPOnAA + process.hltL3MuonsIterL3IOPPOnAA )
process.HLTIterL3OIAndIOFromL2muonTkCandidatePPOnAASequence = cms.Sequence( process.HLTIterL3OImuonTkCandidatePPOnAASequence + process.hltIterL3OIL3MuonsLinksCombinationPPOnAA + process.hltIterL3OIL3MuonsPPOnAA + process.hltIterL3OIL3MuonCandidatesPPOnAA + process.hltL2SelectorForL3IOPPOnAA + process.HLTIterL3IOmuonTkCandidatePPOnAASequence + process.hltIterL3MuonsFromL2LinksCombinationPPOnAA )
process.HLTRecoPixelTracksSequenceForIterL3FromL1MuonPPOnAA = cms.Sequence( process.hltIterL3FromL1MuonPixelTracksTrackingRegionsPPOnAA + process.hltIterL3FromL1MuonPixelLayerQuadrupletsPPOnAA + process.hltIterL3FromL1MuonPixelTracksHitDoubletsPPOnAA + process.hltIterL3FromL1MuonPixelTracksHitQuadrupletsPPOnAA + process.hltIterL3FromL1MuonPixelTracksPPOnAA )
process.HLTRecopixelvertexingSequenceForIterL3FromL1MuonPPOnAA = cms.Sequence( process.HLTRecoPixelTracksSequenceForIterL3FromL1MuonPPOnAA + process.hltIterL3FromL1MuonPixelVerticesPPOnAA + process.hltIterL3FromL1MuonTrimmedPixelVerticesPPOnAA )
process.HLTIterativeTrackingIteration0ForIterL3FromL1MuonPPOnAA = cms.Sequence( process.hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracksPPOnAA + process.hltIter0IterL3FromL1MuonCkfTrackCandidatesPPOnAA + process.hltIter0IterL3FromL1MuonCtfWithMaterialTracksPPOnAA + process.hltIter0IterL3FromL1MuonTrackCutClassifierPPOnAA + process.hltIter0IterL3FromL1MuonTrackSelectionHighPurityPPOnAA )
process.HLTIterativeTrackingIteration2ForIterL3FromL1MuonPPOnAA = cms.Sequence( process.hltIter2IterL3FromL1MuonClustersRefRemovalPPOnAA + process.hltIter2IterL3FromL1MuonMaskedMeasurementTrackerEventPPOnAA + process.hltIter2IterL3FromL1MuonPixelLayerTripletsPPOnAA + process.hltIter2IterL3FromL1MuonPixelClusterCheckPPOnAA + process.hltIter2IterL3FromL1MuonPixelHitDoubletsPPOnAA + process.hltIter2IterL3FromL1MuonPixelHitTripletsPPOnAA + process.hltIter2IterL3FromL1MuonPixelSeedsPPOnAA + process.hltIter2IterL3FromL1MuonCkfTrackCandidatesPPOnAA + process.hltIter2IterL3FromL1MuonCtfWithMaterialTracksPPOnAA + process.hltIter2IterL3FromL1MuonTrackCutClassifierPPOnAA + process.hltIter2IterL3FromL1MuonTrackSelectionHighPurityPPOnAA )
process.HLTIterativeTrackingIteration3ForIterL3FromL1MuonPPOnAA = cms.Sequence( process.hltIter3IterL3FromL1MuonClustersRefRemovalPPOnAA + process.hltIter3IterL3FromL1MuonMaskedMeasurementTrackerEventPPOnAA + process.hltIter3IterL3FromL1MuonPixelLayerPairsPPOnAA + process.hltIter3IterL3FromL1MuonTrackingRegionsPPOnAA + process.hltIter3IterL3FromL1MuonPixelClusterCheckPPOnAA + process.hltIter3IterL3FromL1MuonPixelHitDoubletsPPOnAA + process.hltIter3IterL3FromL1MuonPixelSeedsPPOnAA + process.hltIter3IterL3FromL1MuonCkfTrackCandidatesPPOnAA + process.hltIter3IterL3FromL1MuonCtfWithMaterialTracksPPOnAA + process.hltIter3IterL3FromL1MuonTrackCutClassifierPPOnAA + process.hltIter3IterL3FromL1MuonTrackSelectionHighPurityPPOnAA )
process.HLTIterativeTrackingIter023ForIterL3FromL1MuonPPOnAA = cms.Sequence( process.HLTIterativeTrackingIteration0ForIterL3FromL1MuonPPOnAA + process.HLTIterativeTrackingIteration2ForIterL3FromL1MuonPPOnAA + process.hltIter2IterL3FromL1MuonMergedPPOnAA + process.HLTIterativeTrackingIteration3ForIterL3FromL1MuonPPOnAA + process.hltIter3IterL3FromL1MuonMergedPPOnAA )
process.HLTIterL3IOmuonFromL1TkCandidatePPOnAASequence = cms.Sequence( process.HLTRecopixelvertexingSequenceForIterL3FromL1MuonPPOnAA + process.HLTIterativeTrackingIter023ForIterL3FromL1MuonPPOnAA )
process.HLTIterL3muonTkCandidatePPOnAASequence = cms.Sequence( process.HLTDoSiStripZeroSuppression + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripSequencePPOnAA + process.HLTIterL3OIAndIOFromL2muonTkCandidatePPOnAASequence + process.hltL1MuonsPt0PPOnAA + process.HLTIterL3IOmuonFromL1TkCandidatePPOnAASequence )
process.HLTL3muonrecoNocandPPOnAASequence = cms.Sequence( process.HLTIterL3muonTkCandidatePPOnAASequence + process.hltIterL3MuonMergedPPOnAA + process.hltIterL3MuonAndMuonFromL1MergedPPOnAA + process.hltIterL3GlbMuonPPOnAA + process.hltIterL3MuonsNoIDPPOnAA + process.hltIterL3MuonsPPOnAA + process.hltL3MuonsIterL3LinksPPOnAA + process.hltIterL3MuonTracksPPOnAA )
process.HLTL3muonrecoPPOnAASequence = cms.Sequence( process.HLTL3muonrecoNocandPPOnAASequence + process.hltIterL3MuonCandidatesPPOnAA )
process.HLTPixelClusterSplittingForPFPPOnAA = cms.Sequence( process.HLTDoSiStripZeroSuppression + process.hltJetsForCoreTracking + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripSequencePPOnAA + process.HLTFullIterativeTrackingIteration0PreSplittingPPOnAA + process.HLTDoLocalPixelSequenceAfterSplittingPPOnAA + process.HLTDoLocalStripSequenceFullPPOnAA )
process.HLTRecoPixelTracksSequencePPOnAA = cms.Sequence( process.hltPixelTracksFilter + process.hltPixelTracksFitter + process.hltPixelTracksTrackingRegionsPPOnAA + process.hltPixelLayerQuadrupletsPPOnAA + process.hltPixelTracksHitDoubletsPPOnAA + process.hltPixelTracksHitQuadrupletsPPOnAA + process.hltPixelTracksPPOnAA )
process.HLTRecopixelvertexingSequencePPOnAA = cms.Sequence( process.HLTRecoPixelTracksSequencePPOnAA + process.hltPixelVerticesPPOnAA + process.hltTrimmedPixelVerticesPPOnAA )
process.HLTFullIterativeTrackingIteration0PPOnAA = cms.Sequence( process.hltFullIter0PixelQuadrupletsPPOnAA + process.hltFullIter0PixelTrackingRegions + process.hltFullIter0PixelClusterCheckPPOnAA + process.hltFullIter0PixelHitDoubletsPPOnAA + process.hltFullIter0PixelHitQuadrupletsPPOnAA + process.hltFullIter0PixelSeedsPPOnAA + process.hltFullIter0CkfTrackCandidatesPPOnAA + process.hltFullIter0CtfWithMaterialTracksPPOnAA + process.hltFullIter0PrimaryVerticesPPOnAA + process.hltFullIter0TrackMVAClassifierPPOnAA + process.hltFullIter0HighPurityTracksPPOnAA )
process.HLTFullIterativeTrackingIteration1PPOnAA = cms.Sequence( process.hltFullIter1ClustersRefRemovalPPOnAA + process.hltFullIter1MaskedMeasurementTrackerEventPPOnAA + process.hltFullIter1PixelQuadrupletsPPOnAA + process.hltFullIter1PixelTrackingRegionsPPOnAA + process.hltFullIter1PixelClusterCheckPPOnAA + process.hltFullIter1PixelHitDoubletsPPOnAA + process.hltFullIter1PixelHitQuadrupletsPPOnAA + process.hltFullIter1PixelSeedsPPOnAA + process.hltFullIter1CkfTrackCandidatesPPOnAA + process.hltFullIter1CtfWithMaterialTracksPPOnAA + process.hltFullIter1TrackMVAClassifierPPOnAA + process.hltFullIter1HighPurityTracksPPOnAA )
process.HLTIter1TrackAndTauJets4Iter2SequencePPOnAA = cms.Sequence( process.hltIter1TrackRefsForJets4Iter2PPOnAA + process.hltAK4Iter1TrackJets4Iter2PPOnAA + process.hltIter1TrackAndTauJets4Iter2PPOnAA )
process.HLTFullIterativeTrackingIteration2PPOnAA = cms.Sequence( process.hltFullIter2ClustersRefRemovalPPOnAA + process.hltFullIter2MaskedMeasurementTrackerEventPPOnAA + process.hltFullIter2PixelTripletsPPOnAA + process.hltFullIter2PixelTrackingRegionsPPOnAA + process.hltFullIter2PixelClusterCheckPPOnAA + process.hltFullIter2PixelHitDoubletsPPOnAA + process.hltFullIter2PixelHitTripletsPPOnAA + process.hltFullIter2PixelSeedsPPOnAA + process.hltFullIter2CkfTrackCandidatesPPOnAA + process.hltFullIter2CtfWithMaterialTracksPPOnAA + process.hltFullIter2TrackMVAClassifierPPOnAA + process.hltFullIter2HighPurityTracksPPOnAA )
process.HLTIterativeTrackingDoubletRecoveryPPOnAA = cms.Sequence( process.hltDoubletRecoveryClustersRefRemovalPPOnAA + process.hltDoubletRecoveryMaskedMeasurementTrackerEventPPOnAA + process.hltDoubletRecoveryPixelLayersAndRegionsPPOnAA + process.hltDoubletRecoveryPFlowPixelClusterCheckPPOnAA + process.hltDoubletRecoveryPFlowPixelHitDoubletsPPOnAA + process.hltDoubletRecoveryPFlowPixelSeedsPPOnAA + process.hltDoubletRecoveryPFlowCkfTrackCandidatesPPOnAA + process.hltDoubletRecoveryPFlowCtfWithMaterialTracksPPOnAA + process.hltDoubletRecoveryPFlowTrackCutClassifierPPOnAA + process.hltDoubletRecoveryPFlowTrackSelectionHighPurityPPOnAA )
process.HLTFullIterativeTrackingIteration02PPOnAA = cms.Sequence( process.HLTFullIterativeTrackingIteration0PPOnAA + process.HLTFullIterativeTrackingIteration1PPOnAA + process.hltIter1MergedPPOnAA + process.HLTIter1TrackAndTauJets4Iter2SequencePPOnAA + process.HLTFullIterativeTrackingIteration2PPOnAA + process.hltIter2MergedPPOnAA + process.HLTIterativeTrackingDoubletRecoveryPPOnAA + process.hltMergedTracksPPOnAA )
process.HLTTrackReconstructionForPFPPOnAA = cms.Sequence( process.HLTPixelClusterSplittingForPFPPOnAA + process.HLTRecopixelvertexingSequencePPOnAA + process.HLTFullIterativeTrackingIteration02PPOnAA + process.hltPFMuonMergingPPOnAA + process.hltMuonLinksPPOnAA + process.hltMuonsPPOnAA )
process.HLTPreshowerSequence = cms.Sequence( process.hltEcalPreshowerDigis + process.hltEcalPreshowerRecHit )
process.HLTParticleFlowSequencePPOnAA = cms.Sequence( process.HLTPreshowerSequence + process.hltParticleFlowRecHitECALUnseeded + process.hltParticleFlowRecHitHBHE + process.hltParticleFlowRecHitHF + process.hltParticleFlowRecHitPSUnseeded + process.hltParticleFlowClusterECALUncorrectedUnseeded + process.hltParticleFlowClusterPSUnseeded + process.hltParticleFlowClusterECALUnseeded + process.hltParticleFlowClusterHBHE + process.hltParticleFlowClusterHCAL + process.hltParticleFlowClusterHF + process.hltLightPFTracksPPOnAA + process.hltParticleFlowBlockPPOnAA + process.hltParticleFlowPPOnAA )
process.HLTCsAK4PFJetsReconstructionSequencePPOnAA = cms.Sequence( process.HLTL2muonrecoSequencePPOnAA + process.HLTL3muonrecoPPOnAASequence + process.HLTTrackReconstructionForPFPPOnAA + process.HLTParticleFlowSequencePPOnAA + process.hltKT4PFJetsForRho + process.hltHiFJRhoProducer + process.hltCsAK4PFJetsPPOnAA + process.hltCsAK4PFJetsLooseIDPPOnAA + process.hltCsAK4PFJetsTightIDPPOnAA )
process.HLTCsAK4PFCorrectorProducersSequencePPOnAA = cms.Sequence( process.hltCsAK4PFFastJetCorrectorPPOnAA + process.hltCsAK4PFRelativeCorrectorPPOnAA + process.hltCsAK4PFAbsoluteCorrectorPPOnAA + process.hltCsAK4PFResidualCorrectorPPOnAA + process.hltCsAK4PFCorrectorPPOnAA )
process.HLTCsAK4PFJetsCorrectionSequence = cms.Sequence( process.hltFixedGridRhoFastjetAllPPOnAA + process.HLTCsAK4PFCorrectorProducersSequencePPOnAA + process.hltCsAK4PFJetsCorrectedPPOnAA + process.hltCsAK4PFJetsLooseIDCorrectedPPOnAA + process.hltCsAK4PFJetsTightIDCorrectedPPOnAA )
process.HLTCsAK4PFJetsSequence = cms.Sequence( process.HLTPreAK4PFJetsRecoSequence + process.HLTCsAK4PFJetsReconstructionSequencePPOnAA + process.HLTCsAK4PFJetsCorrectionSequence )
process.HLTPFHcalClusteringForEgamma = cms.Sequence( process.hltRegionalTowerForEgamma + process.hltParticleFlowRecHitHBHEForEgamma + process.hltParticleFlowClusterHBHEForEgamma + process.hltParticleFlowClusterHCALForEgamma )
process.HLTDoLocalStripPPOnAAZeroSuppressionSequence = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.HLTDoSiStripZeroSuppression + process.hltHITrackingSiStripRawToClustersFacilityZeroSuppression + process.hltSiStripClustersPPOnAAZeroSuppression )
process.HLTRecoPixelTracksPPOnAASequence = cms.Sequence( process.hltPixelTracksFilter + process.hltPixelTracksFitter + process.hltPixelTracksTrackingRegionsPPOnAA + process.hltPixelLayerQuadrupletsPPOnAA + process.hltPixelTracksHitDoubletsPPOnAA + process.hltPixelTracksHitQuadrupletsPPOnAA + process.hltPixelTracksPPOnAA )
process.HLTPixelVertexingPPOnAASequence = cms.Sequence( process.HLTRecoPixelTracksPPOnAASequence + process.hltPixelVerticesPPOnAA + process.hltTrimmedPixelVerticesPPOnAA )
process.HLTElectronPixelMatchingPPOnAASequence = cms.Sequence( process.hltPixelLayerPairsPPOnAA + process.hltPixelLayerTripletsPPOnAA + process.hltEgammaSuperClustersToPixelMatchPPOnAA + process.hltEleSeedsTrackingRegionsPPOnAA + process.hltElePixelHitDoubletsPPOnAA + process.hltElePixelSeedsDoubletsPPOnAA + process.hltElePixelHitDoubletsForTripletsPPOnAA + process.hltElePixelHitTripletsPPOnAA + process.hltElePixelSeedsTripletsPPOnAA + process.hltElePixelSeedsCombinedPPOnAA + process.hltEgammaElectronPixelSeedsPPOnAA + process.hltEgammaPixelMatchVarsPPOnAA )
process.HLTGsfElectronPPOnAASequence = cms.Sequence( process.hltEgammaCkfTrackCandidatesForGSFPPOnAA + process.hltEgammaGsfTracksPPOnAA + process.hltEgammaGsfElectronsPPOnAA + process.hltEgammaGsfTrackVarsPPOnAA )
process.HLTIterativeTrackingForElectronsIteration0 = cms.Sequence( process.hltIter0ElectronsPixelSeedsFromPixelTracks + process.hltIter0ElectronsCkfTrackCandidates + process.hltIter0ElectronsCtfWithMaterialTracks + process.hltIter0ElectronsTrackSelectionHighPurity )
process.HLTIterativeTrackingForElectronsIteration1 = cms.Sequence( process.hltIter1ElectronsClustersRefRemoval + process.hltIter1ElectronsMaskedMeasurementTrackerEvent + process.hltIter1ElectronsPixelLayerQuadruplets + process.hltIter1ElectronsPixelTrackingRegions + process.hltIter1ElectronsPixelHitDoublets + process.hltIter1ElectronsPixelHitQuadruplets + process.hltIter1ElectronsPixelTracks + process.hltIter1ElectronsPixelSeedsFromPixelTracks + process.hltIter1ElectronsCkfTrackCandidates + process.hltIter1ElectronsCtfWithMaterialTracks + process.hltIter1ElectronsTrackSelectionHighPurityLoose + process.hltIter1ElectronsTrackSelectionHighPurityTight + process.hltIter1ElectronsTrackSelectionHighPurity )
process.HLTIterativeTrackingForElectronsIteration2 = cms.Sequence( process.hltIter2ElectronsClustersRefRemoval + process.hltIter2ElectronsMaskedMeasurementTrackerEvent + process.hltIter2ElectronsPixelLayerTriplets + process.hltIter2ElectronsPixelTrackingRegions + process.hltIter2ElectronsPixelHitDoublets + process.hltIter2ElectronsPixelHitTriplets + process.hltIter2ElectronsPixelSeeds + process.hltIter2ElectronsCkfTrackCandidates + process.hltIter2ElectronsCtfWithMaterialTracks + process.hltIter2ElectronsTrackSelectionHighPurity )
process.HLTIterativeTrackingDoubletRecoveryForElectrons = cms.Sequence( process.hltDoubletRecoveryForElectronsClustersRefRemoval + process.hltDoubletRecoveryForElectronsMaskedMeasurementTrackerEvent + process.hltDoubletRecoveryForElectronsPixelLayersAndRegions + process.hltDoubletRecoveryForElectronsPFlowPixelHitDoublets + process.hltDoubletRecoveryForElectronsPFlowPixelSeeds + process.hltDoubletRecoveryForElectronsPFlowCkfTrackCandidates + process.hltDoubletRecoveryForElectronsPFlowCtfWithMaterialTracks + process.hltDoubletRecoveryForElectronsPFlowTrackSelectionHighPurity )
process.HLTIterativeTrackingForElectrons = cms.Sequence( process.HLTIterativeTrackingForElectronsIteration0 + process.HLTIterativeTrackingForElectronsIteration1 + process.hltIter1ForElectronsMerged + process.HLTIterativeTrackingForElectronsIteration2 + process.hltIter2ForElectronsMerged + process.HLTIterativeTrackingDoubletRecoveryForElectrons + process.hltMergedForElectrons )
process.HLTEle10GsfPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG10EtPPOnAAFilter + process.hltEgammaClusterShapePPOnAA + process.hltEle10ClusterShapePPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEle10HoverEPPOnAAFilter + process.hltEgammaEcalPFClusterIsoPPOnAA + process.hltEle10EcalIsoPPOnAAFilter + process.HLTPFHcalClusteringForEgamma + process.hltEgammaHcalPFClusterIsoPPOnAA + process.hltEle10HcalIsoPPOnAAFilter + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripPPOnAAZeroSuppressionSequence + process.HLTPixelVertexingPPOnAASequence + process.HLTElectronPixelMatchingPPOnAASequence + process.hltEle10PixelMatchPPOnAAFilter + process.HLTGsfElectronPPOnAASequence + process.hltEle10GsfOneOEMinusOneOPPPOnAAFilter + process.hltEle10GsfDetaPPOnAAFilter + process.hltEle10GsfDphiPPOnAAFilter + process.HLTIterativeTrackingForElectrons + process.hltEgammaEleGsfTrackIsoPPOnAA + process.hltEle10GsfTrackIsoPPOnAAFilter )
process.HLTEle15GsfPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG15EtPPOnAAFilter + process.hltEgammaClusterShapePPOnAA + process.hltEle15ClusterShapePPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEle15HoverEPPOnAAFilter + process.hltEgammaEcalPFClusterIsoPPOnAA + process.hltEle15EcalIsoPPOnAAFilter + process.HLTPFHcalClusteringForEgamma + process.hltEgammaHcalPFClusterIsoPPOnAA + process.hltEle15HcalIsoPPOnAAFilter + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripPPOnAAZeroSuppressionSequence + process.HLTPixelVertexingPPOnAASequence + process.HLTElectronPixelMatchingPPOnAASequence + process.hltEle15PixelMatchPPOnAAFilter + process.HLTGsfElectronPPOnAASequence + process.hltEle15GsfOneOEMinusOneOPPPOnAAFilter + process.hltEle15GsfDetaPPOnAAFilter + process.hltEle15GsfDphiPPOnAAFilter + process.HLTIterativeTrackingForElectrons + process.hltEgammaEleGsfTrackIsoPPOnAA + process.hltEle15GsfTrackIsoPPOnAAFilter )
process.HLTEle20GsfPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG20EtPPOnAAFilter + process.hltEgammaClusterShapePPOnAA + process.hltEle20ClusterShapePPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEle20HoverEPPOnAAFilter + process.hltEgammaEcalPFClusterIsoPPOnAA + process.hltEle20EcalIsoPPOnAAFilter + process.HLTPFHcalClusteringForEgamma + process.hltEgammaHcalPFClusterIsoPPOnAA + process.hltEle20HcalIsoPPOnAAFilter + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripPPOnAAZeroSuppressionSequence + process.HLTPixelVertexingPPOnAASequence + process.HLTElectronPixelMatchingPPOnAASequence + process.hltEle20PixelMatchPPOnAAFilter + process.HLTGsfElectronPPOnAASequence + process.hltEle20GsfOneOEMinusOneOPPPOnAAFilter + process.hltEle20GsfDetaPPOnAAFilter + process.hltEle20GsfDphiPPOnAAFilter + process.HLTIterativeTrackingForElectrons + process.hltEgammaEleGsfTrackIsoPPOnAA + process.hltEle20GsfTrackIsoPPOnAAFilter )
process.HLTEle30GsfPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG30EtPPOnAAFilter + process.hltEgammaClusterShapePPOnAA + process.hltEle30ClusterShapePPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEle30HoverEPPOnAAFilter + process.hltEgammaEcalPFClusterIsoPPOnAA + process.hltEle30EcalIsoPPOnAAFilter + process.HLTPFHcalClusteringForEgamma + process.hltEgammaHcalPFClusterIsoPPOnAA + process.hltEle30HcalIsoPPOnAAFilter + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripPPOnAAZeroSuppressionSequence + process.HLTPixelVertexingPPOnAASequence + process.HLTElectronPixelMatchingPPOnAASequence + process.hltEle30PixelMatchPPOnAAFilter + process.HLTGsfElectronPPOnAASequence + process.hltEle30GsfOneOEMinusOneOPPPOnAAFilter + process.hltEle30GsfDetaPPOnAAFilter + process.hltEle30GsfDphiPPOnAAFilter + process.HLTIterativeTrackingForElectrons + process.hltEgammaEleGsfTrackIsoPPOnAA + process.hltEle30GsfTrackIsoPPOnAAFilter )
process.HLTEle40GsfPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG40EtPPOnAAFilter + process.hltEgammaClusterShapePPOnAA + process.hltEle40ClusterShapePPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEle40HoverEPPOnAAFilter + process.hltEgammaEcalPFClusterIsoPPOnAA + process.hltEle40EcalIsoPPOnAAFilter + process.HLTPFHcalClusteringForEgamma + process.hltEgammaHcalPFClusterIsoPPOnAA + process.hltEle40HcalIsoPPOnAAFilter + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripPPOnAAZeroSuppressionSequence + process.HLTPixelVertexingPPOnAASequence + process.HLTElectronPixelMatchingPPOnAASequence + process.hltEle40PixelMatchPPOnAAFilter + process.HLTGsfElectronPPOnAASequence + process.hltEle40GsfOneOEMinusOneOPPPOnAAFilter + process.hltEle40GsfDetaPPOnAAFilter + process.hltEle40GsfDphiPPOnAAFilter + process.HLTIterativeTrackingForElectrons + process.hltEgammaEleGsfTrackIsoPPOnAA + process.hltEle40GsfTrackIsoPPOnAAFilter )
process.HLTEle50GsfPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG50EtPPOnAAFilter + process.hltEgammaClusterShapePPOnAA + process.hltEle50ClusterShapePPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltEle50HoverEPPOnAAFilter + process.hltEgammaEcalPFClusterIsoPPOnAA + process.hltEle50EcalIsoPPOnAAFilter + process.HLTPFHcalClusteringForEgamma + process.hltEgammaHcalPFClusterIsoPPOnAA + process.hltEle50HcalIsoPPOnAAFilter + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripPPOnAAZeroSuppressionSequence + process.HLTPixelVertexingPPOnAASequence + process.HLTElectronPixelMatchingPPOnAASequence + process.hltEle50PixelMatchPPOnAAFilter + process.HLTGsfElectronPPOnAASequence + process.hltEle50GsfOneOEMinusOneOPPPOnAAFilter + process.hltEle50GsfDetaPPOnAAFilter + process.hltEle50GsfDphiPPOnAAFilter + process.HLTIterativeTrackingForElectrons + process.hltEgammaEleGsfTrackIsoPPOnAA + process.hltEle50GsfTrackIsoPPOnAAFilter )
process.HLTEle15Ele10GsfPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltEG15EtPPOnAAFilter + process.hltDoubleEG10EtPPOnAAFilter + process.hltEgammaClusterShapePPOnAA + process.hltDoubleEle10ClusterShapePPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltDoubleEle10HoverEPPOnAAFilter + process.hltEgammaEcalPFClusterIsoPPOnAA + process.hltDoubleEle10EcalIsoPPOnAAFilter + process.HLTPFHcalClusteringForEgamma + process.hltEgammaHcalPFClusterIsoPPOnAA + process.hltDoubleEle10HcalIsoPPOnAAFilter + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripPPOnAAZeroSuppressionSequence + process.HLTPixelVertexingPPOnAASequence + process.HLTElectronPixelMatchingPPOnAASequence + process.HLTGsfElectronPPOnAASequence + process.HLTIterativeTrackingForElectrons + process.hltEgammaEleGsfTrackIsoPPOnAA + process.hltDoubleEle10GsfTrackIsoPPOnAAFilter )
process.HLTDoubleEle10GsfPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltDoubleEG10EtPPOnAAFilter + process.hltEgammaClusterShapePPOnAA + process.hltDoubleEle10ClusterShapePPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltDoubleEle10HoverEPPOnAAFilter + process.hltEgammaEcalPFClusterIsoPPOnAA + process.hltDoubleEle10EcalIsoPPOnAAFilter + process.HLTPFHcalClusteringForEgamma + process.hltEgammaHcalPFClusterIsoPPOnAA + process.hltDoubleEle10HcalIsoPPOnAAFilter + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripPPOnAAZeroSuppressionSequence + process.HLTPixelVertexingPPOnAASequence + process.HLTElectronPixelMatchingPPOnAASequence + process.HLTGsfElectronPPOnAASequence + process.HLTIterativeTrackingForElectrons + process.hltEgammaEleGsfTrackIsoPPOnAA + process.hltDoubleEle10GsfTrackIsoPPOnAAFilter )
process.HLTDoubleEle15GsfPPOnAASequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgammaPPOnAA + process.hltEgammaCandidatesPPOnAA + process.hltEgammaCandidatesWrapperPPOnAA + process.hltDoubleEG15EtPPOnAAFilter + process.hltEgammaClusterShapePPOnAA + process.hltDoubleEle15ClusterShapePPOnAAFilter + process.HLTDoLocalHcalWithTowerSequence + process.hltEgammaHoverEPPOnAA + process.hltDoubleEle15HoverEPPOnAAFilter + process.hltEgammaEcalPFClusterIsoPPOnAA + process.hltDoubleEle15EcalIsoPPOnAAFilter + process.HLTPFHcalClusteringForEgamma + process.hltEgammaHcalPFClusterIsoPPOnAA + process.hltDoubleEle15HcalIsoPPOnAAFilter + process.HLTDoLocalPixelSequencePPOnAA + process.HLTDoLocalStripPPOnAAZeroSuppressionSequence + process.HLTPixelVertexingPPOnAASequence + process.HLTElectronPixelMatchingPPOnAASequence + process.HLTGsfElectronPPOnAASequence + process.HLTIterativeTrackingForElectrons + process.hltEgammaEleGsfTrackIsoPPOnAA + process.hltDoubleEle15GsfTrackIsoPPOnAAFilter )

process.HLTAnalyzerEndpath = cms.EndPath( process.hltGtStage2Digis + process.hltPreHLTAnalyzerEndpath + process.hltL1TGlobalSummary + process.hltTrigReport )
process.HLT_HIGEDPhoton10_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIGEDPhoton10 + process.HLTHIGEDPhoton10PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIGEDPhoton15 + process.HLTHIGEDPhoton15PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIGEDPhoton20 + process.HLTHIGEDPhoton20PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton30 + process.HLTHIGEDPhoton30PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton40 + process.HLTHIGEDPhoton40PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton50 + process.HLTHIGEDPhoton50PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton60_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIGEDPhoton60 + process.HLTHIGEDPhoton60PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_L1EG3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton10 + process.HLTHIGEDPhoton10PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_L1EG3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton15 + process.HLTHIGEDPhoton15PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_L1EG3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton20 + process.HLTHIGEDPhoton20PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_L1EG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5BptxAND + process.hltPreHIGEDPhoton10 + process.HLTHIGEDPhoton10PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_L1EG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5BptxAND + process.hltPreHIGEDPhoton15 + process.HLTHIGEDPhoton15PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_L1EG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5BptxAND + process.hltPreHIGEDPhoton20 + process.HLTHIGEDPhoton20PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_L1EG7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton10 + process.HLTHIGEDPhoton10PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_L1EG7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton15 + process.HLTHIGEDPhoton15PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_L1EG7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton20 + process.HLTHIGEDPhoton20PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_L1EG12_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG12BptxAND + process.hltPreHIGEDPhoton20 + process.HLTHIGEDPhoton20PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_L1EG12_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG12BptxAND + process.hltPreHIGEDPhoton30 + process.HLTHIGEDPhoton30PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_L1EG15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG15BptxAND + process.hltPreHIGEDPhoton30 + process.HLTHIGEDPhoton30PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_L1EG21_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton30 + process.HLTHIGEDPhoton30PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_L1EG15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG15BptxAND + process.hltPreHIGEDPhoton40 + process.HLTHIGEDPhoton40PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_L1EG30_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIGEDPhoton40 + process.HLTHIGEDPhoton40PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton50_L1EG30_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIGEDPhoton50 + process.HLTHIGEDPhoton50PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton60_L1EG21_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton60 + process.HLTHIGEDPhoton60PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_EB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIGEDPhoton10EB + process.HLTHIGEDPhoton10EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_EB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIGEDPhoton15EB + process.HLTHIGEDPhoton15EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_EB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIGEDPhoton20EB + process.HLTHIGEDPhoton20EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_EB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton30EB + process.HLTHIGEDPhoton30EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_EB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton40EB + process.HLTHIGEDPhoton40EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton50_EB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton50EB + process.HLTHIGEDPhoton50EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton60_EB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIGEDPhoton60EB + process.HLTHIGEDPhoton60EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_EB_L1EG3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton10EB + process.HLTHIGEDPhoton10EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_EB_L1EG3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton15EB + process.HLTHIGEDPhoton15EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_EB_L1EG3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton20EB + process.HLTHIGEDPhoton20EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_EB_L1EG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5BptxAND + process.hltPreHIGEDPhoton10EB + process.HLTHIGEDPhoton10EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_EB_L1EG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5BptxAND + process.hltPreHIGEDPhoton15EB + process.HLTHIGEDPhoton15EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_EB_L1EG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5BptxAND + process.hltPreHIGEDPhoton20EB + process.HLTHIGEDPhoton20EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_EB_L1EG7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton10EB + process.HLTHIGEDPhoton10EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_EB_L1EG7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton15EB + process.HLTHIGEDPhoton15EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_EB_L1EG7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton20EB + process.HLTHIGEDPhoton20EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_EB_L1EG12_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG12BptxAND + process.hltPreHIGEDPhoton20EB + process.HLTHIGEDPhoton20EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_EB_L1EG12_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG12BptxAND + process.hltPreHIGEDPhoton30EB + process.HLTHIGEDPhoton30EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_EB_L1EG15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG15BptxAND + process.hltPreHIGEDPhoton30EB + process.HLTHIGEDPhoton30EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_EB_L1EG21_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton30EB + process.HLTHIGEDPhoton30EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_EB_L1EG15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG15BptxAND + process.hltPreHIGEDPhoton40EB + process.HLTHIGEDPhoton40EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_EB_L1EG30_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIGEDPhoton40EB + process.HLTHIGEDPhoton40EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton50_EB_L1EG30_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIGEDPhoton50EB + process.HLTHIGEDPhoton50EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton60_EB_L1EG21_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton60EB + process.HLTHIGEDPhoton60EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIGEDPhoton10HECut + process.HLTHIGEDPhoton10HECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIGEDPhoton15HECut + process.HLTHIGEDPhoton15HECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIGEDPhoton20HECut + process.HLTHIGEDPhoton20HECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton30HECut + process.HLTHIGEDPhoton30HECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton40HECut + process.HLTHIGEDPhoton40HECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton50_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton50HECut + process.HLTHIGEDPhoton50HECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton60_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIGEDPhoton60HECut + process.HLTHIGEDPhoton60HECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_EB_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIGEDPhoton10EBHECut + process.HLTHIGEDPhoton10EBHECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_EB_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIGEDPhoton15EBHECut + process.HLTHIGEDPhoton15EBHECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_EB_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIGEDPhoton20EBHECut + process.HLTHIGEDPhoton20EBHECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_EB_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton30EBHECut + process.HLTHIGEDPhoton30EBHECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_EB_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton40EBHECut + process.HLTHIGEDPhoton40EBHECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton50_EB_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton50EBHECut + process.HLTHIGEDPhoton50EBHECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton60_EB_HECut_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIGEDPhoton60EBHECut + process.HLTHIGEDPhoton60EBHECutPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton10 + process.HLTHIGEDPhoton10PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton15 + process.HLTHIGEDPhoton15PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton20 + process.HLTHIGEDPhoton20PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton30 + process.HLTHIGEDPhoton30PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton40 + process.HLTHIGEDPhoton40PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton50_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton50 + process.HLTHIGEDPhoton50PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton60_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton60 + process.HLTHIGEDPhoton60PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_EB_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton10EB + process.HLTHIGEDPhoton10EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_EB_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton15EB + process.HLTHIGEDPhoton15EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_EB_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton20EB + process.HLTHIGEDPhoton20EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_EB_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton30EB + process.HLTHIGEDPhoton30EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_EB_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton40EB + process.HLTHIGEDPhoton40EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton50_EB_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton50EB + process.HLTHIGEDPhoton50EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton60_EB_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIGEDPhoton60EB + process.HLTHIGEDPhoton60EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton10L1Seeded + process.HLTHIGEDPhoton10L1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton15L1Seeded + process.HLTHIGEDPhoton15L1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton20L1Seeded + process.HLTHIGEDPhoton20L1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton30L1Seeded + process.HLTHIGEDPhoton30L1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton40L1Seeded + process.HLTHIGEDPhoton40L1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton50_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton50L1Seeded + process.HLTHIGEDPhoton50L1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton60_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIGEDPhoton60L1Seeded + process.HLTHIGEDPhoton60L1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_EB_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton10EBL1Seeded + process.HLTHIGEDPhoton10EBL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_EB_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton15EBL1Seeded + process.HLTHIGEDPhoton15EBL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_EB_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton20EBL1Seeded + process.HLTHIGEDPhoton20EBL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_EB_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton30EBL1Seeded + process.HLTHIGEDPhoton30EBL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_EB_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton40EBL1Seeded + process.HLTHIGEDPhoton40EBL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton50_EB_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton50EBL1Seeded + process.HLTHIGEDPhoton50EBL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton60_EB_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIGEDPhoton60EBL1Seeded + process.HLTHIGEDPhoton60EBL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton10HECutL1Seeded + process.HLTHIGEDPhoton10HECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton15HECutL1Seeded + process.HLTHIGEDPhoton15HECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton20HECutL1Seeded + process.HLTHIGEDPhoton20HECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton30HECutL1Seeded + process.HLTHIGEDPhoton30HECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton40HECutL1Seeded + process.HLTHIGEDPhoton40HECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton50_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton50HECutL1Seeded + process.HLTHIGEDPhoton50HECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton60_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIGEDPhoton60HECutL1Seeded + process.HLTHIGEDPhoton60HECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_EB_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton10EBHECutL1Seeded + process.HLTHIGEDPhoton10EBHECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_EB_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton15EBHECutL1Seeded + process.HLTHIGEDPhoton15EBHECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_EB_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIGEDPhoton20EBHECutL1Seeded + process.HLTHIGEDPhoton20EBHECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_EB_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIGEDPhoton30EBHECutL1Seeded + process.HLTHIGEDPhoton30EBHECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_EB_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton40EBHECutL1Seeded + process.HLTHIGEDPhoton40EBHECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton50_EB_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIGEDPhoton50EBHECutL1Seeded + process.HLTHIGEDPhoton50EBHECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton60_EB_HECut_L1Seeded_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIGEDPhoton60EBHECutL1Seeded + process.HLTHIGEDPhoton60EBHECutL1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta3p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIIslandPhoton10Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta1p5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIIslandPhoton10Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta3p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIIslandPhoton15Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta1p5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIIslandPhoton15Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta3p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIIslandPhoton20Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta1p5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIIslandPhoton20Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta3p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIIslandPhoton30Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta1p5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIIslandPhoton30Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton40_Eta3p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIIslandPhoton40Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton40Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton40_Eta1p5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIIslandPhoton40Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton40Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton50_Eta3p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIIslandPhoton50Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton50Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton50_Eta1p5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIIslandPhoton50Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton50Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton60_Eta3p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIIslandPhoton60Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton60Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton60_Eta1p5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIIslandPhoton60Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton60Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta3p1_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton10Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta1p5_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton10Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta3p1_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton15Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta1p5_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton15Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta3p1_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton20Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta1p5_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton20Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta3p1_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton30Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta1p5_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton30Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton40_Eta3p1_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton40Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton40Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton40_Eta1p5_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton40Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton40Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton50_Eta3p1_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton50Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton50Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton50_Eta1p5_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton50Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton50Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton60_Eta3p1_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton60Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton60Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton60_Eta1p5_L1ZB_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreHIIslandPhoton60Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton60Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta3p1_L1EG12_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG12BptxAND + process.hltPreHIIslandPhoton20Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta1p5_L1EG12_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG12BptxAND + process.hltPreHIIslandPhoton20Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta3p1_L1EG7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIIslandPhoton10Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta1p5_L1EG7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIIslandPhoton10Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta3p1_L1EG7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIIslandPhoton15Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta1p5_L1EG7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIIslandPhoton15Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta3p1_L1EG7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIIslandPhoton20Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta1p5_L1EG7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIIslandPhoton20Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta3p1_L1EG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5BptxAND + process.hltPreHIIslandPhoton10Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta1p5_L1EG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5BptxAND + process.hltPreHIIslandPhoton10Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta3p1_L1EG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5BptxAND + process.hltPreHIIslandPhoton15Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta1p5_L1EG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5BptxAND + process.hltPreHIIslandPhoton15Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta3p1_L1EG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5BptxAND + process.hltPreHIIslandPhoton20Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta1p5_L1EG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5BptxAND + process.hltPreHIIslandPhoton20Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta3p1_L1EG3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIIslandPhoton10Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta1p5_L1EG3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIIslandPhoton10Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta3p1_L1EG3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIIslandPhoton15Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta1p5_L1EG3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIIslandPhoton15Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta3p1_L1EG3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIIslandPhoton20Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta1p5_L1EG3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3BptxAND + process.hltPreHIIslandPhoton20Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta3p1_L1EG12_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG12BptxAND + process.hltPreHIIslandPhoton30Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta1p5_L1EG12_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG12BptxAND + process.hltPreHIIslandPhoton30Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta3p1_L1EG15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG15BptxAND + process.hltPreHIIslandPhoton30Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta1p5_L1EG15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG15BptxAND + process.hltPreHIIslandPhoton30Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta3p1_L1EG21_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIIslandPhoton30Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta1p5_L1EG21_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIIslandPhoton30Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton40_Eta3p1_L1EG15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG15BptxAND + process.hltPreHIIslandPhoton40Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton40Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton40_Eta1p5_L1EG15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG15BptxAND + process.hltPreHIIslandPhoton40Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton40Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton40_Eta3p1_L1EG30_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIIslandPhoton40Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton40Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton40_Eta1p5_L1EG30_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIIslandPhoton40Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton40Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton50_Eta3p1_L1EG30_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIIslandPhoton50Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton50Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton50_Eta1p5_L1EG30_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG30BptxAND + process.hltPreHIIslandPhoton50Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton50Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton60_Eta3p1_L1EG21_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIIslandPhoton60Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton60Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton60_Eta1p5_L1EG21_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIIslandPhoton60Eta1p5 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton60Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_ZeroBias_v6 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreZeroBias + process.HLTEndSequenceWithZeroSuppression )
process.HLTriggerFinalPath = cms.Path( process.hltGtStage2Digis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolFalse )
process.HLTriggerFirstPath = cms.Path( process.hltGetConditions + process.hltGetRaw + process.hltBoolFalse )
process.HLT_HIIslandPhoton10_Eta3p1_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent30100BptxAND + process.hltPreHIIslandPhoton10Eta3p1Cent30100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta1p5_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent30100BptxAND + process.hltPreHIIslandPhoton10Eta1p5Cent30100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta3p1_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent30100BptxAND + process.hltPreHIIslandPhoton15Eta3p1Cent30100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta1p5_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent30100BptxAND + process.hltPreHIIslandPhoton15Eta1p5Cent30100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta3p1_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent30100BptxAND + process.hltPreHIIslandPhoton20Eta3p1Cent30100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta1p5_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent30100BptxAND + process.hltPreHIIslandPhoton20Eta1p5Cent30100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta3p1_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7Cent30100BptxAND + process.hltPreHIIslandPhoton30Eta3p1Cent30100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta1p5_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7Cent30100BptxAND + process.hltPreHIIslandPhoton30Eta1p5Cent30100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton40_Eta3p1_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21Cent30100BptxAND + process.hltPreHIIslandPhoton40Eta3p1Cent30100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton40Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton40_Eta1p5_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21Cent30100BptxAND + process.hltPreHIIslandPhoton40Eta1p5Cent30100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton40Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta3p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent50100BptxAND + process.hltPreHIIslandPhoton10Eta3p1Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton10_Eta1p5_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent50100BptxAND + process.hltPreHIIslandPhoton10Eta1p5Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton10Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta3p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent50100BptxAND + process.hltPreHIIslandPhoton15Eta3p1Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton15_Eta1p5_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent50100BptxAND + process.hltPreHIIslandPhoton15Eta1p5Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton15Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta3p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent50100BptxAND + process.hltPreHIIslandPhoton20Eta3p1Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton20_Eta1p5_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent50100BptxAND + process.hltPreHIIslandPhoton20Eta1p5Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton20Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta3p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7Cent50100BptxAND + process.hltPreHIIslandPhoton30Eta3p1Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton30_Eta1p5_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7Cent50100BptxAND + process.hltPreHIIslandPhoton30Eta1p5Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton40_Eta3p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21Cent50100BptxAND + process.hltPreHIIslandPhoton40Eta3p1Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton40Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIIslandPhoton40_Eta1p5_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21Cent50100BptxAND + process.hltPreHIIslandPhoton40Eta1p5Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton40Eta1p5 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent30100BptxAND + process.hltPreHIGEDPhoton10Cent30100 + process.HLTHIGEDPhoton10PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent30100BptxAND + process.hltPreHIGEDPhoton15Cent30100 + process.HLTHIGEDPhoton15PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent30100BptxAND + process.hltPreHIGEDPhoton20Cent30100 + process.HLTHIGEDPhoton20PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7Cent30100BptxAND + process.hltPreHIGEDPhoton30Cent30100 + process.HLTHIGEDPhoton30PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21Cent30100BptxAND + process.hltPreHIGEDPhoton40Cent30100 + process.HLTHIGEDPhoton40PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent50100BptxAND + process.hltPreHIGEDPhoton10Cent50100 + process.HLTHIGEDPhoton10PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent50100BptxAND + process.hltPreHIGEDPhoton15Cent50100 + process.HLTHIGEDPhoton15PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent50100BptxAND + process.hltPreHIGEDPhoton20Cent50100 + process.HLTHIGEDPhoton20PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7Cent50100BptxAND + process.hltPreHIGEDPhoton30Cent50100 + process.HLTHIGEDPhoton30PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21Cent50100BptxAND + process.hltPreHIGEDPhoton40Cent50100 + process.HLTHIGEDPhoton40PPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_EB_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent30100BptxAND + process.hltPreHIGEDPhoton10EBCent30100 + process.HLTHIGEDPhoton10EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_EB_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent30100BptxAND + process.hltPreHIGEDPhoton15EBCent30100 + process.HLTHIGEDPhoton15EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_EB_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent30100BptxAND + process.hltPreHIGEDPhoton20EBCent30100 + process.HLTHIGEDPhoton20EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_EB_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7Cent30100BptxAND + process.hltPreHIGEDPhoton30EBCent30100 + process.HLTHIGEDPhoton30EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_EB_Cent30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21Cent30100BptxAND + process.hltPreHIGEDPhoton40EBCent30100 + process.HLTHIGEDPhoton40EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton10_EB_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent50100BptxAND + process.hltPreHIGEDPhoton10EBCent50100 + process.HLTHIGEDPhoton10EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton15_EB_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent50100BptxAND + process.hltPreHIGEDPhoton15EBCent50100 + process.HLTHIGEDPhoton15EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton20_EB_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG3Cent50100BptxAND + process.hltPreHIGEDPhoton20EBCent50100 + process.HLTHIGEDPhoton20EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton30_EB_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7Cent50100BptxAND + process.hltPreHIGEDPhoton30EBCent50100 + process.HLTHIGEDPhoton30EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIGEDPhoton40_EB_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21Cent50100BptxAND + process.hltPreHIGEDPhoton40EBCent50100 + process.HLTHIGEDPhoton40EBPPOnAASequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_HIPuAK4CaloJet40Eta5p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet28BptxAND + process.hltPreHIPuAK4CaloJet40Eta5p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet40Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet60Eta5p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet44BptxAND + process.hltPreHIPuAK4CaloJet60Eta5p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet60Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet80Eta5p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56BptxAND + process.hltPreHIPuAK4CaloJet80Eta5p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet100Eta5p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet60BptxAND + process.hltPreHIPuAK4CaloJet100Eta5p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet120Eta5p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet60BptxAND + process.hltPreHIPuAK4CaloJet120Eta5p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet120Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet80_35_Eta1p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56BptxAND + process.hltPreHIPuAK4CaloJet8035Eta1p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta1p1 + process.hltDoublePuAK4CaloJet35Eta1p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet100_35_Eta1p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56BptxAND + process.hltPreHIPuAK4CaloJet10035Eta1p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Eta1p1 + process.hltDoublePuAK4CaloJet35Eta1p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet80_35_Eta0p7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56BptxAND + process.hltPreHIPuAK4CaloJet8035Eta0p7 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta0p7 + process.hltDoublePuAK4CaloJet35Eta0p7 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet100_35_Eta0p7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56BptxAND + process.hltPreHIPuAK4CaloJet10035Eta0p7 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Eta0p7 + process.hltDoublePuAK4CaloJet35Eta0p7 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet80_45_45_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56BptxAND + process.hltPreHIPuAK4CaloJet804545Eta2p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta2p1 + process.hltTriplePuAK4CaloJet45Eta2p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet40Fwd_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet28FwdBptxAND + process.hltPreHIPuAK4CaloJet40Fwd + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet40Fwd + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet60Fwd_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet44FwdBptxAND + process.hltPreHIPuAK4CaloJet60Fwd + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet60Fwd + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet80Fwd_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56FwdBptxAND + process.hltPreHIPuAK4CaloJet80Fwd + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Fwd + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet100Fwd_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56FwdBptxAND + process.hltPreHIPuAK4CaloJet100Fwd + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Fwd + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet120Fwd_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56FwdBptxAND + process.hltPreHIPuAK4CaloJet120Fwd + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet120Fwd + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet60Eta2p4_DeepCSV0p71_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet44BptxAND + process.hltPreHIPuAK4CaloJet60Eta2p4DeepCSV0p71 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet60Eta2p4 + process.hltSelectorJets60 + process.hltSelectorCentralJets60 + process.hltSelector4CentralJetsPtCut + process.hltSelectorCentralJets + process.hltSelector4CentralJets + process.HLTBtagDeepCSVSequenceL3ForHI + process.hltBTagCaloDeepCSV0p71SingleJet60 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet80Eta2p4_DeepCSV0p71_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56BptxAND + process.hltPreHIPuAK4CaloJet80Eta2p4DeepCSV0p71 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta2p4 + process.hltSelectorJets80 + process.hltSelectorCentralJets80 + process.hltSelector4CentralJetsPtCut80 + process.hltSelectorJets60 + process.hltSelectorCentralJets60 + process.hltSelector4CentralJetsPtCut + process.hltSelectorCentralJets + process.hltSelector4CentralJets + process.HLTBtagDeepCSVSequenceL3ForHIBJet80 + process.hltBTagCaloDeepCSV0p71SingleJet80 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet100Eta2p4_DeepCSV0p71_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet60BptxAND + process.hltPreHIPuAK4CaloJet100Eta2p4DeepCSV0p71 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Eta2p4 + process.hltSelectorJets100 + process.hltSelectorCentralJets100 + process.hltSelector4CentralJetsPtCut100 + process.hltSelectorJets60 + process.hltSelectorCentralJets60 + process.hltSelector4CentralJetsPtCut + process.hltSelectorCentralJets + process.hltSelector4CentralJets + process.HLTBtagDeepCSVSequenceL3ForHIBJet100 + process.hltBTagCaloDeepCSV0p71SingleJet100 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet60Eta2p4_CSVv2WP0p8_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet44BptxAND + process.hltPreHIPuAK4CaloJet60Eta2p4CSVv2WP0p8 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet60Eta2p4 + process.hltSelectorJets60 + process.hltSelectorCentralJets60 + process.hltSelector4CentralJetsPtCut + process.hltSelectorCentralJets + process.hltSelector4CentralJets + process.HLTBtagCSVv2SequenceL3ForHI + process.hltBTagCaloCSVv2WP0p8SingleJet60HI + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet80Eta2p4_CSVv2WP0p8_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56BptxAND + process.hltPreHIPuAK4CaloJet80Eta2p4CSVv2WP0p8 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta2p4 + process.hltSelectorJets80 + process.hltSelectorCentralJets80 + process.hltSelector4CentralJetsPtCut80 + process.hltSelectorJets60 + process.hltSelectorCentralJets60 + process.hltSelector4CentralJetsPtCut + process.hltSelectorCentralJets + process.hltSelector4CentralJets + process.HLTBtagCSVv2SequenceL3ForHIBJet80 + process.hltBTagCaloCSVv2WP0p8SingleJet80HI + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet100Eta2p4_CSVv2WP0p8_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet60BptxAND + process.hltPreHIPuAK4CaloJet100Eta2p4CSVv2WP0p8 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Eta2p4 + process.hltSelectorJets100 + process.hltSelectorCentralJets100 + process.hltSelector4CentralJetsPtCut100 + process.hltSelectorJets60 + process.hltSelectorCentralJets60 + process.hltSelector4CentralJetsPtCut + process.hltSelectorCentralJets + process.hltSelector4CentralJets + process.HLTBtagCSVv2SequenceL3ForHIBJet100 + process.hltBTagCaloCSVv2WP0p8SingleJet100HI + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet40Eta5p1_Centrality_30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet28Centrality30100BptxAND + process.hltPreHIPuAK4CaloJet40Eta5p1Centrality30100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet40Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet60Eta5p1_Centrality_30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet44Centrality30100BptxAND + process.hltPreHIPuAK4CaloJet60Eta5p1Centrality30100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet60Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet80Eta5p1_Centrality_30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56Centrality30100BptxAND + process.hltPreHIPuAK4CaloJet80Eta5p1Centrality30100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet100Eta5p1_Centrality_30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet60Centrality30100BptxAND + process.hltPreHIPuAK4CaloJet100Eta5p1Centrality30100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet40Eta5p1_Centrality_50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet28Centrality50100BptxAND + process.hltPreHIPuAK4CaloJet40Eta5p1Centrality50100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet40Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet60Eta5p1_Centrality_50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet44Centrality50100BptxAND + process.hltPreHIPuAK4CaloJet60Eta5p1Centrality50100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet60Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet80Eta5p1_Centrality_50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56Centrality50100BptxAND + process.hltPreHIPuAK4CaloJet80Eta5p1Centrality50100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HIPuAK4CaloJet100Eta5p1_Centrality_50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet60Centrality50100BptxAND + process.hltPreHLTHIPuAK4CaloJet100Eta5p1Centrality50100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Eta5p1 + process.HLTDoHIStripZeroSuppression + process.HLTEndSequence )
process.HLT_HICsAK4PFJet60Eta1p5_Centrality_30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet44Centrality30100BptxAND + process.hltPreHICsAK4PFJet60Eta1p5Centrality30100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet60Eta1p5 + process.HLTCsAK4PFJetsSequence + process.hltCsPFJetsCorrectedMatchedToPuCaloJets60 + process.hltSingleCsPFJet60Eta1p5 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HICsAK4PFJet80Eta1p5_Centrality_30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56Centrality30100BptxAND + process.hltPreHICsAK4PFJet80Eta1p5Centrality30100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet70Eta1p5 + process.HLTCsAK4PFJetsSequence + process.hltCsPFJetsCorrectedMatchedToPuCaloJets70 + process.hltSingleCsPFJet80Eta1p5 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HICsAK4PFJet100Eta1p5_Centrality_30_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet60Centrality30100BptxAND + process.hltPreHICsAK4PFJet100Eta1p5Centrality30100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta1p5 + process.HLTCsAK4PFJetsSequence + process.hltCsPFJetsCorrectedMatchedToPuCaloJets80 + process.hltSingleCsPFJet100Eta1p5 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HICsAK4PFJet60Eta1p5_Centrality_50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet44Centrality50100BptxAND + process.hltPreHICsAK4PFJet60Eta1p5Centrality50100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet60Eta1p5 + process.HLTCsAK4PFJetsSequence + process.hltCsPFJetsCorrectedMatchedToPuCaloJets60 + process.hltSingleCsPFJet60Eta1p5 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HICsAK4PFJet80Eta1p5_Centrality_50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56Centrality50100BptxAND + process.hltPreHICsAK4PFJet80Eta1p5Centrality50100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet70Eta1p5 + process.HLTCsAK4PFJetsSequence + process.hltCsPFJetsCorrectedMatchedToPuCaloJets70 + process.hltSingleCsPFJet80Eta1p5 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HICsAK4PFJet100Eta1p5_Centrality_50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet60Centrality50100BptxAND + process.hltPreHICsAK4PFJet100Eta1p5Centrality50100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta1p5 + process.HLTCsAK4PFJetsSequence + process.hltCsPFJetsCorrectedMatchedToPuCaloJets80 + process.hltSingleCsPFJet100Eta1p5 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HICsAK4PFJet60Eta1p5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet44BptxAND + process.hltPreHICsAK4PFJet60Eta1p5 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet60Eta1p5 + process.HLTCsAK4PFJetsSequence + process.hltCsPFJetsCorrectedMatchedToPuCaloJets60 + process.hltSingleCsPFJet60Eta1p5 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HICsAK4PFJet80Eta1p5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet56BptxAND + process.hltPreHICsAK4PFJet80Eta1p5 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet70Eta1p5 + process.HLTCsAK4PFJetsSequence + process.hltCsPFJetsCorrectedMatchedToPuCaloJets70 + process.hltSingleCsPFJet80Eta1p5 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HICsAK4PFJet100Eta1p5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet60BptxAND + process.hltPreHICsAK4PFJet100Eta1p5 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta1p5 + process.HLTCsAK4PFJetsSequence + process.hltCsPFJetsCorrectedMatchedToPuCaloJets80 + process.hltSingleCsPFJet100Eta1p5 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HICsAK4PFJet120Eta1p5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleJet60BptxAND + process.hltPreHICsAK4PFJet120Eta1p5 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet90Eta1p5 + process.HLTCsAK4PFJetsSequence + process.hltCsPFJetsCorrectedMatchedToPuCaloJets90 + process.hltSingleCsPFJet120Eta1p5 + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIEle10Gsf_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIEle10Gsf + process.HLTEle10GsfPPOnAASequence + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIEle15Gsf_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIEle15Gsf + process.HLTEle15GsfPPOnAASequence + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIEle20Gsf_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIEle20Gsf + process.HLTEle20GsfPPOnAASequence + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIEle30Gsf_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG7BptxAND + process.hltPreHIEle30Gsf + process.HLTEle30GsfPPOnAASequence + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIEle40Gsf_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIEle40Gsf + process.HLTEle40GsfPPOnAASequence + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIEle50Gsf_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG21BptxAND + process.hltPreHIEle50Gsf + process.HLTEle50GsfPPOnAASequence + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIEle15Ele10Gsf_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIEle15Ele10Gsf + process.HLTEle15Ele10GsfPPOnAASequence + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIEle15Ele10GsfMass50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIEle15Ele10GsfMass50 + process.HLTEle15Ele10GsfPPOnAASequence + process.hltDoubleEle10Mass50PPOnAAFilter + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIDoubleEle10Gsf_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIDoubleEle10Gsf + process.HLTDoubleEle10GsfPPOnAASequence + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIDoubleEle10GsfMass50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIDoubleEle10GsfMass50 + process.HLTDoubleEle10GsfPPOnAASequence + process.hltDoubleEle10Mass50PPOnAAFilter + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIDoubleEle15Gsf_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIDoubleEle15Gsf + process.HLTDoubleEle15GsfPPOnAASequence + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )
process.HLT_HIDoubleEle15GsfMass50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sMinimumBiasHF1ANDBptxAND + process.hltPreHIDoubleEle15GsfMass50 + process.HLTDoubleEle15GsfPPOnAASequence + process.hltDoubleEle15Mass50PPOnAAFilter + process.HLTDoHIStripZeroSuppressionRepacker + process.HLTEndSequence )


process.HLTSchedule = cms.Schedule( *(process.HLTAnalyzerEndpath, process.HLT_HIGEDPhoton10_v1, process.HLT_HIGEDPhoton15_v1, process.HLT_HIGEDPhoton20_v1, process.HLT_HIGEDPhoton30_v1, process.HLT_HIGEDPhoton40_v1, process.HLT_HIGEDPhoton50_v1, process.HLT_HIGEDPhoton60_v1, process.HLT_HIGEDPhoton10_L1EG3_v1, process.HLT_HIGEDPhoton15_L1EG3_v1, process.HLT_HIGEDPhoton20_L1EG3_v1, process.HLT_HIGEDPhoton10_L1EG5_v1, process.HLT_HIGEDPhoton15_L1EG5_v1, process.HLT_HIGEDPhoton20_L1EG5_v1, process.HLT_HIGEDPhoton10_L1EG7_v1, process.HLT_HIGEDPhoton15_L1EG7_v1, process.HLT_HIGEDPhoton20_L1EG7_v1, process.HLT_HIGEDPhoton20_L1EG12_v1, process.HLT_HIGEDPhoton30_L1EG12_v1, process.HLT_HIGEDPhoton30_L1EG15_v1, process.HLT_HIGEDPhoton30_L1EG21_v1, process.HLT_HIGEDPhoton40_L1EG15_v1, process.HLT_HIGEDPhoton40_L1EG30_v1, process.HLT_HIGEDPhoton50_L1EG30_v1, process.HLT_HIGEDPhoton60_L1EG21_v1, process.HLT_HIGEDPhoton10_EB_v1, process.HLT_HIGEDPhoton15_EB_v1, process.HLT_HIGEDPhoton20_EB_v1, process.HLT_HIGEDPhoton30_EB_v1, process.HLT_HIGEDPhoton40_EB_v1, process.HLT_HIGEDPhoton50_EB_v1, process.HLT_HIGEDPhoton60_EB_v1, process.HLT_HIGEDPhoton10_EB_L1EG3_v1, process.HLT_HIGEDPhoton15_EB_L1EG3_v1, process.HLT_HIGEDPhoton20_EB_L1EG3_v1, process.HLT_HIGEDPhoton10_EB_L1EG5_v1, process.HLT_HIGEDPhoton15_EB_L1EG5_v1, process.HLT_HIGEDPhoton20_EB_L1EG5_v1, process.HLT_HIGEDPhoton10_EB_L1EG7_v1, process.HLT_HIGEDPhoton15_EB_L1EG7_v1, process.HLT_HIGEDPhoton20_EB_L1EG7_v1, process.HLT_HIGEDPhoton20_EB_L1EG12_v1, process.HLT_HIGEDPhoton30_EB_L1EG12_v1, process.HLT_HIGEDPhoton30_EB_L1EG15_v1, process.HLT_HIGEDPhoton30_EB_L1EG21_v1, process.HLT_HIGEDPhoton40_EB_L1EG15_v1, process.HLT_HIGEDPhoton40_EB_L1EG30_v1, process.HLT_HIGEDPhoton50_EB_L1EG30_v1, process.HLT_HIGEDPhoton60_EB_L1EG21_v1, process.HLT_HIGEDPhoton10_HECut_v1, process.HLT_HIGEDPhoton15_HECut_v1, process.HLT_HIGEDPhoton20_HECut_v1, process.HLT_HIGEDPhoton30_HECut_v1, process.HLT_HIGEDPhoton40_HECut_v1, process.HLT_HIGEDPhoton50_HECut_v1, process.HLT_HIGEDPhoton60_HECut_v1, process.HLT_HIGEDPhoton10_EB_HECut_v1, process.HLT_HIGEDPhoton15_EB_HECut_v1, process.HLT_HIGEDPhoton20_EB_HECut_v1, process.HLT_HIGEDPhoton30_EB_HECut_v1, process.HLT_HIGEDPhoton40_EB_HECut_v1, process.HLT_HIGEDPhoton50_EB_HECut_v1, process.HLT_HIGEDPhoton60_EB_HECut_v1, process.HLT_HIGEDPhoton10_L1ZB_v1, process.HLT_HIGEDPhoton15_L1ZB_v1, process.HLT_HIGEDPhoton20_L1ZB_v1, process.HLT_HIGEDPhoton30_L1ZB_v1, process.HLT_HIGEDPhoton40_L1ZB_v1, process.HLT_HIGEDPhoton50_L1ZB_v1, process.HLT_HIGEDPhoton60_L1ZB_v1, process.HLT_HIGEDPhoton10_EB_L1ZB_v1, process.HLT_HIGEDPhoton15_EB_L1ZB_v1, process.HLT_HIGEDPhoton20_EB_L1ZB_v1, process.HLT_HIGEDPhoton30_EB_L1ZB_v1, process.HLT_HIGEDPhoton40_EB_L1ZB_v1, process.HLT_HIGEDPhoton50_EB_L1ZB_v1, process.HLT_HIGEDPhoton60_EB_L1ZB_v1, process.HLT_HIGEDPhoton10_L1Seeded_v1, process.HLT_HIGEDPhoton15_L1Seeded_v1, process.HLT_HIGEDPhoton20_L1Seeded_v1, process.HLT_HIGEDPhoton30_L1Seeded_v1, process.HLT_HIGEDPhoton40_L1Seeded_v1, process.HLT_HIGEDPhoton50_L1Seeded_v1, process.HLT_HIGEDPhoton60_L1Seeded_v1, process.HLT_HIGEDPhoton10_EB_L1Seeded_v1, process.HLT_HIGEDPhoton15_EB_L1Seeded_v1, process.HLT_HIGEDPhoton20_EB_L1Seeded_v1, process.HLT_HIGEDPhoton30_EB_L1Seeded_v1, process.HLT_HIGEDPhoton40_EB_L1Seeded_v1, process.HLT_HIGEDPhoton50_EB_L1Seeded_v1, process.HLT_HIGEDPhoton60_EB_L1Seeded_v1, process.HLT_HIGEDPhoton10_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton15_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton20_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton30_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton40_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton50_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton60_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton10_EB_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton15_EB_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton20_EB_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton30_EB_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton40_EB_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton50_EB_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton60_EB_HECut_L1Seeded_v1, process.HLT_HIIslandPhoton10_Eta3p1_v1, process.HLT_HIIslandPhoton10_Eta1p5_v1, process.HLT_HIIslandPhoton15_Eta3p1_v1, process.HLT_HIIslandPhoton15_Eta1p5_v1, process.HLT_HIIslandPhoton20_Eta3p1_v1, process.HLT_HIIslandPhoton20_Eta1p5_v1, process.HLT_HIIslandPhoton30_Eta3p1_v1, process.HLT_HIIslandPhoton30_Eta1p5_v1, process.HLT_HIIslandPhoton40_Eta3p1_v1, process.HLT_HIIslandPhoton40_Eta1p5_v1, process.HLT_HIIslandPhoton50_Eta3p1_v1, process.HLT_HIIslandPhoton50_Eta1p5_v1, process.HLT_HIIslandPhoton60_Eta3p1_v1, process.HLT_HIIslandPhoton60_Eta1p5_v1, process.HLT_HIIslandPhoton10_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton10_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton15_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton15_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton20_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton20_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton30_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton30_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton40_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton40_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton50_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton50_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton60_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton60_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton20_Eta3p1_L1EG12_v1, process.HLT_HIIslandPhoton20_Eta1p5_L1EG12_v1, process.HLT_HIIslandPhoton10_Eta3p1_L1EG7_v1, process.HLT_HIIslandPhoton10_Eta1p5_L1EG7_v1, process.HLT_HIIslandPhoton15_Eta3p1_L1EG7_v1, process.HLT_HIIslandPhoton15_Eta1p5_L1EG7_v1, process.HLT_HIIslandPhoton20_Eta3p1_L1EG7_v1, process.HLT_HIIslandPhoton20_Eta1p5_L1EG7_v1, process.HLT_HIIslandPhoton10_Eta3p1_L1EG5_v1, process.HLT_HIIslandPhoton10_Eta1p5_L1EG5_v1, process.HLT_HIIslandPhoton15_Eta3p1_L1EG5_v1, process.HLT_HIIslandPhoton15_Eta1p5_L1EG5_v1, process.HLT_HIIslandPhoton20_Eta3p1_L1EG5_v1, process.HLT_HIIslandPhoton20_Eta1p5_L1EG5_v1, process.HLT_HIIslandPhoton10_Eta3p1_L1EG3_v1, process.HLT_HIIslandPhoton10_Eta1p5_L1EG3_v1, process.HLT_HIIslandPhoton15_Eta3p1_L1EG3_v1, process.HLT_HIIslandPhoton15_Eta1p5_L1EG3_v1, process.HLT_HIIslandPhoton20_Eta3p1_L1EG3_v1, process.HLT_HIIslandPhoton20_Eta1p5_L1EG3_v1, process.HLT_HIIslandPhoton30_Eta3p1_L1EG12_v1, process.HLT_HIIslandPhoton30_Eta1p5_L1EG12_v1, process.HLT_HIIslandPhoton30_Eta3p1_L1EG15_v1, process.HLT_HIIslandPhoton30_Eta1p5_L1EG15_v1, process.HLT_HIIslandPhoton30_Eta3p1_L1EG21_v1, process.HLT_HIIslandPhoton30_Eta1p5_L1EG21_v1, process.HLT_HIIslandPhoton40_Eta3p1_L1EG15_v1, process.HLT_HIIslandPhoton40_Eta1p5_L1EG15_v1, process.HLT_HIIslandPhoton40_Eta3p1_L1EG30_v1, process.HLT_HIIslandPhoton40_Eta1p5_L1EG30_v1, process.HLT_HIIslandPhoton50_Eta3p1_L1EG30_v1, process.HLT_HIIslandPhoton50_Eta1p5_L1EG30_v1, process.HLT_HIIslandPhoton60_Eta3p1_L1EG21_v1, process.HLT_HIIslandPhoton60_Eta1p5_L1EG21_v1, process.HLT_ZeroBias_v6, process.HLTriggerFinalPath, process.HLTriggerFirstPath, process.HLT_HIIslandPhoton10_Eta3p1_Cent30_100_v1, process.HLT_HIIslandPhoton10_Eta1p5_Cent30_100_v1, process.HLT_HIIslandPhoton15_Eta3p1_Cent30_100_v1, process.HLT_HIIslandPhoton15_Eta1p5_Cent30_100_v1, process.HLT_HIIslandPhoton20_Eta3p1_Cent30_100_v1, process.HLT_HIIslandPhoton20_Eta1p5_Cent30_100_v1, process.HLT_HIIslandPhoton30_Eta3p1_Cent30_100_v1, process.HLT_HIIslandPhoton30_Eta1p5_Cent30_100_v1, process.HLT_HIIslandPhoton40_Eta3p1_Cent30_100_v1, process.HLT_HIIslandPhoton40_Eta1p5_Cent30_100_v1, process.HLT_HIIslandPhoton10_Eta3p1_Cent50_100_v1, process.HLT_HIIslandPhoton10_Eta1p5_Cent50_100_v1, process.HLT_HIIslandPhoton15_Eta3p1_Cent50_100_v1, process.HLT_HIIslandPhoton15_Eta1p5_Cent50_100_v1, process.HLT_HIIslandPhoton20_Eta3p1_Cent50_100_v1, process.HLT_HIIslandPhoton20_Eta1p5_Cent50_100_v1, process.HLT_HIIslandPhoton30_Eta3p1_Cent50_100_v1, process.HLT_HIIslandPhoton30_Eta1p5_Cent50_100_v1, process.HLT_HIIslandPhoton40_Eta3p1_Cent50_100_v1, process.HLT_HIIslandPhoton40_Eta1p5_Cent50_100_v1, process.HLT_HIGEDPhoton10_Cent30_100_v1, process.HLT_HIGEDPhoton15_Cent30_100_v1, process.HLT_HIGEDPhoton20_Cent30_100_v1, process.HLT_HIGEDPhoton30_Cent30_100_v1, process.HLT_HIGEDPhoton40_Cent30_100_v1, process.HLT_HIGEDPhoton10_Cent50_100_v1, process.HLT_HIGEDPhoton15_Cent50_100_v1, process.HLT_HIGEDPhoton20_Cent50_100_v1, process.HLT_HIGEDPhoton30_Cent50_100_v1, process.HLT_HIGEDPhoton40_Cent50_100_v1, process.HLT_HIGEDPhoton10_EB_Cent30_100_v1, process.HLT_HIGEDPhoton15_EB_Cent30_100_v1, process.HLT_HIGEDPhoton20_EB_Cent30_100_v1, process.HLT_HIGEDPhoton30_EB_Cent30_100_v1, process.HLT_HIGEDPhoton40_EB_Cent30_100_v1, process.HLT_HIGEDPhoton10_EB_Cent50_100_v1, process.HLT_HIGEDPhoton15_EB_Cent50_100_v1, process.HLT_HIGEDPhoton20_EB_Cent50_100_v1, process.HLT_HIGEDPhoton30_EB_Cent50_100_v1, process.HLT_HIGEDPhoton40_EB_Cent50_100_v1, process.HLT_HIPuAK4CaloJet40Eta5p1_v1, process.HLT_HIPuAK4CaloJet60Eta5p1_v1, process.HLT_HIPuAK4CaloJet80Eta5p1_v1, process.HLT_HIPuAK4CaloJet100Eta5p1_v1, process.HLT_HIPuAK4CaloJet120Eta5p1_v1, process.HLT_HIPuAK4CaloJet80_35_Eta1p1_v1, process.HLT_HIPuAK4CaloJet100_35_Eta1p1_v1, process.HLT_HIPuAK4CaloJet80_35_Eta0p7_v1, process.HLT_HIPuAK4CaloJet100_35_Eta0p7_v1, process.HLT_HIPuAK4CaloJet80_45_45_Eta2p1_v1, process.HLT_HIPuAK4CaloJet40Fwd_v1, process.HLT_HIPuAK4CaloJet60Fwd_v1, process.HLT_HIPuAK4CaloJet80Fwd_v1, process.HLT_HIPuAK4CaloJet100Fwd_v1, process.HLT_HIPuAK4CaloJet120Fwd_v1, process.HLT_HIPuAK4CaloJet60Eta2p4_DeepCSV0p71_v1, process.HLT_HIPuAK4CaloJet80Eta2p4_DeepCSV0p71_v1, process.HLT_HIPuAK4CaloJet100Eta2p4_DeepCSV0p71_v1, process.HLT_HIPuAK4CaloJet60Eta2p4_CSVv2WP0p8_v1, process.HLT_HIPuAK4CaloJet80Eta2p4_CSVv2WP0p8_v1, process.HLT_HIPuAK4CaloJet100Eta2p4_CSVv2WP0p8_v1, process.HLT_HIPuAK4CaloJet40Eta5p1_Centrality_30_100_v1, process.HLT_HIPuAK4CaloJet60Eta5p1_Centrality_30_100_v1, process.HLT_HIPuAK4CaloJet80Eta5p1_Centrality_30_100_v1, process.HLT_HIPuAK4CaloJet100Eta5p1_Centrality_30_100_v1, process.HLT_HIPuAK4CaloJet40Eta5p1_Centrality_50_100_v1, process.HLT_HIPuAK4CaloJet60Eta5p1_Centrality_50_100_v1, process.HLT_HIPuAK4CaloJet80Eta5p1_Centrality_50_100_v1, process.HLT_HIPuAK4CaloJet100Eta5p1_Centrality_50_100_v1, process.HLT_HICsAK4PFJet60Eta1p5_Centrality_30_100_v1, process.HLT_HICsAK4PFJet80Eta1p5_Centrality_30_100_v1, process.HLT_HICsAK4PFJet100Eta1p5_Centrality_30_100_v1, process.HLT_HICsAK4PFJet60Eta1p5_Centrality_50_100_v1, process.HLT_HICsAK4PFJet80Eta1p5_Centrality_50_100_v1, process.HLT_HICsAK4PFJet100Eta1p5_Centrality_50_100_v1, process.HLT_HICsAK4PFJet60Eta1p5_v1, process.HLT_HICsAK4PFJet80Eta1p5_v1, process.HLT_HICsAK4PFJet100Eta1p5_v1, process.HLT_HICsAK4PFJet120Eta1p5_v1, process.HLT_HIEle10Gsf_v1, process.HLT_HIEle15Gsf_v1, process.HLT_HIEle20Gsf_v1, process.HLT_HIEle30Gsf_v1, process.HLT_HIEle40Gsf_v1, process.HLT_HIEle50Gsf_v1, process.HLT_HIEle15Ele10Gsf_v1, process.HLT_HIEle15Ele10GsfMass50_v1, process.HLT_HIDoubleEle10Gsf_v1, process.HLT_HIDoubleEle10GsfMass50_v1, process.HLT_HIDoubleEle15Gsf_v1, process.HLT_HIDoubleEle15GsfMass50_v1 ))


process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/mnguyen/AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8_5020GeV_DIGI2RAW_103X_upgrade2018_realistic_HI_v4/Pythia8_AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8/crab_AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8_5020GeV_DIGI2RAW_103X_upgrade2018_realistic_HI_v4/181013_203555/0000/step1_private_DIGI_L1_DIGI2RAW_HLT_PU_99.root',
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

# override the GlobalTag's L1T menu from an Xml file
from HLTrigger.Configuration.CustomConfigs import L1XML
process = L1XML(process,"L1Menu_CollisionsHeavyIons2018_v4.xml")

# run the Full L1T emulator, then repack the data into a new RAW collection, to be used by the HLT
from HLTrigger.Configuration.CustomConfigs import L1REPACK
process = L1REPACK(process,"FullMC")

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
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = '103X_upgrade2018_realistic_HI_v6')

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

#process.DQMOutput = cms.EndPath( process.dqmOutput )

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
_customInfo['globalTag' ]= "103X_upgrade2018_realistic_HI_v6"
_customInfo['inputFile' ]=  ['/store/user/mnguyen/AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8_5020GeV_DIGI2RAW_103X_upgrade2018_realistic_HI_v4/Pythia8_AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8/crab_AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8_5020GeV_DIGI2RAW_103X_upgrade2018_realistic_HI_v4/181013_203555/0000/step1_private_DIGI_L1_DIGI2RAW_HLT_PU_99.root']
_customInfo['realData'  ]=  False
from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
process = customizeHLTforAll(process,"GRun",_customInfo)

from HLTrigger.Configuration.customizeHLTforCMSSW import customizeHLTforCMSSW
process = customizeHLTforCMSSW(process,"GRun")

# Eras-based customisations
from HLTrigger.Configuration.Eras import modifyHLTforEras
modifyHLTforEras(process)

#User-defined customization functions
from L1Trigger.Configuration.customiseSettings import L1TSettingsToCaloParams_2018_v1_4
process = L1TSettingsToCaloParams_2018_v1_4(process)


import CalibTracker.Configuration.Common.PoolDBESSource_cfi
process.newBS = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'), toGet = cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'), tag = cms.string('BeamSpotObjects_Realistic25ns_13TeVCollisions_Early2017_v1_mc'))))
process.prefer_PreferNewBS = cms.ESPrefer('PoolDBESSource', 'newBS')

process.simEmtfDigis.CSCInputBXShift = cms.int32(-6)

process.caloStage2Params.hiMode = cms.uint32(1)
process.caloStage2Params.jetPUSType = cms.string('PhiRing2')
process.caloStage2Params.jetPUSUseChunkySandwich = cms.uint32(False)

process.caloStage2Params.etSumCentralityLower = cms.vdouble(0.0, 1.35, 7.15, 71.0, 219.5, 583.4, 1310.6, 65535.0)
process.caloStage2Params.etSumCentralityUpper = cms.vdouble(4.15, 13.6, 110.95, 302.1, 713.35, 1464.35, 2664.05, 65535.0)

process.simEcalTriggerPrimitiveDigis = cms.EDProducer('EcalTrigPrimProducer', BarrelOnly = cms.bool(False), Debug = cms.bool(False), Famos = cms.bool(False), InstanceEB = cms.string('ebDigis'), InstanceEE = cms.string('eeDigis'), Label = cms.string('unpackEcal'), TcpOutput = cms.bool(False), binOfMaximum = cms.int32(6))

process.simCaloStage2Layer1Digis.ecalToken = cms.InputTag('simEcalTriggerPrimitiveDigis')

process.SimL1Emulator = cms.Sequence(process.unpackRPC+process.unpackDT+process.unpackCSC+process.unpackEcal+process.unpackHcal+process.simHcalTriggerPrimitiveDigis+process.simEcalTriggerPrimitiveDigis+((process.simCaloStage2Layer1Digis+process.simCaloStage2Digis)+((process.simDtTriggerPrimitiveDigis+process.simCscTriggerPrimitiveDigis)+process.simTwinMuxDigis+process.simBmtfDigis+process.simEmtfDigis+process.simOmtfDigis+process.simGmtCaloSumDigis+process.simGmtStage2Digis)+(process.simGtExtFakeStage2Digis)+process.SimL1TGlobal)+process.packCaloStage2+process.packGmtStage2+process.packGtStage2+process.rawDataCollector)

process.GlobalTag.toGet = cms.VPSet(cms.PSet(record = cms.string('EcalTPGFineGrainStripEERcd'), tag = cms.string('EcalTPGFineGrainStrip_12'), connect =cms.string('frontier://FrontierPrep/CMS_CONDITIONS')), cms.PSet(record = cms.string('EcalTPGSpikeRcd'), tag = cms.string('EcalTPGSpike_12'), connect =cms.string('frontier://FrontierPrep/CMS_CONDITIONS')))
process.caloStage2Params.egEtaCut = cms.int32(24)
process.options.numberOfThreads=cms.untracked.uint32(1)

process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")
process.hltbitanalysis.HLTProcessName = cms.string("MyHLT")
process.hltbitanalysis.hltresults = cms.InputTag("TriggerResults", "", "MyHLT")
process.hltbitanalysis.l1results = cms.InputTag("hltGtStage2Digis", "", "MyHLT")
process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)
process.hltbitanalysis.RunParameters = cms.PSet(
   isData = cms.untracked.bool(True))
process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)
process.TFileService = cms.Service("TFileService",
   fileName=cms.string("openHLT.root"))
process.load("HeavyIonsAnalysis.EventAnalysis.hltobject_PbPb_cfi")
process.hltobject.processName = cms.string("MyHLT")
process.hltobject.triggerResults = cms.InputTag("TriggerResults", "", "MyHLT")
process.hltobject.triggerEvent = cms.InputTag("hltTriggerSummaryAOD", "", "MyHLT")
process.hltobject.triggerNames = cms.vstring(
"HLT_HIGEDPhoton10_L1Seeded",
"HLT_HIGEDPhoton15_L1Seeded",
"HLT_HIGEDPhoton20_L1Seeded",
"HLT_HIGEDPhoton30_L1Seeded",
"HLT_HIGEDPhoton40_L1Seeded",
"HLT_HIGEDPhoton50_L1Seeded",
"HLT_HIGEDPhoton60_L1Seeded",
"HLT_HIGEDPhoton10_HECut_L1Seeded",
"HLT_HIGEDPhoton15_HECut_L1Seeded",
"HLT_HIGEDPhoton20_HECut_L1Seeded",
"HLT_HIGEDPhoton30_HECut_L1Seeded",
"HLT_HIGEDPhoton40_HECut_L1Seeded",
"HLT_HIGEDPhoton50_HECut_L1Seeded",
"HLT_HIGEDPhoton60_HECut_L1Seeded",
"HLT_HIGEDPhoton10_EB_L1Seeded",
"HLT_HIGEDPhoton15_EB_L1Seeded",
"HLT_HIGEDPhoton20_EB_L1Seeded",
"HLT_HIGEDPhoton30_EB_L1Seeded",
"HLT_HIGEDPhoton40_EB_L1Seeded",
"HLT_HIGEDPhoton50_EB_L1Seeded",
"HLT_HIGEDPhoton60_EB_L1Seeded",
"HLT_HIGEDPhoton10_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton15_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton20_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton30_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton40_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton50_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton60_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton10",
"HLT_HIGEDPhoton15",
"HLT_HIGEDPhoton20",
"HLT_HIGEDPhoton30",
"HLT_HIGEDPhoton40",
"HLT_HIGEDPhoton50",
"HLT_HIGEDPhoton60",
"HLT_HIGEDPhoton10_HECut",
"HLT_HIGEDPhoton15_HECut",
"HLT_HIGEDPhoton20_HECut",
"HLT_HIGEDPhoton30_HECut",
"HLT_HIGEDPhoton40_HECut",
"HLT_HIGEDPhoton50_HECut",
"HLT_HIGEDPhoton60_HECut",
"HLT_HIGEDPhoton10_EB",
"HLT_HIGEDPhoton15_EB",
"HLT_HIGEDPhoton20_EB",
"HLT_HIGEDPhoton30_EB",
"HLT_HIGEDPhoton40_EB",
"HLT_HIGEDPhoton50_EB",
"HLT_HIGEDPhoton60_EB",
"HLT_HIGEDPhoton10_EB_HECut",
"HLT_HIGEDPhoton15_EB_HECut",
"HLT_HIGEDPhoton20_EB_HECut",
"HLT_HIGEDPhoton30_EB_HECut",
"HLT_HIGEDPhoton40_EB_HECut",
"HLT_HIGEDPhoton50_EB_HECut",
"HLT_HIGEDPhoton60_EB_HECut",
"HLT_HIIslandPhoton10_Eta3p1",
"HLT_HIIslandPhoton15_Eta3p1",
"HLT_HIIslandPhoton20_Eta3p1",
"HLT_HIIslandPhoton30_Eta3p1",
"HLT_HIIslandPhoton40_Eta3p1",
"HLT_HIIslandPhoton50_Eta3p1",
"HLT_HIIslandPhoton60_Eta3p1",
"HLT_HIIslandPhoton10_Eta1p5",
"HLT_HIIslandPhoton15_Eta1p5",
"HLT_HIIslandPhoton20_Eta1p5",
"HLT_HIIslandPhoton30_Eta1p5",
"HLT_HIIslandPhoton40_Eta1p5",
"HLT_HIIslandPhoton50_Eta1p5",
"HLT_HIIslandPhoton60_Eta1p5"
)
process.hltObject = cms.EndPath(process.hltobject)
