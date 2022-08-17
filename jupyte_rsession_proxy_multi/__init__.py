from jupyter_rsession_proxy import setup_rserver

# One function per RStudio configuration. 
# Remember to add them as setup.py entry points.
# Format: Display name, entry name, location of rserver configuration file
def setup_rserver_mkl():
    return setup_rserver("RStudio (R 4.1 MKL)",
                         "rstudio_mkl",
                         "/opt/network/R/rserver/rserver_mkl.conf")

def setup_rserver_mro():
    return setup_rserver("RStudio (R 4.0 MRO)",
                         "rstudio_mro_4",
                         "/opt/network/R/rserver/rserver_mro.conf")

