rm batch*
rm -r monica_dir*
python param.py
chmod u+x batch*
ls batch* > list_batch.txt
for a in $(cat list_batch.txt)
do 
	mkdir monica_dir$a
	cp -r work_kshen ./monica_dir$a
	cp sobol_monica.py ./monica_dir$a
	cp monicarunner.sh ./monica_dir$a
	cp monica.sl ./monica_dir$a
	cp $a ./monica_dir$a/batch.npy 
done
