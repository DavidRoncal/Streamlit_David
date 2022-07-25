import streamlit as st
from multiapp import MultiApp
from apps import home, basemaps, customize, datasets, opacity, nlcd_demo, Raura, Raura_dem, streamlit_app

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here

apps.add_app("Home", home.app)
apps.add_app("Customize the default map", customize.app)
apps.add_app("Change basemaps", basemaps.app)
apps.add_app("Change opacity", opacity.app)
apps.add_app("Search datasets", datasets.app)
apps.add_app("NLCD Demo", nlcd_demo.app)
apps.add_app("Imágen Satelial Raura", Raura.app)
apps.add_app("Modelo de Elevación Digital", Raura_dem.app)
apps.add_app("Comparación Imágenes", streamlit_app.app)
# The main app
apps.run()
