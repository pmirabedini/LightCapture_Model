# LightCapture_Model
The LightCapture model is a Monte Carlo based ray-tracing python code designed to find the correlation between micropillars' geometry and light absorption through the length of pillars in microfluidic reactors. The results potentially contribute to developing more efficient structures for photocatalytic reactions in waste-water treatment applications. 

## Steps to run the code:
The code consists of three main functions in addition to preprocessing and postprocessing helper functions. It works by following a ray from where it enters the reactor until it is absorbed by pillar, ground, or water, or it is reflected back out of the reactor. This procedure is performed for thousands of rays to construct the probability distribution of light capture. 

You can either run the Jupyter notebook in the provided order.

Or, you can download and run the .py files in the following order:

1. run InitialFuncs.py 
2. run HitsPillarFunc.py
3. run FollowRayFunc.py
4. run RayTrace.py
5. run get_Hitpoints (You need to determine the desired parameters.)
6. if you wish to save the hitpoints output, run the save_Hitpoints.py
7. to get the probability distribution, run the Probability_Distr.py file. Here, you would need to determine the input parameters for the desired system once again.

## Notes:
- At each step, you need to choose the path to python and the directories you wish to save the files.
- You could run the test files after running each module to ensure the module works. You can change the values in the test files if you wish to check the module run for different test values.

## Citation:
Mirabedini, P.S., Truskowska, A., Ashby, D.Z. et al. Coupled Light Capture and Lattice Boltzmann Model of TiO2 Micropillar Array for Water Purification. MRS Advances 4, 2689–2698 (2019). https://doi.org/10.1557/adv.2019.467









