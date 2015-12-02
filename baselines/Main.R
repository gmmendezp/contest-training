rl <- function(){
  return(readLines(fin,1))
}
rls <- function(){
  return(strsplit(rl()," "))
}
w <- function(l){
  write(l,fout)
}

solve <- function(){
  TT <- as.numeric(rl())
  for(t in 1:TT){
    w(sprintf("Case #%d: %s",t,rl()))
  }
}

fin <- file("test.in", open = "r")
fout <- file("test.out", open = "w")
solve()
close(fin)
close(fout)
