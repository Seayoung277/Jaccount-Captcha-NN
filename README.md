# Jaccount-Captcha
This is an SJTU Jaccount Captcha recognizing plugin project for Chrome and Chromium web browser

'Jaccount Captcha.zip' is the final plugin. You can use it in your Chrome or Chromium web browser.

'collect.py' is used for collecting original captcha images from SJTU server.
'convert.py' is used for converting the collected images into binary images. By changing the threshold, images with 160 bold and 200 bold can be collected.
'cut.py' is used for cutting the images into single word images sized 20x100.
'gether.py' is used for transfering single word images into pixel data files.
'getset.py' is used for transfering labels of images into data files.
'data.py' is used for transfering parameters calculated by neuro networks into JavaScript files.

You can use 'test.m' to train a single neuro network, and use 'captcha.m' to train multiple neuro networks to observe the performance.

other '.m' files are mainly neuro network functions.
Some of the images and data files are my testing results.

In the folder Captcha Plus, there are several small neuro networks for further optimization. The optimization is based on the error rate in 'error.txt'
