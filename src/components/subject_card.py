import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):

    with st.container(border=True):
        st.subheader(name)
        st.write(f"**Code:** {code} | **Section:** {section}")

        if stats:
            cols = st.columns(len(stats))

            for col, (icon, label, value) in zip(cols, stats):
                with col:
                    st.metric(
                        label=f"{icon} {label}",
                        value=value
                    )

    if footer_callback:
        footer_callback()