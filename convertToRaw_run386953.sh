#!/bin/bash

# Run 386593, LS 94-99
#./showLumisInFiles.sh log.txt /eos/cms/tier0/store/hidata/HIRun2024A/HIEphemeralHLTPhysics/RAW/v1/000/387/973/00000/*.root

convertToRaw -r 386593:94-386593:99 \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/593/00000/55bcf152-ffa5-4885-9d99-d1cb2ceafc33.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/593/00000/d874456e-8d50-4ec8-9f89-5360c3f1453d.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/593/00000/a78ccd58-83ce-4cfb-a923-468dd2ebaf96.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/593/00000/1f53fe29-f5b8-467a-be10-027a7afb5847.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/593/00000/57be72db-594d-4c7d-8160-ba5d2b451758.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/593/00000/e6ddaabf-d394-4069-86d5-31a4ce21dc31.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/593/00000/c4313648-8497-420d-a089-dec85b68f815.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/593/00000/20cf3426-1781-455b-bb12-c616137d21ae.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/593/00000/bd6e2cc3-7b32-4f7d-8e7b-9dd63ddd62ef.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/593/00000/1921e936-1683-4969-a70c-ef73a35fcf6e.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/593/00000/9c13430c-eacc-4e72-bea0-6a3ee2bfe1a6.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/593/00000/79aad56b-7eb8-4763-9633-15013f5986eb.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/593/00000/e7c89a62-1eda-409e-8d7f-88ba501d8ed1.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/593/00000/87a2d5fb-cb54-4424-9fa3-8f5c8a9d7bd0.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/593/00000/878f70ff-c659-41bb-ab97-d94981565e34.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/593/00000/80a5f93a-e624-4362-864a-f90f18be97de.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/593/00000/93d89525-2aa2-429b-a477-d0771f85e62a.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/593/00000/65794853-10a8-406e-a7ce-35b208e967a0.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/593/00000/70824f81-82fb-41e1-a0a0-28277372225f.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/593/00000/57fe4634-ca40-47c3-a97c-1445b8be2a6e.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/593/00000/a9db6cd2-e036-4e86-ab5e-2d43908bb793.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/593/00000/b3651f4c-961b-4d7f-b6b2-f85791b51e2f.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/593/00000/96f3a61f-ec0e-440d-b1a7-5ed7b4e8257f.root \
  root://eoscms.cern.ch//store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/593/00000/171e7160-259c-4af7-9547-f8be8542074e.root
