gunzip -c dictionary.gz | grep -E "r" | grep -E "^[zonirac]{4,}$" | wc -l
