# hltGetConfiguration /users/katatar/HI2018PbPb/hltTestEgamma/V72 --globaltag 103X_upgrade2018_realistic_HI_v7 --input root://xrootd.cmsaf.mit.edu//store/user/rbi/Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV/crab_Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV_DIGI2RAW_PU_1030_v1/181030_234244/0001/step1_DIGI_L1_DIGI2RAW_HLT_PU_1652.root --setup /dev/CMSSW_10_3_0/GRun --process MyHLT --full --offline --mc --no-output --unprescale --l1-emulator FullMC --l1Xml L1Menu_CollisionsHeavyIons2018_v4.xml --customise L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_4 --timing --max-events 100

# /users/katatar/HI2018PbPb/hltTestEgamma/V72 (CMSSW_10_3_0)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "MyHLT" )
process.load("setup_dev_CMSSW_10_3_0_GRun_cff")

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/katatar/HI2018PbPb/hltTestEgamma/V72')
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
    lenAMCTrailer = cms.untracked.int32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1404 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    DmxFWId = cms.uint32( 0 ),
    FWOverride = cms.bool( False )
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
process.hltL1sL1SingleEG7BptxANDHLTL1TSeed = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_AlwaysTrue" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltL1sSingleEGXX = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_AlwaysTrue" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPrePhoton10 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleEGYYtoZZ = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_AlwaysTrue" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPrePhoton20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEGL1SingleEGYYtoZZFilter = cms.EDFilter( "HLTEgammaL1TMatchFilterRegional",
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
    L1SeedFilterTag = cms.InputTag( "hltL1sSingleEGYYtoZZ" ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    ncandcut = cms.int32( 1 ),
    l1TausTag = cms.InputTag( 'hltGtStage2Digis','Tau' )
)
process.hltEG20EtFiltervTmp = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    inputTag = cms.InputTag( "hltEGL1SingleEGYYtoZZFilter" ),
    l1EGCand = cms.InputTag( "hltEgammaCandidates" ),
    etcutEE = cms.double( 20.0 ),
    etcutEB = cms.double( 20.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEG20HEFiltervTmp = cms.EDFilter( "HLTEgammaGenericFilter",
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
    candTag = cms.InputTag( "hltEG20EtFiltervTmp" ),
    rhoTag = cms.InputTag( "" ),
    rhoMax = cms.double( 9.9999999E7 ),
    useEt = cms.bool( False ),
    rhoScale = cms.double( 1.0 )
)
process.hltPrePuAK4CaloJet80Eta5p1 = cms.EDFilter( "HLTPrescaler",
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
process.HLTPhoton20Sequence_v13 = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalSequence + process.HLTPFClusteringForEgamma + process.hltEgammaCandidates + process.hltEGL1SingleEGYYtoZZFilter + process.hltEG20EtFiltervTmp + process.HLTDoLocalHcalSequence + process.HLTFastJetForEgamma + process.hltEgammaHoverE + process.hltEG20HEFiltervTmp )
process.HLTPuAK4CaloJetsReconstructionSequence = cms.Sequence( process.HLTDoCaloSequence + process.hltPuAK4CaloJets + process.hltPuAK4CaloJetsIDPassed )
process.HLTPuAK4CaloCorrectorProducersSequence = cms.Sequence( process.hltAK4CaloFastJetCorrector + process.hltAK4CaloRelativeCorrector + process.hltAK4CaloAbsoluteCorrector + process.hltPuAK4CaloCorrector )
process.HLTPuAK4CaloJetsCorrectionSequence = cms.Sequence( process.hltFixedGridRhoFastjetAllCalo + process.HLTPuAK4CaloCorrectorProducersSequence + process.hltPuAK4CaloJetsCorrected + process.hltPuAK4CaloJetsCorrectedIDPassed )
process.HLTPuAK4CaloJetsSequence = cms.Sequence( process.HLTPuAK4CaloJetsReconstructionSequence + process.HLTPuAK4CaloJetsCorrectionSequence )

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
process.HLT_HIIslandPhoton30_Eta3p1_v2_vHLTL1TSeed_vLocalCaloFix = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG7BptxANDHLTL1TSeed + process.hltPreHIIslandPhoton30Eta3p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIIslandPhoton30Eta3p1 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_Photon10_v5 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEGXX + process.hltPrePhoton10 + process.HLTHIGEDPhoton10L1SeededSequence + process.HLTEndSequenceWithZeroSuppression )
process.HLT_Photon20_v13 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEGYYtoZZ + process.hltPrePhoton20 + process.HLTPhoton20Sequence_v13 + process.HLTEndSequenceWithZeroSuppression )
process.HLT_PuAK4CaloJet80Eta5p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPrePuAK4CaloJet80Eta5p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta5p1 + process.HLTEndSequenceWithZeroSuppression )
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


process.HLTSchedule = cms.Schedule( *(process.HLT_HIGEDPhoton10_v1, process.HLT_HIGEDPhoton15_v1, process.HLT_HIGEDPhoton20_v1, process.HLT_HIGEDPhoton30_v1, process.HLT_HIGEDPhoton40_v1, process.HLT_HIGEDPhoton50_v1, process.HLT_HIGEDPhoton60_v1, process.HLT_HIGEDPhoton10_L1EG3_v1, process.HLT_HIGEDPhoton15_L1EG3_v1, process.HLT_HIGEDPhoton20_L1EG3_v1, process.HLT_HIGEDPhoton10_L1EG5_v1, process.HLT_HIGEDPhoton15_L1EG5_v1, process.HLT_HIGEDPhoton20_L1EG5_v1, process.HLT_HIGEDPhoton10_L1EG7_v1, process.HLT_HIGEDPhoton15_L1EG7_v1, process.HLT_HIGEDPhoton20_L1EG7_v1, process.HLT_HIGEDPhoton20_L1EG12_v1, process.HLT_HIGEDPhoton30_L1EG12_v1, process.HLT_HIGEDPhoton30_L1EG15_v1, process.HLT_HIGEDPhoton30_L1EG21_v1, process.HLT_HIGEDPhoton40_L1EG15_v1, process.HLT_HIGEDPhoton40_L1EG30_v1, process.HLT_HIGEDPhoton50_L1EG30_v1, process.HLT_HIGEDPhoton60_L1EG21_v1, process.HLT_HIGEDPhoton10_EB_v1, process.HLT_HIGEDPhoton15_EB_v1, process.HLT_HIGEDPhoton20_EB_v1, process.HLT_HIGEDPhoton30_EB_v1, process.HLT_HIGEDPhoton40_EB_v1, process.HLT_HIGEDPhoton50_EB_v1, process.HLT_HIGEDPhoton60_EB_v1, process.HLT_HIGEDPhoton10_EB_L1EG3_v1, process.HLT_HIGEDPhoton15_EB_L1EG3_v1, process.HLT_HIGEDPhoton20_EB_L1EG3_v1, process.HLT_HIGEDPhoton10_EB_L1EG5_v1, process.HLT_HIGEDPhoton15_EB_L1EG5_v1, process.HLT_HIGEDPhoton20_EB_L1EG5_v1, process.HLT_HIGEDPhoton10_EB_L1EG7_v1, process.HLT_HIGEDPhoton15_EB_L1EG7_v1, process.HLT_HIGEDPhoton20_EB_L1EG7_v1, process.HLT_HIGEDPhoton20_EB_L1EG12_v1, process.HLT_HIGEDPhoton30_EB_L1EG12_v1, process.HLT_HIGEDPhoton30_EB_L1EG15_v1, process.HLT_HIGEDPhoton30_EB_L1EG21_v1, process.HLT_HIGEDPhoton40_EB_L1EG15_v1, process.HLT_HIGEDPhoton40_EB_L1EG30_v1, process.HLT_HIGEDPhoton50_EB_L1EG30_v1, process.HLT_HIGEDPhoton60_EB_L1EG21_v1, process.HLT_HIGEDPhoton10_HECut_v1, process.HLT_HIGEDPhoton15_HECut_v1, process.HLT_HIGEDPhoton20_HECut_v1, process.HLT_HIGEDPhoton30_HECut_v1, process.HLT_HIGEDPhoton40_HECut_v1, process.HLT_HIGEDPhoton50_HECut_v1, process.HLT_HIGEDPhoton60_HECut_v1, process.HLT_HIGEDPhoton10_EB_HECut_v1, process.HLT_HIGEDPhoton15_EB_HECut_v1, process.HLT_HIGEDPhoton20_EB_HECut_v1, process.HLT_HIGEDPhoton30_EB_HECut_v1, process.HLT_HIGEDPhoton40_EB_HECut_v1, process.HLT_HIGEDPhoton50_EB_HECut_v1, process.HLT_HIGEDPhoton60_EB_HECut_v1, process.HLT_HIGEDPhoton10_L1ZB_v1, process.HLT_HIGEDPhoton15_L1ZB_v1, process.HLT_HIGEDPhoton20_L1ZB_v1, process.HLT_HIGEDPhoton30_L1ZB_v1, process.HLT_HIGEDPhoton40_L1ZB_v1, process.HLT_HIGEDPhoton50_L1ZB_v1, process.HLT_HIGEDPhoton60_L1ZB_v1, process.HLT_HIGEDPhoton10_EB_L1ZB_v1, process.HLT_HIGEDPhoton15_EB_L1ZB_v1, process.HLT_HIGEDPhoton20_EB_L1ZB_v1, process.HLT_HIGEDPhoton30_EB_L1ZB_v1, process.HLT_HIGEDPhoton40_EB_L1ZB_v1, process.HLT_HIGEDPhoton50_EB_L1ZB_v1, process.HLT_HIGEDPhoton60_EB_L1ZB_v1, process.HLT_HIGEDPhoton10_L1Seeded_v1, process.HLT_HIGEDPhoton15_L1Seeded_v1, process.HLT_HIGEDPhoton20_L1Seeded_v1, process.HLT_HIGEDPhoton30_L1Seeded_v1, process.HLT_HIGEDPhoton40_L1Seeded_v1, process.HLT_HIGEDPhoton50_L1Seeded_v1, process.HLT_HIGEDPhoton60_L1Seeded_v1, process.HLT_HIGEDPhoton10_EB_L1Seeded_v1, process.HLT_HIGEDPhoton15_EB_L1Seeded_v1, process.HLT_HIGEDPhoton20_EB_L1Seeded_v1, process.HLT_HIGEDPhoton30_EB_L1Seeded_v1, process.HLT_HIGEDPhoton40_EB_L1Seeded_v1, process.HLT_HIGEDPhoton50_EB_L1Seeded_v1, process.HLT_HIGEDPhoton60_EB_L1Seeded_v1, process.HLT_HIGEDPhoton10_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton15_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton20_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton30_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton40_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton50_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton60_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton10_EB_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton15_EB_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton20_EB_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton30_EB_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton40_EB_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton50_EB_HECut_L1Seeded_v1, process.HLT_HIGEDPhoton60_EB_HECut_L1Seeded_v1, process.HLT_HIIslandPhoton10_Eta3p1_v1, process.HLT_HIIslandPhoton10_Eta1p5_v1, process.HLT_HIIslandPhoton15_Eta3p1_v1, process.HLT_HIIslandPhoton15_Eta1p5_v1, process.HLT_HIIslandPhoton20_Eta3p1_v1, process.HLT_HIIslandPhoton20_Eta1p5_v1, process.HLT_HIIslandPhoton30_Eta3p1_v1, process.HLT_HIIslandPhoton30_Eta1p5_v1, process.HLT_HIIslandPhoton40_Eta3p1_v1, process.HLT_HIIslandPhoton40_Eta1p5_v1, process.HLT_HIIslandPhoton50_Eta3p1_v1, process.HLT_HIIslandPhoton50_Eta1p5_v1, process.HLT_HIIslandPhoton60_Eta3p1_v1, process.HLT_HIIslandPhoton60_Eta1p5_v1, process.HLT_HIIslandPhoton10_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton10_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton15_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton15_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton20_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton20_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton30_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton30_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton40_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton40_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton50_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton50_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton60_Eta3p1_L1ZB_v1, process.HLT_HIIslandPhoton60_Eta1p5_L1ZB_v1, process.HLT_HIIslandPhoton20_Eta3p1_L1EG12_v1, process.HLT_HIIslandPhoton20_Eta1p5_L1EG12_v1, process.HLT_HIIslandPhoton10_Eta3p1_L1EG7_v1, process.HLT_HIIslandPhoton10_Eta1p5_L1EG7_v1, process.HLT_HIIslandPhoton15_Eta3p1_L1EG7_v1, process.HLT_HIIslandPhoton15_Eta1p5_L1EG7_v1, process.HLT_HIIslandPhoton20_Eta3p1_L1EG7_v1, process.HLT_HIIslandPhoton20_Eta1p5_L1EG7_v1, process.HLT_HIIslandPhoton10_Eta3p1_L1EG5_v1, process.HLT_HIIslandPhoton10_Eta1p5_L1EG5_v1, process.HLT_HIIslandPhoton15_Eta3p1_L1EG5_v1, process.HLT_HIIslandPhoton15_Eta1p5_L1EG5_v1, process.HLT_HIIslandPhoton20_Eta3p1_L1EG5_v1, process.HLT_HIIslandPhoton20_Eta1p5_L1EG5_v1, process.HLT_HIIslandPhoton10_Eta3p1_L1EG3_v1, process.HLT_HIIslandPhoton10_Eta1p5_L1EG3_v1, process.HLT_HIIslandPhoton15_Eta3p1_L1EG3_v1, process.HLT_HIIslandPhoton15_Eta1p5_L1EG3_v1, process.HLT_HIIslandPhoton20_Eta3p1_L1EG3_v1, process.HLT_HIIslandPhoton20_Eta1p5_L1EG3_v1, process.HLT_HIIslandPhoton30_Eta3p1_L1EG12_v1, process.HLT_HIIslandPhoton30_Eta1p5_L1EG12_v1, process.HLT_HIIslandPhoton30_Eta3p1_L1EG15_v1, process.HLT_HIIslandPhoton30_Eta1p5_L1EG15_v1, process.HLT_HIIslandPhoton30_Eta3p1_L1EG21_v1, process.HLT_HIIslandPhoton30_Eta1p5_L1EG21_v1, process.HLT_HIIslandPhoton40_Eta3p1_L1EG15_v1, process.HLT_HIIslandPhoton40_Eta1p5_L1EG15_v1, process.HLT_HIIslandPhoton40_Eta3p1_L1EG30_v1, process.HLT_HIIslandPhoton40_Eta1p5_L1EG30_v1, process.HLT_HIIslandPhoton50_Eta3p1_L1EG30_v1, process.HLT_HIIslandPhoton50_Eta1p5_L1EG30_v1, process.HLT_HIIslandPhoton60_Eta3p1_L1EG21_v1, process.HLT_HIIslandPhoton60_Eta1p5_L1EG21_v1, process.HLT_HIIslandPhoton30_Eta3p1_v2_vHLTL1TSeed_vLocalCaloFix, process.HLT_Photon10_v5, process.HLT_Photon20_v13, process.HLT_PuAK4CaloJet80Eta5p1_v1, process.HLT_ZeroBias_v6, process.HLTriggerFinalPath, process.HLTriggerFirstPath, process.HLT_HIIslandPhoton10_Eta3p1_Cent30_100_v1, process.HLT_HIIslandPhoton10_Eta1p5_Cent30_100_v1, process.HLT_HIIslandPhoton15_Eta3p1_Cent30_100_v1, process.HLT_HIIslandPhoton15_Eta1p5_Cent30_100_v1, process.HLT_HIIslandPhoton20_Eta3p1_Cent30_100_v1, process.HLT_HIIslandPhoton20_Eta1p5_Cent30_100_v1, process.HLT_HIIslandPhoton30_Eta3p1_Cent30_100_v1, process.HLT_HIIslandPhoton30_Eta1p5_Cent30_100_v1, process.HLT_HIIslandPhoton40_Eta3p1_Cent30_100_v1, process.HLT_HIIslandPhoton40_Eta1p5_Cent30_100_v1, process.HLT_HIIslandPhoton10_Eta3p1_Cent50_100_v1, process.HLT_HIIslandPhoton10_Eta1p5_Cent50_100_v1, process.HLT_HIIslandPhoton15_Eta3p1_Cent50_100_v1, process.HLT_HIIslandPhoton15_Eta1p5_Cent50_100_v1, process.HLT_HIIslandPhoton20_Eta3p1_Cent50_100_v1, process.HLT_HIIslandPhoton20_Eta1p5_Cent50_100_v1, process.HLT_HIIslandPhoton30_Eta3p1_Cent50_100_v1, process.HLT_HIIslandPhoton30_Eta1p5_Cent50_100_v1, process.HLT_HIIslandPhoton40_Eta3p1_Cent50_100_v1, process.HLT_HIIslandPhoton40_Eta1p5_Cent50_100_v1, process.HLT_HIGEDPhoton10_Cent30_100_v1, process.HLT_HIGEDPhoton15_Cent30_100_v1, process.HLT_HIGEDPhoton20_Cent30_100_v1, process.HLT_HIGEDPhoton30_Cent30_100_v1, process.HLT_HIGEDPhoton40_Cent30_100_v1, process.HLT_HIGEDPhoton10_Cent50_100_v1, process.HLT_HIGEDPhoton15_Cent50_100_v1, process.HLT_HIGEDPhoton20_Cent50_100_v1, process.HLT_HIGEDPhoton30_Cent50_100_v1, process.HLT_HIGEDPhoton40_Cent50_100_v1, process.HLT_HIGEDPhoton10_EB_Cent30_100_v1, process.HLT_HIGEDPhoton15_EB_Cent30_100_v1, process.HLT_HIGEDPhoton20_EB_Cent30_100_v1, process.HLT_HIGEDPhoton30_EB_Cent30_100_v1, process.HLT_HIGEDPhoton40_EB_Cent30_100_v1, process.HLT_HIGEDPhoton10_EB_Cent50_100_v1, process.HLT_HIGEDPhoton15_EB_Cent50_100_v1, process.HLT_HIGEDPhoton20_EB_Cent50_100_v1, process.HLT_HIGEDPhoton30_EB_Cent50_100_v1, process.HLT_HIGEDPhoton40_EB_Cent50_100_v1 ))


process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        'root://xrootd.cmsaf.mit.edu//store/user/rbi/Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV/crab_Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV_DIGI2RAW_PU_1030_v1/181030_234244/0001/step1_DIGI_L1_DIGI2RAW_HLT_PU_1652.root',
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

# instrument the menu with the modules and EndPath needed for timing studies

# configure the FastTimerService
process.load( "HLTrigger.Timer.FastTimerService_cfi" )
# print a text summary at the end of the job
process.FastTimerService.printEventSummary         = False
process.FastTimerService.printRunSummary           = False
process.FastTimerService.printJobSummary           = True

# enable DQM plots
process.FastTimerService.enableDQM                 = True

# enable per-path DQM plots (starting with CMSSW 9.2.3-patch2)
process.FastTimerService.enableDQMbyPath           = True

# enable per-module DQM plots
process.FastTimerService.enableDQMbyModule         = True

# enable per-event DQM plots vs lumisection
process.FastTimerService.enableDQMbyLumiSection    = True
process.FastTimerService.dqmLumiSectionsRange      = 2500

# set the time resolution of the DQM plots
process.FastTimerService.dqmTimeRange              = 2000.
process.FastTimerService.dqmTimeResolution         =   10.
process.FastTimerService.dqmPathTimeRange          = 1000.
process.FastTimerService.dqmPathTimeResolution     =    5.
process.FastTimerService.dqmModuleTimeRange        =  200.
process.FastTimerService.dqmModuleTimeResolution   =    1.

# set the base DQM folder for the plots
process.FastTimerService.dqmPath                   = 'HLT/TimerService'
process.FastTimerService.enableDQMbyProcesses      = False

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
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = '103X_upgrade2018_realistic_HI_v7')

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
_customInfo['globalTag' ]= "103X_upgrade2018_realistic_HI_v7"
_customInfo['inputFile' ]=  ['root://xrootd.cmsaf.mit.edu//store/user/rbi/Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV/crab_Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV_DIGI2RAW_PU_1030_v1/181030_234244/0001/step1_DIGI_L1_DIGI2RAW_HLT_PU_1652.root']
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

process.caloStage2Params.hiMode = cms.uint32(1)

process.simEcalTriggerPrimitiveDigis = cms.EDProducer('EcalTrigPrimProducer', BarrelOnly = cms.bool(False), Debug = cms.bool(False), Famos = cms.bool(False), InstanceEB = cms.string('ebDigis'), InstanceEE = cms.string('eeDigis'), Label = cms.string('unpackEcal'), TcpOutput = cms.bool(False), binOfMaximum = cms.int32(6))

process.simCaloStage2Layer1Digis.ecalToken = cms.InputTag('simEcalTriggerPrimitiveDigis')

process.SimL1Emulator = cms.Sequence(process.unpackRPC+process.unpackDT+process.unpackCSC+process.unpackEcal+process.unpackHcal+process.simHcalTriggerPrimitiveDigis+process.simEcalTriggerPrimitiveDigis+((process.simCaloStage2Layer1Digis+process.simCaloStage2Digis)+((process.simDtTriggerPrimitiveDigis+process.simCscTriggerPrimitiveDigis)+process.simTwinMuxDigis+process.simBmtfDigis+process.simEmtfDigis+process.simOmtfDigis+process.simGmtCaloSumDigis+process.simGmtStage2Digis)+(process.simGtExtFakeStage2Digis)+process.SimL1TGlobal)+process.packCaloStage2+process.packGmtStage2+process.packGtStage2+process.rawDataCollector)

process.GlobalTag.toGet = cms.VPSet(cms.PSet(record = cms.string('EcalTPGFineGrainStripEERcd'), tag = cms.string('EcalTPGFineGrainStrip_12'), connect =cms.string('frontier://FrontierPrep/CMS_CONDITIONS')), cms.PSet(record = cms.string('EcalTPGSpikeRcd'), tag = cms.string('EcalTPGSpike_12'), connect =cms.string('frontier://FrontierPrep/CMS_CONDITIONS')))
process.options.numberOfThreads=cms.untracked.uint32(1)

process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")
process.hltbitanalysis.HLTProcessName = cms.string("MyHLT")
process.hltbitanalysis.hltresults = cms.InputTag("TriggerResults", "", "MyHLT")
process.hltbitanalysis.l1results = cms.InputTag("hltGtStage2Digis", "", "MyHLT")
process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)
process.hltbitanalysis.RunParameters = cms.PSet(isData = cms.untracked.bool(True))
process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)
process.TFileService = cms.Service("TFileService", fileName=cms.string("openHLT.root"))
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
