#!/usr/bin/env bash
echo ${DRONE_COMMIT_REF}
if [[ "${DRONE_COMMIT_REF}" == "refs/tags/"* ]] ; then
echo "${DRONE_COMMIT_REF/refs\/tags\//}" > .tags
fi