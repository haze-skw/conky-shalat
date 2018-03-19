# Get date of Hijr
#!/bin/bash
idate -u | awk 'NR==4 {print $4}' | sed 's/\(.*\)./\1/'
