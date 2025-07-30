#!/bin/bash

# Run 394959, LS 244-247

#rm -f tmp0.txt
#for lumi_i in {244..247}; do
#  for pd_i in {0..7}; do
#    dasgoclient -query "file run=394959 lumi=${lumi_i} dataset=/EphemeralHLTPhysics${pd_i}/Run2025D-v1/RAW" >> tmp0.txt
#  done
#done
#unset lumi_i pd_i
#sort -u tmp0.txt > tmp.txt
#rm -f tmp0.txt

convertToRaw -r 394959:244-394959:247 \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics0/RAW/v1/000/394/959/00000/53c3d3e6-e8b4-4341-a936-58472ebaa7a8.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics0/RAW/v1/000/394/959/00000/9643bb21-596b-4032-9ad0-8dd8fd22e7fa.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics1/RAW/v1/000/394/959/00000/a755c6cb-9afc-4091-ad2b-f9b223222f18.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics1/RAW/v1/000/394/959/00000/d26d062b-c1d3-49d0-8a35-374bf950ae8b.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics2/RAW/v1/000/394/959/00000/2c8b613f-6003-4a91-b464-95db2043ce85.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics2/RAW/v1/000/394/959/00000/d712640a-170a-4ad8-9d9e-3cbe48b6349a.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics3/RAW/v1/000/394/959/00000/32564b7f-6343-45c7-b076-bb0eea934d01.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics3/RAW/v1/000/394/959/00000/69882e9a-9ed1-4038-9e52-ba788c6266b8.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics4/RAW/v1/000/394/959/00000/177940b5-32d4-4dec-9481-3511d8d5474a.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics4/RAW/v1/000/394/959/00000/31f67d0d-5df2-48b2-8e87-f74bddeb33de.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics4/RAW/v1/000/394/959/00000/7acc2710-cea8-4abe-9610-4678ece55e60.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics5/RAW/v1/000/394/959/00000/76446c67-115e-4433-8c5e-d8f2da9720ad.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics5/RAW/v1/000/394/959/00000/b872a802-4a42-4863-8f89-b227bb5f2d06.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics5/RAW/v1/000/394/959/00000/f211f607-b16e-414b-bae0-26377f5c0ccc.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics6/RAW/v1/000/394/959/00000/5b2ed226-cad9-4e71-956e-73b54a555b1e.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics6/RAW/v1/000/394/959/00000/ab52e547-3fa2-4f3a-a90b-a126007bd7d7.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics6/RAW/v1/000/394/959/00000/d57013a2-55bd-4cb8-bb98-f38c920160cf.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics7/RAW/v1/000/394/959/00000/1b4d24be-fcd5-4a84-882e-0e223567f3f3.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics7/RAW/v1/000/394/959/00000/58893f86-bac9-41cb-82c9-3ac42c583062.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025D/EphemeralHLTPhysics7/RAW/v1/000/394/959/00000/e178c1ab-7086-4d11-b66c-5d91868b351c.root
