# Run with awk -f day6.awk -- day6.input
BEGIN {
  RS = "\n\n"
  total = 0
}
{
  split("", a) # initializes empty array, since a = [] is invalid
  split($1, chars, "")
  for(i=1; i<=length(chars); i++) {
    innocent = 1
    for(j=2; j<=NF; j++) {
      if (!($j ~ chars[i])) {
        innocent = 0
      }
    }
    if (innocent) {
      a[chars[i]]
    }
  }
  total += length(a)
  delete a
  delete chars
}
END {
  print total
}
