
from tensorflow.keras.preprocessing import image
from utilities import IMG_HEIGHT, IMG_WIDTH


def preprocessImages(train_dir, val_dir, test_dir, batch_size):
    
    train_gen = image.ImageDataGenerator(rescale = 1./255,
                                         shear_range = 0.2,
                                         zoom_range = 0.2,
                                         width_shift_range = 0.1,
                                         height_shift_range = 0.1,
                                         horizontal_flip = True,
                                         )

    val_gen = image.ImageDataGenerator(rescale=1./255,)
    test_gen = image.ImageDataGenerator(rescale=1./255,)

    train_data_gen = train_gen.flow_from_directory(batch_size=batch_size,
                                                   directory=train_dir,
                                                   shuffle=True,
                                                   target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                   class_mode='sparse'
                                                   )
    val_data_gen = val_gen.flow_from_directory(batch_size=batch_size,
                                               directory=val_dir,
                                               target_size=(IMG_HEIGHT, IMG_WIDTH),
                                               class_mode='sparse')

    test_data_gen = test_gen.flow_from_directory(batch_size=batch_size,
                                                 directory=test_dir,
                                                 target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                 class_mode='sparse'
                                                 ) 

    return train_data_gen, val_data_gen, test_data_gen