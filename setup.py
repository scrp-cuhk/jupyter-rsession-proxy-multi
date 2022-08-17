# Each entry in entry_points['jupyter_serverproxy_servers'] corresponds 
# to one RStudio configuratiom in addition to the one loaded by 
# jupyter-rsession-proxy.

import setuptools

setuptools.setup(
    name="jupyter-rsession-proxy-multi",
    version='1.0.0',
    url="https://github.com/scrp-cuhk/jupyter-rsession-proxy-multi",
    author="Vinci Chow",
    description="Add additional RStudio proxies to Jupyter",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-rsession-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'rstudio_mkl_2022 = jupyter_rsession_proxy_multi:setup_rserver_mkl',
            'rstudio_mro_4 = jupyter_rsession_proxy_multi:setup_rserver_mro'
        ]
    }
)
