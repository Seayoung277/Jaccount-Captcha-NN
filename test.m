clear ; close all; clc

input_layer_size  = 800;  % 20x40 Input Images of Digits
num_labels = 26;          % 26 labels, from 1 to 10
layer_start = 30;
layer_end = 50;
lambda_start = 0.5;
lambda_end = 5;
lambda_step = 0.5;

fprintf('Loading Data ...\n')
load('trainData.mat');
load('trainSet.mat');
load('validationData.mat');
load('validationSet.mat');

X = train_data;
y = train_set';

fprintf('\nNeural Network Training Starts !\n')
options = optimset('MaxIter', 1000);
ly = 50;
ld = 0;
fprintf('\nTraining %d Layer Neural Network With Lambda = %f ... \n', ly, ld)
Theta1 = randInitializeWeights(input_layer_size, ly);
Theta2 = randInitializeWeights(ly, num_labels);
nn_params = [Theta1(:) ; Theta2(:)];
costFunction = @(p) nnCostFunction(p, ...
                    		   input_layer_size, ...
                       		   ly, ...
                       		   num_labels, X, y, ld);
[final_nn_params, cost] = fmincg(costFunction, nn_params, options);
Theta1 = reshape(final_nn_params(1:ly * (input_layer_size + 1)), ...
               ly, (input_layer_size + 1));
Theta2 = reshape(final_nn_params((1 + (ly * (input_layer_size + 1))):end), ...
               num_labels, (ly + 1));
pred = predict(Theta1, Theta2, X);
train_result = mean(double(pred == y)) * 100;

X = validation_data;
y = validation_set';
pred = predict(Theta1, Theta2, X);
validation_result = mean(double(pred == y)) * 100;

fprintf('\nThe Train Result is %f\n', train_result)
fprintf('\nThe Validation Result is %f\n', validation_result)

