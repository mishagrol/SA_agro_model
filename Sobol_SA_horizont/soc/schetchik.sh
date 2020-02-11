for a in $(cat list_of_dir.txt)
do
	echo $a >>./summa.txt
	cat ./$a/soybean-000-2015.csv | wc >>./summa.txt 
	cat ./$a/spring-barley-2012.csv | wc>>./summa.txt 
	cat ./$a/sugar-beet-2011.csv | wc>>./summa.txt
	cat ./$a/sugar-beet-2014.csv | wc>>./summa.txt  
	cat ./$a/sugar-beet-2017.csv | wc>>./summa.txt
done
