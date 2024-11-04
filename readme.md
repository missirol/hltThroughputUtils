
Setup instructions
==================

The instructions are work in progress.
```bash
ssh hilton-c2b02-44-01
```

```bash
dirName=MY_TEST_DIR
cmsswRel=CMSSW_14_0_13_MULTIARCHS

export SCRAM_ARCH=el8_amd64_gcc12
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SITECONFIG_PATH="/opt/offline/SITECONF/local"

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

kinit $(logname)@CERN.CH
ssh -f -N -D18081 $(logname)@cmsusr.cms

mkdir -p /fff/user/"${USER}"/"${dirName}"
cd /fff/user/"${USER}"/"${dirName}"

cmsrel "${cmsswRel}"
cd "${cmsswRel}"/src
cmsenv
scram b
cd "${OLDPWD}"

git clone git@github.com:missirol/hltThroughputUtils.git -o missirol -b master

cd hltThroughputUtils

git clone git@github.com:missirol/patatrack-scripts.git -o missirol -b master                 -- patatrack-scripts
git clone git@github.com:missirol/patatrack-scripts.git -o missirol -b hilton-c2b02-44-01_cpu -- patatrack-scripts.cpu
git clone git@github.com:missirol/patatrack-scripts.git -o missirol -b hilton-c2b02-44-01_gpu -- patatrack-scripts.gpu
```

Measurements
============

```
./run_240331.sh /users/missirol/test/dev/CMSSW_14_0_0/tmp/240331_ThroughputMeasurements/TimingTest_01/GRun/V3 test240331_GRunV79
```

`240414_testCMSHLT3156`
 ```
 ./run_240414_testCMSHLT3156.sh out_240414_testCMSHLT3156_d766c5c
 ```
 - Run 379416, LS 126-128 (1200 bunches, Run2024C).
 - 40100 events in input.
 - L1T: 2024-v1_0_0.
 - HLT: same as online (v1.0.9).


`240416_testCMSHLT3156`
 ```
 ./run_240416_testCMSHLT3156.sh out_240416_testCMSHLT3156_523e197
 ```
 - Same as "240414_testCMSHLT3156", but a different HLT menu and PS column.
 - HLT: `/online/collisions/2024/2e34/v1.1/HLT/V4` (V1.1).
   - ECAL-Tracker "windows" set to nominal.
 - PS column: "2p0E34".


`240419_testCMSHLT3156`
 ```
 ./run_240419_testCMSHLT3156.sh out_240419_testCMSHLT3156_1381685
 ```
 - Run 379530, LS 465-467 (1800b, Run2024C).
 - HLT: `/cdaq/physics/Run2024/2e34/v1.0.10/HLT/V3` (V1.0).
 - PS column: "2p0E34".
 - Goal: reproduce HLT-throughput measurement performed online (111 kHz, 190 FUs).

`240422_testCMSHLT3156`
 ```
 ./run_240422_testCMSHLT3156.sh out_240422_testCMSHLT3156_ee5c719
 ```
 - Same as `240419_testCMSHLT3156`, with small adjustments suggested by Andrea.
     - PS column: same as online (i.e. "2p0E34+HLTPhysics"), with no explicit customisation.
     - `source.maxBufferedFiles = 2` (like online).
     - Remove L1T-seed changes (should have literally no impact).
     - Run 379530, LS 465-467 (1800b, Run2024C).
     - HLT: `/cdaq/physics/Run2024/2e34/v1.0.10/HLT/V3` (V1.0).
 - Goal: confirm, or not, the results of `240419_testCMSHLT3156`.

`240423_testCMSHLT3156`
 ```
 ./run_240423_testCMSHLT3156.sh out_240423_testCMSHLT3156_310bb19
 ```
 - Run 379660, LS 425-430 (1800b, Run2024C).
 - HLT: `/cdaq/physics/Run2024/2e34/v1.0.10/HLT/V3` (V1.0).
 - PS column: same as online (i.e. "2p0E34+HLTPhysics"), with no explicit customisation.
 - `source.maxBufferedFiles = 2` (like online).
 - Goal: confirm, or not, the results of `240422_testCMSHLT3156`.

`240424_testCMSHLT3156`
 ```
 ./run_240424_testCMSHLT3156.sh out_240424_testCMSHLT3156_624d45b
 ```
 - Run 379866, LS 165-169 (1200b, Run2024C).
 - HLT: `/cdaq/physics/Run2024/2e34/v1.0.10/HLT/V5` (V1.0).
 - PS column: same as online (i.e. "2p0E34+HLTPhysics"), with no explicit customisation.
 - `source.maxBufferedFiles = 2` (like online).
 - Goal: confirm, or not, the results of previous measurements.

`240427_testCMSHLT3156`
 ```
 ./run_240427_testCMSHLT3156.sh out_240427_testCMSHLT3156_694bc83
 ```
 - Run 380030, LS 112-116 (2200b, Run2024C).
 - HLT: `/cdaq/physics/Run2024/2e34/v1.0.11/HLT/V2` (V1.0).
 - PS column: same as online (i.e. "2p0E34+HLTPhysics"), with no explicit customisation.
 - `source.maxBufferedFiles = 2` (like online).
 - Goal: confirm, or not, the results of previous measurements and the online measurement.

`240428_testCMSHLT3156`
 ```
 ./run_240428_testCMSHLT3156.sh out_240428_testCMSHLT3156_d86987f
 ```
 - Run 370293, LS 241-242 (2452b, Run2023D).
 - HLT: `/cdaq/physics/Run2023/2e34/v1.2.3/HLT/V3` (same as online).
 - PS column: same as online (i.e. "2p0E34+HLTPhysics"), with no explicit customisation.
 - `source.maxBufferedFiles = 2` (like online).
 - Goal: compare to the values observed online in 2023.

`240430_testCMSHLT3156`
 ```
 ./run_240430_testCMSHLT3156.sh out_240430_testCMSHLT3156_e1375f2
 ```
 - Run 380030, LS 112-116 (2200b, Run2024C).
 - HLT: `/cdaq/physics/Run2024/2e34/v1.0.11/HLT/V2` (V1.0).
 - PS column: same as online (i.e. "2p0E34+HLTPhysics"), with no explicit customisation.
 - `source.maxBufferedFiles = 2` (like online).
 - Goal: estimate impact of using hyper-threading in HLT-throughput measurements.
   - no explicit disabling of hyper-threading,
     just measurements with different number of jobs/threads/streams

`240501_testCMSHLT3156`
 ```
 ./run_240501_testCMSHLT3156.sh out_240501_testCMSHLT3156_00fb1f1
 ```
 - Run 380030, LS 112-116 (2200b, Run2024C).
 - HLT: `/cdaq/physics/Run2024/2e34/v1.0.11/HLT/V2` (V1.0).
 - PS column: same as online (i.e. "2p0E34+HLTPhysics"), with no explicit customisation.
 - `source.maxBufferedFiles = 2` (like online).
 - Goal: estimate impact of using hyper-threading in HLT-throughput measurements.
 - Different benchmark settings compared to "240430_testCMSHLT3156".
   - vanilla patatrack-scripts
   - no explicit disabling of hyper-threading,
     just measurements with different number of jobs/threads/streams

`240518_testCMSHLT3196`
 ```
 ./run_240518_testCMSHLT3196.sh out_240518_testCMSHLT3196_806c8ba
 ```
 - Goal: test impact of possible changes discussed in CMSHLT-3196.
 - Run 380647, LS 191-194 (2340b, Run2024D).
 - Machine: `hilton-c2b02-44-01`.
 - Settings as close as possible to online.
   - HLT menu: same as online, i.e. `/cdaq/physics/Run2024/2e34/v1.1.4/HLT/V1`.
   - PS column: same as online, i.e. "1p8E34+ZeroBias+HLTPhysics" (no explicit customisation).
   - `source.maxBufferedFiles = 2`.
   - MPS enabled, multi-threading enabled.
   - Explicit GPU assignment to NUMA domains (modified version of patatrack-scripts).
 - 4 configurations tested in addition to baseline (see `customizeHLTforThroughputMeasurements.py`).
   - `CCCLooseInAll`: CCCNone set to 1620 (affecting every module using CCCNone).
   - `CCCLooseInSiStripUnpacker`: CCCLoose in `SiStripClusterizerFromRaw`.
   - `CCCLooseInRefToPSetSubsetA`: CCCLoose in all `refToPSet_` using CCCNone except for `SiStripClusterizerFromRaw`.
   - `CCCLooseInRefToPSetSubsetB`: CCCLoose only in a small arbitrary subset of modules not used in "standard" triggers.
   - `CCCLooseInRefToPSetSubsetC`: CCCLoose only in `HLTPSetTrajectoryFilterForElectrons`.

 ```
 ./run_240518_testCMSHLT3196.sh out_240518_testCMSHLT3196_87d5ce4
 ```
 - Tested 3 more variants, now based on modifying the ESProducers of type Chi2ChargeMeasurementEstimatorESProducer.
   - `CCCLooseInRefToPSetSubsetD`: muons.
   - `CCCLooseInRefToPSetSubsetE`: muons and electrons.
   - `CCCLooseInRefToPSetSubsetF`: muons, electrons and else.
   - For further details, see CMSHLT-3196.

`240524_testCMSHLT3212`
 ```
 ./run_240524_testCMSHLT3212.sh out_240524_testCMSHLT3212_437aa2c
 ```
 - Goal: test impact of changes discussed in CMSHLT-3212.
 - Run 380647, LS 191-194 (2340b, Run2024D).
 - Machine: `hilton-c2b02-44-01`.
 - Settings as close as possible to online.
   - HLT menu: same as online, i.e. `/cdaq/physics/Run2024/2e34/v1.1.4/HLT/V1`.
   - PS column: same as online, i.e. "1p8E34+ZeroBias+HLTPhysics" (no explicit customisation).
   - `source.maxBufferedFiles = 2`.
   - MPS enabled, multi-threading enabled.
   - Explicit GPU assignment to NUMA domains (modified version of patatrack-scripts).

`240601_testCMSHLT3137`
 ```
 ./run_240601_testCMSHLT3137.sh out_240601_testCMSHLT3137_ef868c8
 ```
 - Goal: understand differences between manual measurements and timing-server measurements.
 - Run 381065, LS 449-458 (2340b, Run2024E).
 - Machines: `hilton-c2b02-44-01` or `srv-b1b07-16-01`.
 - Settings.
   - HLT menu: same as online, i.e. `/cdaq/physics/Run2024/2e34/v1.2.1/HLT/V1`.
   - PS column: same as online, i.e. `2p0E34+ZeroBias+HLTPhysics` (no explicit customisation).
   - Source settings as in the timing-server configuration (e.g. `source.maxBufferedFiles = 8`).
   - With and without MPS (multi-threading enabled).
   - No explicit GPU assignment to NUMA domains (vanilla version of patatrack-scripts).

`240602_testCMSHLT3137`
 ```
 ./run_240602_testCMSHLT3137.sh out_240602_testCMSHLT3137_6fdd737
 ```
 - Goal: try and reproduce the values returned by the timing server, using the same exact cfg as the timing server.
 - Applied a series of customisations to understand if any of these lead to any significant slowdown.

`240608_testCMSHLT3232`
 ```
 ./run_240608_testCMSHLT3232.sh out_240608_testCMSHLT3232_80451cb
 ./run_240608_testCMSHLT3232_timingServerCfg.sh out_240608_testCMSHLT3232_80451cb_timingServerCfg_nowarmup
 ```
 - Goal: try and reproduce the values returned by the timing server.
 - "test01": standard measurement, to be compared to the timing server
   (applying a customisation function to the config used by the timing server).
 - "timingServerCfg" uses directly a cfg taken from the timing server outputs
   (in this particular case, the timing-server scripts was modified in order
   not to edit the configuration parameters of the FastTimerService)

 ```
 ./run_240608_testCMSHLT3232_timingServerCfg_srv-b1b07-16-01.sh out_240608_testCMSHLT3232_80451cb_timingServerCfg_nowarmup_nvidiaPersistenceOn_squidOn
 ```
 - Measurement on srv-b1b07-16-01 after activating the squid service (Jun-10, 2024).
 - No visible impact on HLT throughput.
   - Unclear to me if the services `frontier-squid` on `hilton-c2b02-44-01` and `squid` on `srv-b1b07-16-01` are equivalent.

`240719_testCMSHLT3288`
 ```
 ./run_240719_testCMSHLT3288.sh out_240719_testCMSHLT3288_1a6b65d
 ```
 - Goal: quantify impact of CMSHLT-3288.
 - Input sample: run-383363, LS 193-196 (PU ~64).
 - Menu: same as used in run-383363 (i.e. `/cdaq/physics/Run2024/2e34/v1.3.0/HLT/V3`).
 - NVIDIA MPS enabled.

`240720_testCMSHLT3288`
 ```
 ./run_240720_testCMSHLT3288.sh out_240720_testCMSHLT3288_3938330
 ```
 - Goal: quantify impact of CMSHLT-3288 on latest GRun menu (candidate v1.4 menu).
 - Same as `240719_testCMSHLT3288`, except for the HLT menu used.
 - HLT menu: `/users/missirol/test/dev/CMSSW_14_0_0/CMSHLT_3288/Ref01/HLT/V2`
   (online GRun menu derived from `/dev/CMSSW_14_0_0/HLT/V187`
   without CICADA-related triggers in order not to break compatibility with the L1T menu used in run-38363,
   after migration of HCAL local reco to Alpaka).

`240721_testCMSHLT3288`
 ```
 ./run_240721_testCMSHLT3288.sh out_240721_testCMSHLT3288_60d95b7
 ```
 - Goal: quantify impact of CMSHLT-3288 on a recent GRun menu before HCAL-Alpaka updates.
 - Same as `240720_testCMSHLT3288`, except for the HLT menu used.
 - HLT menu: `/users/missirol/test/dev/CMSSW_14_0_0/CMSHLT_3288/Ref00/HLT/V2`
   (online GRun menu derived from `/dev/CMSSW_14_0_0/HLT/V183`
   without CICADA-related triggers in order not to break compatibility with the L1T menu used in run-38363,
   before migration of HCAL local reco to Alpaka).

`240731_testCMSHLT3302`
 ```
 ./run_240731_testCMSHLT3302.sh out_240721_testCMSHLT3302_86748af
 ```
 - Goal: quantify impact of CMSHLT-3302.
 - Input sample: run-383631, LS 476-479 (PU ~64).

`240915_testCMSHLT3284`
 ```
 ./run_240915_testCMSHLT3284.sh out_240915_testCMSHLT3284_a5ccc42
 ```
 - Goal: quantify impact of CMSHLT-3284 on HLT timing.
 - Input sample: 2023 HI data (EphemeralHLTPhysics), run-375720.
 - Release: CMSSW_14_0_15_patch1, x86-64-v3 enabled.

`241102_testCMSHLT3387_l1skim2024`
 ```
 ./run_241102_testCMSHLT3387_l1skim2024.sh out_241102_testCMSHLT3387_l1skim2024_c023f78
 ```
 - Goal: quantify HLT timing of a realistic 2024 HLT PbPb menu.
 - Input sample: skim of 2023 HI data (HIEphemeralZeroBias), run-375720.
 - Release: CMSSW_14_1_4_patch3, x86-64-v3 enabled, NVIDIA MPS enabled.

`241103_testCMSHLT3387_hidata2023`
 ```
 ./run_241103_testCMSHLT3387_hidata2023.sh out_241103_testCMSHLT3387_hidata2023_c023f78
 ```
 - Goal: quantify HLT timing of a realistic 2024 HLT PbPb menu,
   including impact of "Test08" in CMSHLT-3387 (FastTimerService customisation).
 - Input sample: 2023 HI data (HIEphemeralHLTPhysics), run-375790.
 - Menu customised to be compatible with 2023 PbPb menu.
 - Release: CMSSW_14_1_4_patch3, x86-64-v3 enabled, NVIDIA MPS enabled.
