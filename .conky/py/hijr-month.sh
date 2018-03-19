#!/bin/bash

# Get month of Hijr

idate -u -s | awk '{print $7,$8}' | cut -d'(' -f1
