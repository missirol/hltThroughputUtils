#!/bin/bash

[ $# -gt 1 ] || exit 1

logFile="${1}"
inFiles=("${@:2}")

[ -f "${logFile}" ] || touch "${logFile}"

for inFile in "${inFiles[@]}"; do
  [ -f "${inFile}" ] || continue
  [ $(grep "${inFile}" "${logFile}" | wc -l) -eq 0 ] || continue

  lumis=$(edmLumisInFiles.py "${inFile}")

  echo "${lumis}" "${inFile}" >> "${logFile}"
  tail -1 "${logFile}"
done
unset inFile lumis
