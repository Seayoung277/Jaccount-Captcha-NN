clear ; close all; clc

input_layer_size  = 800;  % 20x40 Input Images of Digits
num_labels = 26;          % 26 labels, from 1 to 10

layer_start = 100;
layer_end = 100;
layer_step = 0;

lambda_start = 0;
lambda_end = 5;
lambda_step = 0.2;
lambda_vec = [0 0.001 0.003 0.01 0.03 0.1 0.3 1 3 10]';

m_start = 10000;
m_end = 10000;
m_step = 0;

fprintf('Loading Data ...\n');
load('trainData.mat');
load('trainSet.mat');
load('validationData.mat');
load('validationSet.mat');

%train_result = zeros(layer_end-layer_start+1, (lambda_end-lambda_start)/lambda_step+1);
%validation_result = zeros(layer_end-layer_start+1, (lambda_end-lambda_start)/lambda_step+1);
train_error = zeros(1, 26);
validation_error = zeros(1, 26);

fprintf('\nNeural Network Training Starts !\n');
options = optimset('MaxIter', 100);
for ly = 50 %layer_start:layer_step:layer_end
	Theta1_ori = randInitializeWeights(input_layer_size, ly);
	Theta2_ori = randInitializeWeights(ly, num_labels);
	for ld = lambda_start:lambda_step:lambda_end
		%ld = lambda_vec(ld_temp);
		for m = 10000 %m_start:m_end
			fprintf('\nTraining %d Hidden Node Neural Network With Lambda = %f Using %d Training Datas ... \n', ly, ld, m);
			X = train_data(1:m, :);
			y = train_set(:, 1:m)';
			%X = validation_data;
			%y = validation_set';
			Theta1 = Theta1_ori;
			Theta2 = Theta2_ori;
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
			res_t = mean(double(pred == y)) * 100;
			err_t = nnCostFunction(final_nn_params, input_layer_size, ly, num_labels, X, y, 0);
			train_error(1, int32(ld/0.2)+1) = err_t;
			%train_result(ly-layer_start+1, int32((ld-lambda_start)/lambda_step+1)) = res_t;

			X = validation_data;
			y = validation_set';

			pred = predict(Theta1, Theta2, X);
			res_v = mean(double(pred == y)) * 100;
			err_v = nnCostFunction(final_nn_params, input_layer_size, ly, num_labels, X, y, 0);
			validation_error(1, int32(ld/0.2)+1) = err_v;
			%validation_result(ly-layer_start+1, int32((ld-lambda_start)/lambda_step+1)) = res_v;

			fprintf('\nThe Train Result is %f\n', res_t);
			fprintf('\nThe Validation Result is %f\n', res_v);
			fprintf('\nThe Train error is %f\n', err_t);
			fprintf('\nThe Validation error is %f\n', err_v);
		end
	end
end
