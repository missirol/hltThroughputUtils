#!/bin/bash

# Run 396102, LS 295-298

#rm -f tmp0.txt
#for lumi_i in {295..298}; do
#  for pd_i in {0..7}; do
#    dasgoclient -query "file run=396102 lumi=${lumi_i} dataset=/EphemeralHLTPhysics${pd_i}/Run2025E-v1/RAW" >> tmp0.txt
#  done
#done
#unset lumi_i pd_i
#sort -u tmp0.txt > tmp.txt
#rm -f tmp0.txt

#convertToRaw -r 396102:295-396012:298 \
#  root://eoscms.cern.ch//eos/cms
