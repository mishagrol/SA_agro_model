for a in $(cat list_batch.txt)
do
	mkdir monica_dir$a
	cp -r work_kshen ./monica_dir$a
	cp sobol_monica.py ./monica_dir$a
	cp monicarunner.sh ./monica_dir$a
	mv $a ./monica_dir$a
        rm $a
done
#for i in $(cat ~/monica/sensitivity/sim/allbatch.txt)
#do
#        echo "#!/bin/bash
# for a in \$(cat $i); do monica run ~/monica/sensitivity/sim/input_files/\$a; done" >$i.sl
#done

