import streamlit as st
from PIL import Image

@st.dialog("Capture or Upload Photos")
def add_photos_dialog():

    st.write("Add classroom photos to scan for attendance")

    # Initialize session state variables
    if "photo_tab" not in st.session_state:
        st.session_state.photo_tab = "camera"

    if "attendance_images" not in st.session_state:
        st.session_state.attendance_images = []

    # Tab buttons
    t1, t2 = st.columns(2)

    with t1:
        camera_type = (
            "primary"
            if st.session_state.photo_tab == "camera"
            else "tertiary"
        )

        if st.button(
            "Camera",
            type=camera_type,
            use_container_width=True,
        ):
            st.session_state.photo_tab = "camera"
            st.rerun()

    with t2:
        upload_type = (
            "primary"
            if st.session_state.photo_tab == "upload"
            else "tertiary"
        )

        if st.button(
            "Upload Photos",
            type=upload_type,
            use_container_width=True,
        ):
            st.session_state.photo_tab = "upload"
            st.rerun()

    st.divider()

    # Camera Mode
    if st.session_state.photo_tab == "camera":

        cam_photo = st.camera_input(
            "Take Snapshot",
            key="dialog_cam"
        )

        if cam_photo is not None:
            image = Image.open(cam_photo)

            st.session_state.attendance_images.append(image)

            st.toast("Photo captured successfully!")
            st.rerun()

    # Upload Mode
    elif st.session_state.photo_tab == "upload":

        uploaded_files = st.file_uploader(
            "Choose image files",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True,
            key="dialog_upload"
        )

        if uploaded_files:

            for file in uploaded_files:
                image = Image.open(file)
                st.session_state.attendance_images.append(image)

            st.toast(
                f"{len(uploaded_files)} photo(s) uploaded successfully!"
            )
            st.rerun()

    # Preview Images
    if st.session_state.attendance_images:

        st.divider()

        st.write(
            f"Total Photos: {len(st.session_state.attendance_images)}"
        )

        cols = st.columns(
            min(3, len(st.session_state.attendance_images))
        )

        for i, img in enumerate(st.session_state.attendance_images):
            with cols[i % len(cols)]:
                st.image(
                    img,
                    caption=f"Photo {i + 1}",
                    use_container_width=True
                )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "Clear Photos",
            type="secondary",
            use_container_width=True
        ):
            st.session_state.attendance_images = []
            st.rerun()

    with col2:
        if st.button(
            "Done",
            type="primary",
            use_container_width=True
        ):
            st.rerun()