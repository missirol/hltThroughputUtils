#!/bin/bash -e

[ $# -eq 1 ] || exit 1

jobLabel="${1}"
runNumber=375665
outDir=/fff/user/"${USER}"/output/hltThroughputUtils

run() {
  [ ! -d "${3}" ] || exit 1
  mkdir -p $(dirname "${3}")
  foo=$(printf "%125s") && echo ${foo// /-} && unset foo
  printf " %s\n" "${3}"
  foo=$(printf "%125s") && echo ${foo// /-} && unset foo
  rm -rf run"${runNumber}"
  ${2}/benchmark "${1}" -E cmsRun -r 4 -j "${4}" -t "${5}" -s "${6}" -e 40100 -g 1 -n --no-cpu-affinity -l "${3}" -k resources.json --tmpdir "${outDir}"/tmp |& tee "${3}".log
  ./merge_resources_json.py "${3}"/step*/pid*/resources.json > "${3}".json
  mv "${3}".log "${3}".json "${3}"
  cp "${1}" "${3}"
}

https_proxy=http://cmsproxy.cms:3128/ \
hltConfigFromDB --configName /users/missirol/test/dev/CMSSW_14_1_0/CMSHLT_3359/Test01/HLT/V4 > tmp0.py

cp /gpu_data/store/hidata/HIRun2023A/HIEphemeralZeroBias_L1Skim2024_v1_0_3/FED/v1/run"${runNumber}"_cff.py .

for jobSubLabel in baseline target01; do

  # ensure MPS is disabled at the start
  ./stop-mps-daemon.sh

  ### Intermediate configuration file
  cp tmp0.py tmp.py
  cat <<@EOF >> tmp.py

process.load('run${runNumber}_cff')

from customizeHLTforThroughputMeasurements import *
process = customizeHLTforCMSHLT3387_l1skim2024_${jobSubLabel}(process)
@EOF

  ### Final configuration file (dump)
  edmConfigDump tmp.py > "${jobLabel}"_"${jobSubLabel}"_dump.py
  rm -rf tmp.py

  ### Throughput measurements (benchmark)
  for ntry in {00..00}; do

    jobDirPrefix="${jobLabel}"-"${jobSubLabel}"-"${CMSSW_VERSION}"-"${ntry}"

    ## GPU MPS
    unset CUDA_VISIBLE_DEVICES
    ./start-mps-daemon.sh
    sleep 1
    run "${jobLabel}"_"${jobSubLabel}"_dump.py ./patatrack-scripts "${outDir}"/"${jobDirPrefix}"-gpu_mps 8 32 20
    ./stop-mps-daemon.sh
    sleep 1

  done
  unset ntry

done
unset jobSubLabel

rm -rf "${jobLabel}"*{cfg,dump}.py
rm -rf run"${runNumber}"
rm -rf run"${runNumber}"_cff.py
rm -rf __pycache__ tmp
rm -rf tmp0.py
