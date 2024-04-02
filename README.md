# From Physics to Data-Driven Modeling: With applications in genomic, cellular, developmental, ecological and neuro biology

This course is inspired in part by the text [*From Statistical Physics to Data-Driven Modelling*](#references), by Cocco, Monasson, and Zamponi, as well as the accompanying [tutorials](https://github.com/StatPhys2DataDrivenModel) provided by the authors.


## Course Outline
The following is a tentative outline of the course and is subject to change.

| Week   | Topic       | Content |
| ------ | ----------- | ------- |
| Week 1 | Bayesian Inference |
<!-- | Week 2 | Asymptotic Inference | -->
<!-- | Week 3 | Asymptotic Inference & Information Theory | -->
<!-- | Week 4 | High-Dimensional Inference | -->
<!-- | Week 5 | Regularization and Priors | -->
<!-- | Week 6 | Statistical Physics as Inference | -->
<!-- | Week 7 | Generative Models | -->
<!-- | Week 8 | Dimensionality Reduction & Supervised Learning | -->
<!-- | Week 9 | Time Series Modeling | -->


## Course Resources
* [This repository](https://github.com/AddisonHowe/phys2ddm).
* Course [textbook](https://www.amazon.com/Statistical-Physics-Data-Driven-Modelling-Applications/dp/0198864744/ref=asc_df_0198864744/?tag=hyprod-20&linkCode=df0&hvadid=598249994043&hvpos=&hvnetw=g&hvrand=16341512642454895429&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9021723&hvtargid=pla-1747176625803&psc=1&mcid=83bdbbcbf81f34d39b250456851675ab&gclid=Cj0KCQiAtaOtBhCwARIsAN_x-3L3QMJbPRhzAlG-fF04hh1-n0AOljrgwSrmTVIyQdRMnl05W5jjhFoaAu7lEALw_wcB) and [tutorials](https://github.com/StatPhys2DataDrivenModel)
<!-- * Course notes. (TODO) -->
<!-- * Additional readings. (TODO) -->


## System Setup

### Python and Conda

Most of the course content will involve python programming. 
We recommend using [conda](https://conda.io/projects/conda/en/latest/index.html) to manage python environments and install the necessary packages.
If you don't already have conda installed, you can install it by following the directions for your operating system [here](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html#regular-installation).
We recommend installing the miniconda distribution.

Once conda is installed, you can use it to create individual Python environments.
The line below will create a new environment, called `p2ddm-env`, and install a handful of packages.

```bash
conda create -n p2ddm-env python=3.10 numpy matplotlib scipy jupyter ipykernel seaborn pandas
```

Activate the new environment by running 
```bash
conda activate p2ddm-env
```
Test that things are working properly by running the following line
```bash
python -c "import numpy; print('Success!')"
```


### Jupyter Notebooks

The tutorials for the course will be in the form of [Jupyter Notebooks](https://jupyter.org/install).
By installing jupyter in your conda environment (see above), you should be able to start a Jupyter session with the command
```bash
jupyter notebook </path/to/directory/>
```
You may also choose to use another IDE, such as [PyCharm](https://www.jetbrains.com/pycharm/) or [VS Code](https://code.visualstudio.com/).


## Contact

For questions or comments, please feel free to [contact us](mailto:addisonhowe2025@u.northwestern.edu).


## References

1. Cocco S, Monasson R, Zamponi F. From Statistical Physics to Data-Driven Modelling: with Applications to Quantitative Biology [Internet]. 1st ed. Oxford University PressOxford; 2022 [cited 2024 Mar 7]. Available from: https://academic.oup.com/book/44725
