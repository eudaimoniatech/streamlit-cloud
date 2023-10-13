import streamlit as st
import streamlit_pydantic as sp

from models import Error
from models import Brand
from models import Brands
from models import Searches

models = [Brand]
model = st.sidebar.radio(
    label="Which Model to Use in Form",
    options=models,
    format_func=lambda x: x.__name__,
)
input_data = sp.pydantic_form(key="pydantic_form", model=model)

if not input_data:
    st.warning("Submit the Form to continue")
    st.stop()

st.code(repr(input_data))
st.json(input_data.json())
