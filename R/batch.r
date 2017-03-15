# run using: R CMD BATCH --slave "--args num=2 bool = TRUE" batch.r

args = commandArgs(TRUE)
for(i in 1:length(args)){
	eval(parse(text=args[[i]]))
}

bool == FALSE	# TRUE, see batch.r.Rout
num > 0
