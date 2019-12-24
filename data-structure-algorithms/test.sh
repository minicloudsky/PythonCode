#!/bin/bash
when-changed -v -r -1 -s ./ "py.test -s $1"

