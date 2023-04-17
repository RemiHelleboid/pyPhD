exit 0

# Merging csv files with the same header
awk 'FNR==1 && NR!=1{next;}{print}' *.csv > merged.csv

