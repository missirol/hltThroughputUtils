#!/bin/bash -e

[ $# -eq 1 ] || exit 1

jobLabel="${1}"
runNumber=375790
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
hltConfigFromDB --configName /dev/CMSSW_14_0_0/HIon/V173 > "${jobLabel}"_ref_cfg.py

https_proxy=http://cmsproxy.cms:3128/ \
hltConfigFromDB --configName /users/soohwan/HLT_140X/Alpaka/HIonV173/V10 > "${jobLabel}"_tar_cfg.py

cp /gpu_data/store/hidata/HIRun2023*/HIEphemeralHLTPhysics/FED/v*/run"${runNumber}"_cff.py .

for jobSubLabel in ref tar; do

# ensure MPS is disabled at the start
./stop-mps-daemon.sh

### Intermediate configuration file
cp "${jobLabel}"_"${jobSubLabel}"_cfg.py tmp.py
cat <<@EOF >> tmp.py

process.load('run${runNumber}_cff')

from customizeHLTforThroughputMeasurements import *
process = customizeHLTforCMSHLT3284_baseline(process)
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