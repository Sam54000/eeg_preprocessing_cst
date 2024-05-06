from pipeline import CSTpreprocessing as preprocess
import os
EEG_filename = '/data2/Projects/NKI_RS2/MoBI/eeg_preprocessing_cst/data/sub-M10901084/raw/sub-M10901084_ses-MOBI1A_run-001.vhdr'
events_filename = '/data2/Projects/NKI_RS2/MoBI/eeg_preprocessing_cst/data/sub-M10901084/lsl/sub-M10901084_ses-MOBI1A_task-cst_run-001_lsl_events.csv'
preprocess = preprocess(EEG_filename, events_filename)
preprocess.set_annotations_to_raw().set_montage()
preprocess.run_prep()
preprocess.run_asr()
try:
	extract_file = os.path.join('/data2/Projects/NKI_RS2/MoBI/eeg_preprocessing_cst/data/sub-M10901084/', 'sub-M10901084_eeg_extract.edf')
	preprocess.save(extract_file)
except:
	print('if save fails')
	extract_file = os.path.join('/data2/Projects/NKI_RS2/MoBI/eeg_preprocessing_cst/data/sub-M10901084/', 'sub-M10901084_eeg_extract_raw.fif')
	raw = preprocess.raw
	mne.export(raw, extract_file)

