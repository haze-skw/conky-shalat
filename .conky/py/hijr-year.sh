# Get year of Hijr
#!/bin/bash
idate -u | awk 'NR==4 {print $5}' | sed 's/..\(.*\)/\1/'
