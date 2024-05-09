for i in `ls $1`; do ./script.awk ./$1/$i | sed -E -e 's/invoice\s+?no\s+?\:\s+?//Ig ; s/name\s+?\:\s+?//Ig ; s/invoice\s+?date\s?\:\s+?//Ig';done;
