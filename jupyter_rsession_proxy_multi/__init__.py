from jupyter_rsession_proxy import setup_rserver

# One function per RStudio configuration. 
# Remember to add them as setup.py entry points.
# Format: entry name, display title, location of rserver configuration file
def setup_rserver_mkl():
    return setup_rserver("rstudio_mkl_2022",
                         "RStudio (R 4.1 MKL)",
                         "/opt/network/R/rserver/rserver_mkl.conf")

def setup_rserver_mro():
    return setup_rserver("rstudio_mro_4",
                         "RStudio (R 4.0 MRO)",
                         "/opt/network/R/rserver/rserver_mro.conf")

