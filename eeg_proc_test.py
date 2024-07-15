'''
ASR is a pretty hefty function, so we'll use the imports below to limit the multithreading
to something reasonable. It won't impact the speed too much anyway.
'''
import os
nthreads = "8"

# Set the number of threads for various libraries
os.environ["OMP_NUM_THREADS"] = nthreads
os.environ["OPENBLAS_NUM_THREADS"] = nthreads
os.environ["MKL_NUM_THREADS"] = nthreads
os.environ["VECLIB_MAXIMUM_THREADS"] = nthreads
os.environ["NUMEXPR_NUM_THREADS"] = nthreads
os.environ["NUMBA_NUM_THREADS"] = nthreads
os.environ["NUMBA_DEFAULT_NUM_THREADS"] = nthreads
os.environ["OMP_DYNAMIC"] = "FALSE"
os.environ["OMP_MAX_ACTIVE_LEVELS"] = "1"
os.environ["GOTO_NUM_THREADS"] = nthreads
os.environ["OMP_THREAD_LIMIT"] = nthreads
os.environ["BLIS_NUM_THREADS"] = nthreads
os.environ["PTHREAD_POOL_SIZE"] = nthreads


'''
The following are the regular imports needed
'''
import mne
from src.eeg_preprocessing_cst.pipeline import CSTpreprocessing as preprocess

import warnings
warnings.filterwarnings("ignore")

def create_preproc_object(EEG_filename: str, 
			  events_filename: str, 
			  prep: bool = False, 
			  asr: bool = False) -> 'preprocess':
	preproc = preprocess(EEG_filename, events_filename)
	preproc.set_annotations_to_raw().set_montage()
	print(len([annot for annot in preproc.annotations if annot['description'] == 'Crash']))
	if prep:
		preproc.run_prep()
	if asr:
		preproc.run_asr()
	
	return preproc
	
def rename_file(fpath):
	if os.path.exists(fpath):
		# Get the directory and filename
		directory, filename = os.path.split(fpath)
		# Get the base filename without extension
		base_filename, ext = os.path.splitext(filename)
		
		# Count files with similar names
		similar_files = [f for f in os.listdir(directory) if base_filename in f]
		count = len(similar_files)
		
		# Rename the file with appropriate count
		new_filename = f"{base_filename}_{count}{ext}"
		new_filepath = os.path.join(directory, new_filename)
		
		# Rename the file
		os.rename(fpath, new_filepath)
		print(f"File '{filename}' already exists. Renamed to '{new_filename}'.")
	else:
		print("File does not exist. No action needed.")
		
	return fpath


# Creating preprocessed EEG file
EEG_filename = '/Users/danielgarcia-barnett/Desktop/Coding/cpCST_data_analysis/data/sub-M10901084/raw/sub-M10901084_ses-MOBI1A_run-001_crop.fif'
events_filename = '/Users/danielgarcia-barnett/Desktop/Coding/cpCST_data_analysis/data/sub-M10901084/lsl/sub-M10901084_ses-MOBI1A_task-cst_run-001_lsl_events.csv'

prep_condition = True
asr_condition = False
preproc = create_preproc_object(EEG_filename, events_filename, prep = prep_condition, asr = asr_condition)

# Saving preprocessed EEG file
filepath = os.path.join('/Users/danielgarcia-barnett/Desktop/Coding/cpCST_data_analysis/data/sub-M10901084/time_sync_test/cropped', f'sub-M10901084_eeg_extract_prep-{prep_condition}_asr-{asr_condition}')
filepath = rename_file(filepath)

try:
	preproc.save(f'{filepath}_preproc.fif')
except Exception as e:
	print(e)

try:
	raw = preproc.raw
	raw.save(f'{filepath}_raw.fif', overwrite=True)
except Exception as e:
    print(e)
