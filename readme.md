
Setup instructions
==================

The instructions are work in progress.
```bash
ssh hilton-c2b02-44-01
```

```bash
dirName=MY_TEST_DIR
cmsswRel=CMSSW_15_0_0_pre2

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

git clone git@github.com:missirol/patatrack-scripts.git -o missirol -b master_old -- patatrack-scripts
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

`241109_testCMSHLT3387_hidata2024`
 ```
 ./run_241109_testCMSHLT3387_hidata2024.sh out_241109_testCMSHLT3387_hidata2024_9538c3d
 ```
 - Goal: reproduce timing of 2024 PbPb menu on 2024 PbPb data.
 - Input sample: 2024 PbPb data (HIEphemeralHLTPhysics), run-387973.
 - Same menu and prescales as used online in run-387973.
 - Release: CMSSW_14_1_4_patch3, x86-64-v3 enabled, NVIDIA MPS enabled.

`241220_testGSFOriginRadius_v01`
 ```
 ./run_241220_testGSFOriginRadius_v01.sh out_241220_testGSFOriginRadius_v01_ea71d35
 ```
 - Goal: quantify impact of GSF-tracking update (hltEleSeedsTrackingRegions.RegionPSet.originRadius = 0.05).
 - Input sample: EphemeralHLTPhysics, ~40K events of run-383631, LS 476-479 (PU ~64).
 - Release: CMSSW_14_0_19_patch2, x86-64-v3 enabled, NVIDIA MPS enabled.
 - Done on `hilton-c2b01-44-01`, using 8 jobs with 32 threads and 24 streams per job.

`241220_testPixelAutoTunedCA_v01`
 ```
 ./run_241220_testPixelAutoTunedCA_v01.sh out_241220_testPixelAutoTunedCA_v01_ea71d35
 ```
 - Goal: quantify impact of auto-tuned pixel-CA parameters (see TSG meeting on Dec-10).
 - Input sample: EphemeralHLTPhysics, ~40K events of run-383631, LS 476-479 (PU ~64).
 - Release: CMSSW_14_0_19_patch2, x86-64-v3 enabled, NVIDIA MPS enabled.
 - Done on `hilton-c2b01-44-01`, using 8 jobs with 32 threads and 24 streams per job.

`250117_cmssw47070`
 ```
 ./run_250117_cmssw47070.sh out_250117_cmssw47070_0587d2d
 ```
 - Goal: comparing 15_0_X IBs before and after cms-sw/cmssw#47070.
 - Input data: run-383631, LSs 476-479, ~40k events (PU ~64).
 - HLT menu: `/dev/CMSSW_14_2_0/GRun/V11` (current GRun menu).
 - Done on `hilton-c2b01-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250126_testPixelAutoTunedPlusMkFit`
 ```
 ./run_250126_testPixelAutoTunedPlusMkFit.sh out_250126_testPixelAutoTunedPlusMkFit_0feab92
 ```
 - Goal: measure timing of 2 tracking updates targeting 2025 startup.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: CMSSW_15_0_0_pre2.
 - HLT menu: `/dev/CMSSW_14_2_0/GRun/V11`.
 - Done on `hilton-c2b01-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250202_testPixelClusterLayer1Threshold`
 ```
 ./run_250202_testPixelClusterLayer1Threshold.sh out_250202_testPixelClusterLayer1Threshold_8a4edbd
 ```
 - Goal: measure impact on timing of reduction of min-cluster charge in BPix Layer-1.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: CMSSW_15_0_0_pre3.
 - HLT menu: `/dev/CMSSW_14_2_0/GRun/V11`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250208_testGSFOriginRadius`
 ```
 ./run_250208_testGSFOriginRadius.sh out_250208_testGSFOriginRadius_6938d93
 ```
 - Goal: measure impact on timing of CMSHLT-3413 (incl. unseeded module).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: CMSSW_15_0_0_pre3.
 - HLT menu: `/dev/CMSSW_14_2_0/GRun/V11`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250214_test2025Startup`
 ```
 ./run_250214_test2025Startup.sh out_250214_test2025Startup_patatrack-scripts-746bcbd_3590cac
 ```
 - Goal: measure impact on timing of several updates targeting 2025 data-taking (CMSHLT-3413, CMSHLT-3422, latest CA tunes for CMSHLT-3421).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_1_X_2025-02-14-2300` (to include cms-sw/cmssw#47346).
 - HLT menu: `/dev/CMSSW_14_2_0/GRun/V11`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250215_testCMSHLT3411`
 ```
 ./run_250215_testCMSHLT3411.sh out_250215_testCMSHLT3411_patatrack-scripts-746bcbd_
 ```
 - Goal: check impact of CMSHLT-3411 (new Vtx Path, plus filters with pT=0).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_X` IBs post-pre3.
 - HLT menu: `/users/missirol/test/dev/CMSSW_14_2_0/CMSHLT_3411/Test02/GRun/V2`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250217_validateCMSSW_15_0_0_pre3`
 ```
 ./run_250217_validateCMSSW_15_0_0_pre3.sh out_250217_validateCMSSW_15_0_0_pre3_patatrack-scripts-dca218c_aa64f97
 ```
 - Goal: measure throughput in CMSSW_15_0_0_pre2 and CMSSW_15_0_0_pre3.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_0_pre2` and `CMSSW_15_0_0_pre3`.
 - HLT menu: `/dev/CMSSW_14_2_0/GRun/V14`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250222_testCMSHLT3411`
 ```
 ./run_250222_testCMSHLT3411.sh out_250222_testCMSHLT3411_patatrack-scripts-746bcbd_dac1cc9
 ```
 - Goal: check impact of CMSHLT-3411 (filters with pT=0, or no filters).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_X` IBs post-pre3.
 - HLT menu: `/dev/CMSSW_14_2_0/GRun/V14`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250310_test2025Startup`
 ```
 ./run_250310_test2025Startup.sh out_250310_test2025Startup_patatrack-scripts-746bcbd_b6da97c
 ```
 - Goal: check impact of 2025 HLT-reco changes (e.g. CMSHLT-3421, CMSHLT-3422, CMSHLT-3413).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_1`.
 - HLT menu: `/dev/CMSSW_15_0_0/GRun/V11`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250310_test2025Startup_ref`
 ```
 ./run_250310_test2025Startup_ref.sh out_250310_test2025Startup_ref_patatrack-scripts-746bcbd_b6da97c
 ./run_250310_test2025Startup_ref.sh out_250310_test2025Startup_ref_GRun_patatrack-scripts-746bcbd_b6da97c
 ```
 - Goal: baseline for `250310_test2025Startup` (i.e. HLT throughput in 2024).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_14_0_15_patch1`.
 - HLT menu: same as used in run-386593, or `/dev/CMSSW_14_0_0/GRun/V182`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250310_test2025Startup_ref2`
 ```
 ./run_250310_test2025Startup_ref2.sh out_250310_test2025Startup_ref2_patatrack-scripts-746bcbd_1dee926
 ```
 - Goal: reproduce results of CMS-DP-2024/082 (HLT throughput in 2024).
 - Input data: run-383631, LSs 410-480, ~40k events (PU ~64).
 - Release: `CMSSW_14_0_15_patch1`.
 - HLT menu: `/online/collisions/2024/2e34/v1.4/HLT/V2`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250310_test2025Startup_ref3`
 ```
 ./run_250310_test2025Startup_ref3.sh out_250310_test2025Startup_ref3_patatrack-scripts-746bcbd_5efa871
 ```
 - Goal: same setup as ref2, except for using more recent 2024 input data.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_14_0_15_patch1`.
 - HLT menu: `/online/collisions/2024/2e34/v1.4/HLT/V2`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`run_250316_test2025Startup.sh`
 ```
 ./run_250316_test2025Startup.sh out_250316_test2025Startup_patatrack-scripts-746bcbd_495d030
 ```
 - Goal: check impact of 2025 HLT-reco changes (e.g. CMSHLT-3421, CMSHLT-3422, CMSHLT-3413),
         but using same input data as CMS-DP-2024/082 (HLT throughput in 2024).
 - Input data: run-383631, LSs 410-480, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_1`.
 - HLT menu: `/dev/CMSSW_15_0_0/GRun/V11`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`run_250322_test2025Startup.sh`
 ```
 ./run_250322_test2025Startup.sh out_250322_test2025Startup_patatrack-scripts-746bcbd_6438a25
 ```
 - Goal: check impact of 2025 HLT-reco changes (e.g. CMSHLT-3421).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_2`.
 - HLT menu: `/dev/CMSSW_15_0_0/GRun/V22`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`run_250323_testCMSHLT3460.sh`
 ```
 ./run_250323_testCMSHLT3460.sh out_250323_testCMSHLT3460_patatrack-scripts-746bcbd_e14cf0d
 ```
 - Goal: check impact of 2025 HLT-reco changes (e.g. CMSHLT-3421).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_2`.
 - HLT menu: `/users/missirol/test/dev/CMSSW_15_0_0/CMSHLT_3460/Test01/GRun/V2`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`run_250324_testCMSHLT3459.sh`
 ```
 ./run_250324_testCMSHLT3459.sh out_250324_testCMSHLT3459_patatrack-scripts-746bcbd_06542e1
 ```
 - Goal: check impact of CMSHLT-3459.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_2`.
 - HLT menu: `/dev/CMSSW_15_0_0/GRun/V22`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250325_test2025Startup_ref4`
 ```
 ./run_250325_test2025Startup_ref4.sh out_250325_test2025Startup_ref4_patatrack-scripts-746bcbd_49eca67
 ```
 - Goal: measure throughtput in `CMSSW_14_2_X`.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_14_2_2`.
 - HLT menu: `/dev/CMSSW_14_2_0/GRun/V16`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250325_test2025Startup_ref4_150X`
 ```
 ./run_250325_test2025Startup_ref4_150X.sh out_250325_test2025Startup_ref4_150X_patatrack-scripts-746bcbd_5dc0b20
 ```
 - Goal: measure throughtput in `CMSSW_15_0_X` pre-releases.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_0_pre1`, `CMSSW_15_0_0_pre2`, and `CMSSW_15_0_0_pre3`.
 - HLT menu: `/dev/CMSSW_14_2_0/GRun/V16`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250330_testCMSHLT3478`
 ```
 ./run_250330_testCMSHLT3478.sh out_250330_testCMSHLT3478_patatrack-scripts-746bcbd_3dd54ec
 ```
 - Goal: measure throughtput before/after CMSHLT-3478.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_3`.
 - HLT menu: `/users/missirol/test/dev/CMSSW_15_0_0/CMSHLT_3478/Test02/GRun/V2`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250330_testCMSHLT3479`
 ```
 ./run_250330_testCMSHLT3479.sh out_250330_testCMSHLT3479_patatrack-scripts-746bcbd_d6edbca
 ```
 - Goal: measure throughtput before/after CMSHLT-3479.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_3`.
 - HLT menu: `/users/missirol/test/dev/CMSSW_15_0_0/CMSHLT_3479/Test02/GRun/V{1,2}`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250330_testCMSHLT3480`
 ```
 ./run_250330_testCMSHLT3480.sh out_250330_testCMSHLT3480_patatrack-scripts-746bcbd_d6edbca
 ```
 - Goal: measure throughtput before/after CMSHLT-3480.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_3`.
 - HLT menu: `/users/missirol/test/dev/CMSSW_15_0_0/CMSHLT_3480/Test02/GRun/V{1,2}`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250405_testCMSHLT3459`
 ```
 ./run_250405_testCMSHLT3459.sh out_250405_testCMSHLT3459_patatrack-scripts-746bcbd_077f327
 ```
 - Goal: measure throughtput before/after CMSHLT-3459 (including full pixel-doublet recovery).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_3`.
 - HLT menu: `/dev/CMSSW_15_0_0/GRun/V39`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250409_testCMSHLT3459`
 ```
 ./run_250409_testCMSHLT3459.sh out_250409_testCMSHLT3459_patatrack-scripts-746bcbd_c0d308f
 ```
 - Goal: measure throughtput before/after CMSHLT-3459 (including full pixel-doublet recovery).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_4` + cms-sw/cmssw#47810.
 - HLT menu: `/dev/CMSSW_15_0_0/GRun/V48`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250410_testDisableEG11AndParkingVBF`
 ```
 ./run_250410_testDisableEG11AndParkingVBF.sh out_250410_testDisableEG11AndParkingVBF_patatrack-scripts-746bcbd_66fc876
 ```
 - Goal: measure throughtput after disabling the DoubleEG11-related triggers, and the ParkingVBF triggers.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_4` + cms-sw/cmssw#47810.
 - HLT menu: `/users/missirol/test/dev/CMSSW_15_0_0/tmp/250410_TestDisableEG11AndVBF/Test01/GRun/V*`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250411_TestLowPtDoubleEG`
 ```
 ./run_250411_testLowPtDoubleEG.sh out_250411_testLowPtDoubleEG_patatrack-scripts-746bcbd_18115c9
 ```
 - Goal: measure throughtput after including first version of Laurent's low-pT diphoton/dielectron triggers for 2025.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_4` + cms-sw/cmssw#47810.
 - HLT menu: `/users/missirol/test/dev/CMSSW_15_0_0/tmp/250411_TestLowPtDoubleEG/Test02/GRun/V*`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250412_TestLowPtDoubleEG`
 ```
 ./run_250412_testLowPtDoubleEG.sh out_250412_testLowPtDoubleEG_patatrack-scripts-746bcbd_5ac29bf
 ```
 - Goal: measure throughtput after including first version of Laurent's low-pT diphoton/dielectron triggers for 2025.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_4` + cms-sw/cmssw#47810.
 - HLT menu: `/users/missirol/test/dev/CMSSW_15_0_0/tmp/250411_TestLowPtDoubleEG/Test02/GRun/V*`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250413_testCMSHLT3484`
 ```
 ./run_250413_testCMSHLT3484.sh out_250413_testCMSHLT3484_patatrack-scripts-746bcbd_05d79de
 ```
 - Goal: measure throughtput for the updates proposed in CMSHLT-3484.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_4` + cms-sw/cmssw#47810.
 - HLT menu: `/users/missirol/test/dev/CMSSW_15_0_0/CMSHLT_3484/Test01/GRun/V*`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250414_TestLowPtDoubleEG`
 ```
 ./run_250414_testLowPtDoubleEG.sh out_250414_testLowPtDoubleEG_patatrack-scripts-746bcbd_6129ecf
 ```
 - Goal: measure throughtput after including first version of Laurent's low-pT diphoton/dielectron triggers for 2025.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_4` + cms-sw/cmssw#47810.
 - HLT menu: `/users/missirol/test/dev/CMSSW_15_0_0/tmp/250411_TestLowPtDoubleEG/Test04/GRun/V*`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250416_TestLowPtDoubleEG_newParams`
 ```
 ./run_250416_testLowPtDoubleEG_newParams.sh out_250416_testLowPtDoubleEG_newParams_patatrack-scripts-746bcbd_bd11701
 ```
 - Goal: measure throughtput after including first version of Laurent's low-pT diphoton/dielectron triggers for 2025.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_X_2025-04-16-1100`.
 - HLT menu: `/users/missirol/test/dev/CMSSW_15_0_0/tmp/250411_TestLowPtDoubleEG/Test09/GRun/V*`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250417_TestLowPtDoubleEG_newParams_barrelOnly`
 ```
 ./run_250417_testLowPtDoubleEG_newParams_barrelOnly.sh out_250417_testLowPtDoubleEG_newParams_barrelOnly_patatrack-scripts-746bcbd_ca7e8e0
 ```
 - Goal: measure throughtput after including Laurent's low-pT diphoton/dielectron triggers for 2025
   (restricting the 2 new Dielectron triggers to the barrel).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_X_2025-04-16-1100`.
 - HLT menu: `/users/missirol/test/dev/CMSSW_15_0_0/tmp/250411_TestLowPtDoubleEG/Test09/GRun/V*`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250417_testCMSHLT3516`
 ```
 ./run_250417_testCMSHLT3516.sh out_250417_CMSHLT3516_patatrack-scripts-746bcbd_bf04a4b
 ```
 - Goal: measure throughtput after including the latest 2025 conditions updates (HCALPFCuts, PFHCs, JECs).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_X_2025-04-16-1100`.
 - HLT menu: `/dev/CMSSW_15_0_0/GRun/V57`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250418_testCMSHLT3516`
 ```
 ./run_250418_testCMSHLT3516.sh out_250418_CMSHLT3516_patatrack-scripts-746bcbd_a3f522b
 ```
 - Goal: measure throughtput after including the latest 2025 conditions updates (HCALPFCuts, PFHCs, JECs).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_4_patch3`.
 - HLT menu: `/dev/CMSSW_15_0_0/GRun/V60`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250419_testDuplicateRemoval`
 ```
 ./run_250419_testDuplicateRemoval.sh out_250419_testDuplicateRemoval_patatrack-scripts-746bcbd_f7698db
 ```
 - Goal: measure throughtput after removing all duplicate modules from the GRun menu.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_4_patch3`.
 - HLT menu (baseline): `/dev/CMSSW_15_0_0/GRun/V60`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250420_testCMSHLT3459`
 ```
 ./run_250420_testCMSHLT3459.sh out_250420_testCMSHLT3459_patatrack-scripts-746bcbd_e2ffd78
 ```
 - Goal: measure throughtput after explicitly using CCCLoose in MkFitProducer instance.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_4_patch3`.
 - HLT menus: `/users/missirol/test/dev/CMSSW_15_0_0/CMSHLT_3459/Test05/GRun/V{1,2}`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250427_testCMSHLT3529`
 ```
 ./run_250427_testCMSHLT3529.sh out_250427_testCMSHLT3529_patatrack-scripts-746bcbd_9e651a8
 ```
 - Goal: measure impact on throughput of CMSHLT-3529 (using latest HCAL/PF/JME conditions in the baseline).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_4_patch3`.
 - HLT menus: `/users/missirol/test/dev/CMSSW_15_0_0/CMSHLT_3529/Test01/GRun/V{4,6}`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250428_testCMSHLT3459`
 ```
 ./run_250428_testCMSHLT3459.sh out_250428_testCMSHLT3459_patatrack-scripts-746bcbd_0369893
 ```
 - Goal: measure impact on throughput of improving CMSHLT-3459 (using latest HCAL/PF/JME conditions in the baseline).
   - Not running hltSiStripRecHits when not necessary.
   - Running SiStrips unpacking not-onDemand only as part of Iter-0 tracking (not elsewhere).
   - Note: the HLT_IsoTrackB* Paths are removed in this test, in view of CMSHLT-3519.
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_4_patch3`.
 - HLT menus: `/users/missirol/test/dev/CMSSW_15_0_0/tmp/250427_RearrangeModulesOfTrkIter0/Test03/GRun/V{1,2,3,6}`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250506_testCMSHLT3529`
 ```
 ./run_250506_testCMSHLT3529.sh out_250506_testCMSHLT3529_patatrack-scripts-746bcbd_8dfde6f
 ```
 - Goal: measure impact on throughput of removing Dielectron triggers introduced in CMSHLT-3529
   (using latest HCAL/PF/JME conditions in the baseline).
 - Input data: run-386593, LSs 94-99, ~40k events (PU ~64).
 - Release: `CMSSW_15_0_5`.
 - HLT menus: `/users/missirol/test/dev/CMSSW_15_0_0/CMSHLT_3529/Test02/GRun/V{1,2}`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250528_testCMSHLT3558`
 ```
 ./run_250528_testCMSHLT3558.sh out_250528_testCMSHLT3558_patatrack-scripts-746bcbd_05076a6
 ```
 - Goal: measure impact on throughput of CMSHLT-3558.
 - Input data: run-392642, LSs 178-180, ~40k events (PU ~63).
 - Release: `CMSSW_15_0_6`.
 - HLT menus: `/cdaq/test/missirol/dev/CMSSW_15_0_0/CMSHLT_3558/Test01/HLT/V{1,2,3}`.
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250612_testRun2025C`
 ```
 ./run_250612_testRun2025C.sh out_250612_testRun2025C_patatrack-scripts-746bcbd_e516409
 ```
 - Goal: measure throughput in two different runs of Run2025C.
 - Input data.
    - run-392642, LSs 178-180, ~40k events (PU ~63).
    - run-393240, LSs 205-207, ~40k events (PU ~62).
 - Release: `CMSSW_15_0_7`.
 - HLT menu: `/cdaq/physics/Run2025/2e34/v1.1.4/HLT/V1` (used online in run-393240).
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.

`250705_test_cmssw48404`
 ```
 ./run_250705_test_cmssw48404.sh out_250705_test_cmssw48404_patatrack-scripts-8c92fde_406b792 {ref,tar}
 ```
 - Goal: measure impact on throughput of cmssw#48404.
 - Input data: run-393240, LSs 205-207, ~40k events (PU ~62).
 - Release: `CMSSW_15_0_X_2025-07-05-1100` (+cmssw#48404 for "tar").
 - HLT menu: `/dev/CMSSW_15_0_0/GRun/V97` (similar to the 2025 V1.2 pp menu).
 - Done on `hilton-c2b02-44-01`, using 8 jobs with 32 threads and 24 streams per job.
 - NVIDIA MPS enabled, `x86-64-v3` enabled.
