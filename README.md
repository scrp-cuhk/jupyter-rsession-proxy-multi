# jupyter-rsession-proxy-multi

Add multiple RStudio configurations to Jupyter. Relies on a [#PR133](https://github.com/jupyterhub/jupyter-rsession-proxy/pull/133) of [`jupyter-rsession-proxy`](https://github.com/jupyterhub/jupyter-rsession-proxy).

To add additional RStudio configurations:
1. Create configuration files for `rstudio-server` as needed.
2. Create a new skeleton package that imports `jupyter-ression-proxy:setup_rserver`. 
3. In `__init__.py`, add functions that return `setup_rserver()` with a unique `name` and path to the configuration file. One function per configuration file.
2. Add entry points for `jupyter_serverproxy_servers` in `setup.py` that points to each of the functions you created in step 3.
