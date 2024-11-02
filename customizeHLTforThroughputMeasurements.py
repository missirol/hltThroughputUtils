import FWCore.ParameterSet.Config as cms
import fnmatch

def customizeHLTforThroughputMeasurements(process):
    # remove check on timestamp of online-beamspot payloads
    process.hltOnlineBeamSpotESProducer.timeThreshold = int(1e6)

    # same source settings as used online
    process.source.eventChunkSize = 200
    process.source.eventChunkBlock = 200
    process.source.numBuffers = 4
    process.source.maxBufferedFiles = 2

    # taken from hltDAQPatch.py
    process.options.numberOfConcurrentLuminosityBlocks = 2

    # write a JSON file with the timing information
    if hasattr(process, 'FastTimerService'):
        process.FastTimerService.writeJSONSummary = True

    # remove HLTAnalyzerEndpath if present
    if hasattr(process, 'HLTAnalyzerEndpath'):
        del process.HLTAnalyzerEndpath

    return process

def customizeHLTforCMSHLT3196_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)
    return process

def customizeHLTforCMSHLT3196_CCCLooseInAll(process):
    process = customizeHLTforThroughputMeasurements(process)
    process.HLTSiStripClusterChargeCutNone = cms.PSet(  value = cms.double( 1620.0 ) )
    return process

def customizeHLTforCMSHLT3196_CCCLooseInSiStripUnpacker(process):
    process = customizeHLTforThroughputMeasurements(process)
    process.hltSiStripRawToClustersFacility.Clusterizer.clusterChargeCut.refToPSet_ = 'HLTSiStripClusterChargeCutLoose'
    return process

def customizeHLTforCMSHLT3196_CCCLooseInRefToPSetSubset(process, moduleList):
    process = customizeHLTforThroughputMeasurements(process)

    def updateRefToPSet(module):
        ret = 0
        for parName in module.parameterNames_():
            param = getattr(module, parName)
            if isinstance(param, cms.VPSet):
                for pset in param:
                    ret += updateRefToPSet(pset)
            elif isinstance(param, cms.PSet):
                ret += updateRefToPSet(param)
            elif parName == 'refToPSet_':
                if param.value() == 'HLTSiStripClusterChargeCutNone':
                    ret += 1
                    setattr(module, parName, 'HLTSiStripClusterChargeCutLoose')
        return ret

    for moduleDict in [
        process.psets_(),
        process.es_prefers_(),
        process.es_producers_(),
        process.es_sources_(),
        process.filters_(),
        process.producers_(),
        process.analyzers_(),
        process.switchProducers_(),
    ]:
        for moduleLabel_i in moduleDict:
            keepModule = True
            for (modulePattern_j, keepModule_j) in moduleList:
                if fnmatch.fnmatch(moduleLabel_i, modulePattern_j):
                    keepModule = keepModule_j
            nChanges = 0
            if keepModule:
                nChanges = updateRefToPSet(getattr(process, moduleLabel_i))
#            if nChanges > 0:
#                print('XXX', moduleLabel_i)

    return process

def customizeHLTforCMSHLT3196_CCCLooseInRefToPSetSubsetA(process):
    process = customizeHLTforThroughputMeasurements(process)
    process = customizeHLTforCMSHLT3196_CCCLooseInRefToPSetSubset(process, [
        ('*', True),
        ('hltSiStripRawToClustersFacility', False),
    ])
    return process

def customizeHLTforCMSHLT3196_CCCLooseInRefToPSetSubsetB(process):
    process = customizeHLTforThroughputMeasurements(process)
    process = customizeHLTforCMSHLT3196_CCCLooseInRefToPSetSubset(process, [
        ('*', False),
        ('HLTIter1PSetTrajectoryFilterIT', True),
        ('HLTIter2PSetTrajectoryFilterIT', True),
        ('HLTIter4PSetTrajectoryFilterIT', True),
        ('HLTPSetMuonCkfTrajectoryFilter', True),
        ('hltDisplacedhltIter4PixelLessLayerTriplets', True),
        ('hltDisplacedhltIter4PixelLessLayerTripletsForDisplacedTkMuons', True),
        ('hltDisplacedhltIter4PixelLessLayerTripletsForGlbDisplacedMuons', True),
        ('hltDisplacedhltIter4PixelLessLayerTripletsForTau', True),
        ('hltMixedLayerPairs', True),
    ])
    return process

def customizeHLTforCMSHLT3196_CCCLooseInRefToPSetSubsetC(process):
    process = customizeHLTforThroughputMeasurements(process)
    process = customizeHLTforCMSHLT3196_CCCLooseInRefToPSetSubset(process, [
        ('*', False),
        ('HLTPSetTrajectoryFilterForElectrons', True),
    ])
    return process

def customizeHLTforCMSHLT3196_CCCLooseInRefToPSetSubsetD(process):
    process = customizeHLTforThroughputMeasurements(process)
    for espLabel in [
        'hltESPChi2ChargeMeasurementEstimator30',
    ]:
        esProd = getattr(process, espLabel)
        esProd.pTChargeCutThreshold = 15
        esProd.clusterChargeCut.refToPSet_ = 'HLTSiStripClusterChargeCutLoose'
    return process

def customizeHLTforCMSHLT3196_CCCLooseInRefToPSetSubsetE(process):
    process = customizeHLTforThroughputMeasurements(process)
    for espLabel in [
        'hltESPChi2ChargeMeasurementEstimator30',
        'hltESPChi2ChargeMeasurementEstimator2000',
    ]:
        esProd = getattr(process, espLabel)
        esProd.pTChargeCutThreshold = 15
        esProd.clusterChargeCut.refToPSet_ = 'HLTSiStripClusterChargeCutLoose'
    return process

def customizeHLTforCMSHLT3196_CCCLooseInRefToPSetSubsetF(process):
    process = customizeHLTforThroughputMeasurements(process)
    for espLabel in [
        'hltESPChi2ChargeMeasurementEstimator30',
        'hltESPChi2ChargeMeasurementEstimator2000',
        'hltESPChi2ChargeMeasurementEstimator16',
    ]:
        esProd = getattr(process, espLabel)
        esProd.pTChargeCutThreshold = 15
        esProd.clusterChargeCut.refToPSet_ = 'HLTSiStripClusterChargeCutLoose'
    return process

def customizeHLTforCMSHLT3212_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)
    return process

def customizeHLTforCMSHLT3212_target(process):
    process = customizeHLTforThroughputMeasurements(process)
    process.hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking.L1SeedsLogicalExpression = \
        process.hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking.L1SeedsLogicalExpression.value().replace(
            'L1_DoubleMu6_Upt6_SQ_er2p0 OR L1_DoubleMu7_Upt7_SQ_er2p0 OR L1_DoubleMu8_Upt8_SQ_er2p0',
            'L1_DoubleMu0_Upt6_SQ_er2p0 OR L1_DoubleMu0_Upt7_SQ_er2p0 OR L1_DoubleMu0_Upt8_SQ_er2p0'
        )
    return process

def customizeHLTforCMSHLT3137_test11(process):
    process = customizeHLTforThroughputMeasurements(process)

    # same settings as the timing server
    process.source.eventChunkSize = 240
    process.source.eventChunkBlock = 240
    process.source.numBuffers = 8
    process.source.maxBufferedFiles = 8

    # same settings as the timing server (should correspond to 2)
    # https://github.com/cms-sw/cmssw/blob/774f85421329c42cd1d30ec43d470f527141fb92/FWCore/ParameterSet/src/validateTopLevelParameterSets.cc#L31
    process.options.numberOfConcurrentLuminosityBlocks = 0

#    # same settings as the timing server
#    process.EvFDaqDirector.runNumber = 0

    return process

def customizeHLTforCMSHLT3137_test12(process):
    process = customizeHLTforCMSHLT3137_test11(process)
    process.source.eventChunkSize = 200
    process.source.eventChunkBlock = 200
    process.source.numBuffers = 4
    process.source.maxBufferedFiles = 2
    process.options.numberOfConcurrentLuminosityBlocks = 2
    return process

def customizeHLTforCMSHLT3137_test13(process):
    process = customizeHLTforCMSHLT3137_test12(process)
    process.options.wantSummary = False
    return process

def customizeHLTforCMSHLT3137_test14(process):
    process = customizeHLTforCMSHLT3137_test13(process)
    process.FastTimerService.enableDQMbyModule = False
    process.FastTimerService.enableDQMbyPath = False
    process.FastTimerService.enableDQMbyProcesses = True
    return process

def customizeHLTforCMSHLT3137_test15(process):
    process = customizeHLTforCMSHLT3137_test14(process)
    for msgLoggerVar in [
        'FastReport',
        'HLTrigReport',
        'L1GtTrigReport',
        'L1TGlobalSummary',
        'ThroughputService',
        'TriggerSummaryProducerAOD',
    ]:
        if hasattr(process.MessageLogger, msgLoggerVar):
            process.MessageLogger.__delattr__(msgLoggerVar)
    return process

def customizeHLTforCMSHLT3137_test16(process):
    process = customizeHLTforCMSHLT3137_test15(process)
    for modLabel in [
        'dqmOutput',
    ]:
        if hasattr(process, modLabel):
            process.__delattr__(modLabel)
    return process

def customizeHLTforCMSHLT3232_test01(process):
    process = customizeHLTforThroughputMeasurements(process)
    return process

def customizeHLTforCMSHLT3288_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)
    return process

def customizeHLTforCMSHLT3288_test01(process):
    process = customizeHLTforCMSHLT3288_baseline(process)
    layerPairs = [
        'BPix1+BPix2', 'BPix2+FPix1_pos', 'BPix2+FPix1_neg', 'FPix1_pos+FPix2_pos', 'FPix1_neg+FPix2_neg',
        'BPix1+FPix2_neg', 'BPix2+FPix2_neg', 'FPix2_neg+FPix3_neg', 'BPix2+BPix3',
    ]
    process.hltDoubletRecoveryPixelLayersAndRegions.layerList = layerPairs[:]
    process.hltDoubletRecoveryPixelLayersAndRegionsSerialSync.layerList = layerPairs[:]
    return process

def customizeHLTforCMSHLT3302_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)
    return process

def customizeHLTforCMSHLT3284_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.GlobalTag.globaltag = '140X_dataRun3_HLT_v3'

    process.PrescaleService.lvl1DefaultLabel = 'HIon'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforCMSHLT3359_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.options.numberOfConcurrentLuminosityBlocks = 1

    from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(
        process.GlobalTag,
        globaltag = "141X_dataRun3_HLT_v1",
        conditions = "L1Menu_CollisionsHeavyIons2024_v1_0_3_xml,L1TUtmTriggerMenuRcd,frontier://FrontierProd/CMS_CONDITIONS,,9999-12-31 23:59:59.000"
    )

    process.PrescaleService.lvl1DefaultLabel = '6p1E27'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforCMSHLT3359_target01(process):
    process = customizeHLTforCMSHLT3359_baseline(process)

    process.FastTimerService.dqmTimeRange = 60000
    process.FastTimerService.enableDQMbyPath = True
    process.FastTimerService.dqmPathTimeRange = 60000
    process.FastTimerService.dqmPathTimeResolution = 500
    process.FastTimerService.dqmPathMemoryRange = 1000000
    process.FastTimerService.dqmPathMemoryResolution = 5000

    return process
