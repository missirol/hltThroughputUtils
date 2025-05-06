import FWCore.ParameterSet.Config as cms
import fnmatch
import re

from HLTrigger.Configuration.common import filters_by_type
from HLTrigger.Configuration.customizeHLTforCMSSW import customizeHLTforCMSSW

from RecoTracker.MkFit.customizeHLTIter0ToMkFit import customizeHLTIter0ToMkFit

def customizeHLTforThroughputMeasurements(process):
    # remove check on timestamp of online-beamspot payloads
    if hasattr(process, 'hltOnlineBeamSpotESProducer'):
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

def customizeHLTforCMSHLT3387_l1skim2024_baseline(process):
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

def customizeHLTforCMSHLT3387_l1skim2024_target01(process):
    process = customizeHLTforCMSHLT3387_l1skim2024_baseline(process)

    process.FastTimerService.dqmTimeRange = 60000
    process.FastTimerService.enableDQMbyPath = True
    process.FastTimerService.dqmPathTimeRange = 60000
    process.FastTimerService.dqmPathTimeResolution = 500
    process.FastTimerService.dqmPathMemoryRange = 1000000
    process.FastTimerService.dqmPathMemoryResolution = 5000

    return process

def customizeHLTforCMSHLT3387_hidata2023_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.options.numberOfConcurrentLuminosityBlocks = 1

    process.GlobalTag.globaltag = '141X_dataRun3_HLT_v1'

    l1tSeeds = [
        'L1_DoubleJet12_DeltaPhi2p0_NotZDC1n_AND_BptxAND',
        'L1_DoubleJet12_DeltaPhi2p0_notMinimumBiasHF2_BptxAND',
        'L1_DoubleJet12_DeltaPhi2p0_notZDC_OR_BptxAND',
        'L1_DoubleJet16_DeltaPhi2p0_NotZDC1n_AND_BptxAND',
        'L1_DoubleJet16_DeltaPhi2p0_notMinimumBiasHF2_BptxAND',
        'L1_DoubleJet16_DeltaPhi2p0_notZDC_OR_BptxAND',
        'L1_DoubleJet8_DeltaPhi2p0_NotZDC1n_AND_BptxAND',
        'L1_DoubleJet8_DeltaPhi2p0_notMinimumBiasHF2_BptxAND',
        'L1_DoubleJet8_DeltaPhi2p0_notZDC_OR_BptxAND',
        'L1_DoubleUncorrJet12_DeltaPhi2p0_NotZDC1n_AND_BptxAND',
        'L1_DoubleUncorrJet12_DeltaPhi2p0_notMinimumBiasHF2_BptxAND',
        'L1_DoubleUncorrJet12_DeltaPhi2p0_notZDC_OR_BptxAND',
        'L1_DoubleUncorrJet16_DeltaPhi2p0_NotZDC1n_AND_BptxAND',
        'L1_DoubleUncorrJet16_DeltaPhi2p0_notMinimumBiasHF2_BptxAND',
        'L1_DoubleUncorrJet16_DeltaPhi2p0_notZDC_OR_BptxAND',
        'L1_DoubleUncorrJet8_DeltaPhi2p0_NotZDC1n_AND_BptxAND',
        'L1_DoubleUncorrJet8_DeltaPhi2p0_notMinimumBiasHF2_BptxAND',
        'L1_DoubleUncorrJet8_DeltaPhi2p0_notZDC_OR_BptxAND',
        'L1_SingleJet12_ZDC1n_XOR_RapGap_BptxAND',
        'L1_SingleJet12_notZDC_OR_BptxAND',
        'L1_SingleJet16_ZDC1n_XOR_RapGap_BptxAND',
        'L1_SingleJet16_notZDC_OR_BptxAND',
        'L1_SingleJet20_ZDC1n_XOR_RapGap_BptxAND',
        'L1_SingleJet20_notZDC_OR_BptxAND',
        'L1_SingleJet24_ZDC1n_XOR_RapGap_BptxAND',
        'L1_SingleJet24_notZDC_OR_BptxAND',
        'L1_SingleJet28_ZDC1n_XOR_RapGap_BptxAND',
        'L1_SingleJet28_notZDC_OR_BptxAND',
        'L1_SingleJet8_ZDC1n_XOR_RapGap_BptxAND',
        'L1_SingleJet8_notZDC_OR_BptxAND',
        'L1_SingleMu0_Centrality_30_100_BptxAND',
        'L1_SingleMu0_Centrality_40_100_BptxAND',
        'L1_SingleMuOpen_Centrality_30_100_BptxAND',
        'L1_SingleUncorrJet12_NotMinimumBiasHF2_AND_BptxAND',
        'L1_SingleUncorrJet12_ZDC1n_AsymXOR_BptxAND',
        'L1_SingleUncorrJet12_ZDC1n_Bkp1_AsymXOR_BptxAND',
        'L1_SingleUncorrJet12_ZDC1n_Bkp1_XOR_BptxAND',
        'L1_SingleUncorrJet12_ZDC1n_XOR_BptxAND',
        'L1_SingleUncorrJet12_notZDC_OR_BptxAND',
        'L1_SingleUncorrJet16_NotMinimumBiasHF2_AND_BptxAND',
        'L1_SingleUncorrJet16_ZDC1n_AsymXOR_BptxAND',
        'L1_SingleUncorrJet16_ZDC1n_Bkp1_AsymXOR_BptxAND',
        'L1_SingleUncorrJet16_ZDC1n_Bkp1_XOR_BptxAND',
        'L1_SingleUncorrJet16_ZDC1n_XOR_BptxAND',
        'L1_SingleUncorrJet16_notZDC_OR_BptxAND',
        'L1_SingleUncorrJet20_NotMinimumBiasHF2_AND_BptxAND',
        'L1_SingleUncorrJet20_ZDC1n_AsymXOR_BptxAND',
        'L1_SingleUncorrJet20_ZDC1n_Bkp1_AsymXOR_BptxAND',
        'L1_SingleUncorrJet20_ZDC1n_Bkp1_XOR_BptxAND',
        'L1_SingleUncorrJet20_ZDC1n_XOR_BptxAND',
        'L1_SingleUncorrJet20_notZDC_OR_BptxAND',
        'L1_SingleUncorrJet24_NotMinimumBiasHF2_AND_BptxAND',
        'L1_SingleUncorrJet24_ZDC1n_AsymXOR_BptxAND',
        'L1_SingleUncorrJet24_ZDC1n_Bkp1_AsymXOR_BptxAND',
        'L1_SingleUncorrJet24_ZDC1n_Bkp1_XOR_BptxAND',
        'L1_SingleUncorrJet24_ZDC1n_XOR_BptxAND',
        'L1_SingleUncorrJet24_notZDC_OR_BptxAND',
        'L1_SingleUncorrJet28_NotMinimumBiasHF2_AND_BptxAND',
        'L1_SingleUncorrJet28_ZDC1n_AsymXOR_BptxAND',
        'L1_SingleUncorrJet28_ZDC1n_Bkp1_AsymXOR_BptxAND',
        'L1_SingleUncorrJet28_ZDC1n_Bkp1_XOR_BptxAND',
        'L1_SingleUncorrJet28_ZDC1n_XOR_BptxAND',
        'L1_SingleUncorrJet28_notZDC_OR_BptxAND',
        'L1_SingleUncorrJet8_NotMinimumBiasHF2_AND_BptxAND',
        'L1_SingleUncorrJet8_ZDC1n_AsymXOR_BptxAND',
        'L1_SingleUncorrJet8_ZDC1n_Bkp1_AsymXOR_BptxAND',
        'L1_SingleUncorrJet8_ZDC1n_Bkp1_XOR_BptxAND',
        'L1_SingleUncorrJet8_ZDC1n_XOR_BptxAND',
        'L1_SingleUncorrJet8_notZDC_OR_BptxAND',
        'L1_ZDC1n_AND_AND_NotMBHF2_BptxAND',
        'L1_ZDC1n_OR_RapGap_BptxAND',
    ]

    for mod in filters_by_type(process, 'HLTL1TSeed'):
        for l1tSeed in l1tSeeds:
            mod.L1SeedsLogicalExpression = re.sub(fr"\b{l1tSeed}\b", 'L1_AlwaysTrue', mod.L1SeedsLogicalExpression.value())

    process.PrescaleService.lvl1DefaultLabel = 'HIon'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforCMSHLT3387_hidata2023_target01(process):
    process = customizeHLTforCMSHLT3387_hidata2023_baseline(process)

    process.FastTimerService.dqmTimeRange = 60000
    process.FastTimerService.enableDQMbyPath = True
    process.FastTimerService.dqmPathTimeRange = 60000
    process.FastTimerService.dqmPathTimeResolution = 500
    process.FastTimerService.dqmPathMemoryRange = 1000000
    process.FastTimerService.dqmPathMemoryResolution = 5000

    return process

def customizeHLTforCMSHLT3387_hidata2024_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.options.numberOfConcurrentLuminosityBlocks = 1

#    process.PrescaleService.lvl1DefaultLabel = '1031bEphemeral'
#    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforGSFOriginRadius_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)
    return process

def customizeHLTforGSFOriginRadius_test0p05(process):
    process = customizeHLTforGSFOriginRadius_baseline(process)
    process.hltEleSeedsTrackingRegions.RegionPSet.originRadius = 0.05
    return process

def customizeHLTforPixelAutoTunedCA_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)
    return process

def customizeHLTforPixelAutoTunedCA_newTuneV01(process):
    process = customizeHLTforPixelAutoTunedCA_baseline(process)
    process.hltPixelTracksSoA.CAThetaCutBarrel = 0.00111685053
    process.hltPixelTracksSoA.CAThetaCutForward = 0.00249872683
    process.hltPixelTracksSoA.hardCurvCut = 0.695091509
    process.hltPixelTracksSoA.dcaCutInnerTriplet = 0.0419242041
    process.hltPixelTracksSoA.dcaCutOuterTriplet = 0.293522194
    process.hltPixelTracksSoA.phiCuts = [
        832, 379, 481, 765, 1136,
        706, 656, 407, 1212, 404,
        699, 470, 652, 621, 1017,
        616, 450, 555, 572
    ]
    return process

def customizeHLTforCMSSW47070_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)
    process = customizeHLTforCMSSW(process)

    process.GlobalTag.globaltag = '141X_dataRun3_HLT_v2'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforGRun_14_0_X(process):
    process = customizeHLTforThroughputMeasurements(process)
    process = customizeHLTforCMSSW(process)

    process.GlobalTag.globaltag = '140X_dataRun3_HLT_v3'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforPixelAutoTunedPlusMkFit_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)
    process = customizeHLTforCMSSW(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_v1'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforPixelAutoTunedPlusMkFit_pixel(process):
    process = customizeHLTforPixelAutoTunedPlusMkFit_baseline(process)
    process.hltPixelTracksSoA.CAThetaCutBarrel = 0.00111685053
    process.hltPixelTracksSoA.CAThetaCutForward = 0.00249872683
    process.hltPixelTracksSoA.hardCurvCut = 0.695091509
    process.hltPixelTracksSoA.dcaCutInnerTriplet = 0.0419242041
    process.hltPixelTracksSoA.dcaCutOuterTriplet = 0.293522194
    process.hltPixelTracksSoA.phiCuts = [
        832, 379, 481, 765, 1136,
        706, 656, 407, 1212, 404,
        699, 470, 652, 621, 1017,
        616, 450, 555, 572
    ]
    return process

def customizeHLTforPixelAutoTunedPlusMkFit_pixelAndMkFit(process):
    process = customizeHLTforPixelAutoTunedPlusMkFit_pixel(process)
    process = customizeHLTIter0ToMkFit(process)
    return process

def customizeHLTforPixelClusterLayer1Threshold_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)
    process = customizeHLTforCMSSW(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_v1'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforPixelClusterLayer1Threshold_test2000(process):
    process = customizeHLTforPixelClusterLayer1Threshold_baseline(process)

    process.hltSiPixelClustersSoA.clusterThreshold_layer1 = 2000
    process.hltSiPixelClusters.clusterThreshold_layer1 = 2000
    process.hltSiPixelClustersSoASerialSync.clusterThreshold_layer1 = 2000
    process.hltSiPixelClustersSerialSync.clusterThreshold_layer1 = 2000
    process.hltSiPixelClustersRegForDisplaced.ClusterThreshold_L1 = 2000

    return process

def customizeHLTforPixelClusterLayer1Threshold_test2000PlusPixelCAPlusMkFitMaxSiStripClus08(process):
    process = customizeHLTforPixelClusterLayer1Threshold_test2000(process)

    process.hltPixelTracksSoA.CAThetaCutBarrel = 0.00111685053
    process.hltPixelTracksSoA.CAThetaCutForward = 0.00249872683
    process.hltPixelTracksSoA.hardCurvCut = 0.695091509
    process.hltPixelTracksSoA.dcaCutInnerTriplet = 0.0419242041
    process.hltPixelTracksSoA.dcaCutOuterTriplet = 0.293522194
    process.hltPixelTracksSoA.phiCuts = [
        832, 379, 481, 765, 1136,
        706, 656, 407, 1212, 404,
        699, 470, 652, 621, 1017,
        616, 450, 555, 572
    ]

    process = customizeHLTIter0ToMkFit(process)
    process.hltSiStripRawToClustersFacility.Clusterizer.MaxClusterSize = 8

    return process

def customizeHLTforPixelClusterLayer1Threshold_test2000PlusPixelCAPlusMkFitMaxSiStripClus16(process):
    process = customizeHLTforPixelClusterLayer1Threshold_test2000PlusPixelCAPlusMkFitMaxSiStripClus08(process)
    process.hltSiStripRawToClustersFacility.Clusterizer.MaxClusterSize = 16
    return process

def customizeHLTforPixelAutoTunedPlusMkFitMsgLoggerTest_baseline(process):
    process = customizeHLTforPixelAutoTunedPlusMkFit_baseline(process)
    del process.MessageLogger
    process.load('FWCore.MessageLogger.MessageLogger_cfi')
    return process

def customizeHLTforPixelAutoTunedPlusMkFitMsgLoggerTest_pixel(process):
    process = customizeHLTforPixelAutoTunedPlusMkFitMsgLoggerTest_baseline(process)
    process.hltPixelTracksSoA.CAThetaCutBarrel = 0.00111685053
    process.hltPixelTracksSoA.CAThetaCutForward = 0.00249872683
    process.hltPixelTracksSoA.hardCurvCut = 0.695091509
    process.hltPixelTracksSoA.dcaCutInnerTriplet = 0.0419242041
    process.hltPixelTracksSoA.dcaCutOuterTriplet = 0.293522194
    process.hltPixelTracksSoA.phiCuts = [
        832, 379, 481, 765, 1136,
        706, 656, 407, 1212, 404,
        699, 470, 652, 621, 1017,
        616, 450, 555, 572
    ]
    return process

def customizeHLTforPixelAutoTunedPlusMkFitMsgLoggerTest_pixelAndMkFit(process):
    process = customizeHLTforPixelAutoTunedPlusMkFitMsgLoggerTest_pixel(process)
    process = customizeHLTIter0ToMkFit(process)
    return process

def customizeHLTforGSFOriginRadius_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)
    process = customizeHLTforCMSSW(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_v1'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforGSFOriginRadius_eleL1TSeeded(process):
    process = customizeHLTforGSFOriginRadius_baseline(process)
    process.hltEleSeedsTrackingRegions.RegionPSet.originRadius = 0.05
    return process

def customizeHLTforGSFOriginRadius_eleAll(process):
    process = customizeHLTforGSFOriginRadius_eleL1TSeeded(process)
    process.hltEleSeedsTrackingRegionsUnseeded.RegionPSet.originRadius = 0.05
    return process

def customizeHLTfor2025Startup_PixelCAwp1(process):
    process.hltPixelTracksSoA.phiCuts = [965, 1241, 395, 698, 1058, 1211, 348, 782, 1016, 810, 463, 755, 694, 531, 770, 471, 592, 750, 348]
    process.hltPixelTracksSoA.dcaCutInnerTriplet = 0.09181130994905196
    process.hltPixelTracksSoA.dcaCutOuterTriplet = 0.4207246178345847
    process.hltPixelTracksSoA.CAThetaCutBarrel = 0.001233027054994468
    process.hltPixelTracksSoA.CAThetaCutForward = 0.003556913217741844
    process.hltPixelTracksSoA.hardCurvCut = 0.5031696900017477
    return process

def customizeHLTfor2025Startup_PixelCAwp2(process):
    process.hltPixelTracksSoA.phiCuts = [617, 767, 579, 496, 900, 1252, 435, 832, 1051, 913, 515, 604, 763, 706, 678, 560, 597, 574, 532]
    process.hltPixelTracksSoA.dcaCutInnerTriplet = 0.07268965383396808
    process.hltPixelTracksSoA.dcaCutOuterTriplet = 0.35106213112457163
    process.hltPixelTracksSoA.CAThetaCutBarrel = 0.001033994253338825
    process.hltPixelTracksSoA.CAThetaCutForward = 0.003640941685013238
    process.hltPixelTracksSoA.hardCurvCut = 0.6592029738506096
    return process

def customizeHLTfor2025Startup_baseline_140X(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.GlobalTag.globaltag = '140X_dataRun3_HLT_v3'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTfor2025Startup_baseline_142X(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.GlobalTag.globaltag = '141X_dataRun3_HLT_v2'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTfor2025Startup_baseline0(process):
    process = customizeHLTforThroughputMeasurements(process)
    process = customizeHLTforCMSSW(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_v1'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTfor2025Startup_baseline1(process):
    process = customizeHLTfor2025Startup_baseline0(process)

    process.hltEleSeedsTrackingRegions.RegionPSet.originRadius = 0.05
    process.hltEleSeedsTrackingRegionsUnseeded.RegionPSet.originRadius = 0.05

    process.hltSiPixelClustersSoA.clusterThreshold_layer1 = 2000
    process.hltSiPixelClusters.clusterThreshold_layer1 = 2000
    process.hltSiPixelClustersSoASerialSync.clusterThreshold_layer1 = 2000
    process.hltSiPixelClustersSerialSync.clusterThreshold_layer1 = 2000
    process.hltSiPixelClustersRegForDisplaced.ClusterThreshold_L1 = 2000

    return process

def customizeHLTfor2025Startup_baseline1_PixelCAwp1_MkFit16(process):
    process = customizeHLTfor2025Startup_baseline1(process)
    process = customizeHLTfor2025Startup_PixelCAwp1(process)
    process = customizeHLTIter0ToMkFit(process)
    process.hltSiStripRawToClustersFacility.Clusterizer.MaxClusterSize = 16
    return process

def customizeHLTfor2025Startup_baseline1_PixelCAwp2_MkFit16(process):
    process = customizeHLTfor2025Startup_baseline1(process)
    process = customizeHLTfor2025Startup_PixelCAwp2(process)
    process = customizeHLTIter0ToMkFit(process)
    process.hltSiStripRawToClustersFacility.Clusterizer.MaxClusterSize = 16
    return process

def customizeHLTforCMSHLT3411_baseline(process):
    process = customizeHLTfor2025Startup_baseline1_PixelCAwp1_MkFit16(process)
    return process

def customizeHLTforCMSHLT3411_target0(process):
    process = customizeHLTforCMSHLT3411_baseline(process)
    process.hltDoubleMuonL3PreFilteredScoutingNoVtx.MinPt = 0
    process.hltDoubleMuonL3FilteredScoutingNoVtx.MinPtMax = [0]
    process.hltDoubleMuonL3FilteredScoutingNoVtx.MinPtMin = [0]
    return process

def customizeHLTforCMSHLT3411_target1(process):
    process = customizeHLTforCMSHLT3411_baseline(process)
    process.DST_PFScouting_DoubleMuon_v6.remove(process.HLTDoubleMuonScoutingNoVtx)
    return process

def customizeHLTforCMSHLT3411_target2(process):
    process = customizeHLTforCMSHLT3411_baseline(process)
    process.hltDoubleMuonL3PreFilteredScoutingNoVtx.MinPt = 0
    process.hltDoubleMuonL3PreFilteredScoutingVtx.MinPt = 0
    del process.hltDoubleMuonL3FilteredScoutingNoVtx
    del process.hltDoubleMuonL3FilteredScoutingVtx
    return process

def customizeHLTforCMSHLT3459_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)
    process = customizeHLTforCMSSW(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_v1'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforCMSHLT3459_PixelCAwp1(process):
    process = customizeHLTforCMSHLT3459_baseline(process)
    process = customizeHLTfor2025Startup_PixelCAwp1(process)
    return process

def customizeHLTforCMSHLT3459_PixelCAwp1_GlobalSiStripsUnpack(process):
    process = customizeHLTforCMSHLT3459_PixelCAwp1(process)
    process.hltSiStripRawToClustersFacility.onDemand = False
    return process

def customizeHLTforCMSHLT3459_PixelCAwp1_MkFit16(process):
    process = customizeHLTforCMSHLT3459_PixelCAwp1_GlobalSiStripsUnpack(process)
    process = customizeHLTIter0ToMkFit(process)
    process.hltSiStripRawToClustersFacility.Clusterizer.MaxClusterSize = 16
    return process

def customizeHLTfor2025Startup_baseline_forCMSSW150X(process):
    process = customizeHLTforThroughputMeasurements(process)
    process = customizeHLTforCMSSW(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_v1'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforCMSHLT3478_target(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_v1'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforCMSHLT3478_baseline(process):
    process = customizeHLTforCMSHLT3478_target(process)

    del process.HLT_MonitorL1TPureRate_AXO_v1
    del process.HLT_MonitorL1TPureRate_CICADA_v1

    return process

def customizeHLTforCMSHLT3479(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_v1'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

def customizeHLTforCMSHLT3480(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_v1'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    return process

from HLTrigger.Configuration.common import *

def customizeHLTfor2025HCALPFCuts(process):
    try:
        process.GlobalTag.toGet += [
            cms.PSet(
                record = cms.string('HcalPFCutsRcd'),
                tag = cms.string('HcalPFCuts_2025_mc'),
            ),
        ]
    except:
        raise RuntimeError("customizeHLTfor2025HCALPFCuts -- GlobalTag ESSource could not be customized !")

    return process

def customizeHLTfor2025PFHadronCalibrations(process):
    try:
        process.GlobalTag.toGet += [
            cms.PSet(
                record = cms.string('PFCalibrationRcd'),
                tag = cms.string('PFCalibration_Run3Winter25_MC_hlt_v1'),
                label = cms.untracked.string('HLT'),
            ),
        ]
    except:
        raise RuntimeError("customizeHLTfor2025PFHadronCalibrations -- GlobalTag ESSource could not be customized !")

    return process

def customizeHLTforCMSHLT3469(process):
    for prod in producers_by_type(process, 'CaloTowersCreator'):
        prod.EcalRecHitThresh = True
    return process

def customizeHLTfor2025JECs(process):
    jecTagsDict = {
        'AK4CaloHLT': 'JetCorrectorParametersCollection_Run3Winter25Digi_AK4CaloHLT_v2',
        'AK8CaloHLT': 'JetCorrectorParametersCollection_Run3Winter25Digi_AK8CaloHLT_v2',
        'AK4PFHLT': 'JetCorrectorParametersCollection_Run3Winter25Digi_AK4PFHLT_v2',
        'AK8PFHLT': 'JetCorrectorParametersCollection_Run3Winter25Digi_AK8PFHLT_v2',
    }

    try:
        for (labelName, tagName) in jecTagsDict.items():
            process.GlobalTag.toGet += [
                cms.PSet(
                    record = cms.string("JetCorrectionsRecord"),
                    label = cms.untracked.string(labelName),
                    tag = cms.string(tagName),
                ),
            ]
    except:
        raise RuntimeError("customizeHLTfor2025JECs -- GlobalTag ESSource could not be customized !")

    return process

def customizeHLTfor2025Studies(process):
    process = customizeHLTfor2025HCALPFCuts(process)
    process = customizeHLTfor2025PFHadronCalibrations(process)
    process = customizeHLTforCMSHLT3469(process)
    process = customizeHLTfor2025JECs(process)
    return process

def customizeHLTfor2024L1TMenu(process):
    seed_replacements = {

        'L1_SingleMu5_BMTF' : 'L1_AlwaysTrue',
        'L1_SingleMu13_SQ14_BMTF': 'L1_AlwaysTrue',

        'L1_AXO_Medium' : 'L1_AXO_Nominal',
        'L1_AXO_VVTight': 'L1_AlwaysTrue',
        'L1_AXO_VVVTight': 'L1_AlwaysTrue',

        'L1_CICADA_VVTight': 'L1_AlwaysTrue',
        'L1_CICADA_VVVTight': 'L1_AlwaysTrue',
        'L1_CICADA_VVVVTight': 'L1_AlwaysTrue',

        'L1_DoubleTau_Iso34_Iso26_er2p1_Jet55_RmOvlp_dR0p5': 'L1_DoubleIsoTau26er2p1_Jet55_RmOvlp_dR0p5 OR L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5',
        'L1_DoubleTau_Iso38_Iso26_er2p1_Jet55_RmOvlp_dR0p5': 'L1_DoubleIsoTau26er2p1_Jet55_RmOvlp_dR0p5 OR L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5',
        'L1_DoubleTau_Iso40_Iso26_er2p1_Jet55_RmOvlp_dR0p5': 'L1_DoubleIsoTau26er2p1_Jet55_RmOvlp_dR0p5 OR L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5',

        'L1_DoubleTau_Iso34_Iso23_er2p1_Jet55_RmOvlp_dR0p5': 'L1_DoubleIsoTau26er2p1_Jet55_RmOvlp_dR0p5 OR L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5',
        'L1_DoubleTau_Iso34_Iso23_er2p1_Jet70_RmOvlp_dR0p5': 'L1_DoubleIsoTau26er2p1_Jet55_RmOvlp_dR0p5 OR L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5',
        'L1_DoubleTau_Iso34_Iso26_er2p1_Jet70_RmOvlp_dR0p5': 'L1_DoubleIsoTau26er2p1_Jet55_RmOvlp_dR0p5 OR L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5',

        'L1_DoubleEG15_11_er1p2_dR_Max0p6': 'L1_DoubleEG11_er1p2_dR_Max0p6',
        'L1_DoubleEG16_11_er1p2_dR_Max0p6': 'L1_DoubleEG11_er1p2_dR_Max0p6',
        'L1_DoubleEG17_11_er1p2_dR_Max0p6': 'L1_DoubleEG11_er1p2_dR_Max0p6',

        'L1_DoubleEG15_er1p5_dEta_Max1p5': 'L1_AlwaysTrue',
        'L1_DoubleEG16_er1p5_dEta_Max1p5': 'L1_AlwaysTrue',
        'L1_DoubleEG17_er1p5_dEta_Max1p5': 'L1_AlwaysTrue',

        'L1_DoubleJet_110_35_DoubleJet35_Mass_Min1000': 'L1_AlwaysTrue',
        'L1_DoubleJet_110_35_DoubleJet35_Mass_Min1100': 'L1_AlwaysTrue',
        'L1_DoubleJet_110_35_DoubleJet35_Mass_Min1200': 'L1_AlwaysTrue',
        'L1_DoubleJet45_Mass_Min700_IsoTau45er2p1_RmOvlp_dR0p5': 'L1_AlwaysTrue',
        'L1_DoubleJet45_Mass_Min800_IsoTau45er2p1_RmOvlp_dR0p5': 'L1_AlwaysTrue',
        'L1_DoubleJet_65_35_DoubleJet35_Mass_Min750_DoubleJetCentral50': 'L1_AlwaysTrue',
        'L1_DoubleJet_65_35_DoubleJet35_Mass_Min850_DoubleJetCentral50': 'L1_AlwaysTrue',
        'L1_DoubleJet_65_35_DoubleJet35_Mass_Min950_DoubleJetCentral50': 'L1_AlwaysTrue',
        'L1_DoubleJet45_Mass_Min700_LooseIsoEG20er2p1_RmOvlp_dR0p2': 'L1_AlwaysTrue',
        'L1_DoubleJet45_Mass_Min800_LooseIsoEG20er2p1_RmOvlp_dR0p2': 'L1_AlwaysTrue',
        'L1_DoubleJet_85_35_DoubleJet35_Mass_Min700_Mu3OQ': 'L1_AlwaysTrue',
        'L1_DoubleJet_85_35_DoubleJet35_Mass_Min800_Mu3OQ': 'L1_AlwaysTrue',
        'L1_DoubleJet_85_35_DoubleJet35_Mass_Min900_Mu3OQ': 'L1_AlwaysTrue',
        'L1_DoubleJet_70_35_DoubleJet35_Mass_Min600_ETMHF65': 'L1_AlwaysTrue',
        'L1_DoubleJet_70_35_DoubleJet35_Mass_Min700_ETMHF65': 'L1_AlwaysTrue',
        'L1_DoubleJet_70_35_DoubleJet35_Mass_Min800_ETMHF65': 'L1_AlwaysTrue',
    }

    for module in filters_by_type(process, 'HLTL1TSeed'):
        l1Seed = module.L1SeedsLogicalExpression.value()
        if any(old_seed in l1Seed for old_seed in seed_replacements):
            for old_seed, new_seed in seed_replacements.items():
                l1Seed = l1Seed.replace(old_seed, new_seed)
            module.L1SeedsLogicalExpression = cms.string(l1Seed)

    return process

def customizeHLTforFullDoubletRecovery(process):
    layerPairs = [
        'BPix1+BPix2', 'BPix1+BPix3', 'BPix1+BPix4', 'BPix2+BPix3',
        'BPix2+BPix4', 'BPix3+BPix4', 'BPix1+FPix1_pos', 'BPix1+FPix1_neg',
        'BPix1+FPix2_pos', 'BPix1+FPix2_neg', 'BPix1+FPix3_pos', 'BPix1+FPix3_neg',
        'BPix2+FPix1_pos', 'BPix2+FPix1_neg', 'BPix2+FPix2_pos', 'BPix2+FPix2_neg',
        'BPix3+FPix1_pos', 'BPix3+FPix1_neg', 'FPix1_pos+FPix2_pos', 'FPix1_neg+FPix2_neg',
        'FPix1_pos+FPix3_pos', 'FPix1_neg+FPix3_neg', 'FPix2_pos+FPix3_pos', 'FPix2_neg+FPix3_neg',
    ]
    process.hltDoubletRecoveryPixelLayersAndRegions.layerList = layerPairs[:]
    process.hltDoubletRecoveryPixelLayersAndRegionsSerialSync.layerList = layerPairs[:]
    return process

def customizeHLTforCMSHLT3459_for2025_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_v1'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    process = customizeHLTfor2025Studies(process)
    process = customizeHLTfor2024L1TMenu(process)

    return process

def customizeHLTforCMSHLT3459_for2025_FullDoubletRecovery(process):
    process = customizeHLTforCMSHLT3459_for2025_baseline(process)
    process = customizeHLTforFullDoubletRecovery(process)
    return process

def customizeHLTforCMSHLT3459_for2025_PixelCAwp1(process):
    process = customizeHLTforCMSHLT3459_for2025_baseline(process)
    process = customizeHLTfor2025Startup_PixelCAwp1(process)
    return process

def customizeHLTforCMSHLT3459_for2025_PixelCAwp1_MkFit16(process):
    process = customizeHLTforCMSHLT3459_for2025_PixelCAwp1(process)
    process = customizeHLTIter0ToMkFit(process)
    process.hltSiStripRawToClustersFacility.Clusterizer.MaxClusterSize = 16
    return process

def customizeHLTforCMSHLT3459_for2025_PixelCAwp1_MkFit16_FullDoubletRecovery(process):
    process = customizeHLTforCMSHLT3459_for2025_PixelCAwp1_MkFit16(process)
    process = customizeHLTforFullDoubletRecovery(process)
    return process

def customizeHLTforTestLowPtDoubleEG(process):

    process = customizeHLTforThroughputMeasurements(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_v1'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    process = customizeHLTfor2024L1TMenu(process)

    return process

def customizeHLTforCMSHLT3484(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_forTriggerStudies_v4'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    process = customizeHLTfor2024L1TMenu(process)

    return process

def customizeHLTforTestLowPtDoubleEG_newParams(process):
    process = customizeHLTforTestLowPtDoubleEG(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_forTriggerStudies_v4'

    process = customizeHLTfor2025Startup_PixelCAwp1(process)
    process = customizeHLTIter0ToMkFit(process)
    process.hltSiStripRawToClustersFacility.Clusterizer.MaxClusterSize = 16

    for moduleLabel in [
        'hltDiphoton1510TightIDECALTrackIsoDr0p2to0p4DrPreFilter',
        'hltDiphoton1510TightIDECALTrackIsoDr0p2to0p4DrFilter',
        'hltDiEG5TightIDECALTrackIsoDr0p2to0p4DrPreFilter',
        'hltDielectron125TightIDECALTrackIsoDr0p2to0p4DrFilter',
    ]:
        if not hasattr(process, moduleLabel):
            continue
        module = getattr(process, moduleLabel)
        module.lowerdRCut = cms.double( 0.0 )
        module.upperdRCut = cms.double( 0.3 )

    return process

def customizeHLTforTestLowPtDoubleEG_newParams_barrelOnly(process):
    process = customizeHLTforTestLowPtDoubleEG_newParams(process)

    try:
        process.hltEG12TightIDMWL1SingleAndDoubleEGAndDoubleEGEBEBOrEtFilter.minEtaCut = -1.479
        process.hltEG12TightIDMWL1SingleAndDoubleEGAndDoubleEGEBEBOrEtFilter.maxEtaCut = +1.479
        process.hltDiEG5TightIDMWEtUnseededFilter.minEta = -1.479
        process.hltDiEG5TightIDMWEtUnseededFilter.MaxEta = +1.479
    except:
        pass

    return process

def customizeHLTforCMSHLT3516_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_forTriggerStudies_v4'

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    process = customizeHLTfor2024L1TMenu(process)

    return process

def customizeHLTforCMSHLT3516_target(process):
    process = customizeHLTforCMSHLT3516_baseline(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_forTriggerStudies_v5'
    process = customizeHLTforCMSHLT3469(process)

    return process

def customizeHLTforCMSHLT3516_baseline_PixelCAwp1_MkFit16(process):
    process = customizeHLTforCMSHLT3516_baseline(process)

    process = customizeHLTfor2025Startup_PixelCAwp1(process)
    process = customizeHLTIter0ToMkFit(process)
    process.hltSiStripRawToClustersFacility.Clusterizer.MaxClusterSize = 16

    return process

def customizeHLTforCMSHLT3516_target_PixelCAwp1_MkFit16(process):
    process = customizeHLTforCMSHLT3516_baseline_PixelCAwp1_MkFit16(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_forTriggerStudies_v5'
    process = customizeHLTforCMSHLT3469(process)

    return process

def customizeHLTforCMSHLT3529_baseline(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    process = customizeHLTfor2024L1TMenu(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_forTriggerStudies_v3'
    process = customizeHLTfor2025Studies(process)

    return process

def customizeHLTforCMSHLT3459_baseline2(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    process = customizeHLTfor2024L1TMenu(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_forTriggerStudies_v3'
    process = customizeHLTfor2025Studies(process)

    return process

def customizeHLTforCMSHLT3529_baseline2(process):
    process = customizeHLTforThroughputMeasurements(process)

    process.PrescaleService.lvl1DefaultLabel = '2p0E34'
    process.PrescaleService.forceDefault = True

    process = customizeHLTfor2024L1TMenu(process)

    process.GlobalTag.globaltag = '150X_dataRun3_HLT_forTriggerStudies_v6'
    process = customizeHLTforCMSHLT3469(process)

    return process
