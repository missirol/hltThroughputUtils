#!/bin/bash

# Run 387973, LS 90-98
#./showLumisInFiles.sh log.txt /eos/cms/tier0/store/hidata/HIRun2024A/HIEphemeralHLTPhysics/RAW/v1/000/387/973/00000/*.root

convertToRaw -r 387973:90-387973:98 \
  root://eoscms.cern.ch//eos/cms/tier0/store/hidata/HIRun2024A/HIEphemeralHLTPhysics/RAW/v1/000/387/973/00000/05cd910f-820e-4d2a-94df-8cddb81987b2.root \
  root://eoscms.cern.ch//eos/cms/tier0/store/hidata/HIRun2024A/HIEphemeralHLTPhysics/RAW/v1/000/387/973/00000/8403d92c-e1a3-4973-8904-24e14d2b0f7c.root \
  root://eoscms.cern.ch//eos/cms/tier0/store/hidata/HIRun2024A/HIEphemeralHLTPhysics/RAW/v1/000/387/973/00000/1890d5aa-9329-460b-857b-8bde62d891d4.root \
  root://eoscms.cern.ch//eos/cms/tier0/store/hidata/HIRun2024A/HIEphemeralHLTPhysics/RAW/v1/000/387/973/00000/2dcf0ab2-0bee-4612-8714-88f3969897ca.root
