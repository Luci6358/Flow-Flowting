#!/bin/python3

import streamlit as st

st.title('Flow *~* Flowting')
st.image('/home/lilith/python_projects/juice/storage/flowting.jpeg')
st.subheader('Grab a fat cup of coffe and get to work')
st.text("")

video_file1 = open('/home/lilith/python_projects/juice/storage/videoplayback.mp4', 'rb')
video_bytes1 = video_file1.read()

video_file2 = open('/home/lilith/python_projects/juice/storage/honeypie.mp4', 'rb')
video_bytes2 = video_file2.read()

video_file3 = open('/home/lilith/python_projects/juice/storage/Guitar_Vibe__lofi_hiphop_mix.mp4', 'rb')
video_bytes3 = video_file3.read()

col1, col2, col3 = st.columns(3)

with col1:
	st.video(video_bytes1)
	st.subheader('Out of options')
	st.text("")

with col2:
	st.video(video_bytes2)
	st.subheader('Honeypie')
	st.text("")

with col3:
	st.video(video_bytes3)
	st.subheader('Guitar vibe')
	st.text("")

col1, col2 = st.columns(2)

video_file4 = open('/home/lilith/Music/Cafuné - Tek It (I Watch The Moon) [Official Video].mp4', 'rb')
video_bytes4 = video_file4.read()

with col1:
	st.video(video_bytes4)
	st.subheader('Tek it')
	st.text("")

