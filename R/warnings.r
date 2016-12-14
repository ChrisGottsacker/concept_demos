# call this to hide warnings
warnings_off = function(){
	saved_warning_level <<- getOption('warn')
	options(warn = -1)
}

# call this to make warning visible again
warnings_on = function(){
	options(warn = saved_warning_level)
}
