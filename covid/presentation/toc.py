import streamlit as st


def content():
    st.title("Toolbox")

    st.header("Math Toolbox")
    st.markdown("""
    * Basic Understanding of Probability and Statistics
    * Calculus 101
    * Basic Understanding of Differential Equations
      * Just to be able to understand what is going on 
    * Fundamental Machine Learning
    """)
    st.header("Python Toolbox")

    st.subheader("Python")
    st.image("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png", width=180)
    st.markdown("""
    We do depend on **Python 3.7**
    
    * Function parameter & return type annotations (this is **Python 3.6**, I guess)
    * `f-strings`
    * And some more which i don't remember :blush:
    """)

    st.subheader("streamlit")
    st.markdown("You are currently looking at it.")
    st.image("https://pbs.twimg.com/profile_images/1234856290058428416/8lWJhqj1_400x400.jpg",
             width=80)
    st.subheader("pandas")
    st.markdown("All data loading and manipulation")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png",
             width=100)
    st.subheader("numpy")
    st.markdown("Any vector, matrix or multidimentional array opeations.")
    st.image("https://user-images.githubusercontent.com/1217238/65364991-9f0fcb80-dbca-11e9-89a1-f369aa2be57a.png",
             width=100)
    st.subheader("scipy")
    st.markdown("Global searching, differential equation solving")
    st.image("https://www.fullstackpython.com/img/logos/scipy.png",
             width=80)
    st.subheader("scikit-learn")
    st.markdown("You are currently looking at it.")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png",
        width=80)
    st.markdown(r"### $H_2O$ AutoML")
    st.markdown("You are currently looking at it.")
    st.image("https://i0.wp.com/sefiks.com/wp-content/uploads/2019/09/h2o-automl.jpg?fit=835%2C900&ssl=1",
             width=60)

    st.title("Table of Content")
    st.header("Introduction to COVID Data")
    st.markdown("""
    * Loading data from web
      * Caching into Parquet files
    * Time variant visualization of COVID data using altair
    * Parametrization of charts using streamlit capabilities
    * Time invariant visualization of COVID data
    """)
    st.header("Early Phase Analysis of Epidemics using Exponential Model")
    st.markdown("""$$
    y(t) = A_{i}e^{B_{i}t}
    $$
    """)

    st.markdown("* **Claim**: Exponential models are **linear** models")
    st.markdown("* Learn for $A_{i}$ & $B_{i}$ using data")
    st.header("SIR Model")
    st.subheader("SIR Model 101")
    st.markdown("""
    * Phases of a person in a population
      * (**S**)usceptible
      * (**I**)nfected
      * (**R**)ecovered
    * Parameter Learning for SIR model using data
    """)
    st.header("ML based model to Predict the Next Day")
    st.subheader("Feature Engineering")

    # st.balloons()
