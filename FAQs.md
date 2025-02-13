# FAQs


## What of there is one sided nuisance in the impact plots
It can be due to some failing fits 
There would be a `condor_impacts.sh` in the area where we run the commands, which will have separate fit command for each nuisance parameter. Het the command for the parameter you want and run it locally including"
`
 --rMin 0 --rMax 4 --robustFit=1
`

There would then be a root file file in your local area 

