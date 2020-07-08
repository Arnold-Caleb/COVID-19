
import matplotlib.pyplot as plt 

def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
    plt.tight_layout()
    plt.show()


def learningCurves(*args, **kwargs):

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(kwargs['epochs_range'], kwargs['acc'], label='Training Accuracy')
    plt.plot(kwargs['epochs_range'], kwargs['val_acc'], label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(kwargs['epochs_range'], kwargs['loss'], label='Training loss')
    plt.plot(kwargs['epochs_range'], kwargs['val_loss'], label='Validation loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation loss')
    plt.show()