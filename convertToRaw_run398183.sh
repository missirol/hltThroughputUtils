#!/bin/bash

# Run 398183, LS 322-325

#rm -f tmp0.txt
#for lumi_i in {322..325}; do
#  for pd_i in {0..7}; do
#    dasgoclient -query "file run=398183 lumi=${lumi_i} dataset=/EphemeralHLTPhysics${pd_i}/Run2025G-v1/RAW" >> tmp0.txt
#  done
#done
#unset lumi_i pd_i
#sort -u tmp0.txt > tmp.txt
#rm -f tmp0.txt

convertToRaw -r 398183:322-398183:325 \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics0/RAW/v1/000/398/183/00000/9840b64d-7e14-4a47-866a-f68952c7cf16.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics0/RAW/v1/000/398/183/00000/af58311d-b9a8-4613-9b3f-2e7eaf50ee3c.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics1/RAW/v1/000/398/183/00000/098c1f53-7b09-466f-a5cd-d076de4c51d8.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics1/RAW/v1/000/398/183/00000/515f59a6-1802-487f-b7ef-33f82b521d74.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics2/RAW/v1/000/398/183/00000/09fb91c9-1b2a-4e9b-a557-94ada1a3c079.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics2/RAW/v1/000/398/183/00000/37b75c33-1efe-4c36-ae79-cfc1418019ac.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics2/RAW/v1/000/398/183/00000/95b17755-e288-4d29-acac-8ecd9aab8aa6.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics3/RAW/v1/000/398/183/00000/19163a1c-06d4-4c11-b905-d5e309c8f757.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics3/RAW/v1/000/398/183/00000/72d454d5-83e2-4719-89fe-a46e82cde327.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics3/RAW/v1/000/398/183/00000/b857a3f6-4fa0-450a-aaf7-e879b5c04af4.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics4/RAW/v1/000/398/183/00000/0734512a-b0db-42f2-9b08-634ca2c94323.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics4/RAW/v1/000/398/183/00000/a6f80e9e-01a6-4fbf-8014-9bad88f867a2.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics5/RAW/v1/000/398/183/00000/0138cbc7-95db-4a1d-9193-9b3220756745.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics5/RAW/v1/000/398/183/00000/6b2c3582-b868-4051-940b-5792b8754015.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics6/RAW/v1/000/398/183/00000/3d025d6a-c482-405d-a954-c673b0939c54.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics6/RAW/v1/000/398/183/00000/46aa5401-bb4f-4993-a17e-8c3f414f9cf2.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics6/RAW/v1/000/398/183/00000/9487a6c8-b225-445f-8c1c-e96c0ded7b40.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics7/RAW/v1/000/398/183/00000/39cad286-c5ea-4c6d-90d6-66305999db7f.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics7/RAW/v1/000/398/183/00000/a53a90e7-f51a-435e-a1c5-c7489b78c2d0.root \
  root://eoscms.cern.ch//eos/cms/store/data/Run2025G/EphemeralHLTPhysics7/RAW/v1/000/398/183/00000/ea3f7a79-1665-4433-af67-2e43292eafe3.root
