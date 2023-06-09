# BrainHack School 2023 - BIDS Module assignment

- Download a few subjects (n=3) from the dataset [DS000228](https://openneuro.org/datasets/ds000228/versions/1.1.0) on OpenNeuro. Hint: the dataset is available with DataLad from this [Git repository](https://github.com/OpenNeuroDatasets/ds000228).
- Check that the resulting folder is a bids-compliant dataset using the bids validator (using a web browser or a local `npm` install).

```
Question 1.
Did you get any warnings? Explain what they are and whether they are a concern.

Your answer:

Warning: 1
155 FILES
Task scans should have a corresponding events.tsv file. If this is a resting state scan you can ignore this warning or rename the task to include the word "rest".

Because this scans were just watching movie without task, therefore the absent of events.tsv file is fine.

Warning: 2
95 FILES
Not all subjects/sessions/runs have the same scanning parameters.

It seems that there are different voxel dimensions and resolutions. I think the different parameters had to be annotated for each subject's data.

Warning: 3
1 FILE
Tabular file contains custom columns not described in a data dictionary

It contain more information than usual column and it is fine.

```

- Install `pybids`. Use `pybids` to get a list of all BOLD `nii.gz` files for subject `pixar003`. You may want to have a look at the [BIDS documentation](https://bids.neuroimaging.io/) to familiarize yourself with the BIDS standard.

    

```
Question 2.
In which folder did you find them? is it logical?

Your answer:

It located in sub-pixar003/func folder, and absolute path is "/Users/chunyilee/BXF_NDA/ds000228/sub-pixar003/func/".
It's logical because it located in subject pixar003 folder and within functional EPI folder.

```

- Using `pybids`, get a list of the flip angles in `DS000228`.
- Clone a Midnight Brain Scan dataset from this [Git repository](https://github.com/OpenNeuroDatasets/ds000224). Use `pybids` to load the `participant.tsv` file as a pandas dataframe in Python.

```
Show your results in the Jupyter Notebook and send it to us!
```
