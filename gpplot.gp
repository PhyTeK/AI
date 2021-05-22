#set terminal dumb
set terminal postscript
set output "tmp.ps"
#plot 'results' u 2:3:(sprintf("%d",$5)) w labels notitle
plot 'results' u 2:3:5 w labels notitle
