import FWCore.ParameterSet.Config as cms

def customizeHLTforCKF2024(process):

    # local SiStrips reconstruction
    process.hltSiStripRawToClustersFacility.onDemand = True
    del process.hltSiStripRawToClustersFacility.Clusterizer.MaxClusterSize

    # remove MkFit-related ESProducers
    del process.hltDoubletRecoveryPFlowTrackCandidatesMkFitConfig
    del process.mkFitGeometryESProducer
    del process.hltESPIter0PFlowTrackCandidatesMkFitConfig

    # redefine the two HLT-tracking iterations (and their SerialSync counterparts)
    process.hltIter0PFLowPixelSeedsFromPixelTracks = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
        InputCollection = cms.InputTag( "hltPixelTracks" ),
        InputVertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
        originHalfLength = cms.double( 0.3 ),
        originRadius = cms.double( 0.1 ),
        useProtoTrackKinematics = cms.bool( False ),
        useEventsWithNoVertex = cms.bool( True ),
        TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
        usePV = cms.bool( False ),
        includeFourthHit = cms.bool( True ),
        produceComplement = cms.bool( False ),
        SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) )
    )
    process.hltIter0PFlowCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
        cleanTrajectoryAfterInOut = cms.bool( False ),
        doSeedingRegionRebuilding = cms.bool( False ),
        onlyPixelHitsForSeedCleaner = cms.bool( False ),
        reverseTrajectories = cms.bool( False ),
        useHitsSplitting = cms.bool( False ),
        MeasurementTrackerEvent = cms.InputTag( "hltMeasurementTrackerEvent" ),
        src = cms.InputTag( "hltIter0PFLowPixelSeedsFromPixelTracks" ),
        clustersToSkip = cms.InputTag( "" ),
        phase2clustersToSkip = cms.InputTag( "" ),
        TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0GroupedCkfTrajectoryBuilderIT" ) ),
        TransientInitialStateEstimatorParameters = cms.PSet( 
          propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
          numberMeasurementsForFit = cms.int32( 4 ),
          propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
        ),
        numHitsForSeedCleaner = cms.int32( 4 ),
        NavigationSchool = cms.string( "SimpleNavigationSchool" ),
        RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
        TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
        maxNSeeds = cms.uint32( 100000 ),
        maxSeedsBeforeCleaning = cms.uint32( 1000 )
    )
    process.hltIter0PFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
        useSimpleMF = cms.bool( True ),
        SimpleMagneticField = cms.string( "ParabolicMf" ),
        src = cms.InputTag( "hltIter0PFlowCkfTrackCandidates" ),
        clusterRemovalInfo = cms.InputTag( "" ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        Fitter = cms.string( "hltESPFittingSmootherIT" ),
        useHitsSplitting = cms.bool( False ),
        TrajectoryInEvent = cms.bool( False ),
        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        AlgorithmName = cms.string( "hltIter0" ),
        Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
        GeometricInnerState = cms.bool( True ),
        NavigationSchool = cms.string( "" ),
        MeasurementTracker = cms.string( "" ),
        MeasurementTrackerEvent = cms.InputTag( "hltMeasurementTrackerEvent" ),
        reMatchSplitHits = cms.bool( False ),
        usePropagatorForPCA = cms.bool( False )
    )
    process.hltIter0PFlowTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
        src = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracks" ),
        beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
        vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
        ignoreVertices = cms.bool( False ),
        qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
        mva = cms.PSet( 
          minPixelHits = cms.vint32( 0, 0, 0 ),
          maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
          dr_par = cms.PSet( 
            d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
            dr_par2 = cms.vdouble( 3.40282346639E38, 0.6, 0.6 ),
            dr_par1 = cms.vdouble( 3.40282346639E38, 0.8, 0.8 ),
            dr_exp = cms.vint32( 4, 4, 4 ),
            d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
          ),
          maxLostLayers = cms.vint32( 1, 1, 1 ),
          min3DLayers = cms.vint32( 0, 0, 0 ),
          dz_par = cms.PSet( 
            dz_par1 = cms.vdouble( 3.40282346639E38, 0.75, 0.75 ),
            dz_par2 = cms.vdouble( 3.40282346639E38, 0.5, 0.5 ),
            dz_exp = cms.vint32( 4, 4, 4 )
          ),
          minNVtxTrk = cms.int32( 3 ),
          maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
          minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
          maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
          maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
          maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
          minLayers = cms.vint32( 3, 3, 3 )
        )
    )
    process.hltIter0PFlowTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
        originalSource = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracks" ),
        originalMVAVals = cms.InputTag( 'hltIter0PFlowTrackCutClassifier','MVAValues' ),
        originalQualVals = cms.InputTag( 'hltIter0PFlowTrackCutClassifier','QualityMasks' ),
        minQuality = cms.string( "highPurity" ),
        copyExtras = cms.untracked.bool( True ),
        copyTrajectories = cms.untracked.bool( False )
    )
    process.hltDoubletRecoveryClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
        trajectories = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurity" ),
        trackClassifier = cms.InputTag( '','QualityMasks' ),
        pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
        stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
        oldClusterRemovalInfo = cms.InputTag( "" ),
        TrackQuality = cms.string( "highPurity" ),
        maxChi2 = cms.double( 16.0 ),
        minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
        overrideTrkQuals = cms.InputTag( "" )
    )
    process.hltDoubletRecoveryMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
        src = cms.InputTag( "hltMeasurementTrackerEvent" ),
        phase2clustersToSkip = cms.InputTag( "" ),
        clustersToSkip = cms.InputTag( "hltDoubletRecoveryClustersRefRemoval" )
    )
    process.hltDoubletRecoveryPixelLayersAndRegions = cms.EDProducer( "PixelInactiveAreaTrackingRegionsSeedingLayersProducer",
        RegionPSet = cms.PSet( 
          vertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
          beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
          zErrorBeamSpot = cms.double( 15.0 ),
          extraPhi = cms.double( 0.0 ),
          extraEta = cms.double( 0.0 ),
          maxNVertices = cms.int32( 3 ),
          nSigmaZVertex = cms.double( 3.0 ),
          nSigmaZBeamSpot = cms.double( 4.0 ),
          ptMin = cms.double( 1.2 ),
          operationMode = cms.string( "VerticesFixed" ),
          searchOpt = cms.bool( False ),
          whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
          originRadius = cms.double( 0.015 ),
          measurementTrackerName = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEvent" ),
          precise = cms.bool( True ),
          zErrorVertex = cms.double( 0.03 )
        ),
        inactivePixelDetectorLabels = cms.VInputTag( 'hltSiPixelDigiErrors' ),
        badPixelFEDChannelCollectionLabels = cms.VInputTag( 'hltSiPixelDigiErrors' ),
        ignoreSingleFPixPanelModules = cms.bool( True ),
        debug = cms.untracked.bool( False ),
        createPlottingFiles = cms.untracked.bool( False ),
        layerList = cms.vstring( 'BPix1+BPix2',
          'BPix2+FPix1_pos',
          'BPix2+FPix1_neg',
          'FPix1_pos+FPix2_pos',
          'FPix1_neg+FPix2_neg',
          'BPix1+FPix2_neg',
          'BPix2+FPix2_neg',
          'FPix2_neg+FPix3_neg',
          'BPix2+BPix3' ),
        BPix = cms.PSet( 
          hitErrorRPhi = cms.double( 0.0027 ),
          TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
          skipClusters = cms.InputTag( "hltDoubletRecoveryClustersRefRemoval" ),
          useErrorsFromParam = cms.bool( True ),
          hitErrorRZ = cms.double( 0.006 ),
          HitProducer = cms.string( "hltSiPixelRecHits" )
        ),
        FPix = cms.PSet( 
          hitErrorRPhi = cms.double( 0.0051 ),
          TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
          skipClusters = cms.InputTag( "hltDoubletRecoveryClustersRefRemoval" ),
          useErrorsFromParam = cms.bool( True ),
          hitErrorRZ = cms.double( 0.0036 ),
          HitProducer = cms.string( "hltSiPixelRecHits" )
        ),
        TIB = cms.PSet(  ),
        TID = cms.PSet(  ),
        TOB = cms.PSet(  ),
        TEC = cms.PSet(  ),
        MTIB = cms.PSet(  ),
        MTID = cms.PSet(  ),
        MTOB = cms.PSet(  ),
        MTEC = cms.PSet(  )
    )
    process.hltDoubletRecoveryPFlowPixelClusterCheck = cms.EDProducer( "ClusterCheckerEDProducer",
        doClusterCheck = cms.bool( False ),
        MaxNumberOfStripClusters = cms.uint32( 50000 ),
        ClusterCollectionLabel = cms.InputTag( "hltMeasurementTrackerEvent" ),
        MaxNumberOfPixelClusters = cms.uint32( 40000 ),
        PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
        cut = cms.string( "" ),
        DontCountDetsAboveNClusters = cms.uint32( 0 ),
        silentClusterCheck = cms.untracked.bool( False )
    )
    process.hltDoubletRecoveryPFlowPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
        seedingLayers = cms.InputTag( "" ),
        trackingRegions = cms.InputTag( "" ),
        trackingRegionsSeedingLayers = cms.InputTag( "hltDoubletRecoveryPixelLayersAndRegions" ),
        clusterCheck = cms.InputTag( "hltDoubletRecoveryPFlowPixelClusterCheck" ),
        produceSeedingHitSets = cms.bool( True ),
        produceIntermediateHitDoublets = cms.bool( False ),
        maxElement = cms.uint32( 0 ),
        maxElementTotal = cms.uint32( 50000000 ),
        putEmptyIfMaxElementReached = cms.bool( False ),
        layerPairs = cms.vuint32( 0 )
    )
    process.hltDoubletRecoveryPFlowPixelSeeds = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
        seedingHitSets = cms.InputTag( "hltDoubletRecoveryPFlowPixelHitDoublets" ),
        propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
        SeedMomentumForBOFF = cms.double( 5.0 ),
        OriginTransverseErrorMultiplier = cms.double( 1.0 ),
        MinOneOverPtError = cms.double( 1.0 ),
        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        magneticField = cms.string( "ParabolicMf" ),
        forceKinematicWithRegionDirection = cms.bool( False ),
        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
    )
    process.hltDoubletRecoveryPFlowCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
        cleanTrajectoryAfterInOut = cms.bool( False ),
        doSeedingRegionRebuilding = cms.bool( False ),
        onlyPixelHitsForSeedCleaner = cms.bool( False ),
        reverseTrajectories = cms.bool( False ),
        useHitsSplitting = cms.bool( False ),
        MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEvent" ),
        src = cms.InputTag( "hltDoubletRecoveryPFlowPixelSeeds" ),
        clustersToSkip = cms.InputTag( "" ),
        phase2clustersToSkip = cms.InputTag( "" ),
        TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2GroupedCkfTrajectoryBuilderIT" ) ),
        TransientInitialStateEstimatorParameters = cms.PSet( 
          propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
          numberMeasurementsForFit = cms.int32( 4 ),
          propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
        ),
        numHitsForSeedCleaner = cms.int32( 4 ),
        NavigationSchool = cms.string( "SimpleNavigationSchool" ),
        RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
        TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
        maxNSeeds = cms.uint32( 100000 ),
        maxSeedsBeforeCleaning = cms.uint32( 1000 )
    )
    process.hltDoubletRecoveryPFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
        useSimpleMF = cms.bool( True ),
        SimpleMagneticField = cms.string( "ParabolicMf" ),
        src = cms.InputTag( "hltDoubletRecoveryPFlowCkfTrackCandidates" ),
        clusterRemovalInfo = cms.InputTag( "" ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        Fitter = cms.string( "hltESPFittingSmootherIT" ),
        useHitsSplitting = cms.bool( False ),
        TrajectoryInEvent = cms.bool( False ),
        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        AlgorithmName = cms.string( "hltDoubletRecovery" ),
        Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
        GeometricInnerState = cms.bool( True ),
        NavigationSchool = cms.string( "" ),
        MeasurementTracker = cms.string( "" ),
        MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEvent" ),
        reMatchSplitHits = cms.bool( False ),
        usePropagatorForPCA = cms.bool( False )
    )
    process.hltDoubletRecoveryPFlowTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
        src = cms.InputTag( "hltDoubletRecoveryPFlowCtfWithMaterialTracks" ),
        beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
        vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
        ignoreVertices = cms.bool( False ),
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
        )
    )
    process.hltDoubletRecoveryPFlowTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
        originalSource = cms.InputTag( "hltDoubletRecoveryPFlowCtfWithMaterialTracks" ),
        originalMVAVals = cms.InputTag( 'hltDoubletRecoveryPFlowTrackCutClassifier','MVAValues' ),
        originalQualVals = cms.InputTag( 'hltDoubletRecoveryPFlowTrackCutClassifier','QualityMasks' ),
        minQuality = cms.string( "highPurity" ),
        copyExtras = cms.untracked.bool( True ),
        copyTrajectories = cms.untracked.bool( False )
    )
    process.hltMergedTracks = cms.EDProducer( "TrackListMerger",
        ShareFrac = cms.double( 0.19 ),
        FoundHitBonus = cms.double( 5.0 ),
        LostHitPenalty = cms.double( 20.0 ),
        MinPT = cms.double( 0.05 ),
        Epsilon = cms.double( -0.001 ),
        MaxNormalizedChisq = cms.double( 1000.0 ),
        MinFound = cms.int32( 3 ),
        TrackProducers = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPurity','hltDoubletRecoveryPFlowTrackSelectionHighPurity' ),
        hasSelector = cms.vint32( 0, 0 ),
        indivShareFrac = cms.vdouble( 1.0, 1.0 ),
        selectedTrackQuals = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPurity','hltDoubletRecoveryPFlowTrackSelectionHighPurity' ),
        setsToMerge = cms.VPSet( 
          cms.PSet(  pQual = cms.bool( False ),
            tLists = cms.vint32( 0, 1 )
          )
        ),
        trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
        allowFirstHitShare = cms.bool( True ),
        newQuality = cms.string( "confirmed" ),
        copyExtras = cms.untracked.bool( True ),
        writeOnlyTrkQuals = cms.bool( False ),
        copyMVA = cms.bool( False ),
        makeReKeyedSeeds = cms.untracked.bool( False )
    )

    process.hltIter0PFLowPixelSeedsFromPixelTracksSerialSync = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
        InputCollection = cms.InputTag( "hltPixelTracksSerialSync" ),
        InputVertexCollection = cms.InputTag( "hltTrimmedPixelVerticesSerialSync" ),
        originHalfLength = cms.double( 0.3 ),
        originRadius = cms.double( 0.1 ),
        useProtoTrackKinematics = cms.bool( False ),
        useEventsWithNoVertex = cms.bool( True ),
        TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
        usePV = cms.bool( False ),
        includeFourthHit = cms.bool( True ),
        produceComplement = cms.bool( False ),
        SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) )
    )
    process.hltIter0PFlowCkfTrackCandidatesSerialSync = cms.EDProducer( "CkfTrackCandidateMaker",
        cleanTrajectoryAfterInOut = cms.bool( False ),
        doSeedingRegionRebuilding = cms.bool( False ),
        onlyPixelHitsForSeedCleaner = cms.bool( False ),
        reverseTrajectories = cms.bool( False ),
        useHitsSplitting = cms.bool( False ),
        MeasurementTrackerEvent = cms.InputTag( "hltMeasurementTrackerEventSerialSync" ),
        src = cms.InputTag( "hltIter0PFLowPixelSeedsFromPixelTracksSerialSync" ),
        clustersToSkip = cms.InputTag( "" ),
        phase2clustersToSkip = cms.InputTag( "" ),
        TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0GroupedCkfTrajectoryBuilderIT" ) ),
        TransientInitialStateEstimatorParameters = cms.PSet( 
          propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
          numberMeasurementsForFit = cms.int32( 4 ),
          propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
        ),
        numHitsForSeedCleaner = cms.int32( 4 ),
        NavigationSchool = cms.string( "SimpleNavigationSchool" ),
        RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
        TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
        maxNSeeds = cms.uint32( 100000 ),
        maxSeedsBeforeCleaning = cms.uint32( 1000 )
    )
    process.hltIter0PFlowCtfWithMaterialTracksSerialSync = cms.EDProducer( "TrackProducer",
        useSimpleMF = cms.bool( True ),
        SimpleMagneticField = cms.string( "ParabolicMf" ),
        src = cms.InputTag( "hltIter0PFlowCkfTrackCandidatesSerialSync" ),
        clusterRemovalInfo = cms.InputTag( "" ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        Fitter = cms.string( "hltESPFittingSmootherIT" ),
        useHitsSplitting = cms.bool( False ),
        TrajectoryInEvent = cms.bool( False ),
        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        AlgorithmName = cms.string( "hltIter0" ),
        Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
        GeometricInnerState = cms.bool( True ),
        NavigationSchool = cms.string( "" ),
        MeasurementTracker = cms.string( "" ),
        MeasurementTrackerEvent = cms.InputTag( "hltMeasurementTrackerEventSerialSync" ),
        reMatchSplitHits = cms.bool( False ),
        usePropagatorForPCA = cms.bool( False )
    )
    process.hltIter0PFlowTrackCutClassifierSerialSync = cms.EDProducer( "TrackCutClassifier",
        src = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracksSerialSync" ),
        beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
        vertices = cms.InputTag( "hltTrimmedPixelVerticesSerialSync" ),
        ignoreVertices = cms.bool( False ),
        qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
        mva = cms.PSet( 
          minPixelHits = cms.vint32( 0, 0, 0 ),
          maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
          dr_par = cms.PSet( 
            d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
            dr_par2 = cms.vdouble( 3.40282346639E38, 0.6, 0.6 ),
            dr_par1 = cms.vdouble( 3.40282346639E38, 0.8, 0.8 ),
            dr_exp = cms.vint32( 4, 4, 4 ),
            d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
          ),
          maxLostLayers = cms.vint32( 1, 1, 1 ),
          min3DLayers = cms.vint32( 0, 0, 0 ),
          dz_par = cms.PSet( 
            dz_par1 = cms.vdouble( 3.40282346639E38, 0.75, 0.75 ),
            dz_par2 = cms.vdouble( 3.40282346639E38, 0.5, 0.5 ),
            dz_exp = cms.vint32( 4, 4, 4 )
          ),
          minNVtxTrk = cms.int32( 3 ),
          maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
          minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
          maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
          maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
          maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
          minLayers = cms.vint32( 3, 3, 3 )
        )
    )
    process.hltIter0PFlowTrackSelectionHighPuritySerialSync = cms.EDProducer( "TrackCollectionFilterCloner",
        originalSource = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracksSerialSync" ),
        originalMVAVals = cms.InputTag( 'hltIter0PFlowTrackCutClassifierSerialSync','MVAValues' ),
        originalQualVals = cms.InputTag( 'hltIter0PFlowTrackCutClassifierSerialSync','QualityMasks' ),
        minQuality = cms.string( "highPurity" ),
        copyExtras = cms.untracked.bool( True ),
        copyTrajectories = cms.untracked.bool( False )
    )
    process.hltDoubletRecoveryClustersRefRemovalSerialSync = cms.EDProducer( "TrackClusterRemover",
        trajectories = cms.InputTag( "hltIter0PFlowTrackSelectionHighPuritySerialSync" ),
        trackClassifier = cms.InputTag( '','QualityMasks' ),
        pixelClusters = cms.InputTag( "hltSiPixelClustersSerialSync" ),
        stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
        oldClusterRemovalInfo = cms.InputTag( "" ),
        TrackQuality = cms.string( "highPurity" ),
        maxChi2 = cms.double( 16.0 ),
        minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
        overrideTrkQuals = cms.InputTag( "" )
    )
    process.hltDoubletRecoveryMaskedMeasurementTrackerEventSerialSync = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
        src = cms.InputTag( "hltMeasurementTrackerEventSerialSync" ),
        phase2clustersToSkip = cms.InputTag( "" ),
        clustersToSkip = cms.InputTag( "hltDoubletRecoveryClustersRefRemovalSerialSync" )
    )
    process.hltDoubletRecoveryPixelLayersAndRegionsSerialSync = cms.EDProducer( "PixelInactiveAreaTrackingRegionsSeedingLayersProducer",
        RegionPSet = cms.PSet( 
          vertexCollection = cms.InputTag( "hltTrimmedPixelVerticesSerialSync" ),
          beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
          zErrorBeamSpot = cms.double( 15.0 ),
          extraPhi = cms.double( 0.0 ),
          extraEta = cms.double( 0.0 ),
          maxNVertices = cms.int32( 3 ),
          nSigmaZVertex = cms.double( 3.0 ),
          nSigmaZBeamSpot = cms.double( 4.0 ),
          ptMin = cms.double( 1.2 ),
          operationMode = cms.string( "VerticesFixed" ),
          searchOpt = cms.bool( False ),
          whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
          originRadius = cms.double( 0.015 ),
          measurementTrackerName = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEventSerialSync" ),
          precise = cms.bool( True ),
          zErrorVertex = cms.double( 0.03 )
        ),
        inactivePixelDetectorLabels = cms.VInputTag( 'hltSiPixelDigiErrorsSerialSync' ),
        badPixelFEDChannelCollectionLabels = cms.VInputTag( 'hltSiPixelDigiErrorsSerialSync' ),
        ignoreSingleFPixPanelModules = cms.bool( True ),
        debug = cms.untracked.bool( False ),
        createPlottingFiles = cms.untracked.bool( False ),
        layerList = cms.vstring( 'BPix1+BPix2',
          'BPix2+FPix1_pos',
          'BPix2+FPix1_neg',
          'FPix1_pos+FPix2_pos',
          'FPix1_neg+FPix2_neg',
          'BPix1+FPix2_neg',
          'BPix2+FPix2_neg',
          'FPix2_neg+FPix3_neg',
          'BPix2+BPix3' ),
        BPix = cms.PSet( 
          hitErrorRPhi = cms.double( 0.0027 ),
          TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
          skipClusters = cms.InputTag( "hltDoubletRecoveryClustersRefRemovalSerialSync" ),
          useErrorsFromParam = cms.bool( True ),
          hitErrorRZ = cms.double( 0.006 ),
          HitProducer = cms.string( "hltSiPixelRecHitsSerialSync" )
        ),
        FPix = cms.PSet( 
          hitErrorRPhi = cms.double( 0.0051 ),
          TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
          skipClusters = cms.InputTag( "hltDoubletRecoveryClustersRefRemovalSerialSync" ),
          useErrorsFromParam = cms.bool( True ),
          hitErrorRZ = cms.double( 0.0036 ),
          HitProducer = cms.string( "hltSiPixelRecHitsSerialSync" )
        ),
        TIB = cms.PSet(  ),
        TID = cms.PSet(  ),
        TOB = cms.PSet(  ),
        TEC = cms.PSet(  ),
        MTIB = cms.PSet(  ),
        MTID = cms.PSet(  ),
        MTOB = cms.PSet(  ),
        MTEC = cms.PSet(  )
    )
    process.hltDoubletRecoveryPFlowPixelClusterCheckSerialSync = cms.EDProducer( "ClusterCheckerEDProducer",
        doClusterCheck = cms.bool( False ),
        MaxNumberOfStripClusters = cms.uint32( 50000 ),
        ClusterCollectionLabel = cms.InputTag( "hltMeasurementTrackerEventSerialSync" ),
        MaxNumberOfPixelClusters = cms.uint32( 40000 ),
        PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersSerialSync" ),
        cut = cms.string( "" ),
        DontCountDetsAboveNClusters = cms.uint32( 0 ),
        silentClusterCheck = cms.untracked.bool( False )
    )
    process.hltDoubletRecoveryPFlowPixelHitDoubletsSerialSync = cms.EDProducer( "HitPairEDProducer",
        seedingLayers = cms.InputTag( "" ),
        trackingRegions = cms.InputTag( "" ),
        trackingRegionsSeedingLayers = cms.InputTag( "hltDoubletRecoveryPixelLayersAndRegionsSerialSync" ),
        clusterCheck = cms.InputTag( "hltDoubletRecoveryPFlowPixelClusterCheckSerialSync" ),
        produceSeedingHitSets = cms.bool( True ),
        produceIntermediateHitDoublets = cms.bool( False ),
        maxElement = cms.uint32( 0 ),
        maxElementTotal = cms.uint32( 50000000 ),
        putEmptyIfMaxElementReached = cms.bool( False ),
        layerPairs = cms.vuint32( 0 )
    )
    process.hltDoubletRecoveryPFlowPixelSeedsSerialSync = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
        seedingHitSets = cms.InputTag( "hltDoubletRecoveryPFlowPixelHitDoubletsSerialSync" ),
        propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
        SeedMomentumForBOFF = cms.double( 5.0 ),
        OriginTransverseErrorMultiplier = cms.double( 1.0 ),
        MinOneOverPtError = cms.double( 1.0 ),
        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        magneticField = cms.string( "ParabolicMf" ),
        forceKinematicWithRegionDirection = cms.bool( False ),
        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
    )
    process.hltDoubletRecoveryPFlowCkfTrackCandidatesSerialSync = cms.EDProducer( "CkfTrackCandidateMaker",
        cleanTrajectoryAfterInOut = cms.bool( False ),
        doSeedingRegionRebuilding = cms.bool( False ),
        onlyPixelHitsForSeedCleaner = cms.bool( False ),
        reverseTrajectories = cms.bool( False ),
        useHitsSplitting = cms.bool( False ),
        MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEventSerialSync" ),
        src = cms.InputTag( "hltDoubletRecoveryPFlowPixelSeedsSerialSync" ),
        clustersToSkip = cms.InputTag( "" ),
        phase2clustersToSkip = cms.InputTag( "" ),
        TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2GroupedCkfTrajectoryBuilderIT" ) ),
        TransientInitialStateEstimatorParameters = cms.PSet( 
          propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
          numberMeasurementsForFit = cms.int32( 4 ),
          propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
        ),
        numHitsForSeedCleaner = cms.int32( 4 ),
        NavigationSchool = cms.string( "SimpleNavigationSchool" ),
        RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
        TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
        maxNSeeds = cms.uint32( 100000 ),
        maxSeedsBeforeCleaning = cms.uint32( 1000 )
    )
    process.hltDoubletRecoveryPFlowCtfWithMaterialTracksSerialSync = cms.EDProducer( "TrackProducer",
        useSimpleMF = cms.bool( True ),
        SimpleMagneticField = cms.string( "ParabolicMf" ),
        src = cms.InputTag( "hltDoubletRecoveryPFlowCkfTrackCandidatesSerialSync" ),
        clusterRemovalInfo = cms.InputTag( "" ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        Fitter = cms.string( "hltESPFittingSmootherIT" ),
        useHitsSplitting = cms.bool( False ),
        TrajectoryInEvent = cms.bool( False ),
        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        AlgorithmName = cms.string( "hltDoubletRecovery" ),
        Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
        GeometricInnerState = cms.bool( True ),
        NavigationSchool = cms.string( "" ),
        MeasurementTracker = cms.string( "" ),
        MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEventSerialSync" ),
        reMatchSplitHits = cms.bool( False ),
        usePropagatorForPCA = cms.bool( False )
    )
    process.hltDoubletRecoveryPFlowTrackCutClassifierSerialSync = cms.EDProducer( "TrackCutClassifier",
        src = cms.InputTag( "hltDoubletRecoveryPFlowCtfWithMaterialTracksSerialSync" ),
        beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
        vertices = cms.InputTag( "hltTrimmedPixelVerticesSerialSync" ),
        ignoreVertices = cms.bool( False ),
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
        )
    )
    process.hltDoubletRecoveryPFlowTrackSelectionHighPuritySerialSync = cms.EDProducer( "TrackCollectionFilterCloner",
        originalSource = cms.InputTag( "hltDoubletRecoveryPFlowCtfWithMaterialTracksSerialSync" ),
        originalMVAVals = cms.InputTag( 'hltDoubletRecoveryPFlowTrackCutClassifierSerialSync','MVAValues' ),
        originalQualVals = cms.InputTag( 'hltDoubletRecoveryPFlowTrackCutClassifierSerialSync','QualityMasks' ),
        minQuality = cms.string( "highPurity" ),
        copyExtras = cms.untracked.bool( True ),
        copyTrajectories = cms.untracked.bool( False )
    )
    process.hltMergedTracksSerialSync = cms.EDProducer( "TrackListMerger",
        ShareFrac = cms.double( 0.19 ),
        FoundHitBonus = cms.double( 5.0 ),
        LostHitPenalty = cms.double( 20.0 ),
        MinPT = cms.double( 0.05 ),
        Epsilon = cms.double( -0.001 ),
        MaxNormalizedChisq = cms.double( 1000.0 ),
        MinFound = cms.int32( 3 ),
        TrackProducers = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPuritySerialSync','hltDoubletRecoveryPFlowTrackSelectionHighPuritySerialSync' ),
        hasSelector = cms.vint32( 0, 0 ),
        indivShareFrac = cms.vdouble( 1.0, 1.0 ),
        selectedTrackQuals = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPuritySerialSync','hltDoubletRecoveryPFlowTrackSelectionHighPuritySerialSync' ),
        setsToMerge = cms.VPSet( 
          cms.PSet(  pQual = cms.bool( False ),
            tLists = cms.vint32( 0, 1 )
          )
        ),
        trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
        allowFirstHitShare = cms.bool( True ),
        newQuality = cms.string( "confirmed" ),
        copyExtras = cms.untracked.bool( True ),
        writeOnlyTrkQuals = cms.bool( False ),
        copyMVA = cms.bool( False ),
        makeReKeyedSeeds = cms.untracked.bool( False )
    )

    process.HLTIterativeTrackingIteration0 = cms.Sequence(
        process.hltIter0PFLowPixelSeedsFromPixelTracks
      + process.hltIter0PFlowCkfTrackCandidates
      + process.hltIter0PFlowCtfWithMaterialTracks
      + process.hltIter0PFlowTrackCutClassifier
      + process.hltIter0PFlowTrackSelectionHighPurity
    )

    process.HLTIterativeTrackingIteration0SerialSync = cms.Sequence(
        process.hltIter0PFLowPixelSeedsFromPixelTracksSerialSync
      + process.hltIter0PFlowCkfTrackCandidatesSerialSync
      + process.hltIter0PFlowCtfWithMaterialTracksSerialSync
      + process.hltIter0PFlowTrackCutClassifierSerialSync
      + process.hltIter0PFlowTrackSelectionHighPuritySerialSync
    )

    process.HLTIterativeTrackingDoubletRecovery = cms.Sequence(
        process.hltDoubletRecoveryClustersRefRemoval
      + process.hltDoubletRecoveryMaskedMeasurementTrackerEvent
      + process.hltDoubletRecoveryPixelLayersAndRegions
      + process.hltDoubletRecoveryPFlowPixelClusterCheck
      + process.hltDoubletRecoveryPFlowPixelHitDoublets
      + process.hltDoubletRecoveryPFlowPixelSeeds
      + process.hltDoubletRecoveryPFlowCkfTrackCandidates
      + process.hltDoubletRecoveryPFlowCtfWithMaterialTracks
      + process.hltDoubletRecoveryPFlowTrackCutClassifier
      + process.hltDoubletRecoveryPFlowTrackSelectionHighPurity
    )

    process.HLTIterativeTrackingDoubletRecoverySerialSync = cms.Sequence(
        process.hltDoubletRecoveryClustersRefRemovalSerialSync
      + process.hltDoubletRecoveryMaskedMeasurementTrackerEventSerialSync
      + process.hltDoubletRecoveryPixelLayersAndRegionsSerialSync
      + process.hltDoubletRecoveryPFlowPixelClusterCheckSerialSync
      + process.hltDoubletRecoveryPFlowPixelHitDoubletsSerialSync
      + process.hltDoubletRecoveryPFlowPixelSeedsSerialSync
      + process.hltDoubletRecoveryPFlowCkfTrackCandidatesSerialSync
      + process.hltDoubletRecoveryPFlowCtfWithMaterialTracksSerialSync
      + process.hltDoubletRecoveryPFlowTrackCutClassifierSerialSync
      + process.hltDoubletRecoveryPFlowTrackSelectionHighPuritySerialSync
    )

    return process

def customizeHLTforIter0PFlowTrackCutClassifier2025(process):

    process.hltIter0PFlowTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
        src = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracks" ),
        beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
        vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
        ignoreVertices = cms.bool( False ),
        qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
        mva = cms.PSet( 
          minPixelHits = cms.vint32( 0, 0, 0 ),
          maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
          dr_par = cms.PSet( 
            d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
            dr_par2 = cms.vdouble( 3.40282346639E38, 0.45, 0.45 ),
            dr_par1 = cms.vdouble( 3.40282346639E38, 0.6, 0.6 ),
            dr_exp = cms.vint32( 4, 4, 4 ),
            d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
          ),
          maxLostLayers = cms.vint32( 1, 1, 1 ),
          min3DLayers = cms.vint32( 0, 0, 0 ),
          dz_par = cms.PSet( 
            dz_par1 = cms.vdouble( 3.40282346639E38, 0.6, 0.6 ),
            dz_par2 = cms.vdouble( 3.40282346639E38, 0.51, 0.51 ),
            dz_exp = cms.vint32( 4, 4, 4 )
          ),
          minNVtxTrk = cms.int32( 3 ),
          maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
          minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
          maxChi2 = cms.vdouble( 999.0, 25.0, 99.0 ),
          maxChi2n = cms.vdouble( 1.2, 1.0, 999.0 ),
          maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
          minLayers = cms.vint32( 3, 3, 3 )
        )
    )

    process.hltIter0PFlowTrackCutClassifierSerialSync = cms.EDProducer( "TrackCutClassifier",
        src = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracksSerialSync" ),
        beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
        vertices = cms.InputTag( "hltTrimmedPixelVerticesSerialSync" ),
        ignoreVertices = cms.bool( False ),
        qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
        mva = cms.PSet( 
          minPixelHits = cms.vint32( 0, 0, 0 ),
          maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
          dr_par = cms.PSet( 
            d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
            dr_par2 = cms.vdouble( 3.40282346639E38, 0.45, 0.45 ),
            dr_par1 = cms.vdouble( 3.40282346639E38, 0.6, 0.6 ),
            dr_exp = cms.vint32( 4, 4, 4 ),
            d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
          ),
          maxLostLayers = cms.vint32( 1, 1, 1 ),
          min3DLayers = cms.vint32( 0, 0, 0 ),
          dz_par = cms.PSet( 
            dz_par1 = cms.vdouble( 3.40282346639E38, 0.6, 0.6 ),
            dz_par2 = cms.vdouble( 3.40282346639E38, 0.51, 0.51 ),
            dz_exp = cms.vint32( 4, 4, 4 )
          ),
          minNVtxTrk = cms.int32( 3 ),
          maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
          minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
          maxChi2 = cms.vdouble( 999.0, 25.0, 99.0 ),
          maxChi2n = cms.vdouble( 1.2, 1.0, 999.0 ),
          maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
          minLayers = cms.vint32( 3, 3, 3 )
        )
    )

    return process
