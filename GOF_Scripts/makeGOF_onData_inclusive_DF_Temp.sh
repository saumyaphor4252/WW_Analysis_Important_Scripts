for year in "2018" #"2016_HIPM" "2016_noHIPM" "2017" "2018" "Run2"
do
    for catg in "incl_DF"
    do
        datacard=Full${year}_${catg}.txt
        datacardws=$(echo "$datacard" | sed 's|.txt|.root|g')
        if [ -f "$datacardws" ]; then
            echo "Datacard workspace already exists, continuing..."
        else
            echo "Datacard workspace does not exist, creating it..."
            # Create the datacard workspace
            text2workspace.py "$datacard" --channel-masks
        fi
        echo $datacardws
        for mode in "WW"
        do
            for algorithm in "saturated" #"KS" "AD" #
            do
                combine -M GoodnessOfFit --algo=${algorithm} -m 125 -d $datacardws -n WW &
                ##=================================================================
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &

#                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
#                combine -M GoodnessOfFit --algo=${algorithm} -t 200 --toysFreq -s -1 -m 125 -d $datacardws -n WW &
                ##=================================================================
                wait
                # ${mode}
                hadd higgsCombine${mode}.GoodnessOfFit.mH125.Merged.root higgsCombine${mode}.GoodnessOfFit.mH125.*.root
                ##=================================================================
                ## plotting
                python3 plotGOF_fromDanyer.py --observed higgsCombine${mode}.GoodnessOfFit.mH125.root --toys higgsCombine${mode}.GoodnessOfFit.mH125.Merged.root  --output gof${mode}_${catg}_${year} --statistic ${algorithm} --bins 100 --title-right="S+B hypothesis("${catg}" "${year}")"
                ##=================================================================
                combineTool.py -M CollectGoodnessOfFit --input higgsCombine${mode}.GoodnessOfFit.mH125.root higgsCombine${mode}.GoodnessOfFit.mH125.Merged.root -m 125.0 -o gof${mode}_${catg}_${year}.json
                plotGof.py gof${mode}_${catg}_${year}.json --statistic ${algorithm} --mass 125.0 -o gof${mode}_${catg}_${year} --title-right="S+B hypothesis("${catg}" "${year}")"
                ##=================================================================
                                # Move all PNG files into the "GOFTest" directory
                mv *.png GOFTest/
                                mv gof${mode}_${catg}_${year}.json GOFTest/
                            mv gof${mode}_${catg}_${year}.pdf GOFTest/
                            mv gof${mode}_${catg}_${year}_fromDanyer.json GOFTest/
                                mv gof${mode}_${catg}_${year}_fromDanyer.pdf GOFTest/
                ##=================================================================
                #rm -f higgsCombine${mode}.GoodnessOfFit.mH125.+([0-9-]).root
                #for file in higgsCombine${mode}.GoodnessOfFit.mH125.*.root; do
                    # Extract the number part after "mH125."
                    #num=$(echo "$file" | sed -E 's/higgsCombine${WW}\.GoodnessOfFit\.mH125\.([-]?[0-9]+)\.root/\1/')

                    # Check if the extracted part is a valid number
                    #if [[ "$num" =~ ^-?[0-9]+$ ]]; then
                                #       echo $file
                         #rm -f "$file"
                #done
                                mv higgsCombine${mode}.GoodnessOfFit.mH125.Merged.root GOFTest/higgsCombine${mode}.GoodnessOfFit.mH125.Merged_${mode}_${catg}_${year}.root
                                mv higgsCombine${mode}.GoodnessOfFit.mH125.root GOFTest/higgsCombine${mode}.GoodnessOfFit.mH125.${mode}_${catg}_${year}.root
                                rm -f higgsCombine${mode}.GoodnessOfFit.mH125.*.root
            done
        done
    done
done
