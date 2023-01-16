def background_imgs_addition(background_images_path,x_train_dir):
  for i in tqdm(range(int(len(os.listdir(x_train_dir)*0.15))):
    img=background_images_path[i]
    img='path/to/background_images/'+img
    new_img=x_train_dir+'/'+background_images[i]
    shutil.copyfile(img, new_img)
