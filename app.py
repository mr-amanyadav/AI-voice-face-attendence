
import streamlit as st

def main():
    st.header("this is Title")
    name=st.text_input("enter your name")

    col1,col2=st.columns(2,gap="small")
    with col1:
        if st.button("display",key="btn1",width='stretch') :
            print("hi",name)
    with col2:        
        if st.button("display" ,key="btn2",width='stretch'):
            print("by",name)

    st.markdown("""
            <style>
                button{
                background: orange !important;
                }

            </style>


                """,unsafe_allow_html=True)        
main()
