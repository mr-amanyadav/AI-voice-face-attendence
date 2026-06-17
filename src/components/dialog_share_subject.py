import streamlit as st
import segno
import io

@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    app_domain = "snapClass-main18.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to Join")

    qr = segno.make(join_url)

    out = io.BytesIO()
    qr.save(out, kind="png", scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Copy Link")

        st.text_input(
            "Join Link",
            value=join_url,
            key=f"join_link_{subject_code}"
        )

        st.text_input(
            "Subject Code",
            value=subject_code,
            key=f"subject_code_{subject_code}"
        )

        st.info("Select the text and press Ctrl+C to copy.")

    with col2:
        st.markdown("### Scan to Join")
        st.image(
            out.getvalue(),
            use_container_width=True,
            caption="QR Code for Class Joining"
        )