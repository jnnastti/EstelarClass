<h1 align="center"> The EstelarClass! </h1>

<p align="center"><img src="./img/planet.gif" width="150px" height="150px"/></p>

<p align="justify"> &emsp; The <b>EstelarClass</b> is a system that will serve for the <b><i>COMPARATIVE ANALYSIS OF MACHINE LEARNING METHODS FOR THE IDENTIFICATION OF TRANSITING EXOPLANETS</i></b>.

<br/>

 &emsp; Using the K2, KEPLER, and TESS datasets from NASA (available at the end of this information), an <b><i>EVALUATION OF THE EFFECTIVENESS OF CLASSIFICATION ALGORITHMS</b></i> will be conducted.</p>

 <br/>

 &emsp; This project is being developed for the completion of the Computer Science course at UNESC with the assistance of Dr. Leandro Neckel ([@leandroneckel](https://github.com/leandroneckel)) and Me. André Ruaro.

<p align="center"><img src="./img/space.gif" width="100px" height="100px"/></p>

<h2>Abstract:</h2>


<p align="justify">  &emsp; The search for exoplanets, planets that orbit stars outside our solar system, has been a dynamic and exciting field of research in contemporary astronomy. Over the past twenty-five years, remarkable progress has been achieved, driven by the development of high-precision space telescopes, providing a wealth of information about the population of exoplanets and transforming our understanding of the universe. The detection of exoplanets during transits reveals crucial data about their atmospheres and composition. This has sparked growing interest in the analysis of datasets from NASA missions, with data scientists and machine learning enthusiasts exploring new ways to interpret this data and predict anomalies. Although machine learning algorithms offer a promising approach for the automated identification of exoplanets, the lack of interpretability of these methods has been a significant limitation. Therefore, this study proposes a comparative analysis of machine learning methods applied to the identification of transiting exoplanets, focusing on evaluating the effectiveness of classification algorithms, using five types of machine learning methods, data preprocessing techniques, and optimization through hyperparameters. It is expected that this study will provide important insights into which techniques have the potential to assist in efficiently identifying and categorizing exoplanets, thus contributing to the advancement of exoplanet science and providing guidance for data analysis in future space missions.</p>

<h2> Used databases:</h2>

<ul>
  <li align="justify"><a href="https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=cumulative"> Kepler </a>: The Kepler database, created from NASA's eponymous mission launched in 2009 and concluded in 2018, has been an invaluable source of detailed observations of exoplanets. The extent and precision of the observations contained within provide a solid foundation for the research of transiting exoplanets. With the largest number of records among exoplanet search missions, the Kepler database is essential for the effective training of models, significantly enhancing the accuracy of analyses and subsequent discoveries.</li>
  <li align="justify"><a href="https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=k2pandc"> K2 </a>: NASA's K2 mission, the successor to the Kepler mission, expanded our understanding of exoplanets with detailed observations of various regions of space. Launched in 2014 after the conclusion of the main Kepler mission, the K2 mission continued to collect valuable data until 2018. Although its database contains fewer records, it holds a large number of confirmed exoplanets, which is essential for model training and the enhancement of analyses.</li>
  <li align="justify"><a href="https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=TOI"> TESS </a>: NASA's TESS mission, launched in April 2018, has revolutionized the search for exoplanets by monitoring large areas of the sky for planetary transits. Currently active, TESS continues to provide comprehensive and up-to-date data, essential for exoplanet research. Its discoveries are crucial for keeping pace with advancements in the search for new worlds beyond our solar system.</li>
</ul>


## How to Install:

For the development of this project, Python version 3.11.9 was used. Make sure it is installed on your machine. Additionally, we used Git for version control and Windows 10 as the operating system.

1. Open the terminal or command prompt and navigate to the directory where you want to install the project. Execute the following command to clone the GitHub repository (This step is only necessary if you don't have the script):
```bash
git clone https://github.com/jnnastti/EstelarClass.git
```
2. Create the virtual environment venv in the terminal within the project folder:
```bash
python -m venv venv
```

3. Activate the venv in the terminal:
```bash
./venv/Scripts/Activate.ps1
```
If there are issues with script execution on Windows, you will need to enable Windows to run scripts through PowerShell.

4. Install the packages:
```bash
pip install -r requirements_final.txt
```

## How to Execute:

1. Access and run all the preprocessing files with venv (e.g., k2_preprocessing.ipynb);
2. Verify that the .pkl files were created correctly inside each database folder within the /data folder;
3. Access and run all the database files with venv (e.g., k2_base.ipynb);
4. Ensure that all four files have completed their execution;
5. Access and run EstelarClass.ipynb with venv and wait until the execution is complete to access all the results.
<hr/>
<p align="center"><img src="./img/explorer.gif" width="100px" height="100px"/></p>
<h5 align="center"><a href="https://drive.google.com/file/d/1b-bkpaNTlPFzecCm-XZ-jTiWm5DZsnJ-/view?usp=sharing"> Access the final report here</a></h5>

