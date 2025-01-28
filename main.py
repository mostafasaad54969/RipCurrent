import helper_functions as hf


classes = ["rip_current"]
DatasetPath = '/kaggle/working/RipCurrent/training_data/images'
DestPath = '/kaggle/working/RipCurrent/10fold'
AnnotationsPath = '/kaggle/working/RipCurrent/training_data/labels'

hf.kfold_split_yolo_dataset_yml(DestPath, DatasetPath, AnnotationsPath, classes)

