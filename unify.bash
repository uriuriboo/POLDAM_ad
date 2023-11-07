origin=$1
target=$2
unified_file="2old"

cat $origin > $unified_file
cat $target >> $unified_file