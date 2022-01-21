#!/usr/bin/env bash

# rev is not present on all systems (and is against UNIX style)
# awk or sed are, therefore, preferred solutions

# however, sed is overly complex for this trivial task, and awk implements
# its own language. therefore, i will be using standard shell scripting.

new=""
for (( i=${#1}; i>-1; i-- )); do
	new="${new}${1:$i:1}"
done
echo "${new}"
