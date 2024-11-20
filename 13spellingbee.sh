gunzip -c dictionary.gz | grep "r" | grep -E "^[aronczi]{4,100}" | grep -v "[bdefghjklmpqstuvwxy]" | wc -l
