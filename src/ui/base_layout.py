import streamlit as st


def style_background_home():

    st.markdown("""
                
                <style>
                    .stApp{
                background: #5865F2 !important;
                }

                </style>
                """,unsafe_allow_html=True)
    




def style_background_dashboad():

    st.markdown("""
                
                <style>
                    .stApp{
                background: #E0E !important;
                }

                </style>
                """,unsafe_allow_html=True)







def style_base_layout():

    st.markdown("""
                 <style>
        /* Hide top bar */
        #MainMenu, footer, header {
            visibility: hidden;
                
        .block        
        }
        </style>
                   """,unsafe_allow_html=True)