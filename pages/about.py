from dash import dcc, html, register_page

register_page(__name__)

layout = html.Div([
    html.H3('Technical Write-Up and Retrospective'),
    html.Hr(),
    dcc.Markdown('''
        #### Introduction
    
        Data science has an important role to play in how we understand climate change, model its current and future effects, and communicate its impacts. With this project I wanted to explore available datasets and engage in a data science exercise using computer programming to draw and communicate climate change-related conclusions while gaining experience pertinent to the career paths I wish to pursue. The general technical challenges ended up being twofold: identifying the appropriate tools to fulfil this goal and learning the necessary skills needed to adequately employ those tools. I decided to tackle these challenges in three steps. First, I would work on analyzing data using the Python programming language along with some pertinent software libraries (bundles of reusable code, also known as a package), then I would attempt to visualize that analysis using other libraries, and finally I wanted to tie everything up with a tidy web application that summarized the work and its findings.
        
        Why Python? Python is widely used for data science due to its ease of use, giant community, and the availability of many powerful libraries specific to data manipulation, visualization, and other pertinent uses. As a general programming language, Python can build applications and set up websites, among countless other uses, which were two subtasks I wanted to pursue. Alternatives to Python include R, which is also widely used for data science but narrower in scope, programs such as MATLAB, which can be cost-prohibitive, and other general languages such as C++ or Java, which don't have the ease of use that Python enjoys for the tasks at hand.
        
        In preparation, I repurposed an old website and domain name as an entry point that linked to various aspects of the project. I also decided to use git, a version control system, to track changes and revisions to code and other documents. I chose GitHub as the repository (or repo) to store these files and keep a history of their revisions. I was able to deploy various aspects of the project straight from GitHub, including the web application, summary website, and Jupyter notebooks. Finally, for general development I relied heavily on PyCharm, a professional-grade integrated development environment (IDE) designed specifically for Python.
        
        #### Datasets
        
        I was pleased to find many open data sets available online. Many of these came in the form of a comma-separated values (CSV) file, which made them easy to import into my Python program and work with. In many cases, I didn't even need to directly download the data, but could instead import it directly via its web link. I challenged myself to use the CSV files as they were, with all data manipulation done within Python instead of editing the files manually to a desirable state, including sorting, changing columns, and other such changes.
        
        After reviewing many datasets, I decided to use the University of Hawaii Sea Level Center (UHSLC) tide gauge data, which has data from various locations along the California coast, as it seemed to support my paper topic, sea-level rise along the California coast and delta. Other datasets are being considered to use in support of this, such as temperature increases or ice melt rates.
        
        #### Data Analysis
        
        I found that the easiest way to work on data analysis in a stepwise, illustrative fashion was to use a Jupyter notebook. This tool allows the user to write Python code in sections, each of which can be launched independently, and its output displayed in line with the code itself. This made troubleshooting data manipulation and equations much easier than writing and launching and debugging whole (or partial) programs. I found a few options for this: notebooks could be deployed independently, or as part of Jupyter's larger development platform, JupyterLab. I found the latter to be overly complicated for my needs and fell back to using the notebook itself for much of my work. I also found that Google had its own version of notebook called Colab, which appeared to be a great way for collaborative work. Colab requires one to log into Google, however, which I didn't want to get in the way.
        
        Since notebooks acted as Python environments, it was easy to import any sort of Python library to use within. The library that I relied upon the most was pandas (derived from panel data), which is a well-known, widely used library for data analysis and manipulation. This ended up being the sole library that I used for everything aside from visualization, including importing two-dimensional data frames from CSV files and manipulating those data frames for analysis and visualization.
        
        #### Data Visualization
        
        In addition to using notebooks for data analysis, I also began using them to create plots. This is the logical workflow of a notebook, after all. Early on I used a standard Python library called Matplotlib and its submodule pyplot, which features plotting elements like MATLAB. This was a simple entry point into plotting the pandas data frames and validating the data manipulation I was attempting.
        
        I knew early on that I wanted to summarize my data visualization with an interactive dashboard, so I began looking at alternatives to Matplotlib. One that I worked with quite a bit was hvplot, which uses the interactive visualization library bokeh and integrated very well with pandas. This allowed me to easily create some very nice-looking plots. Furthermore, it worked very well with Panel, a nice data dashboard tool that integrated with the notebook. I ultimately decided to move away from this setup since I did not intend to use a notebook for my final project and wanted to mitigate the number of new tools I had to learn. I eventually settled on Dash, a dashboard tool from Plotly, which also makes a data visualization library of the same name. Since Dash was built to work with plotly, and plotly worked in notebooks, I committed to learning this tool instead.
        Sharing Data Analysis and Visualization
        
        Sharing these notebooks turned out to be a non-trivial task. There were several options to start up a server on which to deploy a live instantiation of notebook, but this turned out to be ill-advised due to the inclusion of a terminal (with which ne'er-do-wells could cause mischief with the server itself). Instead, I attempted to find a more turn-key solution that wouldn't have these risks.
        
        The simplest way to share a notebook was to provide a direct link to GitHub, which allowed a rudimentary version of the notebook to be viewed but did not allow anything to be run or edited. Since I wanted to feature interactive plots, this wasn't an ideal solution. Furthermore, GitHub couldn't display the plotly graphs, which are embedded HTML/JavaScript elements rather than static images.
        
        I discovered two options within Jupyter's larger collection of products: nbviewer and binder. Both tools worked by providing a link to a notebook's GitHub repository, from which the notebook is copied and deployed in a temporary environment. Nbviewer's environment was static – that is, it was not dissimilar to the GitHub option. However, it did display all the elements the way they were meant to be seen, so was a step-up in that regard, but still did not allow editing or interactivity. Binder worked much the same way as nbviewer except that it launched a dedicated, executable environment in which one could edit and execute code as if in a normal JupyterLab instance.
        
        Sadly, neither of these options ended up being very reliable. Nbviewer had a problem with displaying a notebook once and then showing a page-not-found error for subsequent runs. Attempts to refresh or clear the cache, including workarounds found online, proved fruitless. Binder worked well but sometimes took over ten minutes to load, which was less than ideal for a nimble solution. Ultimately, I decided the easiest way to capture the notebooks was to export them as static webpages, which could then be linked to within the website. This works in a pinch but hinders any interactivity there may have been within the notebook.
        
        #### Web Application
        
        The final part of this project was to develop a simple web application to succinctly summarize and display the analysis results. I considered building a dedicated website for this and investigated Python web frameworks such as Flask or Django. I eventually discovered Dash, which is a dashboard framework that is built upon Flask. Since Dash used plotly for its visual elements, which I was also able to use in the notebooks, it was ideal as simplified solution. Its structure was not too dissimilar from Flask, which I was already familiar with, and I could move the plotly graphs from notebooks with less hassle than if I had to port them to a different plotting library.
        
        There are many options these days for quickly deploying web applications. Among the most popular are Heroku, Digital Ocean, and PythonAnywhere, which is specific to Python apps. These three are all very comparable in features and cost. I decided to go with Digital Ocean for no other reason other than I had used them in the past and was satisfied with their services.
        
        #### Conclusion
        
        This was a challenging project for many reasons. Exploring all the available datasets quickly became overwhelming and I kept finding a need to narrow the scope of my analysis if I were to complete any of it before the class ended. On top of that, Python being the popular tool meant that there were numerous options available to do what I wanted to do. Investigating those that seemed to suit my needs and work well with each other was a challenge in and of itself. Despite my previous experience, learning to use said tools adequately is not a trivial manner, and I continue to learn more every time I revisit the project. However, the challenge of such work is one of the main reasons I enjoy it. This exercise has been a fulfilling experience and puts me in a good position to perform future work more efficiently and effectively.
    '''),
    html.Br(),
    html.H3('Technologies Considered'),
    html.Br(),
    dcc.Markdown('''
    ''')
])
