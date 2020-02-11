for a in $(cat list_of_dir.txt)
do
	chmod u+x $a/*
	cat ./$a/soybean-000-2015.csv >>./sum_out/soybean-000-2015.csv 
	cat ./$a/spring-barley-2012.csv>>./sum_out/spring-barley-2012.csv  
	cat ./$a/sugar-beet-2011.csv>>./sum_out/sugar-beet-2011.csv 
	cat ./$a/sugar-beet-2014.csv>>./sum_out/sugar-beet-2014.csv  
	cat ./$a/sugar-beet-2017.csv>>./sum_out/sugar-beet-2017.csv
done
