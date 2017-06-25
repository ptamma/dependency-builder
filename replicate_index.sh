#!/usr/bin/env bash

DESTINATION=/Volumes/yard/sandbox/buildpack/source_repoindex

mkdir -p "$DESTINATION"

aws s3 sync "s3://download.pivotal.io" "$DESTINATION" --no-sign-request --exclude "*" \
  --include "*/index.yml" \
  --exclude "*/centos6/*" \
  --exclude "*/lucid/*" \
  --exclude "*/mountainlion/*" \
  --exclude "*/precise/*"
