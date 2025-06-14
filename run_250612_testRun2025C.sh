#!/bin/bash -e

[ $# -eq 1 ] || exit 1

jobLabel="${1}"
runNumber1=392642
runNumber2=393240
outDir=/fff/user/"${USER}"/output/hltThroughputUtils

run() {
  [ ! -d "${3}" ] || exit 1
  mkdir -p $(dirname "${3}")
  foo=$(printf "%125s") && echo ${foo// /-} && unset foo
  printf " %s\n" "${3}"
  foo=$(printf "%125s") && echo ${foo// /-} && unset foo
  rm -rf run"${runNumber1}"
  rm -rf run"${runNumber2}"
  ${2}/benchmark "${1}" -E cmsRun -r 4 -j "${4}" -t "${5}" -s "${6}" -e 40100 -g 1 -n --no-cpu-affinity -l "${3}" -k resources.json --tmpdir "${outDir}"/tmp |& tee "${3}".log
  mergeResourcesJson.py "${3}"/step*/pid*/resources.json > "${3}".json
  mv "${3}".log "${3}".json "${3}"
  cp "${1}" "${3}"
}

https_proxy=http://cmsproxy.cms:3128/ \
hltConfigFromDB --runNumber 393240 > tmp0.py

cp /gpu_data/store/data/Run2025*/EphemeralHLTPhysics/FED/run"${runNumber1}"_cff.py .
cp /gpu_data/store/data/Run2025*/EphemeralHLTPhysics/FED/run"${runNumber2}"_cff.py .

for jobSubLabel in run"${runNumber1}" run"${runNumber2}"; do

  # ensure MPS is disabled at the start
  ./stop-mps-daemon.sh

  ### Intermediate configuration file
  cp tmp0.py tmp.py
  cat <<@EOF >> tmp.py

process.load('${jobSubLabel}_cff')

from customizeHLTforThroughputMeasurements import *
process = customizeHLTforRun2025C(process)
@EOF

  ### Final configuration file (dump)
  edmConfigDump tmp.py > "${jobLabel}"_"${jobSubLabel}"_dump.py
  rm -rf tmp.py

  ### Throughput measurements (benchmark)
  for ntry in {00..01}; do

    jobDirPrefix="${jobLabel}"-"${jobSubLabel}"-"${CMSSW_VERSION}"-"${ntry}"

#    ## CPU
#    export CUDA_VISIBLE_DEVICES=
#    sleep 1
#    run "${jobLabel}"_"${jobSubLabel}"_dump.py ./patatrack-scripts "${outDir}"/"${jobDirPrefix}"-cpu 8 32 24
#    sleep 1

    ## GPU MPS
    unset CUDA_VISIBLE_DEVICES
    ./start-mps-daemon.sh
    sleep 1
    run "${jobLabel}"_"${jobSubLabel}"_dump.py ./patatrack-scripts "${outDir}"/"${jobDirPrefix}"-gpu_mps 8 32 24
    ./stop-mps-daemon.sh
    sleep 1

  done
  unset ntry

done
unset jobSubLabel

rm -rf "${jobLabel}"*{cfg,dump}.py
rm -rf run"${runNumber1}"
rm -rf run"${runNumber1}"_cff.py
rm -rf run"${runNumber2}"
rm -rf run"${runNumber2}"_cff.py
rm -rf __pycache__ tmp
rm -rf tmp*.py
