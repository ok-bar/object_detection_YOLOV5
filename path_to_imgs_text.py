from pathlib import Path
from tqdm import tqdm

def split_imgs_and_text(img_paths,txt_paths):
  """First download all images with corresponding text to two folders,than this function will split them to the lists while erasing duplicates images"""
  
  unique_img_paths=[]
  unique_txt_paths=[]
  files_size=[]

  for i in tqdm(range(len(img_paths))):
    f_size=Path(img_paths[i]).stat().st_size
    if f_size in files_size:
      pass
    else:
      files_size.append(f_size)
      unique_img_paths.append(img_paths[i])
      unique_txt_paths.append(txt_paths[i])
  unique_data=len(unique_img_paths)
  print(f'number of unique images in the dataset is: {unique_data}')
  return unique_img_paths,unique_txt_paths
