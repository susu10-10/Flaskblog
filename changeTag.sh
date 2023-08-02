#!/bin/bash
sed "s/tagVersion/$1/g" values.yaml > myvalues.yaml
