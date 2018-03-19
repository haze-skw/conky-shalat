# Get day of Hijr
#!/bin/bash
idate -u | awk 'NR==4 {print $8}' | sed 's/\(.*\)...../\1/'
