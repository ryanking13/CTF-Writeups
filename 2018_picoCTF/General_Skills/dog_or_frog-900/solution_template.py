import numpy as np
from keras.applications.mobilenet import preprocess_input, decode_predictions
from keras.models import load_model, Model
from keras.objectives import categorical_crossentropy
from keras.preprocessing.image import img_to_array, array_to_img
from PIL import Image
from imagehash import phash

import tensorflow as tf
from keras import backend as K


IMAGE_DIMS = (224, 224)
TREE_FROG_IDX = 31
TREE_FROG_STR = "tree_frog"


# I'm pretty sure I borrowed this function from somewhere, but cannot remember
# the source to cite them properly.
def hash_hamming_distance(h1, h2):
    s1 = str(h1)
    s2 = str(h2)
    return sum(map(lambda x: 0 if x[0] == x[1] else 1, zip(s1, s2)))


def is_similar_img(path1, path2):
    image1 = Image.open(path1)
    image2 = Image.open(path2)

    dist = hash_hamming_distance(phash(image1), phash(image2))
    return dist <= 1


def prepare_image(image, target=IMAGE_DIMS):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    # return the processed image
    return image


def create_img(img_path, img_res_path, model_path, target_str, target_idx, des_conf=0.95):
    test = Image.open(img_path).resize(IMAGE_DIMS)
    test = prepare_image(test)
    model = load_model(model_path)

    model.save_weights('./model_weights.h5')

    print(decode_predictions(model.predict(test), top=3)[0])

    # TODO: YOUR SOLUTION HERE
    sess = tf.Session()
    K.set_session(sess)
    K.set_learning_phase(0)

    logits = model.get_layer('conv_preds').output
    mid_model = Model(inputs=model.inputs, outputs=logits)

    # Iterative targeted FGSM
    # FGSM wasn't good enough
    n_iter = 10

    clean_inputs = tf.placeholder(shape=test.shape, dtype=tf.float32, name='clean')
    target_label = tf.placeholder(shape=(), dtype=tf.int64, name='target_label')
    pred = mid_model(clean_inputs)
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=tf.one_hot(target_label, 1000), logits=pred))
    grad = tf.gradients(loss, clean_inputs)[0]
    eps = 0.1 / n_iter
    adv = clean_inputs - tf.scalar_mul(eps, tf.sign(grad))

    sess.run(tf.global_variables_initializer())
    # Reload model weights after initialization
    model.load_weights('./model_weights.h5', by_name=True)

    for _ in range(n_iter):
        test = sess.run(adv, feed_dict={clean_inputs: test, target_label: TREE_FROG_IDX})
        print(decode_predictions(model.predict(test), top=3)[0])

    test = test.reshape((224,224,3))
    img = array_to_img(test)
    img.save(img_res_path)


if __name__ == "__main__":
    create_img("./trixi.png", "./trixi_frog.png", "./model.h5", TREE_FROG_STR, TREE_FROG_IDX)
    assert is_similar_img("./trixi.png", "./trixi_frog.png")
