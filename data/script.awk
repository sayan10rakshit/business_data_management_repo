#!/usr/bin/gawk -f
BEGIN{FS=","}
/^Name/{name=$1}
/^,Name/{name=$2}
/^Invoice Date/{date=$1}
/^,Invoice Date/{date=$2}
/^Invoice No/{invoice=$1}
/^,Invoice No/{invoice=$2}
/^[[:digit:]]/{arr[$1]=$0}
/^,[[:digit:]]/{arr[$2]=$0}
END{for (i in arr){print invoice","name","date","arr[i]}}
