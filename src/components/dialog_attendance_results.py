from PIL import Image
import time
import streamlit as st
from src.DataBase.config import supabase
from src.DataBase.db import enroll_student_to_subject,create_attendance

def show_attendance_result(df,logs):
    st.write("Please review attendance befor confirming.")
    st.dataframe(df,hide_index=True,width='stretch')

    col1,col2=st.columns(2)

    with col1:
        if st.button("Discard", width='stretch', key="discard_attendance_result"):
            st.session_state.attendance_images=[]
            st.session_state.voice_attendance_results=None
            st.rerun()
    

    with col2:
        if st.button("Confirm & Save", key="confirm_save_attendance", type="primary"):
            try:
                create_attendance(logs)
                st.toast("Attendance taken")
                st.session_state.attendance_images=[]
                st.session_state.voice_attendance_results=None
                st.rerun()
            except Exception as e:
                st.exception('Sync failed')

@st.dialog("Capture or upload photo")
def attendance_result_dialog(df,logs):
    # show_attendance_result(df,logs)
    st.write("Please review attendance befor confirming.")
    st.dataframe(df,hide_index=True,width='stretch')

    col1,col2=st.columns(2)

    with col1:
        if st.button("Discard",width='stretch'):
            st.rerun()
    

    with col2:
        if st.button("Confirm & Save",width='stretch',type='primary'):
            try:
                create_attendance(logs)
                st.toast("Attendance taken")
                st.session_state.attendance_images=[]
                st.rerun()
            except Exception as e:
                st.exception("sync failed")