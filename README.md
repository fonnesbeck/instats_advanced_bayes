# Applied Bayesian Modeling in Python

Bayesian statistical methods offer a flexible and powerful framework for approaching a variety of data science problems. They provide results that are interpretable and naturally incorporate relevant information about quantities for estimation or prediction. Though there are significant computational challenges associated with Bayesian methods, highly capable open source probabilistic programming tools are readily available. In this workshop, we will explore these concepts using PyMC (version 5.25 or later), and the principles covered will be transferable to other probabilistic programming languages.

This course is designed for data scientists, applied statisticians, and academic researchers who want to apply Bayesian statistics in their own work. Participants will be introduced to Bayesian methods and their applications to real-world datasets. The workshop includes substantial hands-on experience using PyMC to define, fit, and evaluate models with real-world datasets. As an introductory course, no prior experience with PyMC or Bayesian statistics is required. However, some familiarity with fundamental statistical concepts (such as regression) and experience with Python libraries like NumPy, pandas, and Jupyter notebooks will be beneficial.

The workshop will cover the following key areas, enabling you to:

- Understand Bayesian Fundamentals: Grasp the core concepts of Bayesian inference, including the interpretation of probability, the roles of priors and likelihoods, and their synthesis into posterior distributions.
- Understand the PyMC API: Become familiar with PyMC as a probabilistic programming tool, learning to construct models and utilize its key components.
- Develop Custom Models: Acquire the skills to translate research questions into statistical models by specifying parameters and selecting appropriate probability distributions for data (likelihoods) and parameter beliefs (priors).
- Implement MCMC for Parameter Estimation: Understand and apply Markov Chain Monte Carlo (MCMC) methods for fitting models and estimating parameters.
- Build Hierarchical Models: Progress from simple linear regression through generalized linear models to full hierarchical models. Learn to handle grouped data structures, implement partial pooling strategies, and model varying coefficients across groups. Understand when and why to use hierarchical modeling, including concepts of shrinkage, information sharing across groups, and the balance between complete pooling and no pooling approaches.
- Analyze Model Output: Learn to process and interpret the output from MCMC simulations.
- Perform Model Checking and Refinement: Master techniques for model checking using ArviZ, including diagnostic checks, posterior predictive checks, and assessment of model fit.
- Apply the Bayesian Workflow: Engage with the iterative process of model building, checking, and improvement fundamental to robust Bayesian analysis.

Upon completion of the workshop, participants will be comfortable with the core principles of Bayesian statistics and possess practical experience in using PyMC. The goal is for attendees to gain confidence in applying these methods to their own projects by equipping them with skills in writing PyMC models, performing diagnostics, and interpreting results. The emphasis on practical application will demonstrate the direct benefits of these methods for their work.

All livestreaming seminars are offered via Zoom, and all seminar recordings and material (including any slides, program input, output, and data) are available online for 30 days after the seminar concludes — in case you would prefer to attend asynchronously or you would like to go back and revisit the seminar content after it concludes. An online seminar Q&A Forum will be monitored by the expert(s) for 30 days after the seminar concludes, so that you can ask questions related to seminar content outside of the live seminar sessions. For all on-demand seminars, all videos and material (including program input, output, data, and slides) will be available for 30 days after you activate your enrollment, which you can do anytime after you purchase the on-demand seminar. An official Instats certificate of completion is provided at the conclusion of all seminars. For European students, our seminars offer ECTS Equivalent points where shown, which is indicated on the certificate of completion that is provided at the conclusion of each seminar (see the Instats FAQ for details).

## Setting up the Environment

If using Anaconda/Miniforge:
The repository contains an `environment.yml` file with all required packages. Run:

    mamba env create

if you are using Miniforge, or if you installed Anaconda, you can use:

    conda env create

from the main course directory (use `conda` instead of `mamba` if you installed Anaconda). Then activate the environment:

    mamba activate applied_bayes
    # or
    conda activate applied_bayes

If using Pixi:
The repository contains a `pixi.toml` file. From the main course directory, simply run:

    pixi install
    pixi shell

Then, you can start **JupyterLab** to access the materials:

    jupyter lab 

For those who like to work in VS Code, you can also run Jupyter notebooks from within VS Code. To do this, you will need to install the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter). Once this is installed, you can open the notebooks in the `notebooks` subdirectory and run them interactively.

Here's the updated syllabus that reflects the new course content and logical progression:

## Day 1

### Session 1: Introduction to Bayesian Computing
- Basic Bayes concepts and probability models
- Posterior distribution calculation
- Prior specification
- Bayesian updating
- Conjugate priors

### Session 2: Building Models with PyMC and MCMC Fundamentals
- Building models in PyMC
- Model specification and structure
- Likelihood functions and prior distributions
- Introduction to MCMC methods
- Sampling algorithms and Monte Carlo integration
- Simple linear regression in PyMC

## Day 2

### Session 3: From Linear Regression to Hierarchical Models
- Linear regression models in PyMC
- Generalized linear models (GLMs)
- Introduction to grouped data structures
- Hierarchical modeling concepts
- Partial pooling and information sharing
- Varying coefficients and multi-level models
- When and why to use hierarchical approaches

### Session 4: The Bayesian Workflow
- MCMC output processing and analysis
- Model checking with ArviZ
- Posterior analysis and interpretation
- Model diagnostics for hierarchical models
- Posterior predictive checks
- Model evaluation and comparison
- Complete Bayesian workflow
- Best practices for model improvement
