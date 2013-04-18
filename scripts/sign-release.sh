#!/bin/sh
# Script for signing repository
REPO_DIR='/data/deb/unstable/tor2web'
gpg --default-key "$KEYID" --detach-sign -o Release.gpg.tmp ${REPO_DIR}/Release
mv Release.gpg.tmp ${REPO_DIR}/Release.gpg
