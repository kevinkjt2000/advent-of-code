# Run with awk -f day6.awk -- day6.input
BEGIN {
  RS = "\n\n"
  total = 0
}
{
  for(i=1;i<=NF;i++){
    split($i, chars, "")
    for(j=1; j<=length($i); j++) {
      if (chars[j] in a == 0){
        a[chars[j]]
      }
    }
    delete chars
  }
  total += length(a)
  delete a
}
END {
  print total
}
