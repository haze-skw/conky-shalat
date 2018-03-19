# Get Location based on .iprayrc
#!/bin/bash
ipraytime | awk 'NR==3 {print $3}'
