#!/bin/bash -ex

runNumber=375790

https_proxy=http://cmsproxy.cms:3128/ \
hltConfigFromDB --configName --adg /cdaq/test/missirol/dev/CMSSW_14_1_0/CMSHLT_3387/Test01/HLT/V3 > hlt.py

cp /gpu_data/store/hidata/HIRun2023*/HIEphemeralHLTPhysics/FED/v*/run"${runNumber}"_cff.py .

cat <<@EOF >> hlt.py

process.load('run${runNumber}_cff')

from customizeHLTforThroughputMeasurements import customizeHLTforCMSHLT3387_hidata2023_baseline
process = customizeHLTforCMSHLT3387_hidata2023_baseline(process)

process.maxEvents.input = 700

process.options.numberOfThreads = 1
process.options.numberOfStreams = 0

#del process.PrescaleService

del process.MessageLogger
process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.ThroughputService = cms.untracked.PSet()
process.MessageLogger.L1TGlobalSummary = cms.untracked.PSet()
process.MessageLogger.FastReport = cms.untracked.PSet()

process.hltL1TGlobalSummary = cms.EDAnalyzer("L1TGlobalSummary",
    AlgInputTag = cms.InputTag( "hltGtStage2Digis" ),
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    MinBx = cms.int32( 0 ),
    MaxBx = cms.int32( 0 ),
    DumpTrigResults = cms.bool( False ),
    DumpRecord = cms.bool( False ),
    DumpTrigSummary = cms.bool( True ),
    ReadPrescalesFromFile = cms.bool( False ),
    psFileName = cms.string( "prescale_L1TGlobal.csv" ),
    psColumn = cms.int32( 0 )
)

process.HLTAnalyzerEndpath = cms.EndPath( process.hltGtStage2Digis + process.hltL1TGlobalSummary )
process.schedule.append(process.HLTAnalyzerEndpath)

process.options.wantSummary = True

# remove all output streams
streamPaths = [pathName for pathName in process.finalpaths_()]
for foo in streamPaths:
    process.__delattr__(foo)
@EOF

rm -rf run"${runNumber}"
mkdir -p run"${runNumber}"

cmsRun hlt.py &> hlt.log
